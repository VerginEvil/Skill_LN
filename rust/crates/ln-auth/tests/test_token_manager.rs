use std::time::{SystemTime, UNIX_EPOCH};
use ln_auth::ionapi::IonapiConfig;
use ln_auth::token_manager::{
    extract_auth_code_from_input, OAuth2TokenManager, TokenData, TokenStatus,
};
use tempfile::tempdir;
use tokio::io::{AsyncReadExt, AsyncWriteExt};
use tokio::net::TcpListener;

fn now() -> f64 {
    SystemTime::now()
        .duration_since(UNIX_EPOCH)
        .unwrap()
        .as_secs_f64()
}

#[test]
fn test_token_status_lifecycle() {
    let dir = tempdir().unwrap();
    let mgr = OAuth2TokenManager::new(Some(dir.path().to_path_buf()));
    let env_name = "TEST_ENV";

    // 1. Missing
    assert_eq!(mgr.check_token_status(env_name), TokenStatus::Missing);

    // 2. Valid token (> 300s left)
    let token_valid = TokenData {
        access_token: "mock_access_token".to_string(),
        refresh_token: Some("mock_refresh_token".to_string()),
        token_type: "Bearer".to_string(),
        expires_in: Some(3600.0),
        expires_at: Some(now() + 1000.0),
        updated_at: Some(now()),
        obtained_at: Some(now()),
        scope: Some("openid".to_string()),
        tenant: Some("TENANT_TEST".to_string()),
        gateway_url: Some("https://mock.gateway".to_string()),
    };
    mgr.save_token(env_name, token_valid).unwrap();

    match mgr.check_token_status(env_name) {
        TokenStatus::Valid { access_token, refresh_token, expires_in } => {
            assert_eq!(access_token, "mock_access_token");
            assert_eq!(refresh_token.as_deref(), Some("mock_refresh_token"));
            assert!(expires_in > 300.0);
        }
        other => panic!("Expected TokenStatus::Valid, got {:?}", other),
    }

    // 3. Needs Refresh (<= 300s left, but has refresh_token)
    let token_needs_refresh = TokenData {
        access_token: "expiring_token".to_string(),
        refresh_token: Some("valid_refresh_token".to_string()),
        token_type: "Bearer".to_string(),
        expires_in: Some(200.0),
        expires_at: Some(now() + 200.0),
        updated_at: Some(now()),
        obtained_at: Some(now()),
        scope: None,
        tenant: None,
        gateway_url: None,
    };
    mgr.save_token(env_name, token_needs_refresh).unwrap();

    match mgr.check_token_status(env_name) {
        TokenStatus::NeedsRefresh { refresh_token, expires_in } => {
            assert_eq!(refresh_token, "valid_refresh_token");
            assert!(expires_in <= 300.0);
        }
        other => panic!("Expected TokenStatus::NeedsRefresh, got {:?}", other),
    }

    // 4. Expired (expired with no refresh_token)
    let token_expired = TokenData {
        access_token: "dead_token".to_string(),
        refresh_token: None,
        token_type: "Bearer".to_string(),
        expires_in: Some(10.0),
        expires_at: Some(now() - 100.0),
        updated_at: Some(now() - 200.0),
        obtained_at: Some(now() - 200.0),
        scope: None,
        tenant: None,
        gateway_url: None,
    };
    mgr.save_token(env_name, token_expired).unwrap();

    match mgr.check_token_status(env_name) {
        TokenStatus::Expired { .. } => {}
        other => panic!("Expected TokenStatus::Expired, got {:?}", other),
    }
}

#[test]
fn test_extract_auth_code_from_input() {
    // 1. Raw code
    assert_eq!(extract_auth_code_from_input("xyz789").unwrap(), "xyz789");

    // 2. oob URI
    assert_eq!(
        extract_auth_code_from_input("oob://localhost/lnstudio?code=MY_AUTH_CODE&state=uuid-1234").unwrap(),
        "MY_AUTH_CODE"
    );

    // 3. HTTP localhost redirect URL
    assert_eq!(
        extract_auth_code_from_input("http://127.0.0.1:8080/callback?code=CODE_HTTP_123&state=abc").unwrap(),
        "CODE_HTTP_123"
    );

    // 4. Input with leading/trailing whitespaces and extra params
    assert_eq!(
        extract_auth_code_from_input("   oob://localhost/lnstudio?state=abc&code=TRIMMED_CODE   ").unwrap(),
        "TRIMMED_CODE"
    );

    // 5. Empty input fails
    assert!(extract_auth_code_from_input("   ").is_err());
}

#[tokio::test]
async fn test_mock_oauth2_refresh_and_sa_flow() {
    // Start a mock OAuth2 server on an ephemeral TCP port
    let listener = TcpListener::bind("127.0.0.1:0").await.unwrap();
    let addr = listener.local_addr().unwrap();
    let base_url = format!("http://127.0.0.1:{}", addr.port());

    tokio::spawn(async move {
        while let Ok((mut socket, _)) = listener.accept().await {
            let mut buf = [0u8; 2048];
            let n = socket.read(&mut buf).await.unwrap_or(0);
            let req = String::from_utf8_lossy(&buf[..n]);

            let resp_body = if req.contains("grant_type=refresh_token") {
                r#"{"access_token":"refreshed_access_token_123","token_type":"Bearer","expires_in":3600,"refresh_token":"refreshed_refresh_token_456"}"#
            } else if req.contains("grant_type=password") {
                r#"{"access_token":"sa_access_token_789","token_type":"Bearer","expires_in":3600}"#
            } else if req.contains("grant_type=authorization_code") {
                r#"{"access_token":"exchanged_access_token","token_type":"Bearer","expires_in":1800,"refresh_token":"exchanged_refresh_token"}"#
            } else {
                r#"{"error":"invalid_request"}"#
            };

            let http_response = format!(
                "HTTP/1.1 200 OK\r\nContent-Type: application/json\r\nContent-Length: {}\r\nConnection: close\r\n\r\n{}",
                resp_body.len(),
                resp_body
            );
            let _ = socket.write_all(http_response.as_bytes()).await;
        }
    });

    let ionapi_json = format!(r#"{{
        "ti": "TEST_TENANT",
        "cn": "Test Client",
        "ci": "client_id_test",
        "cs": "client_secret_test",
        "iu": "{base_url}",
        "pu": "{base_url}",
        "oa": "/auth",
        "ot": "/token",
        "saak": "test_saak",
        "sask": "test_sask"
    }}"#);

    let config = IonapiConfig::from_str(&ionapi_json).unwrap();
    let dir = tempdir().unwrap();
    let mgr = OAuth2TokenManager::new(Some(dir.path().to_path_buf()));

    // Test refresh_access_token
    let ref_tok = mgr.refresh_access_token(&config, "mock_ref").await.unwrap();
    assert_eq!(ref_tok.access_token, "refreshed_access_token_123");
    assert_eq!(ref_tok.refresh_token.as_deref(), Some("refreshed_refresh_token_456"));

    // Test acquire_service_account_token
    let sa_tok = mgr.acquire_service_account_token(&config).await.unwrap();
    assert_eq!(sa_tok.access_token, "sa_access_token_789");

    // Test exchange_authorization_code
    let code_tok = mgr.exchange_authorization_code(&config, "test_code", None).await.unwrap();
    assert_eq!(code_tok.access_token, "exchanged_access_token");
    assert_eq!(code_tok.refresh_token.as_deref(), Some("exchanged_refresh_token"));
}
