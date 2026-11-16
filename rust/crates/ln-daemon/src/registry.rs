use std::path::{Path, PathBuf};
use serde::{Deserialize, Serialize};
use sha2::{Digest, Sha256};

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq)]
pub struct DaemonInfo {
    pub port: u16,
    pub pid: u32,
    pub workspace: String,
    pub started_at: f64,
    pub engine: String,
}

pub fn get_daemon_dir() -> PathBuf {
    let dir = dirs::home_dir()
        .unwrap_or_else(|| PathBuf::from("."))
        .join(".ln_studio");
    let _ = std::fs::create_dir_all(&dir);
    dir
}

pub fn compute_workspace_hash(workspace_path: Option<&Path>) -> String {
    let Some(path) = workspace_path else {
        return "global".to_string();
    };

    let norm = path
        .canonicalize()
        .unwrap_or_else(|_| path.to_path_buf())
        .to_string_lossy()
        .replace('\\', "/")
        .to_lowercase();

    let mut hasher = Sha256::new();
    hasher.update(norm.as_bytes());
    let res = hasher.finalize();
    let hex = format!("{res:x}");
    hex[..16].to_string()
}

pub fn get_daemon_reg_file(workspace_path: Option<&Path>) -> PathBuf {
    let h = compute_workspace_hash(workspace_path);
    get_daemon_dir().join(format!("daemon_{h}.json"))
}

pub fn get_daemon_lock_file(workspace_path: Option<&Path>) -> PathBuf {
    let h = compute_workspace_hash(workspace_path);
    get_daemon_dir().join(format!("daemon_{h}.lock"))
}
