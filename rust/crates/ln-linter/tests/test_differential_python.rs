use std::io::Write;
use std::process::Command;
use serde::Deserialize;

use ln_linter::{Auditor4GL, DataDictionaryCache, Severity};

#[derive(Debug, Deserialize)]
#[allow(dead_code)]
struct PythonDiag {
    line: usize,
    severity: String,
    code: String,
    message: String,
}

#[derive(Debug, Deserialize)]
struct PythonReport {
    diagnostics: Vec<PythonDiag>,
}

fn run_python_audit(
    script: &str,
    file_ext: &str,
    mode: Option<&str>,
    cloud: bool,
    dd_cache_path: Option<&str>,
    main_table: Option<&str>,
) -> Vec<PythonDiag> {
    let mut temp = tempfile::Builder::new()
        .prefix("audit_test_")
        .suffix(file_ext)
        .tempfile()
        .unwrap();
    temp.write_all(script.as_bytes()).unwrap();
    let temp_path = temp.path().to_str().unwrap().to_string();

    let mut cmd = Command::new("python");
    cmd.arg("../../../erp-ln-progguide/scripts/audit_4gl.py")
        .arg(&temp_path)
        .arg("--format")
        .arg("json");

    if let Some(m) = mode {
        cmd.arg("--mode").arg(m);
    }
    if cloud {
        cmd.arg("--cloud");
    }
    if let Some(dd) = dd_cache_path {
        cmd.arg("--dd-cache").arg(dd);
    }
    if let Some(mt) = main_table {
        cmd.arg("--main-table").arg(mt);
    }

    let output = cmd.output().expect("Failed to run python audit_4gl.py");
    let stdout = String::from_utf8_lossy(&output.stdout);
    let report: PythonReport = serde_json::from_str(&stdout).unwrap_or_else(|e| {
        panic!("Failed to parse Python JSON output: {e}\nSTDOUT:\n{stdout}\nSTDERR:\n{}", String::from_utf8_lossy(&output.stderr));
    });

    report.diagnostics
}

