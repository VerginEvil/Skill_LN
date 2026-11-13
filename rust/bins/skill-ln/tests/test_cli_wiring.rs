use clap::Parser;
use ln_eclipse_compat::{AdminFile, PropertyBucket};
use skill_ln::cli::Cli;
use skill_ln::commands::execute_command;
use std::sync::Arc;
use tempfile::tempdir;
use tokio::io::{AsyncReadExt, AsyncWriteExt};
use tokio::net::TcpListener;
use tokio::sync::Mutex;

#[tokio::test]
async fn test_cli_five_generators_single_xml_canonical_paths() {
    let tmp = tempdir().unwrap();
    let act = tmp.path();
    AdminFile::new().save_to_path(&act.join(".admin")).unwrap();

    let script_file = tmp.path().join("fn_body.4gl");
    std::fs::write(&script_file, "function extern void txcmgf001_hello()\n{\n}\n").unwrap();
    let content_file = tmp.path().join("cfg.json");
    std::fs::write(&content_file, "{\"ok\":true}").unwrap();

    let cmds = vec![
        vec![
            "skill-ln",
            "message",
            "--code",
            "txcmg0001",
            "--severity",
            "3",
            "--text",
            "Order blocked",
            "--activity",
            act.to_str().unwrap(),
        ],
        vec![
            "skill-ln",
            "question",
            "--code",
            "txcmg0002",
            "--domain",
            "tcyesno",
            "--text",
            "Proceed?",
            "--activity",
            act.to_str().unwrap(),
        ],
        vec![
            "skill-ln",
            "function",
            "--code",
            "txcmgf001",
            "--script-file",
            script_file.to_str().unwrap(),
            "--activity",
            act.to_str().unwrap(),
        ],
        vec![
            "skill-ln",
            "additional",
            "--code",
            "txcmgcfg",
            "--content-file",
            content_file.to_str().unwrap(),
            "--activity",
            act.to_str().unwrap(),
        ],
        vec![
            "skill-ln",
            "report",
            "--code",
            "txcmg04010100",
            "--paper-width",
            "132",
            "--activity",
            act.to_str().unwrap(),
        ],
    ];

    for args in cmds {
        let cli = Cli::parse_from(args);
        execute_command(cli.command).await.unwrap();
    }

    // Legacy plural dirs must NOT exist
    for plural in ["messages", "questions", "functions", "additional", "reports"] {
        assert!(
            !act.join(plural).exists(),
            "Legacy plural directory {:?} must not exist",
            plural
        );
    }

    // Canonical paths & zero-attribute TDE elements
    let msg_path = act.join("tx/message/txcmg0001.msg");
    let qst_path = act.join("tx/question/txcmg0002.qst");
    let fnc_path = act.join("tx/function/cmg/txcmgf001.fnc");
    let add_path = act.join("tx/additional/cmg/txcmgcfg.add");
    let rpt_path = act.join("tx/report/cmg/txcmg04010100.rpt");

    for (p, elem, name_val) in [
        (&msg_path, "DR_Message", "txcmg0001"),
        (&qst_path, "DR_Question", "txcmg0002"),
        (&fnc_path, "DR_Module", "txcmgf001"),
        (&add_path, "DR_AdditionalFile", "txcmgcfg"),
        (&rpt_path, "DR_Report", "txcmg04010100"),
    ] {
        assert!(p.exists(), "Canonical file missing: {:?}", p);
        let xml = std::fs::read_to_string(p).unwrap();
        assert!(xml.contains(&format!("<{elem} ")), "Expected <{elem} in {:?}", p);
        assert!(xml.contains(&format!("<name>{name_val}</name>")), "Expected <name> child in {:?}", p);
        assert!(
            !xml.contains(&format!("<{elem} name=")),
            "Attribute stub forbidden in {:?}",
            p
        );
    }

    let admin = AdminFile::load_from_path(&act.join(".admin")).unwrap();
    assert!(admin.get("tx/message/txcmg0001.msg").is_some());
    assert!(admin.get("tx/question/txcmg0002.qst").is_some());
    assert!(admin.get("tx/function/cmg/txcmgf001.fnc").is_some());
    assert!(admin.get("tx/additional/cmg/txcmgcfg.add").is_some());
    assert!(admin.get("tx/report/cmg/txcmg04010100.rpt").is_some());
}

