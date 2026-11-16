use ln_auth::ionapi::IonapiConfig;

#[test]
fn test_parse_standard_ionapi() {
    let json_data = r#"{
        "ti": "TENANT_DEV",
        "cn": "My Connection",
        "dt": "2026-01-01T00:00:00Z",
        "ci": "client_id_12345",
        "cs": "client_secret_secret_value",
        "iu": "https://mingle-ionapi.inforcloudsuite.com",
        "pu": "https://mingle-sso.inforcloudsuite.com:443/as",
        "oa": "/authorization.oauth2",
        "ot": "/token.oauth2",
        "or": "/revoke.oauth2"
    }"#;

    let config = IonapiConfig::from_str(json_data).expect("Should parse standard ionapi");
    assert_eq!(config.tenant_id, "TENANT_DEV");
    assert_eq!(config.client_id, "client_id_12345");
    assert_eq!(config.client_secret, "client_secret_secret_value");
    assert_eq!(config.gateway_url, "https://mingle-ionapi.inforcloudsuite.com");
    assert_eq!(config.token_url, "https://mingle-sso.inforcloudsuite.com:443/as/token.oauth2");
    assert_eq!(config.auth_url, "https://mingle-sso.inforcloudsuite.com:443/as/authorization.oauth2");
    assert_eq!(config.revoke_url, "https://mingle-sso.inforcloudsuite.com:443/as/revoke.oauth2");
    assert_eq!(
        config.backend_webservice_url,
        "https://mingle-ionapi.inforcloudsuite.com/TENANT_DEV/LN/webservice"
    );
    assert!(!config.has_service_account());
}

#[test]
fn test_parse_service_account_ionapi() {
    let json_data = r#"{
        "ti": "TENANT_PROD",
        "cn": "SA Connection",
        "ci": "client_sa",
        "cs": "client_sa_secret",
        "iu": "https://mingle-ionapi.inforcloudsuite.com/",
        "pu": "https://mingle-sso.inforcloudsuite.com:443/as/",
        "oa": "authorization.oauth2",
        "ot": "token.oauth2",
        "saak": "service_account_access_key",
        "sask": "service_account_secret_key"
    }"#;

    let config = IonapiConfig::from_str(json_data).expect("Should parse service account ionapi");
    assert_eq!(config.tenant_id, "TENANT_PROD");
    assert_eq!(config.token_url, "https://mingle-sso.inforcloudsuite.com:443/as/token.oauth2");
    assert_eq!(
        config.backend_webservice_url,
        "https://mingle-ionapi.inforcloudsuite.com/TENANT_PROD/LN/webservice"
    );
    assert!(config.has_service_account());
    assert_eq!(config.saak.as_deref(), Some("service_account_access_key"));
}

#[test]
fn test_debug_redacts_secrets() {
    let json_data = r#"{
        "ti": "TENANT_TEST",
        "ci": "visible_client_id",
        "cs": "SUPER_SECRET_CLIENT_SECRET",
        "iu": "https://mingle-ionapi.inforcloudsuite.com",
        "pu": "https://mingle-sso.inforcloudsuite.com",
        "oa": "/auth",
        "ot": "/token",
        "sask": "SUPER_SECRET_SA_KEY"
    }"#;

    let config = IonapiConfig::from_str(json_data).expect("Valid config");
    let debug_repr = format!("{:?}", config);
    assert!(debug_repr.contains("visible_client_id"));
    assert!(!debug_repr.contains("SUPER_SECRET_CLIENT_SECRET"));
    assert!(!debug_repr.contains("SUPER_SECRET_SA_KEY"));
    assert!(debug_repr.contains("[REDACTED]"));
}
