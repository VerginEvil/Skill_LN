use ln_auth::ionapi::IonapiConfig;
use ln_auth::prefs::{
    read_connectivity_prefs, read_prefs_file, sync_cloudenv_prefs, sync_connectivity_prefs,
    write_prefs_file,
};
use std::collections::BTreeMap;
use tempfile::tempdir;

#[test]
fn test_prefs_file_raw_read_write() {
    let dir = tempdir().unwrap();
    let file_path = dir.path().join("test.prefs");

    let mut map = BTreeMap::new();
    map.insert("eclipse.preferences.version".into(), "1".into());
    map.insert("key:with:colons".into(), "val:with:colons".into());
    map.insert("simple".into(), "value".into());

    write_prefs_file(&file_path, &map).unwrap();

    let read_back = read_prefs_file(&file_path).unwrap();
    assert_eq!(read_back.get("eclipse.preferences.version"), Some(&"1".to_string()));
    assert_eq!(read_back.get("key:with:colons"), Some(&"val:with:colons".to_string()));
    assert_eq!(read_back.get("simple"), Some(&"value".to_string()));
}

#[test]
fn test_sync_cloudenv_prefs() {
    let dir = tempdir().unwrap();
    let prefs_path = dir.path().join("com.infor.erpln.jca.connectivity.cloudenv.prefs");

    let ionapi_json = r#"{
        "ti": "TENANT_DEV",
        "cn": "Test Env",
        "ci": "client_123",
        "cs": "secret_abc",
        "iu": "https://gateway.example.com",
        "pu": "https://auth.example.com",
        "oa": "/auth",
        "ot": "/token",
        "or": "/revoke"
    }"#;
    let config = IonapiConfig::from_str(ionapi_json).unwrap();

    sync_cloudenv_prefs(&prefs_path, "DEV", &config).unwrap();

    let props = read_prefs_file(&prefs_path).unwrap();
    assert_eq!(props.get("EnvironmentsCount"), Some(&"1".to_string()));
    assert_eq!(props.get("EnvironmentName0"), Some(&"DEV".to_string()));
    assert_eq!(props.get("TenantID0"), Some(&"TENANT_DEV".to_string()));
    assert_eq!(props.get("GatewayURL0"), Some(&"https://gateway.example.com".to_string()));
    assert_eq!(props.get("ClientID0"), Some(&"client_123".to_string()));
}

#[test]
fn test_sync_connectivity_prefs() {
    let dir = tempdir().unwrap();
    let prefs_path = dir.path().join("com.infor.erpln.jca.connectivity.prefs");

    let ionapi_json = r#"{
        "ti": "TENANT_DEV",
        "cn": "Test Env",
        "ci": "client_123",
        "cs": "secret_abc",
        "iu": "https://gateway.example.com",
        "pu": "https://auth.example.com",
        "oa": "/auth",
        "ot": "/token",
        "or": "/revoke"
    }"#;
    let config = IonapiConfig::from_str(ionapi_json).unwrap();

    sync_connectivity_prefs(&prefs_path, "DEV", &config, Some("MyProject")).unwrap();

    let conns = read_connectivity_prefs(&prefs_path).unwrap();
    assert!(conns.contains_key("ProjectServer"));
    let proj_server = conns.get("ProjectServer").unwrap();
    assert_eq!(proj_server.get("ActivationType"), Some(&"http_oauth2".to_string()));
    assert_eq!(proj_server.get("CloudEnvironment"), Some(&"DEV".to_string()));
    assert_eq!(
        proj_server.get("HostName"),
        Some(&"https://gateway.example.com/TENANT_DEV/LN/webservice".to_string())
    );

    // Dev address created
    assert!(conns.contains_key("MyProject_dev"));
    // Rt address created
    assert!(conns.contains_key("MyProject_rt"));
}
