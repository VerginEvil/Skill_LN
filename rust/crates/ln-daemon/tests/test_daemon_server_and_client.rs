use std::time::Duration;
use ln_daemon::client::DaemonClient;
use ln_daemon::server::{DaemonServer, DaemonServerError};
use serde_json::json;
use tempfile::tempdir;
use tokio::io::{AsyncReadExt, AsyncWriteExt};
use tokio::net::TcpListener;

#[tokio::test]
async fn test_daemon_server_client_lifecycle_and_fifo() {
    // 1. Mock JCA HTTP server
    let http_listener = TcpListener::bind("127.0.0.1:0").await.unwrap();
    let http_port = http_listener.local_addr().unwrap().port();
    let backend_url = format!("http://127.0.0.1:{http_port}/TENANT/LN/webservice");

    tokio::spawn(async move {
        while let Ok((mut socket, _)) = http_listener.accept().await {
            let mut buf = [0u8; 4096];
            let n = socket.read(&mut buf).await.unwrap_or(0);
            let req = String::from_utf8_lossy(&buf[..n]);

            let (status_line, body) = if req.contains("method=connect") {
                ("HTTP/1.1 200 OK", "<ConnectResponse><company>0</company><conid>1</conid><version>1</version></ConnectResponse>")
            } else if req.contains("method=share") {
                ("HTTP/1.1 200 OK", "<ConnectResponse><company>0</company><conid>2</conid><version>1</version></ConnectResponse>")
            } else if req.contains("method=bdecall") {
                ("HTTP/1.1 200 OK", "<BdeResponse><DataArea><Result>Success</Result></DataArea></BdeResponse>")
            } else if req.contains("method=disconnect") {
                ("HTTP/1.1 200 OK", "<DisconnectResponse/>")
            } else {
                ("HTTP/1.1 404 Not Found", "Not Found")
            };

            let resp = format!(
                "{}\r\nContent-Type: application/xml\r\nContent-Length: {}\r\nConnection: close\r\n\r\n{}",
                status_line,
                body.len(),
                body
            );
            let _ = socket.write_all(resp.as_bytes()).await;
        }
    });

    let ws_dir = tempdir().unwrap();
    let ws_path = ws_dir.path();

    // 2. Start DaemonServer
    let server = DaemonServer::with_timeouts(Some(ws_path), 0, 1800, 60);
    let ws_path_buf = ws_path.to_path_buf();

    let server_task = tokio::spawn(async move {
        let _ = server.run().await;
    });

    // Wait briefly for daemon to initialize and write registration file
    tokio::time::sleep(Duration::from_millis(150)).await;

    // 3. Connect DaemonClient
    let client = DaemonClient::new(Some(&ws_path_buf));
    let info = client.get_info().expect("Should read daemon registration");
    assert_eq!(info.engine, "rust-native");
    assert!(info.port > 0);

    // 4. Test Single-Leader lock: second daemon on same workspace must fail
    let second_server = DaemonServer::new(Some(&ws_path_buf), 0);
    match second_server.run().await {
        Err(DaemonServerError::AlreadyRunning) => {}
        other => panic!("Expected DaemonServerError::AlreadyRunning, got {:?}", other),
    }

    // 5. Test ping
    let ping_ok = client.ping().await.expect("Ping should succeed");
    assert!(ping_ok);

    // 6. Test status
    let status_res = client.status().await.expect("Status should succeed");
    assert_eq!(status_res.get("status").and_then(|s| s.as_str()), Some("running"));

    // 7. Test update_token
    let token_ok = client.update_token("new_hot_swap_token").await.expect("Update token should succeed");
    assert!(token_ok);

    // 8. Test execute_bde
    let bde_params = json!({
        "backend": backend_url,
        "tenant": "TENANT",
        "token": "bearer_token",
        "bde": "ItemManager",
        "method": "GetItem",
        "mode": "BDE",
        "requestXml": "<Query/>"
    });
    let bde_res = client.send_rpc("execute_bde", bde_params, Duration::from_secs(5)).await.unwrap();
    assert!(bde_res.get("xml").and_then(|x| x.as_str()).unwrap().contains("<Result>Success</Result>"));

    // 9. Test security hard-block on EndActivity
    let blocked_params = json!({
        "backend": backend_url,
        "tenant": "TENANT",
        "token": "bearer_token",
        "bde": "ActivityManager",
        "method": "EndActivity",
        "mode": "BDE",
    });
    let blocked_err = client.send_rpc("execute_bde", blocked_params, Duration::from_secs(5)).await.unwrap_err();
    match blocked_err {
        ln_daemon::client::DaemonClientError::Rpc { code, message } => {
            assert_eq!(code, -32003);
            assert!(message.contains("[SECURITY_BLOCK]"));
        }
        other => panic!("Expected RPC error -32003, got {:?}", other),
    }

    // 10. Test concurrent FIFO requests over multiple client handles
    let mut handles = Vec::new();
    for _i in 0..5 {
        let port = info.port;
        handles.push(tokio::spawn(async move {
            let cl = DaemonClient::with_port(port);
            cl.ping().await.unwrap()
        }));
    }
    for h in handles {
        let ok = h.await.unwrap();
        assert!(ok);
    }

    // 11. Test shutdown
    let shutdown_ok = client.shutdown().await.expect("Shutdown should succeed");
    assert!(shutdown_ok);

    let _ = server_task.await;
}
