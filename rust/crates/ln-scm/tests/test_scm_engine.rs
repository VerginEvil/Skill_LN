use std::fs;
use std::sync::Arc;
use tempfile::tempdir;
use tokio::io::{AsyncReadExt, AsyncWriteExt};
use tokio::net::TcpListener;
use tokio::sync::Mutex;

use ln_eclipse_compat::AdminFile;
use ln_jca::client::HttpClient;
use ln_scm::scm_engine::*;

#[tokio::test]
async fn test_get_only_extension_blocking() {
    let td = tempdir().unwrap();
    let act_dir = td.path();
    let client = HttpClient::new("http://127.0.0.1:9999", "dummy_token");

    // 1. Prefix checks
    let err = assert_not_extension_for_scm("txesswhwmd4300m000", "session").unwrap_err();
    assert!(err.to_string().contains("[GET_ONLY_EXTENSION]"));

    let err = assert_not_extension_for_scm("txestwhwmd400", "table").unwrap_err();
    assert!(err.to_string().contains("[GET_ONLY_EXTENSION]"));

    let err = assert_not_extension_for_scm("whwmd400.eto", "extension").unwrap_err();
    assert!(err.to_string().contains("[GET_ONLY_EXTENSION]"));

    let err = assert_not_extension_for_scm("whwmd400", "ess").unwrap_err();
    assert!(err.to_string().contains("[GET_ONLY_EXTENSION]"));

    // 2. Direct SCM operation blocks
    let err = checkout_component(&client, "session", "txesswhwmd4300m000", act_dir, "PROJ", None, None)
        .await
        .unwrap_err();
    assert!(err.to_string().contains("[GET_ONLY_EXTENSION]"));

    let err = checkin_component(&client, "table", "txestwhwmd400", act_dir, "PROJ", "comment", None, None)
        .await
        .unwrap_err();
    assert!(err.to_string().contains("[GET_ONLY_EXTENSION]"));

    let err = put_component(&client, "session", "txesswhwmd4300m000", act_dir, "PROJ", None, None)
        .await
        .unwrap_err();
    assert!(err.to_string().contains("[GET_ONLY_EXTENSION]"));
}

#[tokio::test]
async fn test_end_activity_gate_hard_block() {
    let err = end_activity_gate("PROJ_1", "TASK1").unwrap_err();
    let msg = err.to_string();
    assert!(msg.contains("[HARD-BLOCKED]"));
    assert!(msg.contains("ADR 0007"));
    assert!(msg.contains("TASK1"));
    assert!(msg.contains("PROJ_1"));
}

#[tokio::test]
async fn test_readonly_guardrail() {
    let td = tempdir().unwrap();
    let act_dir = td.path();
    let client = HttpClient::new("http://127.0.0.1:9999", "dummy_token");

    let comp_file = act_dir.join("tt").join("table").join("adv").join("ttadv999.tbl");
    fs::create_dir_all(comp_file.parent().unwrap()).unwrap();
    fs::write(&comp_file, "<DR_Table><name>ttadv999</name><expression>code</expression></DR_Table>").unwrap();

    set_file_readonly(&comp_file, true).unwrap();
    assert!(is_file_readonly(&comp_file));

    // Attempting put on read-only file fails
    let err = put_component(&client, "table", "ttadv999", act_dir, "PROJ", None, None)
        .await
        .unwrap_err();
    assert!(err.to_string().contains("[READ_ONLY_COMPONENT]"));

    // Clearing read-only allows it to pass the read-only guardrail
    set_file_readonly(&comp_file, false).unwrap();
    assert!(!is_file_readonly(&comp_file));
}

