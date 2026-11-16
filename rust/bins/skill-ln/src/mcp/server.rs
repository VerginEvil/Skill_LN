use serde_json::json;
use tokio::io::{AsyncBufReadExt, AsyncWriteExt, BufReader};
use crate::mcp::protocol::{JsonRpcRequest, JsonRpcResponse};
use crate::mcp::tools::{execute_tool, list_registered_tools};

pub async fn handle_jsonrpc_request(request: JsonRpcRequest) -> Option<JsonRpcResponse> {
    let method = request.method.as_str();

    // Ignore notifications
    if request.id.is_none() && method.starts_with("notifications/") {
        return None;
    }

    match method {
        "initialize" => {
            let params = request.params.unwrap_or_else(|| json!({}));
            let proto = params.get("protocolVersion")
                .and_then(|v| v.as_str())
                .unwrap_or("2024-11-05");

            Some(JsonRpcResponse::success(
                request.id,
                json!({
                    "protocolVersion": proto,
                    "capabilities": {
                        "tools": {}
                    },
                    "serverInfo": {
                        "name": "infor-ln-studio-mcp",
                        "version": "1.0.1"
                    }
                }),
            ))
        }

        "ping" => Some(JsonRpcResponse::success(request.id, json!({}))),

        "tools/list" => Some(JsonRpcResponse::success(
            request.id,
            json!({
                "tools": list_registered_tools()
            }),
        )),

        "tools/call" => {
            let params = request.params.unwrap_or_else(|| json!({}));
            let name = params.get("name").and_then(|v| v.as_str()).unwrap_or("");
            if name.is_empty() {
                return Some(JsonRpcResponse::error(
                    request.id,
                    -32602,
                    "Missing tool name in tools/call".to_string(),
                ));
            }
            let empty_args = json!({});
            let args = params.get("arguments").unwrap_or(&empty_args);
            let res = execute_tool(name, args).await;
            Some(JsonRpcResponse::success(request.id, res))
        }

        _ => Some(JsonRpcResponse::error(
            request.id,
            -32601,
            format!("Method not found: '{}'", method),
        )),
    }
}

pub async fn run_stdio_server() -> Result<(), Box<dyn std::error::Error + Send + Sync>> {
    let stdin = tokio::io::stdin();
    let mut stdout = tokio::io::stdout();
    let reader = BufReader::new(stdin);
    let mut lines = reader.lines();

    eprintln!("[ln-studio-mcp] Stdio JSON-RPC 2.0 server started (listening on stdin)...");

    while let Some(line) = lines.next_line().await? {
        let trimmed = line.trim();
        if trimmed.is_empty() {
            continue;
        }

        let req: JsonRpcRequest = match serde_json::from_str(trimmed) {
            Ok(r) => r,
            Err(e) => {
                eprintln!("[ln-studio-mcp] Failed to parse JSON-RPC request: {}", e);
                let err_resp = JsonRpcResponse::error(
                    None,
                    -32700,
                    format!("Parse error: {}", e),
                );
                let out = serde_json::to_string(&err_resp)?;
                stdout.write_all(out.as_bytes()).await?;
                stdout.write_all(b"\n").await?;
                stdout.flush().await?;
                continue;
            }
        };

        if let Some(resp) = handle_jsonrpc_request(req).await {
            let out = serde_json::to_string(&resp)?;
            stdout.write_all(out.as_bytes()).await?;
            stdout.write_all(b"\n").await?;
            stdout.flush().await?;
        }
    }

    eprintln!("[ln-studio-mcp] Stdio server shutting down.");
    Ok(())
}
