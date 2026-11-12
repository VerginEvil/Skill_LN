use std::collections::HashMap;
use std::fs;
use ln_linter::{Auditor4GL, DataDictionaryCache, FieldMeta, Severity};

#[test]
fn test_valid_dal2_script() {
    let script = r#"
#include <bic_dal>

function extern long before.save.object(long mode)
{
    if mode == DAL_NEW then
        dal.set.error.message("tcgen0001")
        return(DALHOOKERROR)
    endif
    return(0)
}

function extern void item.update(long i.mode)
{
}

function extern long item.check(long has_changed)
{
    return(0)
}
"#;
    let auditor = Auditor4GL::new();
    let diags = auditor.audit_content(script, "tccom001.dal", Some("dal2"), None);
    let errors: Vec<_> = diags.iter().filter(|d| d.severity == Severity::Error).collect();
    let warnings: Vec<_> = diags.iter().filter(|d| d.severity == Severity::Warning).collect();
    assert_eq!(errors.len(), 0, "Expected 0 errors, got: {:?}", errors);
    assert_eq!(warnings.len(), 0, "Expected 0 warnings, got: {:?}", warnings);
}

#[test]
fn test_dal001_interactive_dialog_rejection() {
    let script = r#"
function extern long before.save.object(long mode)
{
    message("Validation failed")
    ask.enum("Do you want to proceed?", 1)
    return(0)
}
"#;
    let auditor = Auditor4GL::new();
    let diags = auditor.audit_content(script, "tccom001.dal", Some("dal2"), None);
    let dal001: Vec<_> = diags.iter().filter(|d| d.code == "DAL001").collect();
    assert_eq!(dal001.len(), 2);
    assert!(dal001.iter().all(|d| d.severity == Severity::Error));
}

#[test]
fn test_dal002_hook_signature_validation() {
    let script = r#"
function extern void item.update()
{
}

function extern long item.check()
{
    return(0)
}
"#;
    let auditor = Auditor4GL::new();
    let diags = auditor.audit_content(script, "tccom001.dal", Some("dal2"), None);
    let dal002: Vec<_> = diags.iter().filter(|d| d.code == "DAL002").collect();
    assert_eq!(dal002.len(), 2);
    assert!(dal002.iter().any(|d| d.message.contains("long i.mode")));
    assert!(dal002.iter().any(|d| d.message.contains("long has_changed")));
}

#[test]
fn test_dal002_command_hook_return_types() {
    let script = r#"
function extern boolean function.approve.before.command()
{
    return(true)
}
"#;
    let auditor = Auditor4GL::new();
    let diags = auditor.audit_content(script, "whinh4131m000.cln", Some("general"), None);
    let dal002: Vec<_> = diags.iter().filter(|d| d.code == "DAL002").collect();
    assert_eq!(dal002.len(), 1);
    assert!(dal002[0].message.contains("must return 'void' or 'long'"));
}

#[test]
fn test_dal003_void_function_return_expression_rejected() {
    let script = r#"
function extern void function.approve.before.command()
{
    return(true)
}
"#;
    let auditor = Auditor4GL::new();
    let diags = auditor.audit_content(script, "whinh4131m000.cln", Some("general"), None);
    let dal003: Vec<_> = diags.iter().filter(|d| d.code == "DAL003").collect();
    assert_eq!(dal003.len(), 1);
    assert!(dal003[0].message.contains("Return value for void function not allowed"));
}

#[test]
fn test_dal004_raw_db_mutation_in_ui_script() {
    let script = r#"
table ttccom001

function void update_customer()
{
    db.update(ttccom001, db.retry)
}
"#;
    let auditor = Auditor4GL::new();
    let diags = auditor.audit_content(script, "tccom001m000.cln", Some("general"), None);
    let dal004: Vec<_> = diags.iter().filter(|d| d.code == "DAL004").collect();
    assert_eq!(dal004.len(), 1);
    assert_eq!(dal004[0].severity, Severity::Error);
    assert!(dal004[0].message.contains("Direct database mutation 'db.update()' on table 'tccom001'"));
}

#[test]
fn test_dal005_transaction_controls_in_dal_rejected() {
    let script = r#"
function extern long before.save.object(long mode)
{
    commit.transaction()
    return(0)
}
"#;
    let auditor = Auditor4GL::new();
    let diags = auditor.audit_content(script, "tccom001.dal", Some("dal2"), None);
    let dal005: Vec<_> = diags.iter().filter(|d| d.code == "DAL005").collect();
    assert_eq!(dal005.len(), 1);
    assert_eq!(dal005[0].severity, Severity::Error);
    assert!(dal005[0].message.contains("Transaction control 'commit.transaction()' is prohibited"));
}

