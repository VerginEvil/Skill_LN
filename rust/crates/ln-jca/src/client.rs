use std::collections::HashMap;
use std::sync::{Arc, Mutex};
use reqwest::header::{HeaderMap, HeaderValue, ACCEPT, AUTHORIZATION, CONTENT_TYPE, COOKIE, SET_COOKIE, USER_AGENT};
use reqwest::Client;
use url::Url;

use crate::error::{BdeExecutionError, JcaError};
use crate::security::assert_not_prohibited_operation;

pub const DEFAULT_USER_AGENT: &str = "JCAWebClient (LNStudio)";

#[derive(Debug, Clone, Default)]
pub struct ConnectOptions {
    pub company: Option<String>,
    pub environment: Option<String>,
    pub command: Option<String>,
    pub client_host: Option<String>,
    pub client_ip: Option<String>,
}

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct ConnectResponse {
    pub company: String,
    pub company_desc: String,
    pub current_pack: String,
    pub first_day_of_week: String,
    pub ln_user: String,
    pub timeout: u32,
    pub conid: String,
    pub version: u32,
    pub raw_xml: String,
}

#[derive(Clone)]
pub struct HttpClient {
    base_url: String,
    access_token: Arc<Mutex<String>>,
    cookies: Arc<Mutex<HashMap<String, String>>>,
    client: Client,
}

impl HttpClient {
    pub fn new(base_url: &str, access_token: &str) -> Self {
        let client = Client::builder()
            .use_rustls_tls()
            .build()
            .unwrap_or_else(|_| Client::new());

        let clean_base = base_url.trim_end_matches('/').to_string();

        Self {
            base_url: clean_base,
            access_token: Arc::new(Mutex::new(access_token.to_string())),
            cookies: Arc::new(Mutex::new(HashMap::new())),
            client,
        }
    }

    pub fn with_client(base_url: &str, access_token: &str, client: Client) -> Self {
        let clean_base = base_url.trim_end_matches('/').to_string();
        Self {
            base_url: clean_base,
            access_token: Arc::new(Mutex::new(access_token.to_string())),
            cookies: Arc::new(Mutex::new(HashMap::new())),
            client,
        }
    }

    pub fn set_access_token(&self, token: &str) {
        if let Ok(mut lock) = self.access_token.lock() {
            *lock = token.to_string();
        }
    }

    pub fn get_access_token(&self) -> String {
        self.access_token.lock().map(|g| g.clone()).unwrap_or_default()
    }

    pub fn get_base_url(&self) -> &str {
        &self.base_url
    }

    fn get_cookie_header(&self) -> Option<String> {
        let lock = self.cookies.lock().ok()?;
        if lock.is_empty() {
            return None;
        }
        let cookie_str = lock
            .iter()
            .map(|(k, v)| format!("{k}={v}"))
            .collect::<Vec<_>>()
            .join("; ");
        Some(cookie_str)
    }

    fn record_cookies_from_headers(&self, headers: &HeaderMap) {
        let mut lock = match self.cookies.lock() {
            Ok(l) => l,
            Err(_) => return,
        };

        for val in headers.get_all(SET_COOKIE) {
            if let Ok(cookie_str) = val.to_str() {
                // Parse key=value before ';'
                let main_part = cookie_str.split(';').next().unwrap_or("").trim();
                if let Some(eq) = main_part.find('=') {
                    let k = main_part[..eq].trim().to_string();
                    let v = main_part[eq + 1..].trim().to_string();
                    if !k.is_empty() {
                        lock.insert(k, v);
                    }
                }
            }
        }
    }

    fn build_headers(&self, content_type: Option<&str>) -> HeaderMap {
        let mut map = HeaderMap::new();
        let tok = self.get_access_token();
        if !tok.is_empty() {
            if let Ok(v) = HeaderValue::from_str(&format!("Bearer {tok}")) {
                map.insert(AUTHORIZATION, v);
            }
        }
        map.insert(USER_AGENT, HeaderValue::from_static(DEFAULT_USER_AGENT));
        map.insert(ACCEPT, HeaderValue::from_static("application/xml"));

        if let Some(ct) = content_type {
            if let Ok(v) = HeaderValue::from_str(ct) {
                map.insert(CONTENT_TYPE, v);
            }
        }

        if let Some(cookie_str) = self.get_cookie_header() {
            if let Ok(v) = HeaderValue::from_str(&cookie_str) {
                map.insert(COOKIE, v);
            }
        }

        map
    }

