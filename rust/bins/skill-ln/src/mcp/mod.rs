pub mod protocol;
pub mod envelope;
pub mod tools;
pub mod server;

pub use protocol::{JsonRpcRequest, JsonRpcResponse, JsonRpcError};
pub use envelope::{McpEnvelope, make_envelope, format_mcp_response};
pub use tools::{list_registered_tools, execute_tool};
pub use server::{handle_jsonrpc_request, run_stdio_server};
