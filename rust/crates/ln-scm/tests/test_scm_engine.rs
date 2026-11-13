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
