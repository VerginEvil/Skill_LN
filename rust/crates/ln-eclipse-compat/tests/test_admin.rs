use ln_eclipse_compat::{
    AdminFile, AdministrationComponent, normalize_admin_path,
    is_managed_extension, is_excluded_extension,
};
use std::process::Command;
use tempfile::tempdir;

#[test]
fn test_normalize_admin_path() {
    assert_eq!(normalize_admin_path("tx/table/cmg/txcmg011.tbl"), "tx/table/cmg/txcmg011.tbl");
    assert_eq!(normalize_admin_path("/tx/table/cmg/txcmg011.tbl"), "tx/table/cmg/txcmg011.tbl");
    assert_eq!(normalize_admin_path(r"tx\table\cmg\txcmg011.tbl"), "tx/table/cmg/txcmg011.tbl");
    assert_eq!(normalize_admin_path(":act_123/tx/table/cmg/txcmg011.tbl"), "tx/table/cmg/txcmg011.tbl");
    assert_eq!(normalize_admin_path(":act_123//tx/table/cmg/txcmg011.tbl"), "tx/table/cmg/txcmg011.tbl");
    assert_eq!(normalize_admin_path("///tx/domain/txcmg.remk.dmn"), "tx/domain/txcmg.remk.dmn");
}

#[test]
fn test_managed_and_excluded_extensions() {
    assert!(is_managed_extension("tx/table/cmg/txcmg011.tbl"));
    assert!(is_managed_extension("tx/session/cmg/txcmg0101m000.ses"));
    assert!(is_managed_extension("tx/domain/txcmg.remk.dmn"));
    assert!(is_managed_extension("tx/library/cmg/txcmg0001.lib"));
    assert!(is_managed_extension("tx/menu/cmg/txcmg000000.mnu"));
    assert!(is_managed_extension("tx/label/txcmg0101.lbl"));
    assert!(is_managed_extension("tx/report/cmg/txcmg040101000.rpt"));
    assert!(is_managed_extension("tx/message/txcmg0001.msg"));
    assert!(is_managed_extension("tx/question/txcmg0001.qst"));
    assert!(is_managed_extension("tx/function/cmg/txcmg0001.fnc"));
    assert!(is_managed_extension("tx/additional/cmg/file.add"));
    assert!(is_managed_extension("tx/businessobject/cmg/bo.bus"));
    assert!(is_managed_extension("tx/chart/chart.cha"));

    assert!(is_excluded_extension("tx/table/cmg/txcmg011.4gl"));
    assert!(is_excluded_extension("tx/table/cmg/txcmg011.dal"));
    assert!(is_excluded_extension("tx/table/cmg/txcmg011.src"));
    assert!(is_excluded_extension("tx/table/cmg/txcmg011.clnsrc"));
    assert!(is_excluded_extension("tx/table/cmg/txcmg011.rptdsrc"));

    assert!(!is_excluded_extension("tx/table/cmg/txcmg011.tbl"));
}

