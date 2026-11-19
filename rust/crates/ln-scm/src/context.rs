use std::collections::HashMap;
use std::path::{Path, PathBuf};
use serde::{Deserialize, Serialize};
use thiserror::Error;

use ln_auth::{
    check_auth_status, read_connectivity_prefs, read_prefs_file, sync_connectivity_prefs,
    IonapiConfig, OAuth2TokenManager,
};
use ln_eclipse_compat::PropertyBucket;
use ln_jca::client::HttpClient;

#[derive(Error, Debug)]
pub enum ContextError {
    #[error("Workspace could not be discovered (pass --workspace or set LN_WORKSPACE)")]
    WorkspaceNotFound,
    #[error("Ambiguous workspace: pass --workspace. Available workspaces: {0:?}")]
    AmbiguousWorkspace(Vec<String>),
    #[error("Activity '{0}' could not be resolved in workspace")]
    ActivityNotFound(String),
    #[error("I/O error: {0}")]
    Io(#[from] std::io::Error),
    #[error("Authentication required or failed: {0}")]
    Auth(String),
    #[error("Workspace configuration error: {0}")]
    Config(String),
}

/// Parsed Eclipse LN Studio activity metadata combining `.project`, `.admin`,
/// workspace `.indexes/properties.index`, and connectivity preferences.
#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct ActivityDotProject {
    pub project_name: String,
    pub task_name: String,
    pub label: String,
    pub application_release: String,
    pub dev_env: String,
    pub dev_repo_address: String,
    pub rt_repo_address: String,
}

impl ActivityDotProject {
    pub fn from_activity_dir(activity_dir: &Path) -> Result<Self, ContextError> {
        if !activity_dir.exists() {
            return Err(ContextError::ActivityNotFound(
                activity_dir.to_string_lossy().to_string(),
            ));
        }

        let mut kv: HashMap<String, String> = HashMap::new();
        let dot_proj = activity_dir.join(".project");
        let mut raw_project_desc_name = String::new();
        if dot_proj.exists() {
            if let Ok(content) = std::fs::read_to_string(&dot_proj) {
                parse_dot_project_xml(&content, &mut kv, &mut raw_project_desc_name);
            }
        }

        let folder_name = activity_dir
            .file_name()
            .and_then(|s| s.to_str())
            .unwrap_or_default();
        let effective_name = if !raw_project_desc_name.is_empty() {
            raw_project_desc_name.as_str()
        } else {
            folder_name
        };

        let (parsed_task, parsed_proj) = parse_task_and_project_from_folder(effective_name);

        // Check activity `.settings/properties.index` and workspace `.indexes/properties.index`
        let mut prop_kv: HashMap<String, String> = HashMap::new();
        let mut idx_candidates = vec![activity_dir.join(".settings").join("properties.index")];
        if let Some(ws) = activity_dir.parent() {
            idx_candidates.push(
                ws.join(".metadata")
                    .join(".plugins")
                    .join("org.eclipse.core.resources")
                    .join(".projects")
                    .join(folder_name)
                    .join(".indexes")
                    .join("properties.index"),
            );
        }
        for idx_path in idx_candidates {
            if idx_path.exists() {
                if let Ok(bucket) = PropertyBucket::load_from_path(&idx_path) {
                    for ((_q, k), v) in bucket.get_properties_for_resource("") {
                        if !v.trim().is_empty() {
                            prop_kv.entry(k).or_insert(v);
                        }
                    }
                }
            }
        }

        let pick = |keys: &[&str], fallback: &str| -> String {
            for k in keys {
                if let Some(v) = kv.get(*k) {
                    if !v.trim().is_empty() {
                        return v.trim().to_string();
                    }
                }
                if let Some(v) = prop_kv.get(*k) {
                    if !v.trim().is_empty() {
                        return v.trim().to_string();
                    }
                }
            }
            fallback.to_string()
        };

        let project_name = pick(&["ProjectName"], &parsed_proj);
        let task_name = pick(&["TaskName"], &parsed_task);
        let label = pick(&["Label", "labelUUID"], "");
        let application_release = pick(&["ApplicationRelease", "PackageVRC", "VRC"], "");
        let dev_env = pick(&["DevelopmentEnvironment", "Environment"], "");
        let default_dev_repo = if !project_name.is_empty() {
            format!("{project_name}_dev")
        } else {
            String::new()
        };
        let default_rt_repo = if !project_name.is_empty() {
            format!("{project_name}_rt")
        } else {
            String::new()
        };

        let dev_repo_address = pick(
            &["DevelopmentTimeRepositoryAddress", "TaskContext"],
            &default_dev_repo,
        );
        let rt_repo_address = pick(&["RunTimeRepositoryAddress"], &default_rt_repo);

        Ok(Self {
            project_name,
            task_name,
            label,
            application_release,
            dev_env,
            dev_repo_address,
            rt_repo_address,
        })
    }
}

