use std::collections::HashMap;
use std::fs::File;
use std::io::Read;
use std::path::PathBuf;
use std::time::{SystemTime, UNIX_EPOCH};
use reqwest::Client;
use serde::{Deserialize, Serialize};
use thiserror::Error;
use url::Url;

use crate::ionapi::IonapiConfig;

pub const TOKEN_EXPIRY_BUFFER_SECONDS: f64 = 300.0; // 5-minute safety buffer

#[derive(Error, Debug)]
pub enum TokenError {
    #[error("I/O error: {0}")]
    Io(#[from] std::io::Error),
    #[error("JSON error: {0}")]
    Json(#[from] serde_json::Error),
    #[error("HTTP request error: {0}")]
    Http(#[from] reqwest::Error),
    #[error("URL parse error: {0}")]
    UrlParse(#[from] url::ParseError),
    #[error("OAuth2 error: {0}")]
    OAuth2(String),
    #[error("Authentication required for environment '{0}'")]
    AuthRequired(String),
}

/// Token payload matching `~/.ln_studio/tokens/<env>.json` exactly.
#[derive(Debug, Clone, PartialEq, Serialize, Deserialize)]
pub struct TokenData {
    pub access_token: String,
    pub refresh_token: Option<String>,
    #[serde(default = "default_bearer")]
    pub token_type: String,
    pub expires_in: Option<f64>,
    pub expires_at: Option<f64>,
    pub updated_at: Option<f64>,
    pub obtained_at: Option<f64>,
    pub scope: Option<String>,
    pub tenant: Option<String>,
    pub gateway_url: Option<String>,
}

fn default_bearer() -> String {
    "Bearer".to_string()
}

#[derive(Debug, Clone, PartialEq)]
pub enum TokenStatus {
    Valid {
        expires_in: f64,
        access_token: String,
        refresh_token: Option<String>,
    },
    NeedsRefresh {
        expires_in: f64,
        refresh_token: String,
    },
    Expired {
        expires_in: f64,
    },
    Missing,
}

pub struct OAuth2TokenManager {
    pub cache_dir: PathBuf,
    client: Client,
}

impl Default for OAuth2TokenManager {
    fn default() -> Self {
        Self::new(None)
    }
}

impl OAuth2TokenManager {
    pub fn new(cache_dir: Option<PathBuf>) -> Self {
        let dir = cache_dir.unwrap_or_else(|| {
            dirs::home_dir()
                .unwrap_or_else(|| PathBuf::from("."))
                .join(".ln_studio")
                .join("tokens")
        });

        // Configure client with rustls-tls-native-certs and system proxies
        let client = Client::builder()
            .use_rustls_tls()
            .user_agent("JCAWebClient (LNStudio)")
            .build()
            .unwrap_or_else(|_| Client::new());

        Self {
            cache_dir: dir,
            client,
        }
    }

    pub fn with_client(cache_dir: Option<PathBuf>, client: Client) -> Self {
        let mut mgr = Self::new(cache_dir);
        mgr.client = client;
        mgr
    }

    fn get_token_path(&self, env_name: &str) -> PathBuf {
        let safe_name: String = env_name
            .chars()
            .map(|c| if c.is_alphanumeric() || c == '.' || c == '-' || c == '_' { c } else { '_' })
            .collect();
        self.cache_dir.join(format!("{safe_name}.json"))
    }

    pub fn load_token(&self, env_name: &str) -> Option<TokenData> {
        let path = self.get_token_path(env_name);
        if !path.exists() {
            return None;
        }
        let mut file = File::open(path).ok()?;
        let mut content = String::new();
        file.read_to_string(&mut content).ok()?;
        serde_json::from_str(&content).ok()
    }

    pub fn save_token(&self, env_name: &str, mut token_data: TokenData) -> Result<PathBuf, TokenError> {
        std::fs::create_dir_all(&self.cache_dir)?;
        let path = self.get_token_path(env_name);

        let now = now_seconds();
        if token_data.expires_at.is_none() {
            if let Some(exp_in) = token_data.expires_in {
                token_data.expires_at = Some(now + exp_in);
            }
        }
        token_data.updated_at = Some(now);
        if token_data.obtained_at.is_none() {
            token_data.obtained_at = Some(now);
        }

        let json = serde_json::to_string_pretty(&token_data)?;
        std::fs::write(&path, json)?;
        Ok(path)
    }

    pub fn check_token_status(&self, env_name: &str) -> TokenStatus {
        let cached = match self.load_token(env_name) {
            Some(t) if !t.access_token.is_empty() => t,
            _ => return TokenStatus::Missing,
        };

        let now = now_seconds();
        let expires_at = cached.expires_at.unwrap_or(0.0);
        let time_left = expires_at - now;

        if time_left > TOKEN_EXPIRY_BUFFER_SECONDS {
            TokenStatus::Valid {
                expires_in: time_left,
                access_token: cached.access_token,
                refresh_token: cached.refresh_token,
            }
        } else if let Some(ref_tok) = cached.refresh_token {
            if !ref_tok.is_empty() {
                TokenStatus::NeedsRefresh {
                    expires_in: time_left.max(0.0),
                    refresh_token: ref_tok,
                }
            } else {
                TokenStatus::Expired {
                    expires_in: time_left.max(0.0),
                }
            }
        } else {
            TokenStatus::Expired {
                expires_in: time_left.max(0.0),
            }
        }
    }

    pub fn build_authorization_url(
        &self,
        config: &IonapiConfig,
        redirect_uri: Option<&str>,
        state: Option<&str>,
    ) -> String {
        let eff_redirect = redirect_uri.unwrap_or(&config.redirect_uri);
        let gen_state = uuid_v4_simple();
        let eff_state = state.unwrap_or(&gen_state);

        let sep = if config.auth_url.contains('?') { "&" } else { "?" };
        let mut params = vec![
            ("client_id", config.client_id.clone()),
            ("response_type", "code".to_string()),
            ("redirect_uri", eff_redirect.to_string()),
            ("state", eff_state.to_string()),
        ];
        if !config.scope.is_empty() && config.scope != "openid" {
            params.push(("scope", config.scope.clone()));
        }

        let encoded = url::form_urlencoded::Serializer::new(String::new())
            .extend_pairs(params)
            .finish();

        format!("{}{sep}{encoded}", config.auth_url)
    }

    /// Tier 2a: Refresh access token using cached refresh_token
    pub async fn refresh_access_token(
        &self,
        config: &IonapiConfig,
        refresh_token: &str,
    ) -> Result<TokenData, TokenError> {
        let mut form = HashMap::new();
        form.insert("grant_type", "refresh_token");
        form.insert("refresh_token", refresh_token);
        form.insert("client_id", &config.client_id);
        form.insert("client_secret", &config.client_secret);

        let resp = self.client.post(&config.token_url)
            .form(&form)
            .send()
            .await?;

        if !resp.status().is_success() {
            let err_text = resp.text().await.unwrap_or_default();
            return Err(TokenError::OAuth2(format!("Token refresh failed: {err_text}")));
        }

        let mut data: RawTokenResponse = resp.json().await?;
        if data.refresh_token.is_none() {
            data.refresh_token = Some(refresh_token.to_string());
        }

        Ok(data.into_token_data(config))
    }

    /// Tier 2b: Service Account password grant (`saak`/`sask`)
    pub async fn acquire_service_account_token(
        &self,
        config: &IonapiConfig,
    ) -> Result<TokenData, TokenError> {
        let saak = config.saak.as_deref().ok_or_else(|| TokenError::OAuth2("Missing saak in .ionapi".into()))?;
        let sask = config.sask.as_deref().ok_or_else(|| TokenError::OAuth2("Missing sask in .ionapi".into()))?;

        let mut form = HashMap::new();
        form.insert("grant_type", "password");
        form.insert("username", saak);
        form.insert("password", sask);
        form.insert("client_id", &config.client_id);
        form.insert("client_secret", &config.client_secret);
        form.insert("scope", if config.scope.is_empty() { "openid" } else { &config.scope });

        let resp = self.client.post(&config.token_url)
            .form(&form)
            .send()
            .await?;

        if !resp.status().is_success() {
            let err_text = resp.text().await.unwrap_or_default();
            return Err(TokenError::OAuth2(format!("Service Account login failed: {err_text}")));
        }

        let data: RawTokenResponse = resp.json().await?;
        Ok(data.into_token_data(config))
    }

    /// Tier 3: Exchange authorization code for token
    pub async fn exchange_authorization_code(
        &self,
        config: &IonapiConfig,
        code: &str,
        redirect_uri: Option<&str>,
    ) -> Result<TokenData, TokenError> {
        let eff_redirect = redirect_uri.unwrap_or(&config.redirect_uri);
        let mut form = HashMap::new();
        form.insert("grant_type", "authorization_code");
        form.insert("code", code);
        form.insert("client_id", &config.client_id);
        form.insert("client_secret", &config.client_secret);
        form.insert("redirect_uri", eff_redirect);

        let resp = self.client.post(&config.token_url)
            .form(&form)
            .send()
            .await?;

        if !resp.status().is_success() {
            let err_text = resp.text().await.unwrap_or_default();
            return Err(TokenError::OAuth2(format!("Authorization code exchange failed: {err_text}")));
        }

        let data: RawTokenResponse = resp.json().await?;
        Ok(data.into_token_data(config))
    }

    /// Executes the full 3-Tier Automated OAuth2 Token Lifecycle.
    pub async fn get_access_token(
        &self,
        env_name: &str,
        config: &IonapiConfig,
    ) -> Result<String, TokenError> {
        // Tier 1: Check cache
        match self.check_token_status(env_name) {
            TokenStatus::Valid { access_token, .. } => return Ok(access_token),
            TokenStatus::NeedsRefresh { refresh_token, .. } => {
                // Tier 2a: Silent refresh
                if let Ok(tok) = self.refresh_access_token(config, &refresh_token).await {
                    let _ = self.save_token(env_name, tok.clone());
                    return Ok(tok.access_token);
                }
            }
            _ => {}
        }

        // Tier 2b: Service Account if present
        if config.has_service_account() {
            let tok = self.acquire_service_account_token(config).await?;
            let _ = self.save_token(env_name, tok.clone());
            return Ok(tok.access_token);
        }

        // Tier 3: Requires Interactive Browser / Login
        let auth_url = self.build_authorization_url(config, None, None);
        Err(TokenError::AuthRequired(format!(
            "No valid token found for '{env_name}'. Please authenticate via browser: {auth_url}"
        )))
    }
}

#[derive(Deserialize)]
struct RawTokenResponse {
    access_token: String,
    refresh_token: Option<String>,
    #[serde(default = "default_bearer")]
    token_type: String,
    expires_in: Option<f64>,
    scope: Option<String>,
}

impl RawTokenResponse {
    fn into_token_data(self, config: &IonapiConfig) -> TokenData {
        let now = now_seconds();
        let expires_at = self.expires_in.map(|exp| now + exp);
        TokenData {
            access_token: self.access_token,
            refresh_token: self.refresh_token,
            token_type: self.token_type,
            expires_in: self.expires_in,
            expires_at,
            updated_at: Some(now),
            obtained_at: Some(now),
            scope: self.scope.or_else(|| Some(config.scope.clone())),
            tenant: Some(config.tenant_id.clone()),
            gateway_url: Some(config.gateway_url.clone()),
        }
    }
}

/// Extracts OAuth2 `code` parameter from pasted redirected URL or raw code.
pub fn extract_auth_code_from_input(input_str: &str) -> Result<String, TokenError> {
    let text = input_str.trim();
    if text.is_empty() {
        return Err(TokenError::OAuth2("Empty authorization code input".into()));
    }

    if text.contains("code=") {
        if let Ok(parsed) = Url::parse(text) {
            for (k, v) in parsed.query_pairs() {
                if k == "code" && !v.is_empty() {
                    return Ok(v.to_string());
                }
            }
        }

        // Fallback search
        if let Some(pos) = text.find("code=") {
            let sub = &text[pos + 5..];
            let end = sub.find('&').or_else(|| sub.find('#')).unwrap_or(sub.len());
            let code = &sub[..end];
            if !code.is_empty() {
                return Ok(code.to_string());
            }
        }
    }

    Ok(text.to_string())
}

fn now_seconds() -> f64 {
    SystemTime::now()
        .duration_since(UNIX_EPOCH)
        .unwrap_or_default()
        .as_secs_f64()
}

fn uuid_v4_simple() -> String {
    let now = SystemTime::now().duration_since(UNIX_EPOCH).unwrap_or_default().as_nanos();
    format!("{:032x}", now)
}
