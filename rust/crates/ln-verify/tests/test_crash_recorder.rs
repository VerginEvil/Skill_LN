use std::collections::HashMap;
use std::fs;
use tempfile::tempdir;

use ln_verify::crash_recorder::*;

#[test]
fn test_sensitive_text_redaction() {
    let raw_req = r#"<Request>
        <token>eyJhGciOiJIUzI1NiJ9.secret_token.sig</token>
        <password>SuperSecret123!</password>
        <cs>client_secret_999</cs>
        <sask>sask_token_value</sask>
        <accessToken>access_token_123</accessToken>
        <refreshToken>refresh_token_456</refreshToken>
    </Request>"#;

    let clean = redact_sensitive_text(raw_req);
    assert!(!clean.contains("SuperSecret123!"));
    assert!(!clean.contains("secret_token"));
    assert!(!clean.contains("client_secret_999"));
    assert!(!clean.contains("sask_token_value"));
    assert!(clean.contains("<password><REDACTED></password>"));
    assert!(clean.contains("<token><REDACTED></token>"));
    assert!(clean.contains("<cs><REDACTED></cs>"));

    // Bearer token
    let auth_header = "Bearer ya29.a0AfH6SM...secret";
    let clean_auth = redact_sensitive_text(auth_header);
    assert_eq!(clean_auth, "Bearer <REDACTED>");

    // JSON token
    let raw_json = r#"{"access_token": "secret123", "client_secret": "my_secret", "status": "ok"}"#;
    let clean_json = redact_sensitive_text(raw_json);
    assert!(!clean_json.contains("secret123"));
    assert!(!clean_json.contains("my_secret"));
    assert!(clean_json.contains(r#""access_token": "<REDACTED>""#));
    assert!(clean_json.contains(r#""client_secret": "<REDACTED>""#));
    assert!(clean_json.contains(r#""status": "ok""#));

    // Cookies
    let raw_cookie = "JSESSIONID=AABBCCDDEEFF; token=XYZ123; path=/";
    let clean_cookie = redact_sensitive_text(raw_cookie);
    assert!(!clean_cookie.contains("AABBCCDDEEFF"));
    assert!(!clean_cookie.contains("XYZ123"));
    assert!(clean_cookie.contains("JSESSIONID=<REDACTED>"));
    assert!(clean_cookie.contains("token=<REDACTED>"));
}

#[test]
fn test_record_crash_fixture_file_creation() {
    let td = tempdir().unwrap();
    let crash_dir = td.path().join("unmapped_packets");

    let mut headers = HashMap::new();
    headers.insert("Authorization".to_string(), "Bearer secret_jwt_token".to_string());
    headers.insert("Content-Type".to_string(), "application/xml".to_string());

    let req_xml = "<StudioComponent><password>mypassword</password></StudioComponent>";
    let resp_body = "<Fault><message>Internal NullPointerException with token=ABC12345</message></Fault>";

    let file_path = record_crash_fixture(
        "StudioComponent",
        "GetRevision",
        "BDE",
        req_xml,
        Some(500),
        Some(&headers),
        resp_body,
        "Simulated 500 Server Error",
        Some(&crash_dir),
    ).unwrap();

    assert!(file_path.exists());
    let content = fs::read_to_string(&file_path).unwrap();

    // Verify parsed JSON
    let parsed: CrashFixture = serde_json::from_str(&content).unwrap();
    assert_eq!(parsed.bde, "StudioComponent");
    assert_eq!(parsed.method, "GetRevision");
    assert_eq!(parsed.mode, "BDE");
    assert_eq!(parsed.response_status, Some(500));
    assert_eq!(parsed.error_message, "Simulated 500 Server Error");

    // Zero-leak check: verify raw secrets NEVER exist in saved fixture
    assert!(!content.contains("mypassword"));
    assert!(!content.contains("secret_jwt_token"));
    assert!(!content.contains("ABC12345"));
    assert!(content.contains("<REDACTED>"));
}
