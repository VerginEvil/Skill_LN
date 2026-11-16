use std::fs;
use tempfile::tempdir;

use ln_scm::extension::*;

#[test]
fn test_new_extension_scaffolding() {
    let td = tempdir().unwrap();
    let root = td.path();

    // 1. Table Extension
    let tbl_path = new_extension("table", "whwmd400", None, "Alice", Some(root)).unwrap();
    assert!(tbl_path.exists());
    assert!(tbl_path.ends_with("extensions/table/whwmd400_ext.4gl") || tbl_path.ends_with("extensions\\table\\whwmd400_ext.4gl"));

    let tbl_code = fs::read_to_string(&tbl_path).unwrap();
    assert!(tbl_code.contains("Extension Script for Table whwmd400"));
    assert!(tbl_code.contains("Author: Alice"));
    assert!(tbl_code.contains("table   twhwmd400"));
    assert!(tbl_code.contains("#include <bic_dal2>"));
    assert!(tbl_code.contains("#include <bic_tableext>"));
    assert!(tbl_code.contains("#context_on \"declarations\""));
    assert!(tbl_code.contains("#context_on \"method.is.allowed\""));

    // 2. Session Extension
    let ses_path = new_extension("session", "whwmd4300m000", None, "Bob", Some(root)).unwrap();
    assert!(ses_path.exists());
    assert!(ses_path.ends_with("extensions/session/whwmd4300m000_ext.4gl") || ses_path.ends_with("extensions\\session\\whwmd4300m000_ext.4gl"));

    let ses_code = fs::read_to_string(&ses_path).unwrap();
    assert!(ses_code.contains("Extension Script for Session whwmd4300m000"));
    assert!(ses_code.contains("Author: Bob"));
    assert!(ses_code.contains("#include <bic_sessionext>"));
    assert!(ses_code.contains("#context_on \"function.custom.action.before.command\""));
}

#[test]
fn test_parse_and_clean_extension_hooks() {
    let td = tempdir().unwrap();
    let root = td.path();
    let tbl_path = new_extension("table", "whwmd400", None, "Developer", Some(root)).unwrap();
    let content = fs::read_to_string(&tbl_path).unwrap();

    let hooks = parse_extension_hooks(&content);
    assert!(hooks.len() >= 6);

    let decl_hook = get_hook(&content, "declarations").expect("declarations hook must be found");
    assert_eq!(decl_hook.name, "declarations");
    let clean = decl_hook.clean_code();
    assert!(!clean.contains("#context_on"));
    assert!(!clean.contains("#context_off"));
    assert!(clean.contains("table   twhwmd400"));
    assert!(clean.contains("#include <bic_dal2>"));

    let summaries = list_hooks(&content);
    assert_eq!(summaries.len(), hooks.len());
    assert_eq!(summaries[0].name, "declarations");
    assert!(summaries[0].code_lines >= 3);
}

#[test]
fn test_guide_and_paste_protocol_formatting() {
    let td = tempdir().unwrap();
    let root = td.path();
    let tbl_path = new_extension("table", "whwmd400", None, "Developer", Some(root)).unwrap();

    let guide_md = format_guide_and_paste_protocol(&tbl_path).unwrap();
    assert!(guide_md.contains("# Agent Guide-and-Paste Protocol (Infor LN Extension Modeler)"));
    assert!(guide_md.contains("ttext1500m000"));
    assert!(guide_md.contains("whwmd400_ext"));
    assert!(guide_md.contains("### Hook 1/"));
    assert!(guide_md.contains("`declarations`"));
    assert!(guide_md.contains("```4gl"));
    assert!(guide_md.contains("table   twhwmd400"));
}

#[test]
fn test_import_extension_from_xml() {
    let td = tempdir().unwrap();
    let root = td.path();

    let xml_file = root.join("txestwhwmd400.lib");
    let xml_content = r#"<DR_Module>
  <Source>
    <expression><![CDATA[
#context_on "declarations"
table twhwmd400
#include <bic_dal2>
#context_off
    ]]></expression>
  </Source>
</DR_Module>"#;
    fs::write(&xml_file, xml_content).unwrap();

    let imported_path = import_extension(&xml_file, None, None, Some(root)).unwrap();
    assert!(imported_path.exists());
    assert!(imported_path.ends_with("whwmd400_ext.4gl"));

    let imported_code = fs::read_to_string(&imported_path).unwrap();
    assert!(imported_code.contains("#context_on \"declarations\""));
    assert!(imported_code.contains("table twhwmd400"));
}

#[test]
fn test_extension_linter_validation() {
    // 1. Nested #context_on triggers EXT003
    let bad_nested = r#"
#context_on "declarations"
#include <bic_dal2>
#context_on "inner"
long x
#context_off
#context_off
"#;
    let diags = lint_extension_source(bad_nested, "txestwhwmd400.4gl");
    assert!(diags.iter().any(|d| d.code == "EXT003" && d.message.contains("Nested")));

    // 2. Table DAL hook in Session Extension triggers EXT002
    let bad_session = r#"
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
    let diags = lint_extension_source(bad_session, "txesswhwmd4300m000.4gl");
    assert!(diags.iter().any(|d| d.code == "EXT002" && d.message.contains("Table DAL hook")));
}