    /// Connect (`GET ?method=connect`)
    pub async fn connect(&self, options: &ConnectOptions) -> Result<ConnectResponse, JcaError> {
        let mut url = Url::parse(&self.base_url)?;
        {
            let mut q = url.query_pairs_mut();
            q.append_pair("method", "connect");
            if let Some(env) = &options.environment {
                q.append_pair("environment", env);
            }
            if let Some(co) = &options.company {
                q.append_pair("company", co);
            }
            if let Some(cmd) = &options.command {
                q.append_pair("command", cmd);
            }
            if let Some(host) = &options.client_host {
                q.append_pair("clientHost", host);
            }
            if let Some(ip) = &options.client_ip {
                q.append_pair("clientIp", ip);
            }
        }

        let headers = self.build_headers(None);
        let resp = self.client.get(url).headers(headers).send().await?;

        self.record_cookies_from_headers(resp.headers());

        let status = resp.status();
        let body = resp.text().await?;

        if !status.is_success() {
            return Err(JcaError::Protocol(format!(
                "Connect failed with status {}: {}",
                status, body
            )));
        }

        parse_connect_response(&body)
    }

    /// Share (`GET ?method=share[&company=<company>]`)
    pub async fn share(&self, company: Option<&str>) -> Result<ConnectResponse, JcaError> {
        let mut url = Url::parse(&self.base_url)?;
        {
            let mut q = url.query_pairs_mut();
            q.append_pair("method", "share");
            if let Some(co) = company {
                q.append_pair("company", co);
            }
        }

        let headers = self.build_headers(None);
        let resp = self.client.get(url).headers(headers).send().await?;

        self.record_cookies_from_headers(resp.headers());

        let status = resp.status();
        let body = resp.text().await?;

        if !status.is_success() {
            return Err(JcaError::Protocol(format!(
                "Share connection failed with status {}: {}",
                status, body
            )));
        }

        parse_connect_response(&body)
    }

    /// BDE Call (`POST ?method=bdecall&bdename=<name>&bdemethod=<method>&conid=<conid>`)
    pub async fn bde_call(
        &self,
        bde_name: &str,
        bde_method: &str,
        conid: &str,
        request_xml: &str,
    ) -> Result<String, JcaError> {
        // Enforce Protocol-Level Hard-Block
        assert_not_prohibited_operation(bde_name, bde_method, request_xml)?;

        let mut url = Url::parse(&self.base_url)?;
        {
            let mut q = url.query_pairs_mut();
            q.append_pair("method", "bdecall");
            q.append_pair("bdename", bde_name);
            q.append_pair("bdemethod", bde_method);
            q.append_pair("conid", conid);
        }

        let headers = self.build_headers(Some("application/xml;charset=utf-8"));
        let resp = self.client.post(url)
            .headers(headers)
            .body(request_xml.to_string())
            .send()
            .await?;

        self.record_cookies_from_headers(resp.headers());

        let status = resp.status();
        let bde_exception_header = resp
            .headers()
            .get("X-Infor-BDEException")
            .and_then(|v| v.to_str().ok())
            .and_then(|s| s.parse::<i32>().ok())
            .unwrap_or(0);

        let body = resp.text().await?;

        if status.as_u16() == 401 {
            return Err(JcaError::Auth(format!("Unauthorized (401): {body}")));
        }

        if status.as_u16() == 404 {
            return Err(JcaError::Protocol(format!("BDE Endpoint Not Found (404): {body}")));
        }

        if !status.is_success() {
            let msg = extract_tag(&body, "message")
                .or_else(|| extract_tag(&body, "error"))
                .unwrap_or_else(|| body.clone());
            return Err(JcaError::Bde(BdeExecutionError {
                message: msg,
                bde: bde_name.to_string(),
                method: bde_method.to_string(),
                status_code: Some(status.as_u16()),
                exception_code: None,
                raw_response: body,
            }));
        }

        if bde_exception_header != 0 {
            let msg = extract_tag(&body, "message")
                .or_else(|| extract_tag(&body, "InformationArea"))
                .or_else(|| extract_tag(&body, "Result"))
                .unwrap_or_else(|| format!("BDE exception {bde_exception_header}"));

            return Err(JcaError::Bde(BdeExecutionError {
                message: msg,
                bde: bde_name.to_string(),
                method: bde_method.to_string(),
                status_code: Some(status.as_u16()),
                exception_code: Some(bde_exception_header),
                raw_response: body,
            }));
        }

        Ok(body)
    }

    /// Keepalive Ping (`GET ?method=ping`)
    pub async fn ping(&self) -> Result<(), JcaError> {
        let mut url = Url::parse(&self.base_url)?;
        url.query_pairs_mut().append_pair("method", "ping");

        let headers = self.build_headers(None);
        let resp = self.client.get(url).headers(headers).send().await?;
        if !resp.status().is_success() {
            let status = resp.status();
            let body = resp.text().await.unwrap_or_default();
            return Err(JcaError::Protocol(format!("Ping failed ({status}): {body}")));
        }
        Ok(())
    }

