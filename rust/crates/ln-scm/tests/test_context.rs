use ln_eclipse_compat::{AdminFile, PropertyBucket};
use ln_scm::context::{ActivityDotProject, WorkspaceContext};
use std::path::Path;
use tempfile::tempdir;

#[test]
fn test_workspace_context_discover_hermetic() {
    let tmp = tempdir().unwrap();
    let ws = tmp.path();

    let settings_dir = ws
        .join(".metadata")
        .join(".plugins")
        .join("org.eclipse.core.runtime")
        .join(".settings");
    std::fs::create_dir_all(&settings_dir).unwrap();
    std::fs::write(
        settings_dir.join("com.infor.erpln.jca.connectivity.prefs"),
        "ActivationType1=http_oauth2\nCloudEnvironment1=TEST_ENV\nCompany1=0\nConfigurationCount=2\nHostName1=https\\://mock.example.com/TENANT/LN/webservice\nName1=ProjectServer\n",
    )
    .unwrap();

    let act_dir = ws.join("task_01 [PROJ_A]");
    std::fs::create_dir_all(&act_dir).unwrap();
    std::fs::write(
        act_dir.join(".project"),
        "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<projectDescription>\n\t<name>task_01 [PROJ_A]</name>\n</projectDescription>\n",
    )
    .unwrap();

    let admin = AdminFile::new();
    admin.save_to_path(&act_dir.join(".admin")).unwrap();

    let idx_path = ws
        .join(".metadata")
        .join(".plugins")
        .join("org.eclipse.core.resources")
        .join(".projects")
        .join("task_01 [PROJ_A]")
        .join(".indexes")
        .join("properties.index");
    let mut bucket = PropertyBucket::new();
    bucket.set_property("ProjectName", "PROJ_A", "", "");
    bucket.set_property("TaskName", "task_01", "", "");
    bucket.set_property("Label", "uuid-lbl-001", "", "");
    bucket.set_property("ApplicationRelease", "10.8", "", "");
    bucket.set_property("DevelopmentEnvironment", "DEV", "", "");
    bucket.set_property("DevelopmentTimeRepositoryAddress", "PROJ_A_dev", "", "");
    bucket.set_property("RunTimeRepositoryAddress", "PROJ_A_rt", "", "");
    bucket.save_to_path(&idx_path).unwrap();

    let ctx = WorkspaceContext::discover(Some(ws), Some(&act_dir)).unwrap();
    assert_eq!(ctx.env_name, "TEST_ENV");
    assert_eq!(ctx.endpoint_url, "https://mock.example.com/TENANT/LN/webservice");
    assert_eq!(ctx.company, "0");

    let (resolved_dir, dot_proj) = ctx.resolve_activity(None).unwrap();
    assert_eq!(resolved_dir, act_dir);
    assert_eq!(dot_proj.project_name, "PROJ_A");
    assert_eq!(dot_proj.task_name, "task_01");
    assert_eq!(dot_proj.label, "uuid-lbl-001");
    assert_eq!(dot_proj.dev_repo_address, "PROJ_A_dev");
    assert_eq!(dot_proj.rt_repo_address, "PROJ_A_rt");
}

#[test]
fn test_workspace_context_real_scs_tst_workspace() {
    let real_ws = Path::new(r"C:\Users\nutdo\OneDrive\Documents\workspace_lnstudio\SCS_TST");
    let real_act = real_ws.join("dev_natt_v01108-1 [EXTce01108]");
    if !real_act.exists() {
        eprintln!("[SKIP] Real SCS_TST activity not found at {:?}", real_act);
        return;
    }

    let ctx = WorkspaceContext::discover(Some(real_ws), Some(&real_act)).unwrap();
    assert_eq!(ctx.env_name, "SCS_TST");
    assert!(
        ctx.endpoint_url.contains("SLNBGS786BCXMXWQ_TST/LN/webservice"),
        "Unexpected endpoint: {}",
        ctx.endpoint_url
    );
    assert_eq!(ctx.company, "0");

    let dot_proj = ActivityDotProject::from_activity_dir(&real_act).unwrap();
    assert_eq!(dot_proj.project_name, "EXTce01108");
    assert_eq!(dot_proj.task_name, "dev_natt_v01108-1");
    assert!(!dot_proj.label.is_empty(), "Expected non-empty label UUID from real activity");
    assert_eq!(dot_proj.dev_repo_address, "EXTce01108_dev");
    assert_eq!(dot_proj.rt_repo_address, "EXTce01108_rt");
}

#[test]
fn test_workspace_discover_fails_fast_when_ambiguous_and_loads_cloudenv_ionapi() {
    let tmp = tempdir().unwrap();
    let ws_root = tmp.path().join("ws_root");
    for name in ["WS_ONE", "WS_TWO"] {
        let sdir = ws_root.join(name).join(".metadata").join(".plugins").join("org.eclipse.core.runtime").join(".settings");
        std::fs::create_dir_all(&sdir).unwrap();
        std::fs::write(
            sdir.join("com.infor.erpln.jca.connectivity.prefs"),
            format!("ActivationType1=http_oauth2\nCloudEnvironment1={name}\nCompany1=0\nConfigurationCount=2\nHostName1=https\\://gw.example.com/T/LN/webservice\nName1=ProjectServer\n"),
        ).unwrap();
    }

    // Ambiguous root with 2 workspaces and no override/CWD match must fail fast listing available workspaces
    let err = WorkspaceContext::discover_with_root(None, None, Some(&ws_root)).unwrap_err();
    let msg = err.to_string();
    assert!(msg.contains("WS_ONE") && msg.contains("WS_TWO"), "Expected available workspaces in error: {msg}");

    // Infers workspace even from nested file/dir inside activity
    let act = ws_root.join("WS_TWO").join("act_01 [EXTdemo]");
    let nested = act.join("tx").join("session").join("inr");
    std::fs::create_dir_all(&nested).unwrap();
    std::fs::write(act.join(".project"), "<projectDescription><name>act_01 [EXTdemo]</name></projectDescription>").unwrap();
    let ctx = WorkspaceContext::discover_with_root(None, Some(&nested), Some(&ws_root)).unwrap();
    assert_eq!(ctx.env_name, "WS_TWO");
}
