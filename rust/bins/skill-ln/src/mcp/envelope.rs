use serde::{Deserialize, Serialize};
use serde_json::{json, Value};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct McpEnvelope {
    pub status: String,
    pub action: String,
    pub result: Value,
    pub message: String,
}

pub fn make_envelope(action: &str, result: Value, message: &str, status: &str) -> McpEnvelope {
    let msg = if message.is_empty() {
        if status == "success" { "Success" } else { "Error" }
    } else {
        message
    };

    McpEnvelope {
        status: status.to_string(),
        action: action.to_string(),
        result,
        message: msg.to_string(),
    }
}

pub fn format_mcp_response(env: McpEnvelope, is_error: bool) -> Value {
    let text = serde_json::to_string_pretty(&env).unwrap_or_else(|_| "{}".to_string());
    json!({
        "content": [
            {
                "type": "text",
                "text": text
            }
        ],
        "isError": is_error
    })
}
