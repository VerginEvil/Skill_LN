use std::path::{Path, PathBuf};
use std::time::Duration;
use serde_json::{json, Value};
use thiserror::Error;
use tokio::io::{AsyncBufReadExt, AsyncWriteExt, BufReader};
use tokio::net::TcpStream;
use tokio::time::timeout;

use crate::registry::{get_daemon_reg_file, DaemonInfo};

#[derive(Error, Debug)]
pub enum DaemonClientError {
    #[error("I/O error: {0}")]
    Io(#[from] std::io::Error),
    #[error("JSON error: {0}")]
    Json(#[from] serde_json::Error),
    #[error("Daemon not running or registration file missing: {0}")]
    NotRunning(String),
    #[error("Daemon timeout: {0}")]
    Timeout(String),
    #[error("Daemon RPC error (code {code}): {message}")]
    Rpc { code: i64, message: String },
}

pub struct DaemonClient {
    workspace_path: Option<PathBuf>,
    port: Option<u16>,
}

impl DaemonClient {
    pub fn new(workspace_path: Option<&Path>) -> Self {
        Self {
            workspace_path: workspace_path.map(|p| p.to_path_buf()),
            port: None,
        }
    }

    pub fn with_port(port: u16) -> Self {
        Self {
            workspace_path: None,
            port: Some(port),
        }
    }

    pub fn get_info(&self) -> Result<DaemonInfo, DaemonClientError> {
        let reg_file = get_daemon_reg_file(self.workspace_path.as_deref());
        if !reg_file.exists() {
            return Err(DaemonClientError::NotRunning(format!(
                "Registration file '{}' not found",
                reg_file.display()
            )));
        }
        let content = std::fs::read_to_string(&reg_file)?;
        let info: DaemonInfo = serde_json::from_str(&content)?;
        Ok(info)
    }

    pub fn get_port(&self) -> Result<u16, DaemonClientError> {
        if let Some(p) = self.port {
            return Ok(p);
        }
        let info = self.get_info()?;
        Ok(info.port)
    }

    pub async fn send_rpc(&self, method: &str, params: Value, timeout_dur: Duration) -> Result<Value, DaemonClientError> {
        let port = self.get_port()?;
        let stream = timeout(timeout_dur, TcpStream::connect(("127.0.0.1", port)))
            .await
            .map_err(|_| DaemonClientError::Timeout("Connect timeout".into()))??;

        let (reader, mut writer) = stream.into_split();
        let mut reader = BufReader::new(reader);

        let req = json!({
            "jsonrpc": "2.0",
            "id": 1,
            "method": method,
            "params": params,
        });

        let mut line = serde_json::to_string(&req)?;
        line.push('\n');

        timeout(timeout_dur, writer.write_all(line.as_bytes()))
            .await
            .map_err(|_| DaemonClientError::Timeout("Write timeout".into()))??;
        timeout(timeout_dur, writer.flush())
            .await
            .map_err(|_| DaemonClientError::Timeout("Flush timeout".into()))??;

        let mut resp_line = String::new();
        timeout(timeout_dur, reader.read_line(&mut resp_line))
            .await
            .map_err(|_| DaemonClientError::Timeout("Read timeout".into()))??;

        if resp_line.trim().is_empty() {
            return Err(DaemonClientError::NotRunning("Empty response from daemon".into()));
        }

        let resp: Value = serde_json::from_str(&resp_line)?;
        if let Some(err_val) = resp.get("error") {
            let code = err_val.get("code").and_then(|c| c.as_i64()).unwrap_or(-32000);
            let msg = err_val.get("message").and_then(|m| m.as_str()).unwrap_or("Unknown error");
            return Err(DaemonClientError::Rpc {
                code,
                message: msg.to_string(),
            });
        }

        Ok(resp.get("result").cloned().unwrap_or(Value::Null))
    }

    pub async fn ping(&self) -> Result<bool, DaemonClientError> {
        let res = self.send_rpc("ping", json!({}), Duration::from_secs(3)).await?;
        Ok(res.get("status").and_then(|s| s.as_str()) == Some("ok"))
    }

    pub async fn status(&self) -> Result<Value, DaemonClientError> {
        self.send_rpc("status", json!({}), Duration::from_secs(5)).await
    }

    pub async fn update_token(&self, new_token: &str) -> Result<bool, DaemonClientError> {
        let res = self.send_rpc("update_token", json!({ "token": new_token }), Duration::from_secs(5)).await?;
        Ok(res.get("status").and_then(|s| s.as_str()) == Some("updated"))
    }

    pub async fn shutdown(&self) -> Result<bool, DaemonClientError> {
        let res = self.send_rpc("shutdown", json!({}), Duration::from_secs(5)).await?;
        Ok(res.get("status").and_then(|s| s.as_str()) == Some("shutting_down"))
    }
}
