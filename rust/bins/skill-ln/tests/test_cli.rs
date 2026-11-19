use clap::Parser;
use skill_ln::cli::Cli;
use skill_ln::commands::execute_command;

#[tokio::test]
async fn test_cli_fn_search_and_doc_search() {
    let fn_cli = Cli::parse_from(["skill-ln", "fn-search", "dal.set.error", "--limit", "5", "--json"]);
    let res = execute_command(fn_cli.command).await;
    assert!(res.is_ok(), "fn-search must succeed");

    let doc_cli = Cli::parse_from(["skill-ln", "doc-search", "dal2", "--limit", "3", "--json"]);
    let res_doc = execute_command(doc_cli.command).await;
    assert!(res_doc.is_ok(), "doc-search must succeed");
}

#[tokio::test]
async fn test_cli_end_activity_gate_hard_blocked() {
    let end_cli = Cli::parse_from([
        "skill-ln", "end-activity",
        "--task", "task_01",
        "--project", "EXTce01107",
    ]);

    let err = execute_command(end_cli.command).await;
    assert!(err.is_err(), "end-activity must be hard-blocked");
    let err_msg = err.unwrap_err().to_string();
    assert!(
        err_msg.contains("PreCommitBoundaryError"),
        "Error message must contain PreCommitBoundaryError, got: {}",
        err_msg
    );
}

#[tokio::test]
async fn test_cli_checkout_component_extension_blocked() {
    let chk_cli = Cli::parse_from([
        "skill-ln", "checkout-component",
        "--type", "library",
        "--name", "txesssli2620m0",
        "--activity", "test_act",
    ]);

    let err = execute_command(chk_cli.command).await;
    assert!(err.is_err(), "checkout on tx* extension component must fail");
    let err_msg = err.unwrap_err().to_string();
    assert!(
        err_msg.contains("ReadOnlyComponentError"),
        "Error message must contain ReadOnlyComponentError, got: {}",
        err_msg
    );
}

#[tokio::test]
async fn test_cli_mcp_setup_output() {
    let setup_cli = Cli::parse_from(["skill-ln", "mcp-setup", "--client", "generic"]);
    let res = execute_command(setup_cli.command).await;
    assert!(res.is_ok());
}

#[test]
fn test_cli_child_process_no_stack_overflow() {
    let bin = env!("CARGO_BIN_EXE_skill-ln");

    let ver = std::process::Command::new(bin)
        .arg("--version")
        .output()
        .expect("Failed to spawn skill-ln --version");
    assert!(
        ver.status.success(),
        "skill-ln --version failed (status={:?}): stderr={}",
        ver.status,
        String::from_utf8_lossy(&ver.stderr)
    );

    let fn_search = std::process::Command::new(bin)
        .args(["fn-search", "db.insert", "--limit", "3", "--json"])
        .output()
        .expect("Failed to spawn skill-ln fn-search");
    assert!(
        fn_search.status.success(),
        "skill-ln fn-search failed (status={:?}): stderr={}",
        fn_search.status,
        String::from_utf8_lossy(&fn_search.stderr)
    );
}

#[tokio::test]
async fn test_cli_import_dd_txt_and_audit_dd_dir() {
    let tmp = tempfile::tempdir().unwrap();
    let dd_dir = tmp.path().join("Table Definitions");
    std::fs::create_dir_all(&dd_dir).unwrap();
    std::fs::write(
        dd_dir.join("cisli220.txt"),
        "Table : ci sli 220 Headers\n1 sfcp Company tcncmp Integer 2 Yes Yes Not applicab\n",
    )
    .unwrap();
    let out_cache = tmp.path().join(".ln_dd_cache.json");

    let imp_cli = Cli::parse_from([
        "skill-ln",
        "import-dd-txt",
        dd_dir.to_str().unwrap(),
        "--out",
        out_cache.to_str().unwrap(),
    ]);
    let res = execute_command(imp_cli.command).await;
    assert!(res.is_ok(), "import-dd-txt must succeed: {:?}", res);
    assert!(out_cache.exists());

    let script = tmp.path().join("s.cln");
    std::fs::write(
        &script,
        "declaration:\n    table tcisli220\nfunction void f() {\n    cisli220.missing_xyz = 1\n}\n",
    )
    .unwrap();
    let aud_cli = Cli::parse_from([
        "skill-ln",
        "audit-4gl",
        script.to_str().unwrap(),
        "--mode",
        "general",
        "--dd-dir",
        dd_dir.to_str().unwrap(),
        "--json",
    ]);
    let aud_res = execute_command(aud_cli.command).await;
    assert!(aud_res.is_ok());
}

#[test]
fn test_login_workspace_path_resolves_to_env_name() {
    let tmp = tempfile::tempdir().unwrap();
    let ws_dir = tmp.path().join("MY_WS_FOLDER");
    let settings_dir = ws_dir
        .join(".metadata")
        .join(".plugins")
        .join("org.eclipse.core.runtime")
        .join(".settings");
    std::fs::create_dir_all(&settings_dir).unwrap();
    std::fs::write(
        settings_dir.join("com.infor.erpln.jca.connectivity.prefs"),
        "ActivationType1=http_oauth2\nCloudEnvironment1=CANONICAL_ENV\nCompany1=0\nConfigurationCount=2\nHostName1=https\\://mock.example.com/T/LN/webservice\nName1=ProjectServer\n",
    )
    .unwrap();

    let key = skill_ln::commands::resolve_login_token_key(Some(ws_dir.to_str().unwrap()), None);
    assert_eq!(key.unwrap(), "CANONICAL_ENV");
}

