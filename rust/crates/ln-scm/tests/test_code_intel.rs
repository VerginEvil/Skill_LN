use std::sync::Arc;
use tokio::io::{AsyncReadExt, AsyncWriteExt};
use tokio::net::TcpListener;
use tokio::sync::Mutex;

use ln_jca::client::HttpClient;
use ln_scm::code_intel::*;

#[tokio::test]
async fn test_fglstudio_code_intel_mock_suite() {
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

            let body = if req.contains("bdename=FglStudio") && req.contains("bdemethod=compileSource") {
                assert!(req.contains("<packageCode>tx</packageCode>"));
                assert!(req.contains("select * from tccom001"));
                "<FglStudioShowResponse><DataArea><compileResult><error line=\"5\" source=\"adhoc.4gl\">Syntax error</error><warning line=\"2\" source=\"adhoc.4gl\" level=\"W2\">Unused variable</warning><bicCommand>bic6.2 -w adhoc.4gl</bicCommand><summary totalErrors=\"1\" totalWarnings=\"1\"/></compileResult></DataArea></FglStudioShowResponse>"
            } else if req.contains("bdename=FglStudio") && req.contains("bdemethod=Searchpattern") {
                assert!(req.contains("<pattern>db.update</pattern>"));
                assert!(req.contains("<packageCode>wh</packageCode>"));
                "<FglStudioResponse><DataArea><results><match component=\"whwmd4100m000\" line=\"120\" snippet=\"db.update(twhwmd400)\" type=\"session\" package=\"wh\"/><match component=\"whwmd400\" line=\"45\" snippet=\"db.update\" type=\"table\" package=\"wh\"/></results></DataArea></FglStudioResponse>"
            } else if req.contains("bdename=fglstudio") && req.contains("bdemethod=isValidFunction") {
                assert!(req.contains("<sourceFileName>whwmd4100m000.4gl</sourceFileName>"));
                assert!(req.contains("<pattern>calculate_total</pattern>"));
                "<fglstudioResponse><DataArea><result>true</result></DataArea></fglstudioResponse>"
            } else if req.contains("bdename=fglstudio") && req.contains("bdemethod=GetCallHierarchyData") {
                assert!(req.contains("<callMode>callers</callMode>"));
                "<fglstudioResponse><DataArea><hierarchy><caller name=\"process_order\" type=\"function\" file=\"whwmd4100m000.4gl\" line=\"88\"/><caller name=\"batch_run\" type=\"function\" file=\"whwmd4200m000.4gl\" line=\"215\"/></hierarchy></DataArea></fglstudioResponse>"
            } else if req.contains("bdename=FglStudio") && req.contains("bdemethod=OpenDeclarationFunction") {
                assert!(req.contains("<compCodeFunction>whwmd4100m000</compCodeFunction>"));
                assert!(req.contains("<function>calculate_total</function>"));
                "<FglStudioResponse><DataArea><compCodeFunction>txwhwmdlib01</compCodeFunction><compTypeFunction>library</compTypeFunction><lineno>142</lineno></DataArea></FglStudioResponse>"
            } else if req.contains("bdename=FglStudio") && req.contains("bdemethod=GetScriptComponents") {
                assert!(req.contains("<packageCode>tx</packageCode>"));
                "<FglStudioResponse><DataArea><components><component name=\"whwmd400\" type=\"table\" versionID=\"B61O_a_ext\"/><component name=\"itccom0001\" type=\"include\" versionID=\"B61O_a_ext\"/></components></DataArea></FglStudioResponse>"
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

    // 1. Test compile_source_adhoc
    let comp_res = compile_source_adhoc(
        &client,
        "tx",
        "select * from tccom001",
        "-w",
        "TEST_PROJ",
        None,
    ).await.unwrap();

    assert!(!comp_res.success); // Has 1 error
    assert_eq!(comp_res.package_code, "tx");
    assert_eq!(comp_res.bic_command, "bic6.2 -w adhoc.4gl");
    assert_eq!(comp_res.errors.len(), 1);
    assert_eq!(comp_res.errors[0].line, 5);
    assert_eq!(comp_res.warnings.len(), 1);
    assert_eq!(comp_res.warnings[0].line, 2);

    // 2. Test search_server_pattern
    let search_res = search_server_pattern(
        &client,
        "db.update",
        "wh",
        "TEST_PROJ",
        None,
    ).await.unwrap();

    assert_eq!(search_res.total_matches, 2);
    assert_eq!(search_res.matches[0].component, "whwmd4100m000");
    assert_eq!(search_res.matches[0].line, 120);
    assert_eq!(search_res.matches[0].comp_type, "session");
    assert_eq!(search_res.matches[1].component, "whwmd400");
    assert_eq!(search_res.matches[1].line, 45);

    // 3. Test get_call_hierarchy
    let call_res = get_call_hierarchy(
        &client,
        "whwmd4100m000.4gl",
        "calculate_total",
        "callers",
        "TEST_PROJ",
        None,
    ).await.unwrap();

    assert!(call_res.is_valid);
    assert_eq!(call_res.total_nodes, 2);
    assert_eq!(call_res.hierarchy[0].function, "process_order");
    assert_eq!(call_res.hierarchy[0].line, 88);
    assert_eq!(call_res.hierarchy[1].function, "batch_run");
    assert_eq!(call_res.hierarchy[1].line, 215);

    // 4. Test open_declaration
    let decl_res = open_declaration(
        &client,
        "whwmd4100m000",
        "session",
        "calculate_total",
        "",
        "TEST_PROJ",
        None,
    ).await.unwrap();

    assert!(decl_res.found);
    assert_eq!(decl_res.component_code, "txwhwmdlib01");
    assert_eq!(decl_res.component_type, "library");
    assert_eq!(decl_res.line_number, 142);

    // 5. Test get_related_script_components
    let rel_res = get_related_script_components(
        &client,
        "tx",
        "#include <itccom0001>\ntable twhwmd400\n",
        "TEST_PROJ",
        None,
    ).await.unwrap();

    assert_eq!(rel_res.total_components, 2);
    assert_eq!(rel_res.components[0].name, "whwmd400");
    assert_eq!(rel_res.components[0].comp_type, "table");
    assert_eq!(rel_res.components[1].name, "itccom0001");
    assert_eq!(rel_res.components[1].comp_type, "include");
}
