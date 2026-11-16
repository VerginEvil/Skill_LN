use std::fs;
use std::sync::Arc;
use tempfile::tempdir;
use tokio::io::{AsyncReadExt, AsyncWriteExt};
use tokio::net::TcpListener;
use tokio::sync::Mutex;

use ln_eclipse_compat::AdminFile;
use ln_jca::client::HttpClient;
use ln_scm::build::*;

#[tokio::test]
async fn test_compile_diagnostics_and_mock_server() {
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
            } else if req.contains("bdename=DR_Table") && req.contains("bdemethod=Compile") {
                assert!(req.contains("<name>ttadv999</name>"));
                assert!(req.contains("<isCheckedOut>yes</isCheckedOut>"));
                "<DR_TableShowResponse><DataArea><compileResult><error line=\"42\" source=\"ttadv999.4gl\">Undefined identifier 'foo'</error><warning line=\"15\" source=\"ttadv999.4gl\" level=\"W1\">Variable 'bar' is unused</warning><bicCommand>bic6.2 -w -u ttadv999</bicCommand><summary totalErrors=\"1\" totalWarnings=\"1\"/></compileResult></DataArea></DR_TableShowResponse>"
            } else if req.contains("bdename=DR_Table") && req.contains("bdemethod=ConvertToRuntime") {
                assert!(req.contains("executionMethod"));
                assert!(req.contains("synchronous"));
                "<DR_TableResponse><DataArea><ok/></DataArea></DR_TableResponse>"
            } else if req.contains("bdename=DR_Table") && req.contains("bdemethod=CreateTables") {
                assert!(req.contains("executionMethod"));
                assert!(req.contains("synchronous"));
                "<DR_TableResponse><DataArea><ok/></DataArea></DR_TableResponse>"
            } else if req.contains("bdename=VSC") && req.contains("bdemethod=executeVSC") {
                assert!(req.contains("<componentName>ttadv999</componentName>"));
                assert!(req.contains("<componentType>table</componentType>"));
                "<VSCShowResponse><DataArea><vscResult verificationCode=\"SUCCESS\"><warning accepted=\"false\" blocking=\"false\" messageID=\"W100\" warningID=\"WARN1\" priority=\"low\" location=\"line 10\" element=\"elem\"><![CDATA[Formatting hint]]></warning></vscResult></DataArea></VSCShowResponse>"
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
    let td = tempdir().unwrap();
    let act_dir = td.path();

    // 1. Test Compile with error diagnostics parsing
    let comp_res = compile_component(&client, "table", "ttadv999", "PROJ_1", Some(act_dir), true)
        .await
        .unwrap();

    assert!(!comp_res.success);
    assert_eq!(comp_res.errors.len(), 1);
    assert_eq!(comp_res.errors[0].line, 42);
    assert_eq!(comp_res.errors[0].message, "Undefined identifier 'foo'");
    assert_eq!(comp_res.errors[0].source, "ttadv999.4gl");

    assert_eq!(comp_res.warnings.len(), 1);
    assert_eq!(comp_res.warnings[0].line, 15);
    assert_eq!(comp_res.warnings[0].code, "W1");

    assert_eq!(comp_res.bic_command, "bic6.2 -w -u ttadv999");
    assert_eq!(comp_res.summary.get("totalErrors").map(|s| s.as_str()), Some("1"));

    // 2. Test ConvertToRuntime (CRDD)
    let crdd_ok = convert_to_runtime(&client, "table", "ttadv999", "PROJ_1", Some(act_dir))
        .await
        .unwrap();
    assert!(crdd_ok);

    // 3. Test CreateTables
    let ct_ok = create_tables(&client, "ttadv999", "PROJ_1", Some(act_dir))
        .await
        .unwrap();
    assert!(ct_ok);

    // 4. Test ExecuteVSC and .admin update
    let comp_file = act_dir.join("tt").join("table").join("adv").join("ttadv999.tbl");
    fs::create_dir_all(comp_file.parent().unwrap()).unwrap();
    fs::write(&comp_file, "<DR_Table><name>ttadv999</name></DR_Table>").unwrap();

    let admin_path = act_dir.join(".admin");
    let mut admin = AdminFile::new();
    admin.after_create("tt/table/adv/ttadv999.tbl");
    admin.save_to_path(&admin_path).unwrap();

    let vsc_res = execute_vsc(&client, "table", "ttadv999", "PROJ_1", Some(act_dir))
        .await
        .unwrap();

    assert!(vsc_res.passed);
    assert_eq!(vsc_res.verification_code, "SUCCESS");
    assert_eq!(vsc_res.warnings.len(), 1);
    assert!(!vsc_res.warnings[0].blocking);
    assert_eq!(vsc_res.warnings[0].message, "Formatting hint");

    // Verify .admin m_isVSCHappy is true
    let updated_admin = AdminFile::load_from_path(&admin_path).unwrap();
    let comp = updated_admin.get("tt/table/adv/ttadv999.tbl").unwrap();
    assert!(comp.is_vsc_happy);
}

