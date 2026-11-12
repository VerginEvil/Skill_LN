use std::fs;
use tempfile::tempdir;

use ln_eclipse_compat::AdminFile;
use ln_model::validator::validate_activity;

#[test]
fn test_validator_layer1_layout_and_admin() {
    let tmp = tempdir().unwrap();
    let act = tmp.path();

    // 1. Missing .admin
    let report1 = validate_activity(act, false, false);
    assert!(report1.warnings().iter().any(|d| d.layer == 1 && d.message.contains("missing .admin")));

    // 2. Initialize .admin
    let admin_file = act.join(".admin");
    let af = AdminFile::new();
    af.save_to_path(&admin_file).unwrap();

    // 3. Add legacy plural directory (ADR 0012 violation)
    let plural_tbl = act.join("tx").join("tables").join("cmg").join("txcmg011.tbl");
    fs::create_dir_all(plural_tbl.parent().unwrap()).unwrap();
    fs::write(&plural_tbl, "<DR_Table><name>txcmg011</name></DR_Table>").unwrap();

    let report2 = validate_activity(act, false, false);
    assert!(report2.errors().iter().any(|d| d.layer == 1 && d.message.contains("Legacy plural directory structure detected")));
}

#[test]
fn test_validator_layer2_layer3_and_layer4() {
    let tmp = tempdir().unwrap();
    let act = tmp.path();

    let admin_file = act.join(".admin");
    let mut af = AdminFile::new();

    // Add table with invalid nativeDatatype (Layer 2 violation) and missing index (Layer 2)
    let tbl_path = act.join("tx").join("table").join("cmg").join("txcmg011.tbl");
    fs::create_dir_all(tbl_path.parent().unwrap()).unwrap();
    let tbl_xml = r#"<?xml version="1.0" encoding="UTF-8"?>
<DR_Table xmlns="http://www.infor.com/businessline/application/dr">
  <name>txcmg011</name>
  <descriptionReference>txcmg011.title</descriptionReference>
  <Column>
    <name>orno</name>
    <nativeDatatype>999</nativeDatatype>
  </Column>
  <DR_Module>
    <Source>
      <expression><![CDATA[
function extern long broken_func()
{
    // SYN001: Unbalanced bracket
    if true then
    return(0)
}
]]></expression>
    </Source>
  </DR_Module>
</DR_Table>"#;
    fs::write(&tbl_path, tbl_xml).unwrap();
    af.after_create("tx/table/cmg/txcmg011.tbl");
    af.save_to_path(&admin_file).unwrap();

    let report = validate_activity(act, false, false);

    // Layer 2: invalid datatype 999 and table missing index
    assert!(report.errors().iter().any(|d| d.layer == 2 && d.message.contains("invalid nativeDatatype 999")));
    assert!(report.errors().iter().any(|d| d.layer == 2 && d.message.contains("must define at least one <Index>")));

    // Layer 3: referenced label 'txcmg011.title' not found in activity label catalog
    assert!(report.errors().iter().any(|d| d.layer == 3 && d.message.contains("Referenced label 'txcmg011.title' not found")));

    // Layer 4: SYN001 syntax error in 4GL script
    assert!(report.diagnostics.iter().any(|d| d.layer == 4 && (d.message.contains("SYN001") || d.message.contains("Unbalanced") || d.message.contains("if"))));
}

#[test]
fn test_validator_safe_fix_mode() {
    let tmp = tempdir().unwrap();
    let act = tmp.path();

    let admin_file = act.join(".admin");
    let af = AdminFile::new();
    af.save_to_path(&admin_file).unwrap();

    // Create a table referencing missing label 'txcmg011.title'
    let tbl_path = act.join("tx").join("table").join("cmg").join("txcmg011.tbl");
    fs::create_dir_all(tbl_path.parent().unwrap()).unwrap();
    let tbl_xml = r#"<?xml version="1.0" encoding="UTF-8"?>
<DR_Table xmlns="http://www.infor.com/businessline/application/dr">
  <name>txcmg011</name>
  <descriptionReference>txcmg011.title</descriptionReference>
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

    // Notice we do NOT register it in .admin yet (testing untracked auto-sync)

    let report_before = validate_activity(act, false, false);
    assert!(report_before.errors().iter().any(|d| d.layer == 3 && d.message.contains("Referenced label 'txcmg011.title' not found")));
    assert!(report_before.warnings().iter().any(|d| d.layer == 1 && d.message.contains("not registered in .admin")));

    // Now run with fix: true
    let report_fixed = validate_activity(act, false, true);
    assert!(!report_fixed.repaired_items.is_empty(), "Repairs should have been recorded");

    // Verify missing label was created
    let fixed_lbl_file = act.join("tx").join("label").join("txcmg011.title.lbl");
    assert!(fixed_lbl_file.is_file(), "Missing label file should be auto-created");
    let lbl_xml = fs::read_to_string(&fixed_lbl_file).unwrap();
    assert!(lbl_xml.contains("<name>txcmg011.title</name>"));

    // Verify .admin was synced
    let af_after = AdminFile::load_from_path(&admin_file).unwrap();
    assert!(af_after.entries.contains_key("tx/table/cmg/txcmg011.tbl") || af_after.entries.contains_key("tx\\table\\cmg\\txcmg011.tbl"));
}