#[tokio::test]
async fn test_scm_lifecycle_mock_server() {
    let listener = TcpListener::bind("127.0.0.1:0").await.unwrap();
    let addr = listener.local_addr().unwrap();
    let base_url = format!("http://127.0.0.1:{}/TENANT/LN/webservice", addr.port());

    let captured_requests: Arc<Mutex<Vec<String>>> = Arc::new(Mutex::new(Vec::new()));
    let req_log = captured_requests.clone();

    tokio::spawn(async move {
        while let Ok((mut socket, _)) = listener.accept().await {
            let mut buf = [0u8; 8192];
            let n = socket.read(&mut buf).await.unwrap_or(0);
            let req = String::from_utf8_lossy(&buf[..n]).to_string();

            let mut log = req_log.lock().await;
            log.push(req.clone());
            drop(log);

            let req_line = req.lines().next().unwrap_or("");
            let is_numeric_conid = req_line
                .split("conid=")
                .nth(1)
                .map(|r| r.split(['&', ' ']).next().unwrap_or(""))
                .map(|c| !c.is_empty() && c.chars().all(|ch| ch.is_ascii_digit()))
                .unwrap_or(false);

            let (status_line, headers, body) = if req_line.contains("method=connect") {
                ("HTTP/1.1 200 OK", "Set-Cookie: JSESSIONID=eng_s0; Path=/\r\nContent-Type: application/xml\r\n", "<ConnectResponse><SessionID>s</SessionID><conid>0</conid></ConnectResponse>")
            } else if req_line.contains("method=share") {
                ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", "<ConnectResponse><SessionID>s</SessionID><conid>1</conid></ConnectResponse>")
            } else if req_line.contains("method=bdecall") && !is_numeric_conid {
                ("HTTP/1.1 500 Internal Server Error", "Content-Type: application/xml\r\n", "<error><info>null</info><message>POST request failed</message><reason>0</reason></error>")
            } else if req.contains("bdename=DR_Table") && req.contains("bdemethod=CheckOut") {
                assert!(req.contains("<name>ttadv999</name>"));
                assert!(req.contains("<type>table</type>"));
                assert!(req.contains("<optionalContent>yes</optionalContent>"));
                let body = "<DR_TableResponse><DataArea><DR_Table><name>ttadv999</name><versionID>B61O_a_ext.1</versionID><dateTime>2026-11-12T10:00:00Z</dateTime><expression>initial code</expression></DR_Table></DataArea></DR_TableResponse>";
                ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", body)
            } else if req.contains("bdename=DR_Table") && req.contains("bdemethod=Put") {
                assert!(req.contains("<name>ttadv999</name>"));
                let body = "<DR_TableResponse><DataArea><DR_Table><name>ttadv999</name><versionID>B61O_a_ext.2</versionID><dateTime>2026-11-12T10:05:00Z</dateTime></DR_Table></DataArea></DR_TableResponse>";
                ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", body)
            } else if req.contains("bdename=DR_Table") && req.contains("bdemethod=CheckIn") {
                assert!(req.contains("<documentation>Checked in by test</documentation>"));
                let body = "<DR_TableResponse><DataArea><DR_Table><name>ttadv999</name><versionID>B61O_a_ext.3</versionID><dateTime>2026-11-12T10:10:00Z</dateTime></DR_Table></DataArea></DR_TableResponse>";
                ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", body)
            } else if req.contains("bdename=DR_Table") && req.contains("bdemethod=UndoCheckOut") {
                assert!(req.contains("<name>ttadv999</name>"));
                assert!(req.contains("<versionID>see Activity ID</versionID>"));
                let body = "<DR_TableResponse><DataArea><DR_Table><name>ttadv999</name><versionID>B61O_a_ext.1</versionID><dateTime>2026-11-12T10:15:00Z</dateTime></DR_Table></DataArea></DR_TableResponse>";
                ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", body)
            } else {
                ("HTTP/1.1 404 Not Found", "Content-Type: text/plain\r\n", "Unknown")
            };

            let resp = format!(
                "{}\r\n{}Content-Length: {}\r\nConnection: close\r\n\r\n{}",
                status_line,
                headers,
                body.len(),
                body
            );
            let _ = socket.write_all(resp.as_bytes()).await;
        }
    });

    let client = HttpClient::new(&base_url, "test_token");
    let td = tempdir().unwrap();
    let act_dir = td.path();

    // 1. CheckOut component
    let checked_out = checkout_component(&client, "table", "ttadv999", act_dir, "PROJ_1", Some("B61O_a_ext"), None)
        .await
        .unwrap();

    assert!(checked_out.path.exists());
    assert!(!is_file_readonly(&checked_out.path));
    assert_eq!(checked_out.receipt.status, "SUCCESS");
    assert_eq!(checked_out.receipt.version_id, "B61O_a_ext.1");
    assert_eq!(checked_out.receipt.receipt_token.len(), 16);

    // Verify .admin status
    let admin_p = act_dir.join(".admin");
    let admin = AdminFile::load_from_path(&admin_p).unwrap();
    let rel_p = checked_out.path.strip_prefix(act_dir).unwrap().to_string_lossy().to_string();
    let comp = admin.get(&rel_p).expect("Admin component must exist");
    assert!(comp.is_checked_out);

    // 2. Put component
    let put_receipt = put_component(&client, "table", "ttadv999", act_dir, "PROJ_1", Some("B61O_a_ext"), None)
        .await
        .unwrap();
    assert_eq!(put_receipt.status, "SUCCESS");
    assert_eq!(put_receipt.version_id, "B61O_a_ext.2");

    // 3. CheckIn component
    let checkin_receipt = checkin_component(
        &client,
        "table",
        "ttadv999",
        act_dir,
        "PROJ_1",
        "Checked in by test",
        Some("B61O_a_ext"),
        None,
    )
    .await
    .unwrap();

    assert_eq!(checkin_receipt.status, "SUCCESS");
    assert_eq!(checkin_receipt.version_id, "B61O_a_ext.3");
    assert!(is_file_readonly(&checked_out.path));

    // Verify .admin after checkin
    let admin = AdminFile::load_from_path(&admin_p).unwrap();
    let comp = admin.get(&rel_p).unwrap();
    assert!(!comp.is_checked_out);
    assert!(comp.is_ever_checked_in);

    // 4. UndoCheckOut component (check out first, then uncheckout)
    set_file_readonly(&checked_out.path, false).unwrap();
    let _ = checkout_component(&client, "table", "ttadv999", act_dir, "PROJ_1", Some("B61O_a_ext"), None)
        .await
        .unwrap();

    let uncheckout_receipt = uncheckout_component(&client, "table", "ttadv999", act_dir, "PROJ_1", Some("B61O_a_ext"), None)
        .await
        .unwrap();
    assert_eq!(uncheckout_receipt.status, "SUCCESS");
    assert!(is_file_readonly(&checked_out.path));

    let admin = AdminFile::load_from_path(&admin_p).unwrap();
    let comp = admin.get(&rel_p).unwrap();
    assert!(!comp.is_checked_out);
}