#[tokio::test]
async fn test_cli_inject_enforces_readonly_guardrail() {
    let tmp = tempfile::tempdir().unwrap();
    let script = tmp.path().join("u.4gl");
    let target = tmp.path().join("txinr1110m000.ses");
    std::fs::write(&script, "before.program:\n").unwrap();
    std::fs::write(&target, "<DR_Controller><DR_Module><Source><expression>old</expression></Source></DR_Module></DR_Controller>").unwrap();

    let mut perms = std::fs::metadata(&target).unwrap().permissions();
    perms.set_readonly(true);
    std::fs::set_permissions(&target, perms).unwrap();

    let cli = Cli::parse_from([
        "skill-ln",
        "inject",
        "--source",
        script.to_str().unwrap(),
        "--target",
        target.to_str().unwrap(),
    ]);
    let err = execute_command(cli.command).await.unwrap_err();
    assert!(err.to_string().contains("ReadOnlyComponentError"), "Got: {err}");

    let mut perms_rw = std::fs::metadata(&target).unwrap().permissions();
    perms_rw.set_readonly(false);
    std::fs::set_permissions(&target, perms_rw).unwrap();
}

#[tokio::test]
async fn test_environments_and_login_status_parity_with_silent_refresh() {
    use std::io::{Read, Write};
    use std::net::TcpListener;

    let listener = TcpListener::bind("127.0.0.1:0").unwrap();
    let addr = listener.local_addr().unwrap();
    let srv = std::thread::spawn(move || {
        for _ in 0..2 {
            if let Ok((mut stream, _)) = listener.accept() {
                let mut buf = [0u8; 2048];
                let _ = stream.read(&mut buf);
                let body = r#"{"access_token":"mock-refreshed-token","refresh_token":"mock-rt-2","expires_in":3600,"token_type":"Bearer"}"#;
                let resp = format!(
                    "HTTP/1.1 200 OK\r\nContent-Type: application/json\r\nContent-Length: {}\r\nConnection: close\r\n\r\n{}",
                    body.len(),
                    body
                );
                let _ = stream.write_all(resp.as_bytes());
            }
        }
    });

    let tmp_home = tempfile::tempdir().unwrap();
    let ws_dir = tmp_home.path().join("CUSTOM_WS_FOLDER");
    let settings_dir = ws_dir
        .join(".metadata")
        .join(".plugins")
        .join("org.eclipse.core.runtime")
        .join(".settings");
    std::fs::create_dir_all(&settings_dir).unwrap();
    std::fs::write(
        settings_dir.join("com.infor.erpln.jca.connectivity.prefs"),
        "ActivationType1=http_oauth2\nCloudEnvironment1=MOCK_CANON_ENV\nCompany1=100\nConfigurationCount=2\nHostName1=https\\://mock.example.com/T/LN/webservice\nName1=ProjectServer\n",
    )
    .unwrap();

    let ln_studio_dir = tmp_home.path().join(".ln_studio");
    let tok_dir = ln_studio_dir.join("tokens");
    std::fs::create_dir_all(&tok_dir).unwrap();

    let ionapi_json = serde_json::json!({
        "ti": "MOCK_CANON_ENV",
        "ci": "cid",
        "cs": "csec",
        "iu": format!("http://{}/", addr),
        "pu": format!("http://{}/", addr),
        "oa": format!("http://{}/as/authorization.oauth2", addr),
        "ot": format!("http://{}/as/token.oauth2", addr)
    });
    let ionapi_cfg = ln_auth::IonapiConfig::from_str(&ionapi_json.to_string()).unwrap();
    ln_auth::sync_cloudenv_prefs(
        &ln_studio_dir.join("com.infor.erpln.jca.connectivity.cloudenv.prefs"),
        "MOCK_CANON_ENV",
        &ionapi_cfg,
    )
    .unwrap();

    let expired_tok = serde_json::json!({
        "access_token": "old-expired",
        "refresh_token": "old-rt",
        "expires_at": 1000.0
    });
    std::fs::write(tok_dir.join("MOCK_CANON_ENV.json"), expired_tok.to_string()).unwrap();

    // Verify environments path, login --workspace <path>, and login --workspace <env_name> produce identical valid refreshed status
    let (env_key, env_ctx, env_rep) = skill_ln::commands::check_and_refresh_env_auth(
        Some(ws_dir.to_str().unwrap()),
        None,
        Some(tmp_home.path()),
    )
    .await
    .unwrap();
    assert_eq!(env_key, "MOCK_CANON_ENV");
    assert_eq!(env_ctx.unwrap().env_name, "MOCK_CANON_ENV");
    assert_eq!(env_rep.status, "valid");
    assert_eq!(env_rep.access_token.as_deref(), Some("mock-refreshed-token"));

    let (path_key, _, path_rep) = skill_ln::commands::check_and_refresh_env_auth(
        Some(ws_dir.to_str().unwrap()),
        None,
        Some(tmp_home.path()),
    )
    .await
    .unwrap();
    let (name_key, _, name_rep) = skill_ln::commands::check_and_refresh_env_auth(
        Some("MOCK_CANON_ENV"),
        None,
        Some(tmp_home.path()),
    )
    .await
    .unwrap();
    assert_eq!(path_key, "MOCK_CANON_ENV");
    assert_eq!(name_key, "MOCK_CANON_ENV");
    assert_eq!(path_rep.status, "valid");
    assert_eq!(name_rep.status, "valid");

    drop(srv);
}
