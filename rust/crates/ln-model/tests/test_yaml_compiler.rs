use std::fs;
use tempfile::tempdir;
use ln_model::*;
use ln_eclipse_compat::admin::AdminFile;

const SAMPLE_YAML: &str = r#"
version_id: B61O_a_ext
application: EXTce01107

domains:
  - name: txcmg.remk
    package: tx
    datatype: string
    length: 100
    description: Billing Remarks
  - name: txcmg.stat
    package: tx
    datatype: enum
    description: Batch Status
    constants:
      - { value: 1, name: open, label: Open }
      - { value: 2, name: approved, label: Approved }
      - { value: 3, name: closed, label: Closed }

tables:
  - code: txcmg011
    description: Billing Batch Header
    package: tx
    module: cmg
    fields:
      - name: btno
        domain: tcmcs.long
        type: long
        mandatory: true
      - name: remk
        domain: txcmg.remk
        type: string
        length: 100
      - name: stat
        domain: txcmg.stat
        type: enum
      - name: lino
        domain: tcmcs.long
        type: long
    indices:
      - id: 1
        columns: [btno]
        primary_key: true

sessions:
  - code: txcmg0110m100
    description: Billing Batch MMT Controller
    type: mmt_controller
    table: txcmg011
    satellites: [txcmg0510m000, txcmg0512m000]
    form_commands:
      - { name: exec.user.0, function: generate.billing, label_code: txcmg0110m100.cmd1, description: Generate Billing }

libraries:
  - code: txibddllitem01
    module: ibd
    type: dll
    description: Item General DLL

menus:
  - code: txgld0000m001
    module: gld
    description: Enhancements Menu
    choices:
      - { position: 10, type: session, target: txcmg0110m100, description: Billing Batch }

reports:
  - code: txcmg04010100
    module: cmg
    description: Billing Summary Report

messages:
  - code: txcmg0001
    description: Validation error for batch
    severity: "3"
    text: "Batch cannot be processed without approval."

questions:
  - code: txcmg0002
    description: Confirm batch posting
    severity: "2"
    domain: tcyesno
    default_answer: yes
    text: "Do you want to post this billing batch?"

functions:
  - code: txcmgf001
    module: cmg
    description: Calculate Batch Total

additionals:
  - code: txcmgcfg
    module: cmg
    description: Config payload
    content: "{\"enabled\": true}"

business_objects:
  - code: txcmgbus01
    module: cmg
    description: Batch BOD
"#;

#[test]
fn test_compile_schema_to_tde_full_pipeline() {
    let tmp = tempdir().unwrap();
    let root = tmp.path();

    let res = compile_schema_to_tde(SAMPLE_YAML, root, true, Some("2026-01-01T00:00:00Z")).unwrap();
    assert!(res.admin_updated);
    assert!(res.admin_path.is_some());

    // Verify all 12 component files exist in the exact Single-XML TDE layout:
    // Module-scoped: {pkg}/{type}/{mod}/{name}.{ext}
    let tbl_path = root.join("tx/table/cmg/txcmg011.tbl");
    assert!(tbl_path.exists(), "Table path missing: {:?}", tbl_path);
    let tbl_content = fs::read_to_string(&tbl_path).unwrap();
    assert!(tbl_content.contains("<name>txcmg011</name>"));
    // TBL003 line number non-mandatory rule verification
    assert!(tbl_content.contains("<name>lino</name>"));
    assert!(tbl_content.contains("<isMandatory>false</isMandatory>"));

    let ses_path = root.join("tx/session/cmg/txcmg0110m100.ses");
    assert!(ses_path.exists(), "Session path missing: {:?}", ses_path);

    let lib_path = root.join("tx/library/ibd/txibddllitem01.lib");
    assert!(lib_path.exists(), "Library path missing: {:?}", lib_path);

    let mnu_path = root.join("tx/menu/gld/txgld0000m001.mnu");
    assert!(mnu_path.exists(), "Menu path missing: {:?}", mnu_path);

    let rpt_path = root.join("tx/report/cmg/txcmg04010100.rpt");
    assert!(rpt_path.exists(), "Report path missing: {:?}", rpt_path);

    let fnc_path = root.join("tx/function/cmg/txcmgf001.fnc");
    assert!(fnc_path.exists(), "Function path missing: {:?}", fnc_path);

    let add_path = root.join("tx/additional/cmg/txcmgcfg.add");
    assert!(add_path.exists(), "Additional file path missing: {:?}", add_path);

    let bus_path = root.join("tx/businessobject/cmg/txcmgbus01.bus");
    assert!(bus_path.exists(), "BusinessObject path missing: {:?}", bus_path);

    // Package-scoped: {pkg}/{type}/{name}.{ext} - NO {mod} subfolder!
    let dmn_remk = root.join("tx/domain/txcmg.remk.dmn");
    assert!(dmn_remk.exists(), "Domain path missing: {:?}", dmn_remk);

    let dmn_stat = root.join("tx/domain/txcmg.stat.dmn");
    assert!(dmn_stat.exists(), "Domain path missing: {:?}", dmn_stat);

    let msg_path = root.join("tx/message/txcmg0001.msg");
    assert!(msg_path.exists(), "Message path missing: {:?}", msg_path);

    let qst_path = root.join("tx/question/txcmg0002.qst");
    assert!(qst_path.exists(), "Question path missing: {:?}", qst_path);

    let lbl_tbl = root.join("tx/label/txcmg011.lbl");
    assert!(lbl_tbl.exists(), "Label path missing: {:?}", lbl_tbl);

    let lbl_stat_open = root.join("tx/label/txcmg.stat010.lbl");
    assert!(lbl_stat_open.exists(), "Enum label missing: {:?}", lbl_stat_open);

    // Verify .admin registration
    let admin_file = AdminFile::load_from_path(&root.join(".admin")).unwrap();
    let entries = &admin_file.entries;
    assert!(!entries.is_empty());
    assert!(entries.iter().any(|(p, _)| p == "tx/table/cmg/txcmg011.tbl"));
    assert!(entries.iter().any(|(p, _)| p == "tx/session/cmg/txcmg0110m100.ses"));
    assert!(entries.iter().any(|(p, _)| p == "tx/domain/txcmg.stat.dmn"));
    assert!(entries.iter().any(|(p, _)| p == "tx/label/txcmg011.lbl"));
}

#[test]
fn test_block_legacy_plural_folders() {
    let bad_path = std::path::Path::new("tx/tables/cmg/txcmg011.tbl");
    let err = validate_no_legacy_plural(bad_path);
    assert!(matches!(err, Err(TdePathError::LegacyPluralFolderBlocked(_))));

    let good_path = std::path::Path::new("tx/table/cmg/txcmg011.tbl");
    assert!(validate_no_legacy_plural(good_path).is_ok());
}