#[tokio::test]
async fn test_cli_all_server_commands_wire_to_jca() {
    let listener = TcpListener::bind("127.0.0.1:0").await.unwrap();
    let addr = listener.local_addr().unwrap();
    let base_url = format!("http://127.0.0.1:{}/TENANT/LN/webservice", addr.port());

    let seen: Arc<Mutex<Vec<String>>> = Arc::new(Mutex::new(Vec::new()));
    let seen_bg = seen.clone();

    tokio::spawn(async move {
        let mut share_n = 1u32;
        while let Ok((mut socket, _)) = listener.accept().await {
            let mut buf = [0u8; 32768];
            let n = socket.read(&mut buf).await.unwrap_or(0);
            let req = String::from_utf8_lossy(&buf[..n]).to_string();
            let req_line = req.lines().next().unwrap_or("").to_string();
            seen_bg.lock().await.push(req_line.clone());

            let is_numeric_conid = req_line
                .split("conid=")
                .nth(1)
                .map(|r| r.split(['&', ' ']).next().unwrap_or(""))
                .map(|c| !c.is_empty() && c.chars().all(|ch| ch.is_ascii_digit()))
                .unwrap_or(false);

            let (status, headers, body) = if req_line.contains("method=connect") {
                ("HTTP/1.1 200 OK", "Set-Cookie: JSESSIONID=cli_s0; Path=/\r\nContent-Type: application/xml\r\n", "<ConnectResponse><SessionID>s</SessionID><conid>0</conid></ConnectResponse>".to_string())
            } else if req_line.contains("method=share") {
                let cid = share_n;
                share_n += 1;
                ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", format!("<ConnectResponse><SessionID>s</SessionID><conid>{cid}</conid></ConnectResponse>"))
            } else if req_line.contains("method=ping") {
                ("HTTP/1.1 200 OK", "Content-Type: text/plain\r\n", "pong".to_string())
            } else if req_line.contains("method=disconnect") {
                ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", "<DisconnectResponse/>".to_string())
            } else if req_line.contains("method=bdecall") && !is_numeric_conid {
                ("HTTP/1.1 500 Internal Server Error", "Content-Type: application/xml\r\n", "<error><info>null</info><message>POST request failed</message><reason>0</reason></error>".to_string())
            } else if req_line.contains("bdename=Application") && req_line.contains("bdemethod=List") {
                ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", "<ApplicationListResponse><DataArea><Application><name>PM</name><description>PM App</description><release>10.8</release></Application></DataArea></ApplicationListResponse>".to_string())
            } else if req_line.contains("bdename=SoftwareProject") && req_line.contains("bdemethod=List") {
                ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", "<SoftwareProjectListResponse><DataArea><SoftwareProject><projectName>PROJ_1</projectName><projectDescription>Demo</projectDescription><projectStatus>active</projectStatus><typeOfProject>standard</typeOfProject><Task><taskName>task_01</taskName><taskStatus>opened</taskStatus><typeOfTask>feature</typeOfTask><assignedTo>u</assignedTo></Task></SoftwareProject></DataArea></SoftwareProjectListResponse>".to_string())
            } else if req_line.contains("bdename=SoftwareProject_V2") && req_line.contains("bdemethod=Show") {
                ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", "<SoftwareProject_V2ShowResponse><DataArea><SoftwareProject_V2><projectName>PROJ_1</projectName><projectDescription>Demo</projectDescription><projectVersionID>B61O_a_ext</projectVersionID><developmentEnvironment>DEV</developmentEnvironment><developmentRepositoryAddress>PROJ_1_dev</developmentRepositoryAddress><runtimeRepositoryAddress>PROJ_1_rt</runtimeRepositoryAddress><integrationWithPMC>false</integrationWithPMC><Package>tx</Package><Task><taskName>task_01</taskName><labelUUID>uuid-lbl-1</labelUUID><taskUUID>uuid-tsk-1</taskUUID><taskVersionID>1</taskVersionID><taskDescription>T1</taskDescription><typeOfTask>feature</typeOfTask><assignedTo>u</assignedTo><taskStatus>opened</taskStatus><taskSeverity>medium</taskSeverity><functionalChange>no</functionalChange></Task></SoftwareProject_V2></DataArea></SoftwareProject_V2ShowResponse>".to_string())
            } else if req_line.contains("bdename=SoftwareProject_V2") && req_line.contains("bdemethod=Change") {
                ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", "<SoftwareProject_V2ChangeResponse><DataArea><SoftwareProject_V2><Task><taskName>task_02</taskName><labelUUID>uuid-lbl-2</labelUUID><taskVersionID>1</taskVersionID><taskStatus>created</taskStatus></Task></SoftwareProject_V2></DataArea></SoftwareProject_V2ChangeResponse>".to_string())
            } else if req_line.contains("bdename=SoftwareProject") && req_line.contains("bdemethod=Change") {
                ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", "<SoftwareProjectChangeResponse><DataArea><SoftwareProject><Task><taskVersionID>2</taskVersionID></Task></SoftwareProject></DataArea></SoftwareProjectChangeResponse>".to_string())
            } else if req_line.contains("bdename=CMLabel") && req_line.contains("bdemethod=GetModifiedComponents") {
                ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", "<CMLabelResponse><DataArea><ModifiedComponent><name>tcibd001</name><type>table</type><package>tc</package></ModifiedComponent></DataArea></CMLabelResponse>".to_string())
            } else if req_line.contains("bdename=FglStudio") && req_line.contains("bdemethod=CleanActivity") {
                ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", "<FglStudioResponse><DataArea><Success/></DataArea></FglStudioResponse>".to_string())
            } else if req_line.contains("bdename=StudioComponent") && req_line.contains("bdemethod=GetBrowseList") {
                ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", "<GetBrowseListResponse><DataArea><Component><name>tcibd001</name><type>table</type><package>tc</package><module>ibd</module><description>Item Data</description><versionID>B61O_a_ext</versionID><isCheckedOut>no</isCheckedOut><isExpired>no</isExpired></Component></DataArea></GetBrowseListResponse>".to_string())
            } else if req_line.contains("bdename=StudioComponent") && (req_line.contains("bdemethod=GetProjectSource") || req_line.contains("bdemethod=GetActivitySource")) {
                ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", "<StudioComponentResponse><DataArea><DR_Table xmlns=\"http://www.infor.com/businessline/application/dr\" version=\"1.0\"><description>Item</description><name>tcibd001</name><Column><name>item</name></Column><Source><expression><![CDATA[function extern void dummy()\n{\n}\n]]></expression></Source></DR_Table></DataArea></StudioComponentResponse>".to_string())
            } else if req_line.contains("bdemethod=DR_Create") || req_line.contains("bdemethod=CheckOut") || req_line.contains("bdemethod=Put") || req_line.contains("bdemethod=CheckIn") || req_line.contains("bdemethod=UndoCheckOut") {
                ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", "<Response><DataArea><DR_Table><name>tcibd001</name><versionID>B61O_a_ext.1</versionID><dateTime>2026-11-13T00:00:00Z</dateTime><Source><expression><![CDATA[function extern void dummy()\n{\n}\n]]></expression></Source></DR_Table></DataArea></Response>".to_string())
            } else if req_line.contains("bdename=FglStudio") && req_line.contains("bdemethod=compileSource") {
                ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", "<FglStudioShowResponse><DataArea><compileResult><summary totalErrors=\"0\" totalWarnings=\"0\"/></compileResult></DataArea></FglStudioShowResponse>".to_string())
            } else if req_line.contains("bdename=FglStudio") && req_line.contains("bdemethod=Searchpattern") {
                ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", "<FglStudioResponse><DataArea><results><match component=\"tcibd001\" line=\"10\" snippet=\"db.eq\" type=\"table\" package=\"tc\"/></results></DataArea></FglStudioResponse>".to_string())
            } else if req_line.contains("bdemethod=isValidFunction") {
                ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", "<fglstudioResponse><DataArea><result>true</result></DataArea></fglstudioResponse>".to_string())
            } else if req_line.contains("bdemethod=GetCallHierarchyData") {
                ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", "<fglstudioResponse><DataArea><hierarchy><caller name=\"main_fn\" type=\"function\" file=\"tcibd001.4gl\" line=\"5\"/></hierarchy></DataArea></fglstudioResponse>".to_string())
            } else if req_line.contains("bdemethod=OpenDeclarationFunction") {
                ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", "<FglStudioResponse><DataArea><compCodeFunction>txlib01</compCodeFunction><compTypeFunction>library</compTypeFunction><lineno>12</lineno></DataArea></FglStudioResponse>".to_string())
            } else if req_line.contains("bdemethod=GetScriptComponents") {
                ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", "<FglStudioResponse><DataArea><components><component name=\"tcibd001\" type=\"table\" versionID=\"B61O_a_ext\"/></components></DataArea></FglStudioResponse>".to_string())
            } else if req_line.contains("bdemethod=GetRevisions") {
                ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", "<FglStudioResponse><DataArea><revisions><revision number=\"1\" versionID=\"B61O_a_ext\" date=\"2026-01-01\" time=\"00:00:00\" author=\"u\" comment=\"init\" task=\"task_01\"/></revisions></DataArea></FglStudioResponse>".to_string())
            } else if req_line.contains("bdemethod=GetRevision") {
                ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", "<DR_TableResponse><DataArea><DR_Table><name>tcibd001</name><Source><expression><![CDATA[| rev1]]></expression></Source></DR_Table></DataArea></DR_TableResponse>".to_string())
            } else if req_line.contains("bdename=DR_Report") && req_line.contains("bdemethod=Generate") {
                ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", "<DR_ReportResponse><DataArea><DR_Report><name>txcmg04010100</name><Source><expression><![CDATA[| rep]]></expression></Source></DR_Report></DataArea></DR_ReportResponse>".to_string())
            } else if req_line.contains("bdemethod=Compile") {
                ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", "<DR_TableShowResponse><DataArea><compileResult><summary totalErrors=\"0\" totalWarnings=\"0\"/></compileResult></DataArea></DR_TableShowResponse>".to_string())
            } else if req_line.contains("bdemethod=ValidateDevelopmentActivity") {
                ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", "<DR_SolutionShowResponse><DataArea><Ok/></DataArea></DR_SolutionShowResponse>".to_string())
            } else {
                ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", "<Ok/>".to_string())
            };

            let resp = format!("{status}\r\n{headers}Content-Length: {}\r\nConnection: close\r\n\r\n{body}", body.len());
            let _ = socket.write_all(resp.as_bytes()).await;
        }
    });

    let tmp = tempdir().unwrap();
    let ws = tmp.path();
    let settings_dir = ws.join(".metadata/.plugins/org.eclipse.core.runtime/.settings");
    std::fs::create_dir_all(&settings_dir).unwrap();
    std::fs::write(
        settings_dir.join("com.infor.erpln.jca.connectivity.prefs"),
        "ActivationType1=http_oauth2\nCloudEnvironment1=MOCK_ENV\nCompany1=0\nConfigurationCount=2\nHostName1=https\\://unused.invalid/LN/webservice\nName1=ProjectServer\n",
    )
    .unwrap();

    let act = ws.join("task_01 [PROJ_1]");
    std::fs::create_dir_all(act.join("tc/table/ibd")).unwrap();
    std::fs::write(
        act.join(".project"),
        "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<projectDescription>\n\t<name>task_01 [PROJ_1]</name>\n</projectDescription>\n",
    )
    .unwrap();
    let tbl_path = act.join("tc/table/ibd/tcibd001.tbl");
    std::fs::write(
        &tbl_path,
        "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<DR_Table xmlns=\"http://www.infor.com/businessline/application/dr\" version=\"1.0\">\n  <name>tcibd001</name>\n  <Source><expression><![CDATA[function extern void dummy()\n{\n}\n]]></expression></Source>\n</DR_Table>\n",
    )
    .unwrap();
    let mut admin = AdminFile::new();
    admin.after_get("tc/table/ibd/tcibd001.tbl");
    admin.save_to_path(&act.join(".admin")).unwrap();

    let mut bucket = PropertyBucket::new();
    bucket.set_property("ProjectName", "PROJ_1", "", "");
    bucket.set_property("TaskName", "task_01", "", "");
    bucket.set_property("Label", "uuid-lbl-1", "", "");
    bucket.set_property("ApplicationRelease", "B61O_a_ext", "", "");
    bucket.set_property("DevelopmentTimeRepositoryAddress", "PROJ_1_dev", "", "");
    bucket.save_to_path(&act.join(".settings/properties.index")).unwrap();

    std::env::set_var("LN_WORKSPACE", ws);
    std::env::set_var("LN_JCA_ENDPOINT", &base_url);
    std::env::set_var("LN_ACCESS_TOKEN", "cli_mock_tok");

    let ws_s = ws.to_str().unwrap();
    let act_s = act.to_str().unwrap();

    let invocations: Vec<Vec<&str>> = vec![
        vec!["skill-ln", "project"],
        vec!["skill-ln", "project-info", "--project", "PROJ_1"],
        vec!["skill-ln", "activity", "--project", "PROJ_1"],
        vec!["skill-ln", "clean-activity", "--project", "PROJ_1", "--task", "task_01"],
        vec!["skill-ln", "explorer", "--type", "table", "--filter", "tcibd*", "--project", "PROJ_1", "--workspace", ws_s],
        vec!["skill-ln", "get-component", "--type", "table", "--name", "tcibd001", "--inspect", "--project", "PROJ_1", "--workspace", ws_s],
        vec!["skill-ln", "sync-reference", "--type", "table", "--name", "tcibd001", "--workspace-dir", ws_s],
        vec!["skill-ln", "compile-source", "--package", "tc", "--code", "function extern void f() {}"],
        vec!["skill-ln", "search-server", "--pattern", "db.eq", "--package", "tc"],
        vec!["skill-ln", "call-hierarchy", "--source-file", "tcibd001.4gl", "--function", "dummy", "--mode", "callers"],
        vec!["skill-ln", "open-declaration", "--comp", "tcibd001", "--type", "table", "--function", "dummy"],
        vec!["skill-ln", "related-components", "--package", "tc", "--code", "table ttcibd001"],
        vec!["skill-ln", "revisions", "--type", "table", "--name", "tcibd001"],
        vec!["skill-ln", "diff-component", "--type", "table", "--name", "tcibd001", "--activity", act_s],
        vec!["skill-ln", "generate-report-server", "--code", "txcmg04010100", "--table", "tcibd001", "--activity", act_s],
        vec!["skill-ln", "checkout-component", "--type", "table", "--name", "tcibd001", "--activity", act_s, "--project", "PROJ_1"],
        vec!["skill-ln", "checkin-component", "--type", "table", "--name", "tcibd001", "--activity", act_s, "--project", "PROJ_1", "--comment", "ci"],
        vec!["skill-ln", "prepare-end-activity", "--activity", act_s, "--project", "PROJ_1"],
        vec!["skill-ln", "deploy-test", "--type", "table", "--name", "tcibd001", "--activity", act_s, "--mode", "compile-only", "--dry-run"],
        vec!["skill-ln", "build", "--activity", act_s],
    ];

    for args in invocations {
        let cli = Cli::parse_from(args);
        execute_command(cli.command).await.unwrap();
    }

    std::env::remove_var("LN_WORKSPACE");
    std::env::remove_var("LN_JCA_ENDPOINT");
    std::env::remove_var("LN_ACCESS_TOKEN");

    let log = seen.lock().await;
    assert!(log.iter().any(|l| l.contains("bdename=Application")), "Expected Application.List JCA hit");
    assert!(log.iter().any(|l| l.contains("bdename=SoftwareProject_V2")), "Expected SoftwareProject_V2.Show JCA hit");
    assert!(log.iter().any(|l| l.contains("bdemethod=CleanActivity")), "Expected CleanActivity JCA hit");
    assert!(log.iter().any(|l| l.contains("bdemethod=GetBrowseList")), "Expected GetBrowseList JCA hit");
    assert!(log.iter().any(|l| l.contains("bdemethod=compileSource")), "Expected compileSource JCA hit");
    assert!(log.iter().any(|l| l.contains("bdemethod=Searchpattern")), "Expected Searchpattern JCA hit");
    assert!(log.iter().any(|l| l.contains("bdemethod=GetRevisions")), "Expected GetRevisions JCA hit");
    assert!(log.iter().any(|l| l.contains("bdemethod=CheckOut")), "Expected CheckOut JCA hit");
    assert!(log.iter().any(|l| l.contains("bdemethod=CheckIn")), "Expected CheckIn JCA hit");
    assert!(log.iter().any(|l| l.contains("bdemethod=ValidateDevelopmentActivity")), "Expected ValidateDevelopmentActivity JCA hit");
    assert!(log.iter().any(|l| l.contains("method=disconnect")), "Expected clean disconnect on exit");
}