#[test]
fn test_parse_scm_receipt_errors() {
    let err_xml = "<error><message>Component locked by user jsmith</message></error>";
    let err = parse_scm_receipt(err_xml, "ttadv999", "table", "CheckOut", "TASK1", "UUID", "B61O").unwrap_err();
    assert!(err.to_string().contains("[SCM_SERVER_ERROR]"));

    let conflict_xml = "<DR_TableResponse><error>Lock conflict occurred on database table</error></DR_TableResponse>";
    let err = parse_scm_receipt(conflict_xml, "ttadv999", "table", "CheckOut", "TASK1", "UUID", "B61O").unwrap_err();
    assert!(err.to_string().contains("[SCM_SERVER_ERROR]"));

    let empty = parse_scm_receipt("", "ttadv999", "table", "CheckOut", "TASK1", "UUID", "B61O").unwrap_err();
    assert!(empty.to_string().contains("empty response"));
}

#[test]
fn test_build_checkin_payload_injection() {
    let xml = "<DR_Table><name>ttadv999</name><expression>hello</expression></DR_Table>";
    let injected = build_checkin_payload(xml, "Fix bug #123 & verify <tag>").unwrap();
    assert!(injected.contains("<Version><documentation>Fix bug #123 &amp; verify &lt;tag&gt;</documentation></Version>"));
    assert!(injected.contains("<expression>hello</expression>"));
}

