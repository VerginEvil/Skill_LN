use ln_jca::bde_manager::{BdeExecutionMode, BdeParams, JcaBdeManager};
use ln_jca::client::{ConnectOptions, HttpClient};
use ln_jca::filter::{BdeFilter, BdeSelection};
use tokio::io::{AsyncReadExt, AsyncWriteExt};
use tokio::net::TcpListener;

#[tokio::test]
async fn test_jca_client_and_bde_manager_lifecycle() {
    let listener = TcpListener::bind("127.0.0.1:0").await.unwrap();
    let addr = listener.local_addr().unwrap();
    let base_url = format!("http://127.0.0.1:{}/TENANT/LN/webservice", addr.port());

    tokio::spawn(async move {
        while let Ok((mut socket, _)) = listener.accept().await {
            let mut buf = [0u8; 4096];
            let n = socket.read(&mut buf).await.unwrap_or(0);
            let req = String::from_utf8_lossy(&buf[..n]);

            let req_lower = req.to_lowercase();
            let req_line = req.lines().next().unwrap_or("");
            let is_numeric_conid = req_line
                .split("conid=")
                .nth(1)
                .map(|rest| rest.split(['&', ' ']).next().unwrap_or(""))
                .map(|c| !c.is_empty() && c.chars().all(|ch| ch.is_ascii_digit()))
                .unwrap_or(false);

            let (status_line, headers, body) = if req.contains("method=connect") {
                assert!(req_lower.contains("authorization: bearer mock_access_token"));
                assert!(req_lower.contains("user-agent: jcawebclient (lnstudio)"));
                let body = "<ConnectResponse><company>0</company><companyDesc>Test Co</companyDesc><currentPack>B61U_a</currentPack><firstdayofweek>1</firstdayofweek><lnuser>testuser</lnuser><timeout>300</timeout><conid>1</conid><version>1</version></ConnectResponse>";
                ("HTTP/1.1 200 OK", "Set-Cookie: JSESSIONID=mock_session_123; Path=/\r\nContent-Type: application/xml\r\n", body)
            } else if req.contains("method=share") {
                assert!(req_lower.contains("cookie: jsessionid=mock_session_123"));
                let body = "<ConnectResponse><company>0</company><conid>2</conid><version>1</version></ConnectResponse>";
                ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", body)
            } else if req.contains("method=disconnect") {
                ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", "<DisconnectResponse/>")
            } else if req.contains("method=ping") {
                assert!(req_lower.contains("cookie: jsessionid=mock_session_123"));
                ("HTTP/1.1 200 OK", "Content-Type: text/plain\r\n", "pong")
            } else if req.contains("method=bdecall") && !is_numeric_conid {
                ("HTTP/1.1 500 Internal Server Error", "Content-Type: application/xml\r\n", "<error><info>null</info><message>POST request failed</message><reason>0</reason></error>")
            } else if req.contains("method=bdecall") && req.contains("bdemethod=ListItems") {
                assert!(req_lower.contains("cookie: jsessionid=mock_session_123"));
                if req.contains("<iteratorID>42</iteratorID>") {
                    // Page 2 (end)
                    let body = "<ListItemsResponse><ControlArea><iteratorID>-1</iteratorID></ControlArea><DataArea><Item id=\"2\"/></DataArea></ListItemsResponse>";
                    ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", body)
                } else {
                    // Page 1
                    let body = "<ListItemsResponse><ControlArea><iteratorID>42</iteratorID></ControlArea><DataArea><Item id=\"1\"/></DataArea></ListItemsResponse>";
                    ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", body)
                }
            } else if req.contains("method=bdecall") && req.contains("bdemethod=GetItem") {
                // SHOW mode
                let body = "<GetItemResponse><ControlArea/><DataArea><ItemDetail id=\"100\"><name>Widget</name></ItemDetail></DataArea></GetItemResponse>";
                ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", body)
            } else if req.contains("method=bdecall") && req.contains("bdemethod=FailCall") {
                // BDE Exception via header
                let body = "<InformationArea><message>Invalid component ID</message></InformationArea>";
                ("HTTP/1.1 200 OK", "X-Infor-BDEException: 101\r\nContent-Type: application/xml\r\n", body)
            } else if req.contains("method=file_download") {
                ("HTTP/1.1 200 OK", "Content-Type: application/octet-stream\r\n", "mock_file_content")
            } else if req.contains("method=file_upload") {
                ("HTTP/1.1 200 OK", "Content-Type: text/plain\r\n", "uploaded")
            } else {
                ("HTTP/1.1 404 Not Found", "Content-Type: text/plain\r\n", "Not Found")
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

    let client = HttpClient::new(&base_url, "mock_access_token");

    // 1. Connect
    let connect_resp = client.connect(&ConnectOptions::default()).await.unwrap();
    assert_eq!(connect_resp.company, "0");
    assert_eq!(connect_resp.company_desc, "Test Co");
    assert_eq!(connect_resp.ln_user, "testuser");
    assert_eq!(connect_resp.conid, "1");
    assert_eq!(connect_resp.version, 1);

    // 2. Share
    let share_resp = client.share(Some("0")).await.unwrap();
    assert_eq!(share_resp.conid, "2");

    // 3. Keepalive ping
    client.ping().await.unwrap();

    // 4. JcaBdeManager - Mode 0 (LIST) with 2-page pagination loop
    let bde_mgr = JcaBdeManager::new(&client, "1");
    let list_params = BdeParams {
        bde_name: "ItemManager".into(),
        method_name: "ListItems".into(),
        mode: Some(BdeExecutionMode::List),
        selection: Some(BdeSelection::from_fields(&["item", "dsca"])),
        filter: BdeFilter::parse("item == 'A'"),
        max_objects: Some(10),
        ..Default::default()
    };
    let list_result = bde_mgr.execute(&list_params).await.unwrap();
    assert!(list_result.contains("<Item id=\"1\"/>"));
    assert!(list_result.contains("<Item id=\"2\"/>"));
    assert_eq!(list_result, "<DataArea><Item id=\"1\"/><Item id=\"2\"/></DataArea>");

    // 5. JcaBdeManager - Mode 1 (SHOW) extracting first child of DataArea
    let show_params = BdeParams {
        bde_name: "ItemManager".into(),
        method_name: "GetItem".into(),
        mode: Some(BdeExecutionMode::Show),
        request_xml: Some("<Query id=\"100\"/>".into()),
        ..Default::default()
    };
    let show_result = bde_mgr.execute(&show_params).await.unwrap();
    assert_eq!(show_result, "<ItemDetail id=\"100\"><name>Widget</name></ItemDetail>");

    // 6. X-Infor-BDEException handling
    let fail_params = BdeParams {
        bde_name: "ItemManager".into(),
        method_name: "FailCall".into(),
        mode: Some(BdeExecutionMode::Bde),
        ..Default::default()
    };
    let err = bde_mgr.execute(&fail_params).await.unwrap_err();
    match err {
        ln_jca::JcaError::Bde(bde_err) => {
            assert_eq!(bde_err.exception_code, Some(101));
            assert!(bde_err.message.contains("Invalid component ID"));
        }
        other => panic!("Expected JcaError::Bde, got {:?}", other),
    }

    // 7. File Download & Upload
    let downloaded = client.file_download("sample.txt", Some("text")).await.unwrap();
    assert_eq!(String::from_utf8_lossy(&downloaded), "mock_file_content");

    client.file_upload("sample.txt", Some("text"), b"new_data").await.unwrap();

    // 8. Protocol Hard-Block pre-check against EndActivity
    let blocked_params = BdeParams {
        bde_name: "ActivityManager".into(),
        method_name: "EndActivity".into(),
        mode: Some(BdeExecutionMode::Bde),
        ..Default::default()
    };
    let blocked_err = bde_mgr.execute(&blocked_params).await.unwrap_err();
    match blocked_err {
        ln_jca::JcaError::Bde(bde_err) => {
            assert!(bde_err.message.contains("[PROHIBITED_OPERATION]"));
        }
        other => panic!("Expected JcaError::Bde prohibited operation, got {:?}", other),
    }
}

#[tokio::test]
async fn test_conid_multiplexing_logical_to_numeric() {
    use std::sync::Arc;
    use tokio::sync::Mutex;

    let listener = TcpListener::bind("127.0.0.1:0").await.unwrap();
    let addr = listener.local_addr().unwrap();
    let base_url = format!("http://127.0.0.1:{}/TENANT/LN/webservice", addr.port());
    let seen = Arc::new(Mutex::new(Vec::<String>::new()));
    let seen_bg = seen.clone();

    tokio::spawn(async move {
        let mut share_counter = 1u32;
        while let Ok((mut socket, _)) = listener.accept().await {
            let mut buf = [0u8; 4096];
            let n = socket.read(&mut buf).await.unwrap_or(0);
            let req = String::from_utf8_lossy(&buf[..n]).to_string();
            let req_line = req.lines().next().unwrap_or("").to_string();
            seen_bg.lock().await.push(req_line.clone());

            let (status_line, headers, body) = if req_line.contains("method=connect") {
                ("HTTP/1.1 200 OK", "Set-Cookie: JSESSIONID=s0; Path=/\r\nContent-Type: application/xml\r\n", "<ConnectResponse><SessionID>s</SessionID><conid>0</conid></ConnectResponse>".to_string())
            } else if req_line.contains("method=share") {
                let cid = share_counter;
                share_counter += 1;
                ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", format!("<ConnectResponse><SessionID>s</SessionID><conid>{cid}</conid></ConnectResponse>"))
            } else if req_line.contains("method=disconnect") {
                ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", "<DisconnectResponse/>".to_string())
            } else if req_line.contains("method=bdecall") {
                let conid = req_line
                    .split("conid=")
                    .nth(1)
                    .map(|r| r.split(['&', ' ']).next().unwrap_or(""))
                    .unwrap_or("");
                if conid.is_empty() || !conid.chars().all(|c| c.is_ascii_digit()) {
                    ("HTTP/1.1 500 Internal Server Error", "Content-Type: application/xml\r\n", "<error><info>null</info><message>POST request failed</message><reason>0</reason></error>".to_string())
                } else {
                    ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", "<ShowResponse><DataArea><Ok/></DataArea></ShowResponse>".to_string())
                }
            } else {
                ("HTTP/1.1 404 Not Found", "Content-Type: text/plain\r\n", "Not Found".to_string())
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

    let client = HttpClient::new(&base_url, "mock_token");

    // 1. ProjectServer -> auto connects to conid=0
    let mgr_ps = JcaBdeManager::new(&client, "ProjectServer");
    let show = BdeParams {
        bde_name: "SoftwareProject_V2".into(),
        method_name: "Show".into(),
        mode: Some(BdeExecutionMode::Show),
        ..Default::default()
    };
    let res0 = mgr_ps.execute(&show).await.unwrap();
    assert!(res0.contains("<Ok/>"));

    // 2. Repository CP -> auto shares to conid=1
    let mgr_dev = JcaBdeManager::new(&client, "EXTce01108_dev");
    let res1 = mgr_dev.execute(&show).await.unwrap();
    assert!(res1.contains("<Ok/>"));

    // 3. Cached reuse: calling EXTce01108_dev again reuses conid=1 without extra share
    let res1b = mgr_dev.execute(&show).await.unwrap();
    assert!(res1b.contains("<Ok/>"));

    // 4. Direct resolve check
    assert_eq!(client.resolve_conid("ProjectServer").await.unwrap(), "0");
    assert_eq!(client.resolve_conid("EXTce01108_dev").await.unwrap(), "1");
    assert_eq!(client.resolve_conid("").await.unwrap(), "0");
    assert_eq!(client.resolve_conid("42").await.unwrap(), "42");

    // 5. Cleanup disconnects
    client.disconnect_all().await.unwrap();

    let log = seen.lock().await;
    let connect_count = log.iter().filter(|l| l.contains("method=connect")).count();
    let share_count = log.iter().filter(|l| l.contains("method=share")).count();
    let disconnect_count = log.iter().filter(|l| l.contains("method=disconnect")).count();
    assert_eq!(connect_count, 1);
    assert_eq!(share_count, 1);
    assert!(disconnect_count >= 2);
}