#[test]
fn test_cld001_cloud_untrusted_function() {
    let script = r#"
#include <bic_cmf>

function void send_legacy_mail()
{
    cmf.create()
}
"#;
    let regular = Auditor4GL::new();
    let diags_reg = regular.audit_content(script, "myscript.cln", Some("general"), None);
    assert!(!diags_reg.iter().any(|d| d.code == "CLD001"));

    let cloud = Auditor4GL::new().with_cloud_mode(true);
    let diags_cloud = cloud.audit_content(script, "myscript.cln", Some("general"), None);
    let cld001: Vec<_> = diags_cloud.iter().filter(|d| d.code == "CLD001").collect();
    assert!(!cld001.is_empty());
    assert_eq!(cld001[0].severity, Severity::Error);
    assert!(cld001[0].message.contains("untrusted"));
}

#[test]
fn test_cld002_deprecated_function() {
    let script = r#"
function void do_field()
{
    add.view.field(1, "x")
}
"#;
    let auditor = Auditor4GL::new();
    let diags = auditor.audit_content(script, "myscript.cln", Some("general"), None);
    let cld002: Vec<_> = diags.iter().filter(|d| d.code == "CLD002").collect();
    assert!(!cld002.is_empty());
    assert_eq!(cld002[0].severity, Severity::Warning);
    assert!(cld002[0].message.contains("deprecated"));
}

#[test]
fn test_inc001_missing_include_header() {
    let script = r#"
function void process_json()
{
    Json.getString(0, "status")
}
"#;
    let auditor = Auditor4GL::new();
    let diags = auditor.audit_content(script, "myscript.cln", Some("general"), None);
    let inc001: Vec<_> = diags.iter().filter(|d| d.code == "INC001").collect();
    assert!(!inc001.is_empty());
    assert_eq!(inc001[0].severity, Severity::Warning);
    assert!(inc001.iter().any(|d| d.message.contains("bic_json")));
}

#[test]
fn test_cav001_anti_pattern_double_equality() {
    let script = r#"
function void calculate(double amount)
{
    if amount == 100.0 then
    endif
}
"#;
    let auditor = Auditor4GL::new();
    let diags = auditor.audit_content(script, "myscript.cln", Some("general"), None);
    let cav001: Vec<_> = diags.iter().filter(|d| d.code == "CAV001").collect();
    assert!(!cav001.is_empty());
    assert_eq!(cav001[0].severity, Severity::Warning);
    assert!(cav001[0].message.contains("floating-point"));
}

#[test]
fn test_syn001_unbalanced_block_detection() {
    let script = r#"
declaration:
    table ttcibd001

function void query_data()
{
    select tcibd001.*
    from tcibd001
    selectdo
        | missing endselect
}
"#;
    let auditor = Auditor4GL::new();
    let diags = auditor.audit_content(script, "myscript.cln", Some("general"), None);
    let syn001: Vec<_> = diags.iter().filter(|d| d.code == "SYN001").collect();
    assert!(!syn001.is_empty());
    assert_eq!(syn001[0].severity, Severity::Error);
    assert!(syn001[0].message.contains("Unclosed 'select' statement"));
}

#[test]
fn test_syn002_misspelled_section_header() {
    let script = r#"
declarashun:
    table ttcibd001
"#;
    let auditor = Auditor4GL::new();
    let diags = auditor.audit_content(script, "myscript.cln", Some("general"), None);
    let syn002: Vec<_> = diags.iter().filter(|d| d.code == "SYN002").collect();
    assert_eq!(syn002.len(), 1);
    assert_eq!(syn002[0].severity, Severity::Error);
    assert!(syn002[0].message.contains("Unrecognized or misspelled section header"));
    assert!(syn002[0].message.contains("declaration:"));
}

#[test]
fn test_str001_unsliced_logname() {
    let script = r#"
table ttxcmg010

function void set_user()
{
    txcmg010.user = logname$
}
"#;
    let regular = Auditor4GL::new();
    let diags_reg = regular.audit_content(script, "txcmg0110m100.cln", None, None);
    let str001_reg: Vec<_> = diags_reg.iter().filter(|d| d.code == "STR001").collect();
    assert_eq!(str001_reg.len(), 1);
    assert_eq!(str001_reg[0].severity, Severity::Warning);

    let cloud = Auditor4GL::new().with_cloud_mode(true);
    let diags_cloud = cloud.audit_content(script, "txcmg0110m100.cln", None, None);
    let str001_cloud: Vec<_> = diags_cloud.iter().filter(|d| d.code == "STR001").collect();
    assert_eq!(str001_cloud.len(), 1);
    assert_eq!(str001_cloud[0].severity, Severity::Error);
}

