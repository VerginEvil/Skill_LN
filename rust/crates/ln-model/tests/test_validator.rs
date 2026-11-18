use std::fs;
use tempfile::tempdir;

use ln_eclipse_compat::AdminFile;
use ln_model::{generate_label_xml, generate_label_xml_with_context};
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

#[test]
fn test_validate_real_server_tbl_with_datatype_and_indexcolumn() {
    let tmp = tempdir().unwrap();
    let act = tmp.path();

    let tbl_path = act.join("tx").join("etable").join("cmg").join("cmg011.tbl");
    fs::create_dir_all(tbl_path.parent().unwrap()).unwrap();
    let tbl_xml = r#"<?xml version="1.0" encoding="UTF-8" standalone="no"?><DR_Table><name>cmg011</name><Column><Audited>true</Audited><Mandatory>true</Mandatory><datatype><DatatypeReference><name>tfgld.btno</name><type>domain</type></DatatypeReference></datatype><label><LabelReference><name>txcmg011.btno</name><type>label</type></LabelReference></label><nativeDatatype>3</nativeDatatype><type>simple</type><name>btno</name></Column><Index><Active>true</Active><AllowDuplicates>false</AllowDuplicates><IndexColumn><sortingOrder>ascending</sortingOrder><column>btno</column><position>1</position></IndexColumn><name>1</name></Index></DR_Table>"#;
    fs::write(&tbl_path, tbl_xml).unwrap();

    let ses_path = act.join("tx").join("esess").join("cmg").join("cmg0512m000.ses");
    fs::create_dir_all(ses_path.parent().unwrap()).unwrap();
    let ses_xml = r#"<?xml version="1.0" encoding="UTF-8" standalone="no"?><DR_Session><name>cmg0512m000</name><toTable>txcmg011</toTable><FormField><fieldName>txcmg011.btno</fieldName></FormField></DR_Session>"#;
    fs::write(&ses_path, ses_xml).unwrap();

    let mut af = AdminFile::new();
    af.after_get("tx/etable/cmg/cmg011.tbl");
    af.after_get("tx/esess/cmg/cmg0512m000.ses");
    af.save_to_path(&act.join(".admin")).unwrap();

    let report = validate_activity(act, false, false);
    assert!(
        report.errors().is_empty(),
        "Expected 0 errors on valid server .tbl/.ses XML, got: {:?}",
        report.errors()
    );
    assert!(
        report.warnings().is_empty(),
        "Expected 0 warnings on valid server .tbl/.ses XML, got: {:?}",
        report.warnings()
    );
}

#[test]
fn test_validate_real_workspace_dev_natt_v01108() {
    let Ok(real_act_str) = std::env::var("LN_TEST_REAL_ACTIVITY") else {
        eprintln!("[SKIP] LN_TEST_REAL_ACTIVITY not set");
        return;
    };
    let real_act = std::path::Path::new(&real_act_str);
    if !real_act.exists() {
        eprintln!("[SKIP] Real activity not found at {:?}", real_act);
        return;
    }

    let report = validate_activity(real_act, false, false);
    let non_layer4_errors: Vec<_> = report
        .errors()
        .into_iter()
        .filter(|d| d.layer != 4)
        .collect();
    assert!(
        non_layer4_errors.is_empty(),
        "Expected 0 Layer 1/2/3 errors on real activity dev_natt_v01108-1, got: {:?}",
        non_layer4_errors
    );

    let tbl_or_ses_errors: Vec<_> = report
        .errors()
        .into_iter()
        .filter(|d| !d.file_path.ends_with("txesssli2620m0.lib"))
        .collect();
    assert!(
        tbl_or_ses_errors.is_empty(),
        "Expected 0 errors outside txesssli2620m0.lib on dev_natt_v01108-1, got: {:?}",
        tbl_or_ses_errors
    );
}

