use std::fs;
use std::process::Command;
use tempfile::tempdir;

use ln_eclipse_compat::AdminFile;
use ln_model::validator::validate_activity;

#[test]
fn test_differential_parity_against_python_validator() {
    let tmp = tempdir().unwrap();
    let act = tmp.path();

    let admin_file = act.join(".admin");
    let mut af = AdminFile::new();

    // Create a package layout with multiple components
    // 1. Table with valid index and columns, but referencing a missing label 'txcmg011.desc'
    let tbl_path = act.join("tx").join("table").join("cmg").join("txcmg011.tbl");
    fs::create_dir_all(tbl_path.parent().unwrap()).unwrap();
    let tbl_xml = r#"<?xml version="1.0" encoding="UTF-8"?>
<DR_Table xmlns="http://www.infor.com/businessline/application/dr" version="1.0">
  <name>txcmg011</name>
  <descriptionReference>txcmg011.desc</descriptionReference>
  <Column>
    <name>orno</name>
    <nativeDatatype>3</nativeDatatype>
  </Column>
  <Index>
    <name>1</name>
    <IndexColumn><name>orno</name></IndexColumn>
  </Index>
</DR_Table>"#;
    fs::write(&tbl_path, tbl_xml).unwrap();
    af.after_create("tx/table/cmg/txcmg011.tbl");

    // 2. Session with a FormGroup hierarchy error
    let ses_path = act.join("tx").join("session").join("cmg").join("txcmg0100m000.ses");
    fs::create_dir_all(ses_path.parent().unwrap()).unwrap();
    let ses_xml = r#"<?xml version="1.0" encoding="UTF-8"?>
<DR_Controller xmlns="http://www.infor.com/businessline/application/dr" version="1.0">
  <name>txcmg0100m000</name>
  <toTable>txcmg011</toTable>
  <FormGroup>
    <groupNumber>1</groupNumber>
    <parentGroup>999</parentGroup>
  </FormGroup>
</DR_Controller>"#;
    fs::write(&ses_path, ses_xml).unwrap();
    af.after_create("tx/session/cmg/txcmg0100m000.ses");

    // 3. Save .admin
    af.save_to_path(&admin_file).unwrap();

    // 4. Run Rust validator
    let rust_report = validate_activity(act, false, false);

    // 5. Run Python validator
    let python_script = std::path::Path::new("../../../ln_studio_skill/tools/validate_ln_activity.py");
    let repo_root = fs::canonicalize(python_script)
        .expect("Should locate validate_ln_activity.py");

    let py_output = Command::new("python")
        .arg(&repo_root)
        .arg(act)
        .arg("--json")
        .output()
        .expect("Should execute Python validator");

    let py_json_str = String::from_utf8_lossy(&py_output.stdout);
    let py_json: serde_json::Value = serde_json::from_str(&py_json_str)
        .unwrap_or_else(|_| panic!("Failed to parse Python validator output: {}", py_json_str));

    // Compare results
    let py_errors = py_json["errors_count"].as_u64().unwrap_or(0);
    let rust_errors = rust_report.errors().len() as u64;

    assert_eq!(
        rust_errors, py_errors,
        "Error counts between Rust ({}) and Python ({}) should match!",
        rust_errors, py_errors
    );

    // Verify both detected the missing label txcmg011.desc (Layer 3)
    let rust_has_missing_label = rust_report.errors().iter().any(|d| d.layer == 3 && d.message.contains("txcmg011.desc"));
    assert!(rust_has_missing_label, "Rust should detect missing label txcmg011.desc");

    let py_diags = py_json["diagnostics"].as_array().unwrap();
    let py_has_missing_label = py_diags.iter().any(|d| {
        let msg = d["message"].as_str().unwrap_or("");
        msg.contains("Layer 3") && msg.contains("txcmg011.desc")
    });
    assert!(py_has_missing_label, "Python should detect missing label txcmg011.desc");

    // Verify both detected the non-existent parentGroup 999 (Layer 2)
    let rust_has_grp_err = rust_report.errors().iter().any(|d| d.layer == 2 && d.message.contains("non-existent parentGroup '999'"));
    assert!(rust_has_grp_err, "Rust should detect non-existent parentGroup '999'");

    let py_has_grp_err = py_diags.iter().any(|d| {
        let msg = d["message"].as_str().unwrap_or("");
        msg.contains("Layer 2") && msg.contains("non-existent parentGroup '999'")
    });
    assert!(py_has_grp_err, "Python should detect non-existent parentGroup '999'");
}