#[test]
fn test_str001_properly_sliced_logname() {
    let script = r#"
table ttxcmg010

function void set_user()
{
    txcmg010.user = strip$(shiftl$(logname$))(1; 16)
}
"#;
    let cloud = Auditor4GL::new().with_cloud_mode(true);
    let diags = cloud.audit_content(script, "txcmg0110m100.cln", None, None);
    assert!(!diags.iter().any(|d| d.code == "STR001"));
}

#[test]
fn test_dbg001_raw_message_in_ui_session() {
    let script = r#"
table ttxcmg010

function void do_something()
{
    message("befre insert %1s - ...", txcmg010.user)
}
"#;
    let auditor = Auditor4GL::new();
    let diags = auditor.audit_content(script, "txcmg0110m100.cln", Some("ui"), None);
    let dbg001: Vec<_> = diags.iter().filter(|d| d.code == "DBG001").collect();
    assert_eq!(dbg001.len(), 1);
    assert_eq!(dbg001[0].severity, Severity::Warning);
}

#[test]
fn test_sql008_array_subscript_in_host_variable() {
    let script = r#"
table ttfacr500

function void query_invoices(long i)
{
    select tfacr500.*
    from   tfacr500 for update
    where  tfacr500.ttyp = :mark_ttyp(1, i)
    and    tfacr500.ninv = :mark_ninv(i)
    selectdo
        commit.transaction()
    endselect
}
"#;
    let auditor = Auditor4GL::new();
    let diags = auditor.audit_content(script, "ttfacr500.cln", Some("general"), None);
    let sql008: Vec<_> = diags.iter().filter(|d| d.code == "SQL008").collect();
    assert_eq!(sql008.len(), 2);
    assert!(sql008.iter().all(|d| d.severity == Severity::Error));
}

#[test]
fn test_sql008_scalar_host_variables_pass() {
    let script = r#"
table ttfacr500

function void query_invoices()
{
    domain tfgld.ttyp l_ttyp
    domain tfgld.docn l_ninv

    select tfacr500.*
    from   tfacr500 for update
    where  tfacr500.fcom = :comp.num
    and    tfacr500.ttyp = :l_ttyp
    and    tfacr500.ninv = :l_ninv
    selectdo
        commit.transaction()
    endselect
}
"#;
    let auditor = Auditor4GL::new();
    let diags = auditor.audit_content(script, "ttfacr500.cln", Some("general"), None);
    assert!(!diags.iter().any(|d| d.code == "SQL008"));
}

#[test]
fn test_arr002_1d_domain_string_array_warning() {
    let script = r#"
domain tccom.bpid mark_itbp(500)
domain tcorno orders(10)
domain tfgld.ttyp mark_ttyp(MAX_MARKED_LINES)
"#;
    let auditor = Auditor4GL::new();
    let diags = auditor.audit_content(script, "txcmg0510m000.cln", None, None);
    let arr002: Vec<_> = diags.iter().filter(|d| d.code == "ARR002").collect();
    assert_eq!(arr002.len(), 3);
    assert!(arr002.iter().all(|d| d.severity == Severity::Warning));
}

#[test]
fn test_arr002_numeric_and_2d_string_arrays_pass() {
    let script = r#"
domain tcamnt period_totals(50)
domain tfgld.docn mark_ninv(500)
domain tfacr.trec mark_trec(500)
domain tcdate batch_dates(20)
string mark_itbp(9, 500)
domain tccom.bpid single_bp
"#;
    let auditor = Auditor4GL::new();
    let diags = auditor.audit_content(script, "txcmg0510m000.cln", None, None);
    assert!(!diags.iter().any(|d| d.code == "ARR002"));
}