#[test]
fn test_layer2_rejects_multiline_xml_and_fix_compacts_single_line() {
    let td = tempfile::tempdir().unwrap();
    let act = td.path().join("dev_test [EXTce01108]");
    let lbl_dir = act.join("tx").join("label");
    let tbl_dir = act.join("tx").join("table").join("inr");
    fs::create_dir_all(&lbl_dir).unwrap();
    fs::create_dir_all(&tbl_dir).unwrap();
    fs::write(act.join(".project"), "<projectDescription/>").unwrap();
    AdminFile::new().save_to_path(&act.join(".admin")).unwrap();

    let bad_lbl = lbl_dir.join("txinr.bad.lbl");
    fs::write(
        &bad_lbl,
        "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<DR_Label>\n  <name>txinr.bad</name>\n</DR_Label>\n",
    )
    .unwrap();
    fs::write(
        tbl_dir.join("txinr110.tbl"),
        r#"<?xml version="1.0" encoding="UTF-8" standalone="no"?><DR_Table><name>txinr110</name><descriptionReference>txinr.missing</descriptionReference><Column><name>item</name><datatype><nativeDatatype>6</nativeDatatype></datatype></Column><Index><IndexColumn><name>item</name></IndexColumn></Index></DR_Table>"#,
    )
    .unwrap();

    let report = validate_activity(&act, false, false);
    assert!(
        report.errors().iter().any(|d| d.layer == 2 && (d.message.to_lowercase().contains("single-line") || d.message.to_lowercase().contains("whitespace"))),
        "Expected Layer 2 single-line error, got: {:?}",
        report.errors()
    );

    validate_activity(&act, false, true);
    let fixed_bad = fs::read_to_string(&bad_lbl).unwrap();
    assert!(!fixed_bad.contains('\n'), "Expected --fix to compact writable pretty-printed XML");
    let created = fs::read_to_string(lbl_dir.join("txinr.missing.lbl")).unwrap();
    assert!(created.starts_with(r#"<?xml version="1.0" encoding="UTF-8" standalone="no"?>"#));
    assert!(created.contains("<LabelVariant>"));
    assert!(!created.contains('\n'));
}

#[test]
fn test_layer3_collects_child_description_references_and_checks_reference_labels() {
    let td = tempfile::tempdir().unwrap();
    let ws = td.path();
    let ref_lbl = ws.join(".reference").join("label");
    fs::create_dir_all(&ref_lbl).unwrap();
    fs::write(
        ref_lbl.join("txwh.cwar.lbl"),
        generate_label_xml("txwh.cwar", "Warehouse", "B61O_a_ext", "EXTce01108", None, None),
    )
    .unwrap();

    let act = ws.join("dev_test [EXTce01108]");
    let tbl_dir = act.join("tx").join("table").join("inr");
    let ses_dir = act.join("tx").join("session").join("inr");
    let lbl_dir = act.join("tx").join("label");
    fs::create_dir_all(&tbl_dir).unwrap();
    fs::create_dir_all(&ses_dir).unwrap();
    fs::create_dir_all(&lbl_dir).unwrap();
    fs::write(act.join(".project"), "<projectDescription/>").unwrap();
    AdminFile::new().save_to_path(&act.join(".admin")).unwrap();

    fs::write(
        lbl_dir.join("txinr110.lbl"),
        generate_label_xml_with_context("txinr110", "Tbl", "B61O_a_ext", "EXTce01108", None, None, 2),
    )
    .unwrap();
    fs::write(
        lbl_dir.join("txinr1110m000.lbl"),
        generate_label_xml_with_context("txinr1110m000", "Ses", "B61O_a_ext", "EXTce01108", None, None, 2),
    )
    .unwrap();

    fs::write(
        tbl_dir.join("txinr110.tbl"),
        r#"<?xml version="1.0" encoding="UTF-8" standalone="no"?><DR_Table><name>txinr110</name><descriptionReference>txinr110</descriptionReference><Column><name>col1</name><descriptionReference>txinr110.missingcol</descriptionReference><datatype><nativeDatatype>6</nativeDatatype></datatype></Column><Index><name>1</name><descriptionReference>txinr110001</descriptionReference><IndexColumn><name>col1</name></IndexColumn></Index></DR_Table>"#,
    )
    .unwrap();

    fs::write(
        ses_dir.join("txinr1110m000.ses"),
        r#"<?xml version="1.0" encoding="UTF-8" standalone="no"?><DR_Controller><name>txinr1110m000</name><descriptionReference>txinr1110m000</descriptionReference><FormCommand><name>cmd1</name><descriptionReference>txinr.missingcmd</descriptionReference></FormCommand><Form><PhysicalFormLayout><FormField><fieldName>wh.cwar</fieldName><fieldLabel>wh.cwar</fieldLabel></FormField></PhysicalFormLayout></Form></DR_Controller>"#,
    )
    .unwrap();

    let report = validate_activity(&act, false, false);
    let msgs: Vec<String> = report.errors().into_iter().filter(|d| d.layer == 3).map(|d| d.message.clone()).collect();
    assert!(msgs.iter().any(|m| m.contains("txinr110.missingcol")), "Missing Column child descriptionReference: {msgs:?}");
    assert!(msgs.iter().any(|m| m.contains("txinr110001")), "Missing Index child descriptionReference: {msgs:?}");
    assert!(msgs.iter().any(|m| m.contains("txinr.missingcmd")), "Missing FormCommand child descriptionReference: {msgs:?}");
    assert!(!msgs.iter().any(|m| m.contains("wh.cwar")), "Should resolve txwh.cwar from .reference/label/: {msgs:?}");

    // Also add fieldLabel referencing missing inr.fldfix and verify --fix auto-creates txinr.fldfix.lbl
    fs::write(
        ses_dir.join("txinr1110m000.ses"),
        r#"<?xml version="1.0" encoding="UTF-8" standalone="no"?><DR_Controller><name>txinr1110m000</name><descriptionReference>txinr1110m000</descriptionReference><Form><PhysicalFormLayout><FormField><fieldName>txinr110.fldfix</fieldName><fieldLabel>inr.fldfix</fieldLabel></FormField></PhysicalFormLayout></Form></DR_Controller>"#,
    )
    .unwrap();
    let _ = validate_activity(&act, false, true);
    assert!(lbl_dir.join("txinr.fldfix.lbl").is_file(), "Expected --fix to create missing label from fieldLabel");
}
