use std::collections::HashMap;
use std::path::{Path, PathBuf};
use std::sync::atomic::{AtomicBool, Ordering};
use std::sync::Arc;
use std::time::{Duration, Instant, SystemTime, UNIX_EPOCH};
use ln_eclipse_compat::{try_acquire_file_lock, LockError, WorkspaceLock};
use ln_jca::bde_manager::{BdeExecutionMode, BdeParams, JcaBdeManager};
use ln_jca::client::{ConnectOptions, HttpClient};
use ln_jca::filter::{BdeFilter, BdeSelection};
use ln_jca::security::assert_not_prohibited_operation;
use serde_json::{json, Value};
use thiserror::Error;
use tokio::io::{AsyncBufReadExt, AsyncWriteExt, BufReader};
use tokio::net::{TcpListener, TcpStream};
use tokio::sync::{mpsc, oneshot};

use crate::registry::{get_daemon_lock_file, get_daemon_reg_file, DaemonInfo};

#[derive(Error, Debug)]
pub enum DaemonServerError {
    #[error("I/O error: {0}")]
    Io(#[from] std::io::Error),
    #[error("JSON error: {0}")]
    Json(#[from] serde_json::Error),
    #[error("Daemon is already running for this workspace (lock held)")]
    AlreadyRunning,
    #[error("Lock error: {0}")]
    Lock(#[from] LockError),
}

struct DaemonTask {
    request: Value,
    response_sender: oneshot::Sender<Value>,
}

pub struct DaemonServer {
    workspace_path: Option<PathBuf>,
    port: u16,
    idle_timeout_seconds: u64,
    keepalive_interval_seconds: u64,
}

impl DaemonServer {
    pub fn new(workspace_path: Option<&Path>, port: u16) -> Self {
        Self {
            workspace_path: workspace_path.map(|p| p.to_path_buf()),
            port,
            idle_timeout_seconds: 1800,
            keepalive_interval_seconds: 60,
        }
    }

    pub fn with_timeouts(
        workspace_path: Option<&Path>,
        port: u16,
        idle_timeout_seconds: u64,
        keepalive_interval_seconds: u64,
    ) -> Self {
        Self {
            workspace_path: workspace_path.map(|p| p.to_path_buf()),
            port,
            idle_timeout_seconds,
            keepalive_interval_seconds,
        }
    }

    pub async fn run(self) -> Result<(), DaemonServerError> {
        // 1. Single-Leader Election Lock
        let lock_file = get_daemon_lock_file(self.workspace_path.as_deref());
        let _lock_guard: WorkspaceLock = match try_acquire_file_lock(&lock_file) {
            Ok(guard) => guard,
            Err(LockError::Locked) => return Err(DaemonServerError::AlreadyRunning),
            Err(e) => return Err(DaemonServerError::Lock(e)),
        };

        // 2. Bind TCP listener on 127.0.0.1
        let listener = TcpListener::bind(("127.0.0.1", self.port)).await?;
        let bound_port = listener.local_addr()?.port();
        let pid = std::process::id();

        // 3. Register daemon in ~/.ln_studio/daemon_<workspace_hash>.json
        let reg_file = get_daemon_reg_file(self.workspace_path.as_deref());
        let info = DaemonInfo {
            port: bound_port,
            pid,
            workspace: self
                .workspace_path
                .as_ref()
                .map(|p| p.to_string_lossy().to_string())
                .unwrap_or_else(|| "global".to_string()),
            started_at: SystemTime::now()
                .duration_since(UNIX_EPOCH)
                .unwrap_or_default()
                .as_secs_f64(),
            engine: "rust-native".to_string(),
        };
        let info_json = serde_json::to_string_pretty(&info)?;
        std::fs::write(&reg_file, info_json)?;

        // Output DAEMON_READY signal
        println!("DAEMON_READY port={bound_port} pid={pid}");

        // 4. Sequential FIFO Command Queue (Pool Size = 1)
        let (task_tx, mut task_rx) = mpsc::channel::<DaemonTask>(100);
        let running_flag = Arc::new(AtomicBool::new(true));
        let running_for_worker = running_flag.clone();
        let reg_file_for_worker = reg_file.clone();

        let idle_timeout = Duration::from_secs(self.idle_timeout_seconds);
        let keepalive_interval = Duration::from_secs(self.keepalive_interval_seconds);

        // Worker Task
        let worker_handle = tokio::spawn(async move {
            let mut active_client: Option<HttpClient> = None;
            let mut primary_conid: Option<String> = None;
            let mut shared_conids: HashMap<String, String> = HashMap::new();
            let mut last_activity = Instant::now();
            let mut last_ping = Instant::now();

            while running_for_worker.load(Ordering::SeqCst) {
                // Poll next task with tick
                let recv_res = tokio::time::timeout(Duration::from_millis(500), task_rx.recv()).await;

                // Idle timeout check
                if last_activity.elapsed() >= idle_timeout {
                    println!("[DAEMON] Idle timeout reached ({}s). Shutting down.", idle_timeout.as_secs());
                    running_for_worker.store(false, Ordering::SeqCst);
                    break;
                }

                // Keepalive ping check
                if let Some(client) = &active_client {
                    if last_ping.elapsed() >= keepalive_interval {
                        let _ = client.ping().await;
                        last_ping = Instant::now();
                    }
                }

                match recv_res {
                    Ok(Some(task)) => {
                        last_activity = Instant::now();
                        let id = task.request.get("id").cloned().unwrap_or(json!(1));
                        let method = task.request.get("method").and_then(|m| m.as_str()).unwrap_or("");
                        let params = task.request.get("params").cloned().unwrap_or(json!({}));

                        let response = match method {
                            "ping" => {
                                json!({
                                    "jsonrpc": "2.0",
                                    "id": id,
                                    "result": { "status": "ok" }
                                })
                            }
                            "status" => {
                                let idle_sec = last_activity.elapsed().as_secs();
                                let active_conns = if primary_conid.is_some() { 1 + shared_conids.len() } else { 0 };
                                json!({
                                    "jsonrpc": "2.0",
                                    "id": id,
                                    "result": {
                                        "status": "running",
                                        "active_connections": active_conns,
                                        "idle_seconds": idle_sec,
                                        "pid": pid,
                                        "port": bound_port,
                                    }
                                })
                            }
                            "update_token" => {
                                if let Some(new_token) = params.get("token").and_then(|t| t.as_str()) {
                                    if let Some(c) = &active_client {
                                        c.set_access_token(new_token);
                                    }
                                }
                                json!({
                                    "jsonrpc": "2.0",
                                    "id": id,
                                    "result": { "status": "updated" }
                                })
                            }
                            "shutdown" => {
                                running_for_worker.store(false, Ordering::SeqCst);
                                json!({
                                    "jsonrpc": "2.0",
                                    "id": id,
                                    "result": { "status": "shutting_down" }
                                })
                            }
                            "execute_bde" | "bde_call" => {
                                handle_execute_bde(
                                    id,
                                    params,
                                    &mut active_client,
                                    &mut primary_conid,
                                    &mut shared_conids,
                                ).await
                            }
                            unknown => {
                                json!({
                                    "jsonrpc": "2.0",
                                    "id": id,
                                    "error": {
                                        "code": -32601,
                                        "message": format!("Method not found: {unknown}")
                                    }
                                })
                            }
                        };

                        let _ = task.response_sender.send(response);

                        if !running_for_worker.load(Ordering::SeqCst) {
                            break;
                        }
                    }
                    Ok(None) => break, // channel closed
                    Err(_) => {} // timeout tick
                }
            }

            // Cleanup JCA connections on exit
            if let Some(client) = active_client {
                let _ = client.disconnect(primary_conid.as_deref()).await;
            }
            let _ = std::fs::remove_file(&reg_file_for_worker);
        });

        // Accept loop
        while running_flag.load(Ordering::SeqCst) {
            let accept_res = tokio::time::timeout(Duration::from_millis(500), listener.accept()).await;
            if let Ok(Ok((socket, _))) = accept_res {
                let task_tx = task_tx.clone();
                tokio::spawn(async move {
                    handle_client_socket(socket, task_tx).await;
                });
            }
        }

        let _ = worker_handle.await;
        let _ = std::fs::remove_file(&reg_file);

        Ok(())
    }
}

async fn handle_client_socket(socket: TcpStream, task_tx: mpsc::Sender<DaemonTask>) {
    let (reader, mut writer) = socket.into_split();
    let mut reader = BufReader::new(reader);
    let mut line = String::new();

    while let Ok(n) = reader.read_line(&mut line).await {
        if n == 0 {
            break;
        }
        let trimmed = line.trim();
        if trimmed.is_empty() {
            line.clear();
            continue;
        }

        let req_json: Value = match serde_json::from_str(trimmed) {
            Ok(v) => v,
            Err(e) => {
                let err_resp = json!({
                    "jsonrpc": "2.0",
                    "id": null,
                    "error": { "code": -32700, "message": format!("Parse error: {e}") }
                });
                let mut out = serde_json::to_string(&err_resp).unwrap_or_default();
                out.push('\n');
                let _ = writer.write_all(out.as_bytes()).await;
                let _ = writer.flush().await;
                line.clear();
                continue;
            }
        };

        let (resp_tx, resp_rx) = oneshot::channel();
        let task = DaemonTask {
            request: req_json,
            response_sender: resp_tx,
        };

        if task_tx.send(task).await.is_err() {
            break;
        }

        if let Ok(resp) = resp_rx.await {
            let mut out = serde_json::to_string(&resp).unwrap_or_default();
            out.push('\n');
            let _ = writer.write_all(out.as_bytes()).await;
            let _ = writer.flush().await;
        }

        line.clear();
    }
}

async fn handle_execute_bde(
    id: Value,
    params: Value,
    active_client: &mut Option<HttpClient>,
    primary_conid: &mut Option<String>,
    shared_conids: &mut HashMap<String, String>,
) -> Value {
    let bde_name = params.get("bde").and_then(|v| v.as_str()).unwrap_or("");
    let method_name = params.get("method").and_then(|v| v.as_str()).unwrap_or("");
    let req_xml = params.get("requestXml").and_then(|v| v.as_str()).unwrap_or("");
    let context_xml = params.get("contextXml").and_then(|v| v.as_str()).map(|s| s.to_string());
    let mode_str = params.get("mode").and_then(|v| v.as_str()).unwrap_or("BDE");
    let conn_point = params.get("connectionPoint").and_then(|v| v.as_str()).unwrap_or("ProjectServer");

    // Security Hard-Block (ADR 0008)
    if let Err(e) = assert_not_prohibited_operation(bde_name, method_name, req_xml) {
        return json!({
            "jsonrpc": "2.0",
            "id": id,
            "error": {
                "code": -32003,
                "message": format!("[SECURITY_BLOCK] Prohibited operation: {e}")
            }
        });
    }

    let backend = params.get("backend").and_then(|v| v.as_str()).unwrap_or("");
    let token = params.get("token").and_then(|v| v.as_str()).unwrap_or("");

    // Initialize or reuse primary client
    let client = match active_client {
        Some(c) if c.get_base_url() == backend.trim_end_matches('/') => {
            if !token.is_empty() {
                c.set_access_token(token);
            }
            c
        }
        _ => {
            let new_c = HttpClient::new(backend, token);
            let conn_res = match new_c.connect(&ConnectOptions::default()).await {
                Ok(resp) => resp,
                Err(e) => {
                    return json!({
                        "jsonrpc": "2.0",
                        "id": id,
                        "error": { "code": -32000, "message": format!("Connect failed: {e}") }
                    });
                }
            };
            *primary_conid = Some(conn_res.conid);
            *active_client = Some(new_c);
            shared_conids.clear();
            active_client.as_ref().unwrap()
        }
    };

    // Determine target conid (ProjectServer vs shared connection point)
    let target_conid = if conn_point == "ProjectServer" {
        primary_conid.as_deref().unwrap_or("1")
    } else {
        if !shared_conids.contains_key(conn_point) {
            match client.share(None).await {
                Ok(share_resp) => {
                    shared_conids.insert(conn_point.to_string(), share_resp.conid);
                }
                Err(e) => {
                    return json!({
                        "jsonrpc": "2.0",
                        "id": id,
                        "error": { "code": -32000, "message": format!("Failed to multiplex connection '{conn_point}': {e}") }
                    });
                }
            }
        }
        shared_conids.get(conn_point).map(|s| s.as_str()).unwrap_or("1")
    };

    // Parse selection, filter, controlling attributes
    let selection = params.get("selectionFields").and_then(|v| v.as_array()).map(|arr| {
        let fields: Vec<&str> = arr.iter().filter_map(|x| x.as_str()).collect();
        BdeSelection::from_fields(&fields)
    });

    let filter = params.get("filterExpression").and_then(|v| v.as_str()).and_then(BdeFilter::parse);
    let max_objects = params.get("maxObjects").and_then(|v| v.as_u64()).map(|n| n as usize);

    let mut controlling_attributes = HashMap::new();
    if let Some(obj) = params.get("controllingAttributes").and_then(|v| v.as_object()) {
        for (k, v) in obj {
            if let Some(s) = v.as_str() {
                controlling_attributes.insert(k.clone(), s.to_string());
            }
        }
    }

    let bde_params = BdeParams {
        bde_name: bde_name.to_string(),
        method_name: method_name.to_string(),
        mode: Some(BdeExecutionMode::from_str(mode_str)),
        request_xml: if req_xml.is_empty() { None } else { Some(req_xml.to_string()) },
        context_xml,
        selection,
        filter,
        max_objects,
        controlling_attributes,
    };

    let bde_mgr = JcaBdeManager::new(client, target_conid);
    match bde_mgr.execute(&bde_params).await {
        Ok(xml_res) => {
            json!({
                "jsonrpc": "2.0",
                "id": id,
                "result": { "xml": xml_res }
            })
        }
        Err(e) => {
            json!({
                "jsonrpc": "2.0",
                "id": id,
                "error": { "code": -32000, "message": e.to_string() }
            })
        }
    }
}