#[test]
fn test_ast_parser_handles_define_macros_and_sql_subqueries() {
    let script = r#"
declaration:
    table ttdsls400
    table ttdsls401

#define OPEN_IF_VALID(x) \
    if (x) > 0 then \
        x = x + 1 \
    endif

function void complex_query()
{
    long cnt
    cnt = 1
    OPEN_IF_VALID(cnt)

    select tdsls400.*
    from tdsls400 for update
    where tdsls400._index1 = {"SO0001"}
    and exists (
        select tdsls401.*
        from tdsls401
        where tdsls401.orno = tdsls400.orno
        and tdsls401.pono = 10
    )
    selectdo
        cnt = cnt + 1
    endselect
}
"#;
    let auditor = Auditor4GL::new();
    let diags = auditor.audit_content(script, "tdsls400.cln", Some("general"), None);
    let syn001_errors: Vec<_> = diags.iter().filter(|d| d.code == "SYN001").collect();
    assert_eq!(syn001_errors.len(), 0, "Expected 0 SYN001 errors, got: {:?}", syn001_errors);
}

#[test]
fn test_tbl001_undeclared_table_and_main_table_exemption() {
    let script = r#"
declaration:
    table ttcibd001

function extern long before.save.object(long mode)
{
    if isspace(tdsls400.orno) then
        return(DALHOOKERROR)
    endif

    select tcibd001.item
    from tcibd001
    where tcibd001._index1 = {:tdsls401.item}
    selectdo
    endselect

    return(0)
}
"#;
    let auditor = Auditor4GL::new();
    let diags = auditor.audit_content(script, "tdsls400.dal", Some("dal2"), None);
    let tbl001: Vec<_> = diags.iter().filter(|d| d.code == "TBL001").collect();
    assert_eq!(tbl001.len(), 1);
    assert!(tbl001[0].message.contains("tdsls401"));

    let auditor_explicit = Auditor4GL::new().with_main_table("tdsls400");
    let diags_explicit = auditor_explicit.audit_content(script, "custom.cln", Some("general"), None);
    let tbl001_exp: Vec<_> = diags_explicit.iter().filter(|d| d.code == "TBL001").collect();
    assert_eq!(tbl001_exp.len(), 1);
    assert!(tbl001_exp[0].message.contains("tdsls401"));
}

#[test]
fn test_tbl002_and_dmn001_dd_cache_validation() {
    let mut cache = DataDictionaryCache::new();
    let mut fields = HashMap::new();
    fields.insert(
        "orno".to_string(),
        FieldMeta {
            name: "orno".to_string(),
            domain: Some("tcorno".to_string()),
            datatype: Some(serde_json::Value::String("string".to_string())),
            ..Default::default()
        },
    );
    fields.insert(
        "ofbp".to_string(),
        FieldMeta {
            name: "ofbp".to_string(),
            domain: Some("tccom.bpid".to_string()),
            datatype: Some(serde_json::Value::String("string".to_string())),
            ..Default::default()
        },
    );
    cache.update_table("tdsls400", fields, None, None);
    cache.update_domain("tcorno", Some("string"), Some(9), None);

    let script = r#"
declaration:
    table ttdsls400
    domain tcorno valid.orno
    domain tcfake.dmn bad.var

function void check_order()
{
    valid.orno = tdsls400.orno
    if isspace(tdsls400.hallucinated_field) then
    endif
}
"#;
    let auditor = Auditor4GL::new().with_dd_cache(cache);
    let diags = auditor.audit_content(script, "test.cln", Some("general"), None);

    let tbl002: Vec<_> = diags.iter().filter(|d| d.code == "TBL002").collect();
    let dmn001: Vec<_> = diags.iter().filter(|d| d.code == "DMN001").collect();

    assert_eq!(tbl002.len(), 1);
    assert!(tbl002[0].message.contains("tdsls400.hallucinated_field"));

    assert_eq!(dmn001.len(), 1);
    assert!(dmn001[0].message.contains("tcfake.dmn"));
}

#[test]
fn test_cav003_call_graph_direct_and_transitive_nested_tx() {
    let script = r#"
declaration:
    table ttdsls400

function void deep_helper_commit()
{
    commit.transaction()
}

function void middle_helper()
{
    deep_helper_commit()
}

function void outer_batch_process()
{
    db.retry.point()
    select tdsls400.*
    from tdsls400 for update
    selectdo
        db.update(ttdsls400, db.retry)
        middle_helper()
    selectempty
    endselect
    commit.transaction()
}
"#;
    let auditor = Auditor4GL::new();
    let diags = auditor.audit_content(script, "batch.cln", Some("general"), None);
    let cav003: Vec<_> = diags.iter().filter(|d| d.code == "CAV003").collect();
    assert!(!cav003.is_empty());
    assert!(cav003.iter().any(|d| d.message.contains("middle_helper")));
}

