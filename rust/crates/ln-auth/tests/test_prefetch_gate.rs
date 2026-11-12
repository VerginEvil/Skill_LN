use ln_auth::prefetch_gate::check_auth_status;
use ln_auth::token_manager::{OAuth2TokenManager, TokenData};
use std::time::{SystemTime, UNIX_EPOCH};
use tempfile::tempdir;

fn now() -> f64 {
    SystemTime::now()
        .duration_since(UNIX_EPOCH)
        .unwrap()
        .as_secs_f64()
}

#[test]
fn test_prefetch_gate_status_report() {
    let dir = tempdir().unwrap();
    let cache_dir = dir.path().to_path_buf();
    let env_name = "DEMO_ENV";

    // 1. Missing token -> status "missing", alert banner present
    let report_missing = check_auth_status(env_name, Some(cache_dir.clone()), Some("https://auth.example.com/login"));
    assert_eq!(report_missing.status, "missing");
    assert!(report_missing.alert_banner.is_some());
    assert!(report_missing.alert_banner.unwrap().contains("https://auth.example.com/login"));

    // 2. Valid token -> status "valid", no alert banner
    let mgr = OAuth2TokenManager::new(Some(cache_dir.clone()));
    let valid_tok = TokenData {
        access_token: "active_token_xyz".into(),
        refresh_token: Some("refresh_xyz".into()),
        token_type: "Bearer".into(),
        expires_in: Some(3600.0),
        expires_at: Some(now() + 1000.0),
        updated_at: Some(now()),
        obtained_at: Some(now()),
        scope: None,
        tenant: None,
        gateway_url: None,
    };
    mgr.save_token(env_name, valid_tok).unwrap();

    let report_valid = check_auth_status(env_name, Some(cache_dir.clone()), None);
    assert_eq!(report_valid.status, "valid");
    assert_eq!(report_valid.access_token.as_deref(), Some("active_token_xyz"));
    assert!(report_valid.alert_banner.is_none());
}
