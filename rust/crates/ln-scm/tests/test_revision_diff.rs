use std::fs;
use std::sync::Arc;
use tempfile::tempdir;
use tokio::io::{AsyncReadExt, AsyncWriteExt};
use tokio::net::TcpListener;
use tokio::sync::Mutex;

use ln_eclipse_compat::AdminFile;
use ln_jca::client::HttpClient;
use ln_scm::revision_diff::*;

#[test]
fn test_lcs_unified_diff_and_structural_extraction() {
    let original = "line 1\nline 2\nline 3\nline 4\n";
    let modified = "line 1\nline 2 modified\nline 3\nline 5\n";

    let diff = generate_unified_diff(original, modified, "server/test.4gl", "local/test.4gl");
    assert!(diff.contains("--- server/test.4gl"));
    assert!(diff.contains("+++ local/test.4gl"));
    assert!(diff.contains("-line 2"));
    assert!(diff.contains("+line 2 modified"));
    assert!(diff.contains("-line 4"));
    assert!(diff.contains("+line 5"));

    // Identical
    let same_diff = generate_unified_diff(original, original, "a", "b");
    assert!(same_diff.is_empty());

    // Structural extraction
    let xml = r#"<DR_Table name="whwmd400">
        <Column name="item" domain="tcitem" label="Item Code"/>
        <Column name="cwar" domain="tccwar" label="Warehouse"/>
        <Index name="1"><Column name="item"/></Index>
        <expression><![CDATA[some 4gl code]]></expression>
    </DR_Table>"#;

    let elements = extract_structural_elements(xml);
    assert_eq!(elements.len(), 3); // 2 Columns + 1 Index, expression ignored
    assert!(elements.contains_key("Column::item"));
    assert!(elements.contains_key("Column::cwar"));
    assert!(elements.contains_key("Index::1"));
}