#[test]
fn test_differential_all_25_rules_against_python() {
    let mut dd_temp = tempfile::Builder::new()
        .prefix("dd_cache_")
        .suffix(".json")
        .tempfile()
        .unwrap();

    let dd_json = r#"{
  "version": "1.0",
  "tables": {
    "tdsls400": {
      "name": "tdsls400",
      "fields": {
        "orno": {"name": "orno", "domain": "tcorno", "datatype": "string"}
      }
    },
    "txcmg010": {
      "name": "txcmg010",
      "fields": {
        "line": {"name": "line", "datatype": "long", "isMandatory": true}
      }
    },
    "tfacr500": {
      "name": "tfacr500",
      "fields": {
        "cdf_stdd": {"name": "cdf_stdd", "domain": "txbsta", "datatype": "enum"}
      }
    }
  },
  "domains": {
    "tcorno": {
      "name": "tcorno",
      "datatype": "string"
    }
  }
}"#;
    dd_temp.write_all(dd_json.as_bytes()).unwrap();
    let dd_path_str = dd_temp.path().to_str().unwrap().to_string();
    let dd_cache = DataDictionaryCache::from_path(dd_temp.path());

    let test_cases: Vec<(&str, &str, Option<&str>, bool, Option<&str>, Option<&str>, &str, Severity)> = vec![
        // (script, file_ext, mode, cloud, dd_cache_path, main_table, expected_rule_code, expected_severity)
        // 1. SYN001
        (
            r#"
declaration:
    table ttcibd001
function void q() {
    select tcibd001.*
    from tcibd001
    selectdo
}
"#,
            ".cln",
            Some("general"),
            false,
            None,
            None,
            "SYN001",
            Severity::Error,
        ),
        // 2. SYN002
        (
            r#"
declarashun:
    table ttcibd001
"#,
            ".cln",
            Some("general"),
            false,
            None,
            None,
            "SYN002",
            Severity::Error,
        ),
        // 3. INC001
        (
            r#"
function void process_json() {
    Json.getString(0, "status")
}
"#,
            ".cln",
            Some("general"),
            false,
            None,
            None,
            "INC001",
            Severity::Warning,
        ),
        // 4. ARR002
        (
            r#"
domain tccom.bpid mark_itbp(500)
"#,
            ".cln",
            Some("general"),
            false,
            None,
            None,
            "ARR002",
            Severity::Warning,
        ),
        // 5. SQL008
        (
            r#"
table ttfacr500
function void q() {
    select tfacr500.*
    from tfacr500
    where tfacr500.ttyp = :mark_ttyp(1)
    selectdo
    endselect
}
"#,
            ".cln",
            Some("general"),
            false,
            None,
            None,
            "SQL008",
            Severity::Error,
        ),
        // 6. STR001
        (
            r#"
table ttxcmg010
function void set_user() {
    txcmg010.user = logname$
}
"#,
            ".cln",
            Some("general"),
            true,
            None,
            None,
            "STR001",
            Severity::Error,
        ),
        // 7. CAV001
        (
            r#"
function void calc(double x) {
    if x == 100.0 then
    endif
}
"#,
            ".cln",
            Some("general"),
            false,
            None,
            None,
            "CAV001",
            Severity::Warning,
        ),
        // 8. DBG001
        (
            r#"
function void do_msg() {
    message("hello")
}
"#,
            ".cln",
            Some("general"),
            false,
            None,
            None,
            "DBG001",
            Severity::Warning,
        ),
        // 9. CLD001
        (
            r#"
#include <bic_cmf>
function void send_legacy_mail() {
    cmf.create()
}
"#,
            ".cln",
            Some("general"),
            true,
            None,
            None,
            "CLD001",
            Severity::Error,
        ),
        // 10. CLD002
        (
            r#"
function void do_field() {
    add.view.field(1, "x")
}
"#,
            ".cln",
            Some("general"),
            false,
            None,
            None,
            "CLD002",
            Severity::Warning,
        ),
        // 11. DAL001
        (
            r#"
function extern long before.save.object(long mode) {
    message("popup")
    return(0)
}
"#,
            ".dal",
            Some("dal2"),
            false,
            None,
            None,
            "DAL001",
            Severity::Error,
        ),
        // 12. DAL002
        (
            r#"
function extern void item.update() {
}
"#,
            ".dal",
            Some("dal2"),
            false,
            None,
            None,
            "DAL002",
            Severity::Error,
        ),
        // 13. DAL003
        (
            r#"
function extern void function.approve.before.command() {
    return(true)
}
"#,
            ".cln",
            Some("general"),
            false,
            None,
            None,
            "DAL003",
            Severity::Error,
        ),
        // 14. DAL004
        (
            r#"
table ttccom001
function void do_mut() {
    db.update(ttccom001, db.retry)
}
"#,
            ".cln",
            Some("general"),
            false,
            None,
            None,
            "DAL004",
            Severity::Error,
        ),
        // 15. DAL005
        (
            r#"
function extern long before.save.object(long mode) {
    commit.transaction()
    return(0)
}
"#,
            ".dal",
            Some("dal2"),
            false,
            None,
            None,
            "DAL005",
            Severity::Error,
        ),
        // 16. CAV003
        (
            r#"
declaration:
    table ttdsls400
function void deep_commit() {
    commit.transaction()
}
function void middle() {
    deep_commit()
}
function void outer() {
    db.retry.point()
    middle()
    commit.transaction()
}
"#,
            ".cln",
            Some("general"),
            false,
            None,
            None,
            "CAV003",
            Severity::Error,
        ),
        // 17. TBL001
        (
            r#"
declaration:
    table ttcibd001
function void do_query() {
    select tcibd001.item
    from tcibd001
    where tcibd001.item = :tdsls401.item
    selectdo
    endselect
}
"#,
            ".cln",
            Some("general"),
            false,
            None,
            None,
            "TBL001",
            Severity::Error,
        ),
        // 18. TBL002
        (
            r#"
declaration:
    table ttdsls400
function void check_order() {
    if isspace(tdsls400.hallucinated_field) then
    endif
}
"#,
            ".cln",
            Some("general"),
            false,
            Some(&dd_path_str),
            None,
            "TBL002",
            Severity::Error,
        ),
        // 19. TBL003
        (
            r#"
table ttxcmg010
function void process_records() {
    txcmg010.line = 0
    db.insert(ttxcmg010, db.retry)
}
"#,
            ".cln",
            Some("general"),
            false,
            Some(&dd_path_str),
            None,
            "TBL003",
            Severity::Error,
        ),
        // 20. DMN001
        (
            r#"
declaration:
    domain tcfake.dmn bad.var
"#,
            ".cln",
            Some("general"),
            false,
            Some(&dd_path_str),
            None,
            "DMN001",
            Severity::Error,
        ),
        // 21. DMN002
        (
            r#"
table ttxcmg010
function void set_dates() {
    txcmg010.docd = date.to.utc(2026, 11, 6, 0, 0, 0)
}
"#,
            ".cln",
            Some("general"),
            false,
            None,
            None,
            "DMN002",
            Severity::Error,
        ),
        // 22. DMN003
        (
            r#"
table ttfacr500
function void check_status() {
    if tfacr500.cdf_stdd <> tfcmg.stdd.selected then
    endif
}
"#,
            ".cln",
            Some("general"),
            false,
            Some(&dd_path_str),
            None,
            "DMN003",
            Severity::Error,
        ),
        // 23. EXT001
        (
            r#"
#include <bic_dam>
#context_on "declarations"
#include <bic_sessionext>
#context_off
"#,
            "whinh4131m000.cln",
            None,
            false,
            None,
            None,
            "EXT001",
            Severity::Error,
        ),
        // 24. EXT002
        (
            r#"
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
"#,
            "whinh431.cln",
            None,
            false,
            None,
            None,
            "EXT002",
            Severity::Error,
        ),
        // 25. EXT003
        (
            r#"
#context_on "declarations"
#include <bic_sessionext>
#context_off
function extern void my_unwrapped_helper()
{
}
"#,
            "whinh4131m000.cln",
            None,
            false,
            None,
            None,
            "EXT003",
            Severity::Error,
        ),
    ];

    for (script, file_ext, mode, cloud, dd_path, main_table, expected_code, expected_sev) in test_cases {
        // Run Python
        let py_diags = run_python_audit(script, file_ext, mode, cloud, dd_path, main_table);
        let py_matches: Vec<_> = py_diags.iter().filter(|d| d.code == expected_code).collect();
        assert!(
            !py_matches.is_empty(),
            "Python failed to detect rule {expected_code} on script:\n{script}"
        );
        let py_rule = py_matches[0];
        assert_eq!(
            py_rule.severity,
            expected_sev.as_str(),
            "Python severity mismatch for {expected_code}"
        );

        // Run Rust
        let mut auditor = Auditor4GL::new().with_cloud_mode(cloud);
        if dd_path.is_some() {
            auditor = auditor.with_dd_cache(dd_cache.clone());
        }
        if let Some(mt) = main_table {
            auditor = auditor.with_main_table(mt);
        }
        let dummy_path = if file_ext.starts_with('.') {
            format!("test_file{file_ext}")
        } else {
            file_ext.to_string()
        };
        let rust_diags = auditor.audit_content(script, &dummy_path, mode, None);
        let rust_matches: Vec<_> = rust_diags.iter().filter(|d| d.code == expected_code).collect();
        assert!(
            !rust_matches.is_empty(),
            "Rust failed to detect rule {expected_code} on script:\n{script}\nGot diags: {:?}",
            rust_diags
        );
        let rust_rule = &rust_matches[0];
        assert_eq!(
            rust_rule.severity,
            expected_sev,
            "Rust severity mismatch for {expected_code}"
        );
        assert_eq!(
            rust_rule.line, py_rule.line,
            "Line number mismatch for rule {expected_code}: Python line {} vs Rust line {}",
            py_rule.line, rust_rule.line
        );
    }
}