    /// Disconnect (`GET ?method=disconnect[&conid=<conid>]`)
    pub async fn disconnect(&self, conid: Option<&str>) -> Result<(), JcaError> {
        let mut url = Url::parse(&self.base_url)?;
        {
            let mut q = url.query_pairs_mut();
            q.append_pair("method", "disconnect");
            if let Some(cid) = conid {
                q.append_pair("conid", cid);
            }
        }

        let headers = self.build_headers(None);
        let _ = self.client.get(url).headers(headers).send().await;
        Ok(())
    }

    /// DLL Call (`POST ?method=dllcall&conid=<conid>`)
    pub async fn dll_call(&self, conid: &str, request_xml: &str) -> Result<String, JcaError> {
        let mut url = Url::parse(&self.base_url)?;
        {
            let mut q = url.query_pairs_mut();
            q.append_pair("method", "dllcall");
            q.append_pair("conid", conid);
        }

        let headers = self.build_headers(Some("application/xml;charset=utf-8"));
        let resp = self.client.post(url)
            .headers(headers)
            .body(request_xml.to_string())
            .send()
            .await?;

        let status = resp.status();
        let body = resp.text().await?;

        if !status.is_success() {
            return Err(JcaError::Protocol(format!("DLL call failed ({status}): {body}")));
        }

        Ok(body)
    }

    /// File Download (`GET ?method=file_download&filename=<name>[&mode=<mode>]`)
    pub async fn file_download(&self, filename: &str, mode: Option<&str>) -> Result<Vec<u8>, JcaError> {
        let mut url = Url::parse(&self.base_url)?;
        {
            let mut q = url.query_pairs_mut();
            q.append_pair("method", "file_download");
            q.append_pair("filename", filename);
            if let Some(m) = mode {
                q.append_pair("mode", m);
            }
        }

        let headers = self.build_headers(None);
        let resp = self.client.get(url).headers(headers).send().await?;

        if !resp.status().is_success() {
            let status = resp.status();
            let body = resp.text().await.unwrap_or_default();
            return Err(JcaError::Protocol(format!("File download failed ({status}): {body}")));
        }

        let bytes = resp.bytes().await?;
        Ok(bytes.to_vec())
    }

    /// File Upload (`POST ?method=file_upload&filename=<name>[&mode=<mode>]`)
    pub async fn file_upload(&self, filename: &str, mode: Option<&str>, data: &[u8]) -> Result<(), JcaError> {
        let mut url = Url::parse(&self.base_url)?;
        {
            let mut q = url.query_pairs_mut();
            q.append_pair("method", "file_upload");
            q.append_pair("filename", filename);
            if let Some(m) = mode {
                q.append_pair("mode", m);
            }
        }

        let headers = self.build_headers(Some("application/octet-stream"));
        let resp = self.client.post(url)
            .headers(headers)
            .body(data.to_vec())
            .send()
            .await?;

        if !resp.status().is_success() {
            let status = resp.status();
            let body = resp.text().await.unwrap_or_default();
            return Err(JcaError::Protocol(format!("File upload failed ({status}): {body}")));
        }

        Ok(())
    }
}

pub fn extract_tag(xml: &str, tag_name: &str) -> Option<String> {
    let open_tag = format!("<{tag_name}>");
    let close_tag = format!("</{tag_name}>");

    let start_idx = xml.find(&open_tag)?;
    let content_start = start_idx + open_tag.len();
    let end_idx = xml[content_start..].find(&close_tag)?;
    Some(xml[content_start..content_start + end_idx].trim().to_string())
}

pub fn parse_connect_response(body: &str) -> Result<ConnectResponse, JcaError> {
    let company = extract_tag(body, "company").unwrap_or_default();
    let company_desc = extract_tag(body, "companyDesc").unwrap_or_default();
    let current_pack = extract_tag(body, "currentPack").unwrap_or_default();
    let first_day_of_week = extract_tag(body, "firstdayofweek").unwrap_or_default();
    let ln_user = extract_tag(body, "lnuser").unwrap_or_default();
    let timeout: u32 = extract_tag(body, "timeout")
        .and_then(|s| s.parse().ok())
        .unwrap_or(300);
    let conid = extract_tag(body, "conid").unwrap_or_else(|| "1".to_string());
    let version: u32 = extract_tag(body, "version")
        .and_then(|s| s.parse().ok())
        .unwrap_or(1);

    if version < 1 {
        return Err(JcaError::Protocol(format!(
            "Unsupported JCA server protocol version: {version}"
        )));
    }

    Ok(ConnectResponse {
        company,
        company_desc,
        current_pack,
        first_day_of_week,
        ln_user,
        timeout,
        conid,
        version,
        raw_xml: body.to_string(),
    })
}