#[test]
fn test_activity_cloud_scm_detection_in_indexes_and_exact_case_checkout() {
    let tmp = tempdir().unwrap();
    let ws = tmp.path();
    let act = ws.join("dev_act [EXTdemo]");
    std::fs::create_dir_all(&act).unwrap();

    let idx = ws
        .join(".metadata")
        .join(".plugins")
        .join("org.eclipse.core.resources")
        .join(".projects")
        .join("dev_act [EXTdemo]")
        .join(".indexes")
        .join("properties.index");

    let mut bucket = ln_eclipse_compat::PropertyBucket::new();
    bucket.set_property("ApplicationUsesSCM", "no", "", "");
    bucket.set_property("Label", "uuid-cloud-act-001", "", "");
    bucket.set_property("TaskName", "dev_act", "", "");
    bucket.set_property("DevelopmentTimeRepositoryAddress", "EXTdemo_dev", "", "");
    bucket.save_to_path(&idx).unwrap();

    let (enabled, reason) = is_project_scm_enabled(&act);
    assert!(enabled, "Expected Activity-based Cloud SCM enabled despite ApplicationUsesSCM=no, got: {reason}");

    // Genuine NON_SCM (no Label/TaskName/dev repo) in .indexes/properties.index must return false
    let mut bucket_non = ln_eclipse_compat::PropertyBucket::new();
    bucket_non.set_property("ApplicationUsesSCM", "no", "", "");
    bucket_non.save_to_path(&idx).unwrap();
    let (disabled, _) = is_project_scm_enabled(&act);
    assert!(!disabled, "Expected genuine ApplicationUsesSCM=no without Cloud SCM metadata to return false");

    let payload = build_checkout_payload("DR_Label", "txinr.addr", "label", "B61O_a_ext", "dev_act", Some("uuid-cloud-act-001"));
    assert!(payload.contains("<name>txinr.addr</name>"), "payload={payload}");
}

#[test]
fn test_sync_admin_preserves_flags_uses_after_create_and_skips_extensions() {
    let tmp = tempdir().unwrap();
    let act = tmp.path();

    let ses_file = act.join("tx").join("session").join("inr").join("txinr1110m000.ses");
    let new_lbl = act.join("tx").join("label").join("txwh.clot.lbl");
    let ext_lib = act.join("tx").join("library").join("ess").join("txesswhwmd4300.lib");
    std::fs::create_dir_all(ses_file.parent().unwrap()).unwrap();
    std::fs::create_dir_all(new_lbl.parent().unwrap()).unwrap();
    std::fs::create_dir_all(ext_lib.parent().unwrap()).unwrap();
    std::fs::write(&ses_file, "<DR_Controller><name>txinr1110m000</name></DR_Controller>").unwrap();
    std::fs::write(&new_lbl, "<DR_Label><name>txwh.clot</name></DR_Label>").unwrap();
    std::fs::write(&ext_lib, "<DR_Module><name>txesswhwmd4300</name></DR_Module>").unwrap();

    // Pre-existing .admin entry for session with CheckedOut + Dirty + EverCheckedIn + activity folder m_path prefix, plus a missing file
    let admin_path = act.join(".admin");
    let mut admin = AdminFile::new();
    admin.after_checkout("tx/session/inr/txinr1110m000.ses");
    {
        let e = admin.get_mut("tx/session/inr/txinr1110m000.ses").unwrap();
        e.is_dirty = true;
        e.path = "dev_act [EXTce01108]/tx/session/inr/txinr1110m000.ses".to_string();
    }
    admin.after_create("tx/label/deleted.lbl");
    admin.save_to_path(&admin_path).unwrap();

    // Default sync_admin preserves missing entries (no prune) and preserves m_path prefix + flags
    let res = ln_scm::scm_engine::sync_admin(act).unwrap();
    assert_eq!(res.added, vec!["tx/label/txwh.clot.lbl"]);
    assert!(res.removed.is_empty(), "Default sync_admin must not prune missing entries");
    assert!(act.join(".admin.bak").exists(), "Expected .admin.bak backup");

    let reloaded = AdminFile::load_from_path(&admin_path).unwrap();
    let ses_entry = reloaded.get("tx/session/inr/txinr1110m000.ses").unwrap();
    assert!(ses_entry.is_checked_out, "Existing CheckedOut flag must be preserved");
    assert!(ses_entry.is_dirty, "Existing Dirty flag must be preserved");
    assert_eq!(
        ses_entry.path,
        "dev_act [EXTce01108]/tx/session/inr/txinr1110m000.ses",
        "Activity folder m_path prefix must be preserved"
    );
    assert!(reloaded.get("tx/label/deleted.lbl").is_some(), "Missing entry must be kept without --prune");

    let lbl_entry = reloaded.get("tx/label/txwh.clot.lbl").unwrap();
    assert!(lbl_entry.is_created, "New writable disk file must use after_create");
    assert!(lbl_entry.is_checked_out);
    assert!(lbl_entry.is_dirty);

    // Prune mode removes deleted.lbl
    let res_prune = ln_scm::scm_engine::sync_admin_with_options(act, true).unwrap();
    assert_eq!(res_prune.removed, vec!["tx/label/deleted.lbl"]);
    let reloaded_pruned = AdminFile::load_from_path(&admin_path).unwrap();
    assert!(reloaded_pruned.get("tx/library/ess/txesswhwmd4300.lib").is_none(), "Extension must be skipped");
    assert!(reloaded_pruned.get("tx/label/deleted.lbl").is_none(), "Deleted file must be pruned with prune=true");
}