#[tokio::test]
async fn test_fglstudio_revisions_and_diff_mock_suite() {
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

            let body = if req_line.contains("method=connect") {
                "<ConnectResponse><SessionID>s</SessionID><conid>0</conid></ConnectResponse>"
            } else if req_line.contains("method=share") {
                "<ConnectResponse><SessionID>s</SessionID><conid>1</conid></ConnectResponse>"
            } else if req_line.contains("method=bdecall") && !is_numeric_conid {
                let resp = "HTTP/1.1 500 Internal Server Error\r\nContent-Type: application/xml\r\nContent-Length: 74\r\nConnection: close\r\n\r\n<error><info>null</info><message>POST request failed</message><reason>0</reason></error>";
                let _ = socket.write_all(resp.as_bytes()).await;
                continue;
            } else if req.contains("bdename=FglStudio") && req.contains("bdemethod=GetRevisions") {
                assert!(req.contains("<compCode>whwmd400</compCode>"));
                "<FglStudioResponse><DataArea><revisions><revision number=\"1\" versionID=\"B61O_a_ext\" date=\"2026-01-10\" time=\"10:00:00\" author=\"userA\" comment=\"Initial creation\" task=\"TASK001\"/><revision number=\"2\" versionID=\"B61O_a_ext\" date=\"2026-02-15\" time=\"14:30:00\" author=\"userB\" comment=\"Added warehouse field\" task=\"TASK002\"/></revisions></DataArea></FglStudioResponse>"
            } else if req.contains("bdename=DR_Table") && req.contains("bdemethod=GetRevision") {
                assert!(req.contains("<name>whwmd400</name>"));
                "<DR_TableResponse><DataArea><DR_Table name=\"whwmd400\"><Column name=\"item\" domain=\"tcitem\" label=\"Item Code\"/><expression><![CDATA[function extern init()\n{\n\tmessage(\"Rev 1\");\n}\n]]></expression></DR_Table></DataArea></DR_TableResponse>"
            } else if req.contains("bdename=DR_Report") && req.contains("bdemethod=Generate") {
                assert!(req.contains("<name>txwhwmd440101000</name>"));
                assert!(req.contains("<table>whwmd400</table>"));
                "<DR_ReportResponse><DataArea><DR_Report name=\"txwhwmd440101000\" versionID=\"B61O_a_ext\" table=\"whwmd400\"><description>Warehouse Report</description><reportSize>132</reportSize><reportType>tabular</reportType><expression><![CDATA[| 4GL Generated Report]]></expression></DR_Report></DataArea></DR_ReportResponse>"
            } else {
                "<ok/>"
            };

            let resp = format!(
                "HTTP/1.1 200 OK\r\nContent-Type: application/xml\r\nContent-Length: {}\r\nConnection: close\r\n\r\n{}",
                body.len(),
                body
            );
            let _ = socket.write_all(resp.as_bytes()).await;
        }
    });

    let client = HttpClient::new(&base_url, "test_token");

    // 1. Test list_component_revisions
    let rev_res = list_component_revisions(
        &client,
        "table",
        "whwmd400",
        "B61O_a_ext",
        "TEST_PROJ",
        None,
    ).await.unwrap();

    assert_eq!(rev_res.total_revisions, 2);
    // Verifies sorted descending by number
    assert_eq!(rev_res.revisions[0].number, 2);
    assert_eq!(rev_res.revisions[0].author, "userB");
    assert_eq!(rev_res.revisions[1].number, 1);
    assert_eq!(rev_res.revisions[1].author, "userA");

    // 2. Test get_component_revision
    let raw_rev_xml = get_component_revision(
        &client,
        "table",
        "whwmd400",
        "B61O_a_ext",
        1,
        "TEST_PROJ",
        None,
    ).await.unwrap();

    assert!(raw_rev_xml.contains("<DR_Table name=\"whwmd400\">"));
    assert!(raw_rev_xml.contains("Rev 1"));

    // 3. Test diff_component
    let td = tempdir().unwrap();
    let act_dir = td.path();
    let tbl_dir = act_dir.join("wh").join("table").join("whwmd");
    fs::create_dir_all(&tbl_dir).unwrap();

    let local_tbl_xml = r#"<DR_Table name="whwmd400">
        <Column name="item" domain="tcitem" label="Item Code"/>
        <Column name="cwar" domain="tccwar" label="Warehouse"/>
        <expression><![CDATA[function extern init()
{
	message("Rev 2 modified");
}
]]></expression>
    </DR_Table>"#;

    fs::write(tbl_dir.join("whwmd400.tbl"), local_tbl_xml).unwrap();

    let diff_res = diff_component(
        &client,
        "table",
        "whwmd400",
        act_dir,
        Some("B61O_a_ext"),
        Some(1),
        "TEST_PROJ",
    ).await.unwrap();

    assert_eq!(diff_res.component_name, "whwmd400");
    assert_eq!(diff_res.target_revision, 1);
    assert!(diff_res.has_script_changes);
    assert!(diff_res.script_diff.contains("-	message(\"Rev 1\");"));
    assert!(diff_res.script_diff.contains("+	message(\"Rev 2 modified\");"));

    assert!(diff_res.has_structural_changes);
    assert_eq!(diff_res.structural_diff.added_elements.len(), 1);
    assert_eq!(diff_res.structural_diff.added_elements[0].name, "cwar");
    assert_eq!(diff_res.structural_diff.removed_elements.len(), 0);

    // 4. Test generate_report_on_server
    let admin = AdminFile::default();
    admin.save_to_path(&act_dir.join(".admin")).unwrap();

    let rpt_res = generate_report_on_server(
        &client,
        "txwhwmd440101000",
        "whwmd400",
        "B61O_a_ext",
        "Warehouse Report",
        "132",
        "tabular",
        "1",
        Some(&["item".to_string(), "cwar".to_string()]),
        true,
        "TEST_PROJ",
        Some(act_dir),
    ).await.unwrap();

    assert!(rpt_res.success);
    assert_eq!(rpt_res.report_name, "txwhwmd440101000");
    assert!(rpt_res.output_file.is_some());

    let rpt_file = act_dir.join("tx").join("report").join("whw").join("txwhwmd440101000.rpt");
    assert!(rpt_file.exists());
    let rpt_content = fs::read_to_string(&rpt_file).unwrap();
    assert!(rpt_content.contains("Warehouse Report"));

    // Verify .admin updated
    let reloaded_admin = AdminFile::load_from_path(&act_dir.join(".admin")).unwrap();
    assert!(reloaded_admin.get("tx/report/whw/txwhwmd440101000.rpt").is_some());
    let rpt_entry = reloaded_admin.get("tx/report/whw/txwhwmd440101000.rpt").unwrap();
    assert!(rpt_entry.is_created);
    assert!(rpt_entry.is_checked_out);
}