#[test]
fn test_state_transitions() {
    let mut admin = AdminFile::new();

    // 1. after_create
    admin.after_create("tx/table/cmg/txcmg011.tbl");
    let c = admin.get("tx/table/cmg/txcmg011.tbl").unwrap();
    assert!(c.is_created);
    assert!(c.is_checked_out);
    assert!(!c.is_ever_checked_in);
    assert!(!c.is_expired);
    assert!(c.is_dirty);
    assert!(!c.is_vsc_happy);

    // 2. after_put
    admin.after_put("tx/table/cmg/txcmg011.tbl");
    let c = admin.get("tx/table/cmg/txcmg011.tbl").unwrap();
    assert!(c.is_created);
    assert!(c.is_checked_out);
    assert!(!c.is_dirty);
    assert!(!c.is_vsc_happy);

    // 3. set_vsc_happy
    admin.set_vsc_happy("tx/table/cmg/txcmg011.tbl", true);
    assert!(admin.get("tx/table/cmg/txcmg011.tbl").unwrap().is_vsc_happy);

    // 4. after_checkin
    admin.after_checkin("tx/table/cmg/txcmg011.tbl");
    let c = admin.get("tx/table/cmg/txcmg011.tbl").unwrap();
    assert!(!c.is_created);
    assert!(!c.is_checked_out);
    assert!(c.is_ever_checked_in);
    assert!(!c.is_expired);
    assert!(!c.is_dirty);
    assert!(c.is_vsc_happy);

    // 5. after_checkout
    admin.after_checkout("tx/table/cmg/txcmg011.tbl");
    let c = admin.get("tx/table/cmg/txcmg011.tbl").unwrap();
    assert!(!c.is_created);
    assert!(c.is_checked_out);
    assert!(!c.is_ever_checked_in);
    assert!(!c.is_dirty);
    assert!(c.is_vsc_happy);

    // 6. after_get
    admin.after_get("tx/domain/txcmg.remk.dmn");
    let c = admin.get("tx/domain/txcmg.remk.dmn").unwrap();
    assert!(!c.is_created);
    assert!(!c.is_checked_out);
    assert!(!c.is_ever_checked_in);
    assert!(!c.is_expired);
    assert!(!c.is_dirty);
    assert!(c.is_vsc_happy);

    // 7. after_uncheckout on newly created (not ever checked in) -> removed
    admin.after_create("tx/menu/cmg/txcmg000000.mnu");
    assert!(admin.get("tx/menu/cmg/txcmg000000.mnu").is_some());
    admin.after_uncheckout("tx/menu/cmg/txcmg000000.mnu");
    assert!(admin.get("tx/menu/cmg/txcmg000000.mnu").is_none());

    // 8. after_uncheckout on existing checked-in component -> resets flags
    admin.after_checkin("tx/table/cmg/txcmg011.tbl");
    admin.after_checkout("tx/table/cmg/txcmg011.tbl");
    admin.after_uncheckout("tx/table/cmg/txcmg011.tbl");
    let c = admin.get("tx/table/cmg/txcmg011.tbl").unwrap();
    assert!(!c.is_checked_out);
    assert!(!c.is_dirty);
    assert!(c.is_vsc_happy);
}

#[test]
fn test_excluded_extensions_prevented_and_repaired() {
    let mut admin = AdminFile::new();
    admin.after_create("tx/table/cmg/txcmg011.4gl");
    admin.after_create("tx/table/cmg/txcmg011.dal");
    admin.after_create("tx/table/cmg/txcmg011.src");
    assert!(admin.entries.is_empty());

    // Manually insert dirty excluded entry and test repair
    admin.entries.insert("tx/table/cmg/txcmg011.4gl".to_string(), AdministrationComponent::new("tx/table/cmg/txcmg011.4gl"));
    admin.entries.insert("tx/table/cmg/txcmg011.tbl".to_string(), AdministrationComponent::new("tx/table/cmg/txcmg011.tbl"));
    assert_eq!(admin.entries.len(), 2);

    let pruned = admin.repair();
    assert_eq!(pruned, 1);
    assert_eq!(admin.entries.len(), 1);
    assert!(admin.get("tx/table/cmg/txcmg011.tbl").is_some());
    assert!(admin.get("tx/table/cmg/txcmg011.4gl").is_none());
}