#[test]
fn test_ext001_include_boundary_and_missing_dam() {
    let script_outside = r#"
#include <bic_dam>
#context_on "declarations"
#include <bic_sessionext>
#context_off
"#;
    let auditor = Auditor4GL::new();
    let diags_outside = auditor.audit_content(script_outside, "whinh4131m000.cln", None, None);
    let ext001_outside: Vec<_> = diags_outside.iter().filter(|d| d.code == "EXT001" && d.message.contains("outside")).collect();
    assert!(!ext001_outside.is_empty());

    let script_missing_dal = r#"
#context_on "declarations"
#include <bic_sessionext>
#context_off
#context_on "function.run.before.command"
function extern void function.run.before.command()
{
    dal.change.object("whinh435")
}
#context_off
"#;
    let diags_missing = auditor.audit_content(script_missing_dal, "whinh4131m000.cln", None, None);
    let ext001_missing: Vec<_> = diags_missing.iter().filter(|d| d.code == "EXT001" && d.message.contains("Missing '#include <bic_dam>'")).collect();
    assert!(!ext001_missing.is_empty());

    let script_ok = r#"
#context_on "declarations"
#include <bic_sessionext>
#include <bic_dam>
#context_off
#context_on "function.run.before.command"
function extern void function.run.before.command()
{
    dal.change.object("whinh435")
}
#context_off
"#;
    let diags_ok = auditor.audit_content(script_ok, "whinh4131m000.cln", None, None);
    assert!(!diags_ok.iter().any(|d| d.code == "EXT001"));
}

#[test]
fn test_ext002_hook_scope_mismatch() {
    let script_tbl_with_cmd = r#"
#context_on "declarations"
table twhinh431
#include <bic_dal2>
#include <bic_tableext>
#context_off
#context_on "function.approve.before.command"
function extern void function.approve.before.command()
{
}
#context_off
"#;
    let auditor = Auditor4GL::new();
    let diags_tbl = auditor.audit_content(script_tbl_with_cmd, "whinh431.cln", None, None);
    let ext002_tbl: Vec<_> = diags_tbl.iter().filter(|d| d.code == "EXT002").collect();
    assert!(!ext002_tbl.is_empty());
    assert!(ext002_tbl.iter().any(|d| d.message.contains("Form Command hook")));

    let script_ses_with_dal = r#"
#context_on "declarations"
#include <bic_sessionext>
#context_off
#context_on "before.save.object"
function extern long before.save.object(long mode)
{
    return(0)
}
#context_off
"#;
    let diags_ses = auditor.audit_content(script_ses_with_dal, "whinh4131m000.cln", None, None);
    let ext002_ses: Vec<_> = diags_ses.iter().filter(|d| d.code == "EXT002").collect();
    assert!(!ext002_ses.is_empty());
    assert!(ext002_ses.iter().any(|d| d.message.contains("Table DAL hook")));
}

#[test]
fn test_ext003_standard_framework_function_protection_and_balance() {
    let script_custom_fn = r#"
#context_on "declarations"
#include <bic_sessionext>
#context_off

function extern void my_unwrapped_helper()
{
}
"#;
    let auditor = Auditor4GL::new();
    let diags_custom = auditor.audit_content(script_custom_fn, "whinh4131m000.cln", None, None);
    let ext003_custom: Vec<_> = diags_custom.iter().filter(|d| d.code == "EXT003" && d.message.contains("my_unwrapped_helper")).collect();
    assert!(!ext003_custom.is_empty());

    let script_unclosed = r#"
#context_on "declarations"
table ttdsls400
"#;
    let diags_unclosed = auditor.audit_content(script_unclosed, "txesttdsls400_ext.4gl", None, None);
    let ext003_unclosed: Vec<_> = diags_unclosed.iter().filter(|d| d.code == "EXT003" && d.message.contains("Unclosed")).collect();
    assert!(!ext003_unclosed.is_empty());

    let script_unmatched = r#"
#context_off
"#;
    let diags_unmatched = auditor.audit_content(script_unmatched, "txesttdsls400_ext.4gl", None, None);
    let ext003_unmatched: Vec<_> = diags_unmatched.iter().filter(|d| d.code == "EXT003" && d.message.contains("Unmatched")).collect();
    assert!(!ext003_unmatched.is_empty());
}

