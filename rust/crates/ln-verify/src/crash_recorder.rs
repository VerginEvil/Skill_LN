use std::collections::HashMap;
use std::fs;
use std::path::{Path, PathBuf};
use regex::Regex;
use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct CrashFixture {
    pub timestamp: String,
    pub bde: String,
    pub method: String,
    pub mode: String,
    pub request_xml: String,
    pub response_status: Option<u16>,
    pub response_headers: HashMap<String, String>,
    pub response_body: String,
    pub error_message: String,
}

/// Redacts sensitive authentication tokens and secrets from strings.
pub fn redact_sensitive_text(text: &str) -> String {
    if text.is_empty() {
        return String::new();
    }

    let mut result = text.to_string();

    // 1. Bearer tokens
    let bearer_re = Regex::new(r"(?i)(Bearer\s+)[A-Za-z0-9_\-\.]+").unwrap();
    result = bearer_re.replace_all(&result, "$1<REDACTED>").to_string();

    // 2. XML tags containing credentials (<cs>, <sask>, <token>, <password>)
    let sensitive_tags = ["cs", "sask", "token", "password", "accessToken", "refreshToken", "clientSecret"];
    for tag in sensitive_tags {
        let pattern = format!(r"(?i)<{tag}>[^<]+</{tag}>");
        if let Ok(re) = Regex::new(&pattern) {
            result = re.replace_all(&result, format!("<{tag}><REDACTED></{tag}>")).to_string();
        }
    }

    // 3. JSON keys containing credentials ("cs": "...", "password": "...", etc.)
    let json_re = Regex::new(r#"(?i)"(cs|sask|token|password|access_token|refresh_token|client_secret)"\s*:\s*"[^"]+""#).unwrap();
    result = json_re.replace_all(&result, r#""$1": "<REDACTED>""#).to_string();

    // 4. Cookies
    let cookie_re = Regex::new(r"(?i)(sessionid|JSESSIONID|token|access_token)=[^;\s&]+").unwrap();
    result = cookie_re.replace_all(&result, "$1=<REDACTED>").to_string();

    result
}

/// Redacts sensitive headers (Authorization, Cookie, etc.)
pub fn redact_headers(headers: &HashMap<String, String>) -> HashMap<String, String> {
    let mut clean = HashMap::new();
    for (k, v) in headers {
        let k_lower = k.to_ascii_lowercase();
        if k_lower == "authorization" || k_lower == "cookie" || k_lower == "set-cookie" || k_lower.contains("secret") || k_lower.contains("token") {
            clean.insert(k.clone(), redact_sensitive_text(v));
        } else {
            clean.insert(k.clone(), v.clone());
        }
    }
    clean
}

/// Resolves the crash packets directory:
/// 1. `LN_CRASH_DIR` environment variable
/// 2. `~/.ln_studio/unmapped_packets/`
pub fn resolve_crash_dir(custom_dir: Option<&Path>) -> PathBuf {
    if let Some(d) = custom_dir {
        return d.to_path_buf();
    }
    if let Ok(env_p) = std::env::var("LN_CRASH_DIR") {
        if !env_p.trim().is_empty() {
            return PathBuf::from(env_p.trim());
        }
    }
    if let Some(home) = dirs::home_dir() {
        home.join(".ln_studio").join("unmapped_packets")
    } else {
        PathBuf::from(".ln_studio").join("unmapped_packets")
    }
}

/// Records a sanitized crash fixture to disk.
pub fn record_crash_fixture(
    bde: &str,
    method: &str,
    mode: &str,
    request_xml: &str,
    response_status: Option<u16>,
    response_headers: Option<&HashMap<String, String>>,
    response_body: &str,
    error_message: &str,
    custom_dir: Option<&Path>,
) -> Result<PathBuf, std::io::Error> {
    let target_dir = resolve_crash_dir(custom_dir);
    fs::create_dir_all(&target_dir)?;

    let now = chrono_timestamp_iso();
    let filename_ts = now.replace(':', "-").replace('.', "_");
    let safe_bde = bde.replace('/', "_").replace('\\', "_");
    let safe_method = method.replace('/', "_").replace('\\', "_");

    let filename = format!("{filename_ts}_{safe_bde}_{safe_method}.json");
    let file_path = target_dir.join(filename);

    let empty_headers = HashMap::new();
    let clean_headers = redact_headers(response_headers.unwrap_or(&empty_headers));

    let fixture = CrashFixture {
        timestamp: now,
        bde: bde.to_string(),
        method: method.to_string(),
        mode: mode.to_string(),
        request_xml: redact_sensitive_text(request_xml),
        response_status,
        response_headers: clean_headers,
        response_body: redact_sensitive_text(response_body),
        error_message: redact_sensitive_text(error_message),
    };

    let json_bytes = serde_json::to_string_pretty(&fixture)
        .map_err(|e| std::io::Error::new(std::io::ErrorKind::Other, e.to_string()))?;

    fs::write(&file_path, json_bytes)?;
    Ok(file_path)
}

fn chrono_timestamp_iso() -> String {
    use std::time::SystemTime;
    let now = SystemTime::now();
    let dur = now.duration_since(SystemTime::UNIX_EPOCH).unwrap_or_default();
    let secs = dur.as_secs();
    let millis = dur.subsec_millis();

    // Standard UTC calculation
    let total_days = secs / 86400;
    let time_secs = secs % 86400;

    let hour = time_secs / 3600;
    let min = (time_secs % 3600) / 60;
    let sec = time_secs % 60;

    // Approximate date from epoch
    let mut y = 1970i64;
    let mut rem_days = total_days as i64;

    loop {
        let is_leap = (y % 4 == 0 && y % 100 != 0) || (y % 400 == 0);
        let days_in_year = if is_leap { 366 } else { 365 };
        if rem_days >= days_in_year {
            rem_days -= days_in_year;
            y += 1;
        } else {
            break;
        }
    }

    let is_leap = (y % 4 == 0 && y % 100 != 0) || (y % 400 == 0);
    let month_days = [
        31, if is_leap { 29 } else { 28 }, 31, 30, 31, 30,
        31, 31, 30, 31, 30, 31,
    ];

    let mut m = 1;
    for &d in &month_days {
        if rem_days >= d {
            rem_days -= d;
            m += 1;
        } else {
            break;
        }
    }
    let d = rem_days + 1;

    format!("{y:04}-{m:02}-{d:02}T{hour:02}:{min:02}:{sec:02}.{millis:03}Z")
}