fn parse_task_and_project_from_folder(name: &str) -> (String, String) {
    let trimmed = name.trim();
    if let (Some(open), Some(close)) = (trimmed.rfind('['), trimmed.rfind(']')) {
        if open < close {
            let task = trimmed[..open].trim().to_string();
            let proj = trimmed[open + 1..close].trim().to_string();
            return (task, proj);
        }
    }
    (trimmed.to_string(), String::new())
}

fn parse_dot_project_xml(
    xml: &str,
    kv_out: &mut HashMap<String, String>,
    desc_name_out: &mut String,
) {
    let mut reader = quick_xml::Reader::from_str(xml);
    reader.config_mut().trim_text(true);
    let mut buf = Vec::new();
    let mut current_tag = String::new();
    let mut in_project_desc = false;
    let mut pending_key: Option<String> = None;

    loop {
        match reader.read_event_into(&mut buf) {
            Ok(quick_xml::events::Event::Start(e)) => {
                let tag = String::from_utf8_lossy(e.local_name().as_ref()).to_string();
                if tag == "projectDescription" {
                    in_project_desc = true;
                }
                current_tag = tag;
            }
            Ok(quick_xml::events::Event::End(e)) => {
                let tag = String::from_utf8_lossy(e.local_name().as_ref()).to_string();
                if tag == "projectDescription" {
                    in_project_desc = false;
                }
                current_tag.clear();
            }
            Ok(quick_xml::events::Event::Text(e)) => {
                let text = e.unescape().unwrap_or_default().trim().to_string();
                if text.is_empty() {
                    buf.clear();
                    continue;
                }
                match current_tag.as_str() {
                    "name" if in_project_desc && desc_name_out.is_empty() => {
                        *desc_name_out = text;
                    }
                    "key" => pending_key = Some(text),
                    "value" => {
                        if let Some(k) = pending_key.take() {
                            kv_out.insert(k, text);
                        }
                    }
                    _ => {}
                }
            }
            Ok(quick_xml::events::Event::Eof) | Err(_) => break,
            _ => {}
        }
        buf.clear();
    }
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct WorkspaceContext {
    pub workspace_dir: PathBuf,
    pub env_name: String,
    pub endpoint_url: String,
    pub company: String,
    pub default_activity_dir: Option<PathBuf>,
}

impl WorkspaceContext {
    /// Discovers Eclipse workspace configuration, JCA endpoint, company, and active activity.
    pub fn discover(
        workspace_override: Option<&Path>,
        activity_override: Option<&Path>,
    ) -> Result<Self, ContextError> {
        Self::discover_with_root(workspace_override, activity_override, None)
    }

    pub fn default_workspace_roots() -> Vec<PathBuf> {
        let mut roots = Vec::new();
        if let Ok(r) = std::env::var("LN_WORKSPACE_ROOT") {
            let p = PathBuf::from(r.trim());
            if p.is_dir() {
                roots.push(p);
            }
        }
        if let Some(d) = dirs::document_dir() {
            let p = d.join("workspace_lnstudio");
            if p.is_dir() && !roots.contains(&p) {
                roots.push(p);
            }
        }
        if let Some(h) = dirs::home_dir() {
            for p in [
                h.join("OneDrive").join("Documents").join("workspace_lnstudio"),
                h.join("Documents").join("workspace_lnstudio"),
            ] {
                if p.is_dir() && !roots.contains(&p) {
                    roots.push(p);
                }
            }
        }
        roots
    }

    pub fn resolve_workspace_arg(ws: &str) -> Option<PathBuf> {
        let direct = PathBuf::from(ws);
        if direct.exists() && direct.is_dir() {
            return Some(direct);
        }
        for root in Self::default_workspace_roots() {
            let cand = root.join(ws);
            if cand.exists() && cand.is_dir() {
                return Some(cand);
            }
        }
        None
    }

    pub fn discover_with_root(
        workspace_override: Option<&Path>,
        activity_override: Option<&Path>,
        ws_root_override: Option<&Path>,
    ) -> Result<Self, ContextError> {
        let mut ws_dir: Option<PathBuf> = None;
        let mut act_dir: Option<PathBuf> = activity_override.map(|p| p.to_path_buf());

        if let Some(w) = workspace_override {
            if w.exists() {
                ws_dir = Some(w.to_path_buf());
            } else if let Some(s) = w.to_str() {
                if let Some(resolved) = Self::resolve_workspace_arg(s) {
                    ws_dir = Some(resolved);
                }
            }
        }

        let find_ws_in_ancestors = |start: &Path| -> Option<(PathBuf, Option<PathBuf>)> {
            let mut cur_act: Option<PathBuf> = None;
            let abs = std::fs::canonicalize(start).unwrap_or_else(|_| start.to_path_buf());
            for anc in abs.ancestors() {
                if cur_act.is_none() && (anc.join(".project").exists() || anc.join(".admin").exists()) {
                    cur_act = Some(anc.to_path_buf());
                }
                if anc.join(".metadata").is_dir() {
                    return Some((anc.to_path_buf(), cur_act));
                }
            }
            None
        };

        if ws_dir.is_none() {
            if let Some(act) = activity_override {
                if let Some((w, detected_act)) = find_ws_in_ancestors(act) {
                    ws_dir = Some(w);
                    if detected_act.is_some() {
                        act_dir = detected_act;
                    }
                }
            }
        }

        if ws_dir.is_none() {
            if let Ok(cwd) = std::env::current_dir() {
                if let Some((w, detected_act)) = find_ws_in_ancestors(&cwd) {
                    ws_dir = Some(w);
                    if act_dir.is_none() {
                        act_dir = detected_act;
                    }
                }
            }
        }

        if ws_dir.is_none() {
            if let Ok(env_ws) = std::env::var("LN_WORKSPACE") {
                let trimmed = env_ws.trim();
                let p = PathBuf::from(trimmed);
                if p.exists() {
                    ws_dir = Some(p);
                } else if let Some(resolved) = Self::resolve_workspace_arg(trimmed) {
                    ws_dir = Some(resolved);
                }
            }
        }

        if ws_dir.is_none() {
            if let Some(home) = dirs::home_dir() {
                let cfg = home.join(".ln_studio").join("config.json");
                if cfg.exists() {
                    if let Ok(text) = std::fs::read_to_string(&cfg) {
                        if let Ok(val) = serde_json::from_str::<serde_json::Value>(&text) {
                            if let Some(active) = val.get("active_workspace").and_then(|v| v.as_str()) {
                                let p = PathBuf::from(active);
                                if p.exists() {
                                    ws_dir = Some(p);
                                }
                            }
                        }
                    }
                }
            }
        }

        if ws_dir.is_none() {
            let roots: Vec<PathBuf> = if let Some(r) = ws_root_override {
                vec![r.to_path_buf()]
            } else {
                Self::default_workspace_roots()
            };
            let mut found_workspaces: Vec<PathBuf> = Vec::new();
            for root in roots {
                if !root.is_dir() {
                    continue;
                }
                if root.join(".metadata").is_dir() {
                    found_workspaces.push(root.clone());
                }
                if let Ok(entries) = std::fs::read_dir(&root) {
                    for entry in entries.flatten() {
                        let p = entry.path();
                        if p.is_dir() && p.join(".metadata").is_dir() && !found_workspaces.contains(&p) {
                            found_workspaces.push(p);
                        }
                    }
                }
            }
            if found_workspaces.len() == 1 {
                ws_dir = Some(found_workspaces.remove(0));
            } else if found_workspaces.len() > 1 {
                let mut names: Vec<String> = found_workspaces
                    .iter()
                    .filter_map(|p| p.file_name().and_then(|s| s.to_str()).map(|s| s.to_string()))
                    .collect();
                names.sort();
                return Err(ContextError::AmbiguousWorkspace(names));
            }
        }

        let workspace_dir = ws_dir.ok_or(ContextError::WorkspaceNotFound)?;

        let settings_dir = workspace_dir
            .join(".metadata")
            .join(".plugins")
            .join("org.eclipse.core.runtime")
            .join(".settings");

        let mut env_name = workspace_dir
            .file_name()
            .and_then(|s| s.to_str())
            .unwrap_or("DEFAULT")
            .to_string();
        let mut endpoint_url = String::new();
        let mut company = "0".to_string();

        for fname in [
            "com.infor.erpln.jca.connectivity.prefs",
            "com.infor.ln.studio.integration.connectivity.prefs",
        ] {
            let p = settings_dir.join(fname);
            if p.exists() {
                if let Ok(conns) = read_connectivity_prefs(&p) {
                    if let Some(ps) = conns.get("ProjectServer") {
                        if let Some(ce) = ps.get("CloudEnvironment").filter(|s| !s.is_empty()) {
                            env_name = ce.clone();
                        }
                        if let Some(host) = ps.get("HostName").filter(|s| !s.is_empty()) {
                            endpoint_url = host.clone();
                        }
                        if let Some(co) = ps.get("Company").filter(|s| !s.is_empty()) {
                            company = co.clone();
                        }
                        break;
                    }
                }
            }
        }

        let cloud_prefs = settings_dir.join("com.infor.ln.studio.Global.cloudenv.prefs");
        if cloud_prefs.exists() {
            if let Ok(props) = read_prefs_file(&cloud_prefs) {
                if endpoint_url.is_empty() {
                    if let Some(host) = props.get("GatewayURL0").filter(|s| !s.is_empty()) {
                        endpoint_url = host.clone();
                    }
                }
            }
        }

        if let Ok(override_ep) = std::env::var("LN_JCA_ENDPOINT") {
            let trimmed = override_ep.trim();
            if !trimmed.is_empty() {
                endpoint_url = trimmed.to_string();
            }
        }

        if endpoint_url.is_empty() {
            return Err(ContextError::Config(format!(
                "No JCA endpoint found in workspace '{}' (set LN_JCA_ENDPOINT or configure ProjectServer)",
                workspace_dir.display()
            )));
        }

        if act_dir.is_none() {
            // Pick first valid activity directory containing `.project`
            if let Ok(entries) = std::fs::read_dir(&workspace_dir) {
                let mut candidates: Vec<PathBuf> = entries
                    .filter_map(|e| e.ok())
                    .map(|e| e.path())
                    .filter(|p| p.is_dir() && p.join(".project").exists())
                    .collect();
                candidates.sort();
                if let Some(first) = candidates.into_iter().next() {
                    act_dir = Some(first);
                }
            }
        }

        Ok(Self {
            workspace_dir,
            env_name,
            endpoint_url,
            company,
            default_activity_dir: act_dir,
        })
    }

    /// Resolves an activity directory (by path, folder name, or task name) and parses its metadata.
    pub fn resolve_activity(
        &self,
        activity_name_or_dir: Option<&str>,
    ) -> Result<(PathBuf, ActivityDotProject), ContextError> {
        let dir = if let Some(spec) = activity_name_or_dir.filter(|s| !s.trim().is_empty()) {
            let direct = PathBuf::from(spec);
            if direct.exists() && direct.is_dir() {
                direct
            } else {
                let in_ws = self.workspace_dir.join(spec);
                if in_ws.exists() && in_ws.is_dir() {
                    in_ws
                } else {
                    let mut matched = None;
                    if let Ok(entries) = std::fs::read_dir(&self.workspace_dir) {
                        for entry in entries.filter_map(|e| e.ok()) {
                            let path = entry.path();
                            if !path.is_dir() {
                                continue;
                            }
                            let name = entry.file_name().to_string_lossy().to_string();
                            if name == spec || name.starts_with(&format!("{spec} [")) {
                                matched = Some(path);
                                break;
                            }
                        }
                    }
                    matched.ok_or_else(|| ContextError::ActivityNotFound(spec.to_string()))?
                }
            }
        } else if let Some(def) = &self.default_activity_dir {
            def.clone()
        } else {
            return Err(ContextError::ActivityNotFound("<default>".into()));
        };

        let meta = ActivityDotProject::from_activity_dir(&dir)?;
        Ok((dir, meta))
    }

    /// Loads (and refreshes if needed) the OAuth2 Bearer token via `ln_auth` and builds an `HttpClient`.
    pub async fn build_authenticated_client(&self) -> Result<HttpClient, ContextError> {
        if let Ok(tok) = std::env::var("LN_ACCESS_TOKEN") {
            let trimmed = tok.trim();
            if !trimmed.is_empty() {
                let client = HttpClient::new(&self.endpoint_url, trimmed);
                client.set_default_company(&self.company);
                return Ok(client);
            }
        }

        let ws_folder = self
            .workspace_dir
            .file_name()
            .and_then(|s| s.to_str())
            .unwrap_or(&self.env_name);

        let mut token_env = self.env_name.clone();
        let mut report = check_auth_status(&token_env, None, None);
        if report.access_token.is_none() && token_env != ws_folder {
            let alt_report = check_auth_status(ws_folder, None, None);
            if alt_report.access_token.is_some()
                || alt_report.status == "needs_refresh"
                || alt_report.status == "expired"
            {
                token_env = ws_folder.to_string();
                report = alt_report;
            }
        }

        if let Some(tok) = report.access_token {
            let client = HttpClient::new(&self.endpoint_url, &tok);
            client.set_default_company(&self.company);
            return Ok(client);
        }

        if report.status == "needs_refresh" || report.status == "expired" {
            let mgr = OAuth2TokenManager::new(None);
            if let Some(cached) = mgr.load_token(&token_env) {
                if let Some(refresh_tok) = cached.refresh_token {
                    if let Some(ionapi) = self.find_ionapi_config() {
                        if let Ok(new_tok) = mgr.refresh_access_token(&ionapi, &refresh_tok).await {
                            let access = new_tok.access_token.clone();
                            let _ = mgr.save_token(&token_env, new_tok);
                            let prefs_path = self
                                .workspace_dir
                                .join(".metadata")
                                .join(".plugins")
                                .join("org.eclipse.core.runtime")
                                .join(".settings")
                                .join("com.infor.erpln.jca.connectivity.prefs");
                            if prefs_path.exists() {
                                let _ = sync_connectivity_prefs(&prefs_path, &token_env, &ionapi, None);
                            }
                            let client = HttpClient::new(&self.endpoint_url, &access);
                            client.set_default_company(&self.company);
                            return Ok(client);
                        }
                    }
                }
            }
        }

        if let Some(banner) = report.alert_banner {
            return Err(ContextError::Auth(banner));
        }

        Err(ContextError::Auth(format!(
            "No valid OAuth2 token cached for environment '{token_env}'"
        )))
    }

    pub fn load_ionapi_from_cloudenv(env_name: &str, studio_override: Option<&Path>) -> Option<IonapiConfig> {
        Self::load_ionapi_from_cloudenv_with_home(env_name, studio_override, None)
    }

    pub fn load_ionapi_from_cloudenv_with_home(
        env_name: &str,
        studio_override: Option<&Path>,
        home_override: Option<&Path>,
    ) -> Option<IonapiConfig> {
        let mut prefs_candidates: Vec<PathBuf> = Vec::new();
        let resolved_home = home_override.map(PathBuf::from).or_else(|| {
            std::env::var_os("USERPROFILE")
                .or_else(|| std::env::var_os("HOME"))
                .map(PathBuf::from)
        });
        if let Some(home) = resolved_home {
            prefs_candidates.push(
                home.join(".ln_studio")
                    .join("com.infor.erpln.jca.connectivity.cloudenv.prefs"),
            );
        }

        let mut studio_candidates: Vec<PathBuf> = Vec::new();
        if let Some(p) = studio_override {
            studio_candidates.push(p.to_path_buf());
        }
        if let Ok(p) = std::env::var("LN_STUDIO_PATH") {
            studio_candidates.push(PathBuf::from(p));
        }
        if let Ok(p) = std::env::var("LN_STUDIO_HOME") {
            studio_candidates.push(PathBuf::from(p));
        }
        for studio_dir in studio_candidates {
            prefs_candidates.push(
                studio_dir
                    .join("configuration")
                    .join(".settings")
                    .join("com.infor.erpln.jca.connectivity.cloudenv.prefs"),
            );
        }

        for prefs_path in prefs_candidates {
            if !prefs_path.is_file() {
                continue;
            }
            if let Ok(props) = read_prefs_file(&prefs_path) {
                let count: usize = props.get("EnvironmentsCount").and_then(|s| s.parse().ok()).unwrap_or(0);
                for i in 0..count {
                    let name_i = props.get(&format!("EnvironmentName{i}")).map(|s| s.as_str()).unwrap_or("");
                    if name_i.eq_ignore_ascii_case(env_name) {
                        let json_val = serde_json::json!({
                            "ti": props.get(&format!("TenantID{i}")).cloned().unwrap_or_default(),
                            "cn": "LNStudio",
                            "dt": "11",
                            "ci": props.get(&format!("ClientID{i}")).cloned().unwrap_or_default(),
                            "cs": props.get(&format!("ClientSecret{i}")).cloned().unwrap_or_default(),
                            "iu": props.get(&format!("GatewayURL{i}")).cloned().unwrap_or_default(),
                            "pu": "",
                            "oa": props.get(&format!("AuthorizationCodeURL{i}")).cloned().unwrap_or_default(),
                            "ot": props.get(&format!("RequestTokenURL{i}")).cloned().unwrap_or_default(),
                            "or": props.get(&format!("RevokeTokenURL{i}")).cloned().unwrap_or_default(),
                            "sc": props.get(&format!("AppScope{i}")).cloned().unwrap_or_default(),
                        });
                        if let Ok(cfg) = IonapiConfig::from_str(&json_val.to_string()) {
                            return Some(cfg);
                        }
                    }
                }
            }
        }
        None
    }

    pub fn find_ionapi_config(&self) -> Option<IonapiConfig> {
        let mut candidates = Vec::new();
        if let Ok(p) = std::env::var("LN_IONAPI_PATH") {
            candidates.push(PathBuf::from(p));
        }
        if let Ok(entries) = std::fs::read_dir(&self.workspace_dir) {
            for e in entries.filter_map(|e| e.ok()) {
                let p = e.path();
                if p.extension().and_then(|s| s.to_str()) == Some("ionapi") {
                    candidates.push(p);
                }
            }
        }
        if let Some(home) = dirs::home_dir() {
            let ln_dir = home.join(".ln_studio");
            candidates.push(ln_dir.join(format!("{}.ionapi", self.env_name)));
        }

        for p in candidates {
            if p.exists() {
                if let Ok(cfg) = IonapiConfig::load_from_path(&p) {
                    return Some(cfg);
                }
            }
        }

        let ws_folder = self
            .workspace_dir
            .file_name()
            .and_then(|s| s.to_str())
            .unwrap_or(&self.env_name);
        Self::load_ionapi_from_cloudenv(&self.env_name, None)
            .or_else(|| Self::load_ionapi_from_cloudenv(ws_folder, None))
    }
}