#[tokio::test]
async fn test_deploy_test_dry_run_and_extension_block() {
    let td = tempdir().unwrap();
    let act_dir = td.path();
    let client = HttpClient::new("http://127.0.0.1:9999", "dummy");

    // 1. Extension component block
    let err = deploy_test(&client, "session", "txesswhwmd4300m000", act_dir, "PROJ_1", "comment", "compile-only", false)
        .await
        .unwrap_err();
    assert!(err.to_string().contains("[GET_ONLY_EXTENSION]") || err.to_string().contains("Extension Modeler Rule"));

    // 2. Dry run compile-only
    let dry_res = deploy_test(&client, "table", "ttadv999", act_dir, "PROJ_1", "comment", "compile-only", true)
        .await
        .unwrap();
    assert!(dry_res.dry_run);
    assert!(dry_res.success);
    assert_eq!(dry_res.planned_steps, vec!["Put", "Compile", "executeVSC", "CheckIn"]);
    assert!(dry_res.lock_warning.is_empty());

    // 3. Dry run schema-crdd with table lock warning
    let dry_schema = deploy_test(&client, "table", "ttadv999", act_dir, "PROJ_1", "comment", "schema-crdd", true)
        .await
        .unwrap();
    assert!(dry_schema.dry_run);
    assert!(dry_schema.success);
    assert_eq!(
        dry_schema.planned_steps,
        vec!["Put", "Compile", "ConvertToRuntime", "CreateTables", "executeVSC", "CheckIn"]
    );
    assert!(dry_schema.lock_warning.contains("[TABLE LOCK WARNING]"));
}

#[tokio::test]
async fn test_prepare_end_activity_and_diagnose() {
    let listener = TcpListener::bind("127.0.0.1:0").await.unwrap();
    let addr = listener.local_addr().unwrap();
    let base_url = format!("http://127.0.0.1:{}/TENANT/LN/webservice", addr.port());

    tokio::spawn(async move {
        while let Ok((mut socket, _)) = listener.accept().await {
            let mut buf = [0u8; 8192];
            let n = socket.read(&mut buf).await.unwrap_or(0);
            let req = String::from_utf8_lossy(&buf[..n]).to_string();

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
            } else if req.contains("bdename=CMLabel") && req.contains("bdemethod=GetModifiedComponents") {
                "<CMLabelResponse><DataArea><ModifiedComponent><name>ttadv999</name><type>table</type></ModifiedComponent></DataArea></CMLabelResponse>"
            } else if req.contains("bdename=DR_Solution") && req.contains("bdemethod=ValidateDevelopmentActivity") {
                assert!(req.contains("<CMLabel>"));
                assert!(req.contains("<name>ttadv999</name>"));
                "<DR_SolutionShowResponse><DataArea><result>VALID</result></DataArea></DR_SolutionShowResponse>"
            } else if req.contains("bdename=DR_Table") && req.contains("bdemethod=Compile") {
                "<DR_TableShowResponse><DataArea><compileResult/></DataArea></DR_TableShowResponse>"
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
    let td = tempdir().unwrap();
    let act_dir = td.path();

    // Bootstrap local metadata files: .project, .admin, .settings/properties.index
    fs::write(act_dir.join(".project"), "<projectDescription><name>TASK1 [PROJ_1]</name></projectDescription>").unwrap();
    let admin_path = act_dir.join(".admin");
    let mut admin = AdminFile::new();
    admin.after_create("tt/table/adv/ttadv999.tbl");
    admin.save_to_path(&admin_path).unwrap();

    let settings_dir = act_dir.join(".settings");
    fs::create_dir_all(&settings_dir).unwrap();
    fs::write(settings_dir.join("properties.index"), "activityUUID=uuid-123\nsoftwareProject=PROJ_1\nTaskName=TASK1\n").unwrap();

    let comp_file = act_dir.join("tt").join("table").join("adv").join("ttadv999.tbl");
    fs::create_dir_all(comp_file.parent().unwrap()).unwrap();
    fs::write(&comp_file, "<DR_Table><name>ttadv999</name><expression>table tttadv999</expression></DR_Table>").unwrap();

    // Run prepare_end_activity
    let prep_res = prepare_end_activity(&client, act_dir, "PROJ_1").await.unwrap();
    assert_eq!(prep_res.activity, "TASK1");
    assert_eq!(prep_res.project, "PROJ_1");
    assert!(prep_res.server_valid);
    assert!(prep_res.metadata_synced);
    assert!(prep_res.ready_for_human_review);
    assert_eq!(prep_res.components_count, 1);
    assert!(prep_res.commit_summary.contains("READY FOR HUMAN DELIVERY APPROVAL"));

    // Run diagnose
    let diag = diagnose(&client, "table", "ttadv999", "PROJ_1", Some(act_dir)).await.unwrap();
    assert_eq!(diag.component, "ttadv999");
    assert!(diag.compiler_success);
}
