use std::fmt;
use std::fs::File;
use std::io::Read;
use std::path::Path;
use serde::{Deserialize, Serialize};
use thiserror::Error;

pub const DEFAULT_REDIRECT_URI: &str = "oob://localhost/lnstudio";

#[derive(Error, Debug)]
pub enum IonapiError {
    #[error("I/O error: {0}")]
    Io(#[from] std::io::Error),
    #[error("Failed to parse JSON: {0}")]
    Json(#[from] serde_json::Error),
    #[error("Invalid .ionapi format: {0}")]
    InvalidFormat(String),
}

/// Raw parsed structure from Infor ION API (.ionapi) credentials JSON.
#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
pub struct RawIonapi {
    #[serde(default)]
    pub ti: String, // Tenant ID
    #[serde(default)]
    pub cn: String, // Client Name
    #[serde(default)]
    pub dt: serde_json::Value, // Device Type (e.g. "11" or 11)
    #[serde(default)]
    pub ci: String, // Client ID
    #[serde(default)]
    pub cs: String, // Client Secret
    #[serde(default)]
    pub iu: String, // Gateway / ION API Base URL
    #[serde(default)]
    pub pu: String, // Passport URL
    #[serde(default = "default_oa")]
    pub oa: String, // Authorization endpoint (default: "as/authorization.oauth2")
    #[serde(default = "default_ot")]
    pub ot: String, // Token endpoint (default: "as/token.oauth2")
    #[serde(default = "default_or")]
    pub or: String, // Revoke endpoint (default: "as/revoke_token.oauth2")
    #[serde(default = "default_scope")]
    pub sc: String, // Scope (default: "openid")
    pub saak: Option<String>, // Service Account Access Key
    pub sask: Option<String>, // Service Account Secret Key
    pub ru: Option<String>,   // Redirect URI
}

fn default_oa() -> String { "as/authorization.oauth2".into() }
fn default_ot() -> String { "as/token.oauth2".into() }
fn default_or() -> String { "as/revoke_token.oauth2".into() }
fn default_scope() -> String { "openid".into() }

/// Fully resolved IonapiConfig with computed endpoint URLs.
#[derive(Clone, PartialEq, Eq, Serialize, Deserialize)]
pub struct IonapiConfig {
    pub tenant_id: String,
    pub client_name: String,
    pub device_type: String,
    pub client_id: String,
    pub client_secret: String,
    pub gateway_url: String,
    pub auth_url: String,
    pub token_url: String,
    pub revoke_url: String,
    pub scope: String,
    pub saak: Option<String>,
    pub sask: Option<String>,
    pub redirect_uri: String,
    pub backend_webservice_url: String,
}

impl fmt::Debug for IonapiConfig {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.debug_struct("IonapiConfig")
            .field("tenant_id", &self.tenant_id)
            .field("client_name", &self.client_name)
            .field("device_type", &self.device_type)
            .field("client_id", &self.client_id)
            .field("client_secret", &"[REDACTED]")
            .field("gateway_url", &self.gateway_url)
            .field("auth_url", &self.auth_url)
            .field("token_url", &self.token_url)
            .field("revoke_url", &self.revoke_url)
            .field("scope", &self.scope)
            .field("saak", &self.saak)
            .field("sask", &self.sask.as_ref().map(|_| "[REDACTED]"))
            .field("redirect_uri", &self.redirect_uri)
            .field("backend_webservice_url", &self.backend_webservice_url)
            .finish()
    }
}

impl IonapiConfig {
    pub fn load_from_path(path: &Path) -> Result<Self, IonapiError> {
        let mut file = File::open(path)?;
        let mut content = String::new();
        file.read_to_string(&mut content)?;
        Self::parse_json(&content)
    }

    pub fn from_str(json_str: &str) -> Result<Self, IonapiError> {
        Self::parse_json(json_str)
    }

    pub fn parse_json(json_str: &str) -> Result<Self, IonapiError> {
        let raw: RawIonapi = serde_json::from_str(json_str)?;

        let iu = raw.iu.trim().trim_end_matches('/').to_string();
        let pu = raw.pu.trim().trim_end_matches('/').to_string();

        let oa = raw.oa.trim().trim_start_matches('/');
        let ot = raw.ot.trim().trim_start_matches('/');
        let or_url = raw.or.trim().trim_start_matches('/');

        let auth_url = if oa.starts_with("http://") || oa.starts_with("https://") {
            oa.to_string()
        } else {
            format!("{pu}/{oa}")
        };

        let token_url = if ot.starts_with("http://") || ot.starts_with("https://") {
            ot.to_string()
        } else {
            format!("{pu}/{ot}")
        };

        let revoke_url = if or_url.starts_with("http://") || or_url.starts_with("https://") {
            or_url.to_string()
        } else {
            format!("{pu}/{or_url}")
        };

        let dt_str = match &raw.dt {
            serde_json::Value::String(s) => s.clone(),
            serde_json::Value::Number(n) => n.to_string(),
            _ => "11".to_string(),
        };

        let redirect_uri = raw.ru.unwrap_or_else(|| DEFAULT_REDIRECT_URI.to_string());
        let backend_webservice_url = format!("{iu}/{}/LN/webservice", raw.ti);

        Ok(Self {
            tenant_id: raw.ti,
            client_name: raw.cn,
            device_type: dt_str,
            client_id: raw.ci,
            client_secret: raw.cs,
            gateway_url: iu,
            auth_url,
            token_url,
            revoke_url,
            scope: raw.sc,
            saak: raw.saak,
            sask: raw.sask,
            redirect_uri,
            backend_webservice_url,
        })
    }

    pub fn has_service_account(&self) -> bool {
        self.saak.is_some() && self.sask.is_some()
    }
}