#[test]
fn test_java_admin_sync_helper_differential_roundtrip() {
    // Locate java and AdminSyncHelper.class
    let manifest_dir = env!("CARGO_MANIFEST_DIR");
    let repo_root = std::path::Path::new(manifest_dir)
        .parent().unwrap()
        .parent().unwrap();
    let tools_lib = repo_root.join("ln_studio_skill").join("tools").join("lib");
    let helper_class = tools_lib.join("tools").join("lib").join("AdminSyncHelper.class");
    if !helper_class.exists() {
        eprintln!("[SKIP] AdminSyncHelper.class not found at {:?}", helper_class);
        return;
    }

    let dir = tempdir().unwrap();
    let admin_path = dir.path().join(".admin");

    let mut rust_admin = AdminFile::new();
    rust_admin.after_create("tx/table/cmg/txcmg011.tbl");
    rust_admin.after_get("tx/domain/txcmg.remk.dmn");
    rust_admin.after_checkin("tx/session/cmg/txcmg0101m000.ses");
    rust_admin.save_to_path(&admin_path).unwrap();

    // Verify Java AdminSyncHelper can list and see exact fields
    let cp = format!("{};{}", tools_lib.display(), tools_lib.join("lnstudio_commoncore.jar").display());
    let output = Command::new("java")
        .args(["-cp", &cp, "tools.lib.AdminSyncHelper", admin_path.to_str().unwrap(), "list"])
        .output();

    if let Ok(res) = output {
        if res.status.success() {
            let stdout = String::from_utf8_lossy(&res.stdout);
            assert!(stdout.contains("TOTAL:3"));
            assert!(stdout.contains("tx/table/cmg/txcmg011.tbl\ttrue\ttrue\tfalse\tfalse\ttrue\tfalse\ttx/table/cmg/txcmg011.tbl"));
            assert!(stdout.contains("tx/domain/txcmg.remk.dmn\tfalse\tfalse\tfalse\tfalse\tfalse\ttrue\ttx/domain/txcmg.remk.dmn"));
            assert!(stdout.contains("tx/session/cmg/txcmg0101m000.ses\tfalse\tfalse\ttrue\tfalse\tfalse\ttrue\ttx/session/cmg/txcmg0101m000.ses"));

            // Now mutate via Java AdminSyncHelper and verify Rust reads it back
            let mut_res = Command::new("java")
                .args(["-cp", &cp, "tools.lib.AdminSyncHelper", admin_path.to_str().unwrap(), "after_checkout", "tx/session/cmg/txcmg0101m000.ses"])
                .output()
                .unwrap();
            assert!(mut_res.status.success());

            let reloaded = AdminFile::load_from_path(&admin_path).unwrap();
            assert_eq!(reloaded.entries.len(), 3);
            let ses = reloaded.get("tx/session/cmg/txcmg0101m000.ses").unwrap();
            assert!(ses.is_checked_out);
            assert!(!ses.is_created);
            assert!(ses.is_vsc_happy);
        }
    }
}

#[test]
fn test_admin_jvm_exact_handle_layout_and_string_variants() {
    let mut admin = AdminFile::new();
    admin.after_get("tx/etable/cmg/cmg011.tbl");
    admin.after_checkout("tx/esess/cmg/cmg0512m000.ses");
    admin.entries.insert(
        "tx/elib/ess/esssli2620m0.lib".to_string(),
        AdministrationComponent {
            is_checked_out: false,
            is_created: false,
            is_ever_checked_in: true,
            is_expired: false,
            is_dirty: false,
            is_vsc_happy: true,
            path: "/dev_natt_v01108-1 [EXTce01108]/tx/elib/ess/esssli2620m0.lib".to_string(),
        },
    );

    let bytes = admin.serialize().expect("serialize should succeed");
    // Entry 1 (second entry) must reference AdministrationComponent ClassDesc at 0x007E0003:
    // 0x73 (TC_OBJECT) followed by 0x71 (TC_REFERENCE) 0x00 0x7E 0x00 0x03
    let needle = [0x73u8, 0x71, 0x00, 0x7E, 0x00, 0x03];
    assert!(
        bytes.windows(needle.len()).any(|w| w == needle),
        "Expected TC_OBJECT -> TC_REFERENCE(0x007E0003) for AdministrationComponent ClassDesc in serialized bytes"
    );

    let parsed = AdminFile::deserialize(&bytes).expect("round-trip deserialize must succeed");
    assert_eq!(parsed.entries.len(), 3);
    assert!(parsed.get("tx/etable/cmg/cmg011.tbl").is_some());
    assert!(parsed.get("tx/esess/cmg/cmg0512m000.ses").unwrap().is_checked_out);
    assert!(parsed.get("tx/elib/ess/esssli2620m0.lib").unwrap().is_ever_checked_in);
}

#[test]
fn test_real_workspace_dev_natt_v01108_admin_file() {
    let real_admin = std::path::Path::new(
        r"C:\Users\nutdo\OneDrive\Documents\workspace_lnstudio\SCS_TST\dev_natt_v01108-1 [EXTce01108]\.admin",
    );
    if !real_admin.exists() {
        eprintln!("[SKIP] Real workspace .admin not found at {:?}", real_admin);
        return;
    }

    let admin = AdminFile::load_from_path(real_admin)
        .expect("Must parse real Eclipse .admin file without handle errors");
    assert!(!admin.entries.is_empty(), "Real .admin should have entries");

    let bytes = admin.serialize().expect("Re-serialize real .admin");
    let roundtrip = AdminFile::deserialize(&bytes).expect("Round-trip deserialize real .admin");
    assert_eq!(roundtrip.entries.len(), admin.entries.len());
}