#[test]
fn test_dmn002_utc_assigned_to_date_field() {
    let script = r#"
table ttxcmg010

function void set_dates()
{
    txcmg010.docd = date.to.utc(2026, 11, 6, 0, 0, 0)
    txcmg010.dued = utc.num()
}
"#;
    let auditor = Auditor4GL::new();
    let diags = auditor.audit_content(script, "txcmg0110m100.cln", None, None);
    let dmn002: Vec<_> = diags.iter().filter(|d| d.code == "DMN002").collect();
    assert_eq!(dmn002.len(), 2);
    assert!(dmn002.iter().all(|d| d.severity == Severity::Error));
}

#[test]
fn test_tbl003_mandatory_numeric_assigned_zero() {
    let mut cache = DataDictionaryCache::new();
    let mut fields = HashMap::new();
    fields.insert(
        "line".to_string(),
        FieldMeta {
            name: "line".to_string(),
            datatype: Some(serde_json::Value::String("long".to_string())),
            is_mandatory: Some(true),
            ..Default::default()
        },
    );
    cache.update_table("txcmg010", fields, None, None);

    let script = r#"
table ttxcmg010
table ttfacr500

function void process_records()
{
    txcmg010.line = 0
    db.insert(ttxcmg010, db.retry)
}
"#;
    let auditor = Auditor4GL::new().with_dd_cache(cache);
    let diags = auditor.audit_content(script, "txcmg0110m100.cln", None, None);
    let tbl003: Vec<_> = diags.iter().filter(|d| d.code == "TBL003").collect();
    assert_eq!(tbl003.len(), 1);
    assert_eq!(tbl003[0].severity, Severity::Error);
    assert!(tbl003[0].message.contains("Error 205"));
}

#[test]
fn test_dmn003_cross_domain_and_literal_enum_comparisons() {
    let mut cache = DataDictionaryCache::new();
    let mut fields = HashMap::new();
    fields.insert(
        "cdf_stdd".to_string(),
        FieldMeta {
            name: "cdf_stdd".to_string(),
            domain: Some("txbsta".to_string()),
            datatype: Some(serde_json::Value::String("enum".to_string())),
            ..Default::default()
        },
    );
    cache.update_table("tfacr500", fields, None, None);

    let script_cross = r#"
table ttfacr500

function void check_status()
{
    if tfacr500.cdf_stdd <> tfcmg.stdd.selected then
        return
    endif
}
"#;
    let auditor = Auditor4GL::new().with_dd_cache(cache.clone());
    let diags_cross = auditor.audit_content(script_cross, "txcmg0110m100.cln", None, None);
    let dmn003_cross: Vec<_> = diags_cross.iter().filter(|d| d.code == "DMN003").collect();
    assert_eq!(dmn003_cross.len(), 1);
    assert_eq!(dmn003_cross[0].severity, Severity::Error);
    assert!(dmn003_cross[0].message.contains("Cross-domain"));

    let script_lit = r#"
table ttfacr500

function void check_status()
{
    if tfacr500.cdf_stdd == 1 then
        return
    endif
}
"#;
    let diags_lit = auditor.audit_content(script_lit, "txcmg0110m100.cln", None, None);
    let dmn003_lit: Vec<_> = diags_lit.iter().filter(|d| d.code == "DMN003").collect();
    assert_eq!(dmn003_lit.len(), 1);
    assert_eq!(dmn003_lit[0].severity, Severity::Error);
    assert!(dmn003_lit[0].message.contains("Integer literal"));

    let script_zero = r#"
table ttfacr500

function void check_status()
{
    if tfacr500.cdf_stdd == 0 then
        return
    endif
}
"#;
    let diags_zero = auditor.audit_content(script_zero, "txcmg0110m100.cln", None, None);
    let dmn003_zero: Vec<_> = diags_zero.iter().filter(|d| d.code == "DMN003").collect();
    assert_eq!(dmn003_zero.len(), 1);
    assert_eq!(dmn003_zero[0].severity, Severity::Warning);
}

#[test]
fn test_rayon_parallel_directory_audit() {
    let temp_dir = tempfile::tempdir().unwrap();
    let file1 = temp_dir.path().join("file1.cln");
    let file2 = temp_dir.path().join("file2.cln");

    let script1 = "declaration:\n    table ttcibd001\n";
    let script2 = "declarashun:\n    table ttcibd001\n";

    fs::write(&file1, script1).unwrap();
    fs::write(&file2, script2).unwrap();

    let auditor = Auditor4GL::new();
    let diags = auditor.audit_path(temp_dir.path(), Some("general")).unwrap();

    let syn002: Vec<_> = diags.iter().filter(|d| d.code == "SYN002").collect();
    assert_eq!(syn002.len(), 1);
}