#[test]
fn test_sync_admin_fails_fast_on_corrupt_admin_and_respects_readonly_new_files() {
    let tmp = tempdir().unwrap();
    let act = tmp.path();
    let lbl = act.join("tx").join("label").join("txro.lbl");
    std::fs::create_dir_all(lbl.parent().unwrap()).unwrap();
    std::fs::write(&lbl, "<DR_Label><name>txro</name></DR_Label>").unwrap();

    // 1. Corrupt .admin must fail fast without overwriting
    let admin_path = act.join(".admin");
    std::fs::write(&admin_path, b"CORRUPT_ADMIN_BYTES").unwrap();
    let err = ln_scm::scm_engine::sync_admin(act).unwrap_err();
    assert!(
        err.to_string().to_lowercase().contains("admin") || err.to_string().to_lowercase().contains("corrupt") || err.to_string().to_lowercase().contains("malformed") || err.to_string().to_lowercase().contains("magic"),
        "Unexpected error message: {err}"
    );
    assert_eq!(std::fs::read(&admin_path).unwrap(), b"CORRUPT_ADMIN_BYTES");

    // 2. Read-only untracked file gets after_get (isCheckedout=false), not after_create
    std::fs::remove_file(&admin_path).unwrap();
    let mut perms = std::fs::metadata(&lbl).unwrap().permissions();
    perms.set_readonly(true);
    std::fs::set_permissions(&lbl, perms).unwrap();

    let res = ln_scm::scm_engine::sync_admin(act).unwrap();
    assert_eq!(res.added, vec!["tx/label/txro.lbl"]);
    let admin = AdminFile::load_from_path(&admin_path).unwrap();
    let ro_entry = admin.get("tx/label/txro.lbl").unwrap();
    assert!(!ro_entry.is_checked_out, "Read-Only untracked file must not be marked checked out");
    assert!(!ro_entry.is_created);

    // Cleanup readonly for tempdir removal
    let mut perms_rw = std::fs::metadata(&lbl).unwrap().permissions();
    perms_rw.set_readonly(false);
    std::fs::set_permissions(&lbl, perms_rw).unwrap();
}

