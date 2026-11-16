use std::path::PathBuf;
use serde::{Deserialize, Serialize};
use crate::token_manager::{OAuth2TokenManager, TokenStatus};

#[derive(Debug, Clone, PartialEq, Serialize, Deserialize)]
pub struct AuthStatusReport {
    pub status: String,
    pub expires_in: Option<f64>,
    pub has_refresh_token: bool,
    pub access_token: Option<String>,
    pub alert_banner: Option<String>,
}

/// Enforces the Pre-Fetch-Auth-Gate (ADR 0010): checks cached token status
/// and formats an alert banner when interactive login is required.
pub fn check_auth_status(env_name: &str, cache_dir: Option<PathBuf>, auth_url: Option<&str>) -> AuthStatusReport {
    let mgr = OAuth2TokenManager::new(cache_dir);
    match mgr.check_token_status(env_name) {
        TokenStatus::Valid { expires_in, access_token, refresh_token } => {
            AuthStatusReport {
                status: "valid".into(),
                expires_in: Some(expires_in),
                has_refresh_token: refresh_token.is_some(),
                access_token: Some(access_token),
                alert_banner: None,
            }
        }
        TokenStatus::NeedsRefresh { expires_in, .. } => {
            AuthStatusReport {
                status: "needs_refresh".into(),
                expires_in: Some(expires_in),
                has_refresh_token: true,
                access_token: None,
                alert_banner: Some(format!(
                    "[AUTH ALERT] Token for '{env_name}' is near expiry ({:.0}s remaining). Silent renewal pending.",
                    expires_in
                )),
            }
        }
        TokenStatus::Expired { expires_in } => {
            let banner = format_auth_alert_banner(env_name, auth_url);
            AuthStatusReport {
                status: "expired".into(),
                expires_in: Some(expires_in),
                has_refresh_token: false,
                access_token: None,
                alert_banner: Some(banner),
            }
        }
        TokenStatus::Missing => {
            let banner = format_auth_alert_banner(env_name, auth_url);
            AuthStatusReport {
                status: "missing".into(),
                expires_in: None,
                has_refresh_token: false,
                access_token: None,
                alert_banner: Some(banner),
            }
        }
    }
}

pub fn format_auth_alert_banner(env_name: &str, auth_url: Option<&str>) -> String {
    let url_str = auth_url.unwrap_or("<authorization_url>");
    format!(
        "\n=======================================================\n\
         [OAUTH2 LOGIN REQUIRED FOR '{env_name}']\n\
         Authorization URL:\n  {url_str}\n\
         After signing in, copy the redirected URL (e.g. oob://localhost/lnstudio?code=...)\n\
         or paste the authorization code to complete login.\n\
         =======================================================\n"
    )
}