#[tokio::test]
async fn test_put_and_checkin_auto_dr_create_and_checkout_mock_server() {
    use std::sync::atomic::{AtomicBool, Ordering};

    let listener = TcpListener::bind("127.0.0.1:0").await.unwrap();
    let addr = listener.local_addr().unwrap();
    let base_url = format!("http://127.0.0.1:{}/TENANT/LN/webservice", addr.port());

    let created = Arc::new(AtomicBool::new(false));
    let checked_out = Arc::new(AtomicBool::new(false));
    let captured_create_req: Arc<Mutex<String>> = Arc::new(Mutex::new(String::new()));

    let c_created = created.clone();
    let c_checked_out = checked_out.clone();
    let c_create_req = captured_create_req.clone();

    tokio::spawn(async move {
        while let Ok((mut socket, _)) = listener.accept().await {
            let mut buf = [0u8; 16384];
            let n = socket.read(&mut buf).await.unwrap_or(0);
            let req = String::from_utf8_lossy(&buf[..n]).to_string();
            let req_line = req.lines().next().unwrap_or("");

            let (status_line, headers, body) = if req_line.contains("method=connect") {
                ("HTTP/1.1 200 OK", "Set-Cookie: JSESSIONID=s0; Path=/\r\nContent-Type: application/xml\r\n", "<ConnectResponse><SessionID>s</SessionID><conid>0</conid></ConnectResponse>")
            } else if req_line.contains("method=share") {
                ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", "<ConnectResponse><SessionID>s</SessionID><conid>1</conid></ConnectResponse>")
            } else if req.contains("bdename=DR_Label") && req.contains("bdemethod=DR_Create") {
                *c_create_req.lock().await = req.clone();
                c_created.store(true, Ordering::SeqCst);
                ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", "<DR_LabelResponse><DataArea><DR_Label><name>txwh.clot</name><versionID>B61O_a_ext.1</versionID></DR_Label></DataArea></DR_LabelResponse>")
            } else if req.contains("bdename=DR_Label") && req.contains("bdemethod=CheckOut") {
                c_checked_out.store(true, Ordering::SeqCst);
                ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", "<DR_LabelResponse><DataArea><DR_Label><name>txwh.clot</name><versionID>B61O_a_ext.1</versionID></DR_Label></DataArea></DR_LabelResponse>")
            } else if req.contains("bdename=DR_Label") && (req.contains("bdemethod=Put") || req.contains("bdemethod=CheckIn")) {
                if !c_created.load(Ordering::SeqCst) {
                    ("HTTP/1.1 500 Internal Server Error", "Content-Type: application/xml\r\n", "<error><message>Label not found</message></error>")
                } else if !c_checked_out.load(Ordering::SeqCst) {
                    ("HTTP/1.1 500 Internal Server Error", "Content-Type: application/xml\r\n", "<error><message>Label has not been checked out</message></error>")
                } else {
                    ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", "<DR_LabelResponse><DataArea><DR_Label><name>txwh.clot</name><versionID>B61O_a_ext.2</versionID></DR_Label></DataArea></DR_LabelResponse>")
                }
            } else {
                ("HTTP/1.1 404 Not Found", "Content-Type: text/plain\r\n", "Unknown")
            };

            let resp = format!(
                "{}\r\n{}Content-Length: {}\r\nConnection: close\r\n\r\n{}",
                status_line, headers, body.len(), body
            );
            let _ = socket.write_all(resp.as_bytes()).await;
        }
    });

    let client = HttpClient::new(&base_url, "test_token");
    let td = tempdir().unwrap();
    let act_dir = td.path().join("dev_test [EXTce01107]");
    fs::create_dir_all(&act_dir).unwrap();
    fs::write(act_dir.join(".project"), "<projectDescription/>").unwrap();
    let mut admin = AdminFile::new();
    admin.after_create("tx/label/txwh.clot.lbl");
    admin.save_to_path(&act_dir.join(".admin")).unwrap();

    let lbl_path = act_dir.join("tx").join("label").join("txwh.clot.lbl");
    fs::create_dir_all(lbl_path.parent().unwrap()).unwrap();
    fs::write(&lbl_path, "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?><DR_Label><name>txwh.clot</name></DR_Label>").unwrap();

    let put_res = put_component(&client, "label", "txwh.clot", &act_dir, "EXTce01107", Some("B61O_a_ext"), None)
        .await
        .unwrap();
    assert_eq!(put_res.status, "SUCCESS");
    assert!(created.load(Ordering::SeqCst));
    assert!(checked_out.load(Ordering::SeqCst));

    let create_req_body = captured_create_req.lock().await.clone();
    assert!(!create_req_body.contains("request=<?xml"), "DR_Create payload should strip <?xml declaration");

    created.store(false, Ordering::SeqCst);
    checked_out.store(false, Ordering::SeqCst);
    let cki_res = checkin_component(&client, "label", "txwh.clot", &act_dir, "EXTce01107", "Add lot label", Some("B61O_a_ext"), None)
        .await
        .unwrap();
    assert_eq!(cki_res.status, "SUCCESS");
    assert!(created.load(Ordering::SeqCst));
    assert!(checked_out.load(Ordering::SeqCst));
}
