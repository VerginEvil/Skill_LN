use serde_json::json;
use skill_ln::mcp::{
    execute_tool, handle_jsonrpc_request, list_registered_tools,
    JsonRpcRequest,
};

#[test]
fn test_mcp_initialize_and_ping() {
    let init_req = JsonRpcRequest {
        jsonrpc: "2.0".to_string(),
        id: Some(json!(1)),
        method: "initialize".to_string(),
        params: Some(json!({
            "protocolVersion": "2024-11-05",
            "clientInfo": {"name": "test-client", "version": "1.0.0"}
        })),
    };

    let res = handle_jsonrpc_request(init_req).expect("initialize must return response");
    assert_eq!(res.jsonrpc, "2.0");
    assert_eq!(res.id, Some(json!(1)));
    let result = res.result.expect("result must be present");
    assert_eq!(result["serverInfo"]["name"], "infor-ln-studio-mcp");
    assert_eq!(result["serverInfo"]["version"], "1.0.1");

    let ping_req = JsonRpcRequest {
        jsonrpc: "2.0".to_string(),
        id: Some(json!(2)),
        method: "ping".to_string(),
        params: None,
    };
    let res_ping = handle_jsonrpc_request(ping_req).expect("ping must return response");
    assert_eq!(res_ping.id, Some(json!(2)));
    assert_eq!(res_ping.result, Some(json!({})));
}

#[test]
fn test_mcp_tools_list_schema_and_count() {
    let tools = list_registered_tools();
    assert_eq!(tools.len(), 25, "Must expose exactly 25 MCP tools");

    let expected_tools = [
        "ln_list_environments",
        "ln_login",
        "ln_connect",
        "ln_explore_projects",
        "ln_explore_activities",
        "ln_explore_components",
        "ln_create_activity",
        "ln_clean_activity",
        "ln_get_component",
        "ln_sync_reference",
        "ln_checkout_component",
        "ln_uncheckout_component",
        "ln_checkin_component",
        "ln_checkout_activity",
        "ln_checkin_activity",
        "ln_create_component",
        "ln_clone_component",
        "ln_validate_activity",
        "ln_deploy_test",
        "ln_prepare_end_activity",
        "ln_end_activity",
        "ln_project_activity",
        "ln_code_intelligence",
        "ln_version_diff",
        "ln_adhoc_compile",
    ];

    let names: Vec<String> = tools
        .iter()
        .filter_map(|t| t["name"].as_str().map(|s| s.to_string()))
        .collect();

    for et in expected_tools {
        assert!(names.contains(&et.to_string()), "Tool '{}' missing from registry", et);
    }
}

#[test]
fn test_mcp_execute_tools_parity_and_envelope() {
    // 1. ln_list_environments
    let res = execute_tool("ln_list_environments", &json!({}));
    assert_eq!(res["isError"], false);
    let text = res["content"][0]["text"].as_str().unwrap();
    assert!(text.contains("workspaces"));

    // 2. ln_explore_projects
    let res = execute_tool("ln_explore_projects", &json!({"mock": true}));
    assert_eq!(res["isError"], false);
    let text = res["content"][0]["text"].as_str().unwrap();
    assert!(text.contains("EXTce01107"));

    // 3. ln_checkout_component (Standard component -> success)
    let res = execute_tool("ln_checkout_component", &json!({
        "type": "table",
        "name": "ttadv300",
        "activity": "act1",
        "project": "EXTce01107",
        "mock": true
    }));
    assert_eq!(res["isError"], false);
    let text = res["content"][0]["text"].as_str().unwrap();
    assert!(text.contains("checked_out"));

    // 4. ln_checkout_component (Extension Modeler tx* component -> ReadOnlyComponentError)
    let res_ext = execute_tool("ln_checkout_component", &json!({
        "type": "library",
        "name": "txesssli2620m0",
        "activity": "act1",
        "project": "EXTce01107",
        "mock": true
    }));
    assert_eq!(res_ext["isError"], true);
    let text = res_ext["content"][0]["text"].as_str().unwrap();
    assert!(text.contains("ReadOnlyComponentError"), "Expected ReadOnlyComponentError, got: {}", text);

    // 5. ln_end_activity (Hard blocked -> PreCommitBoundaryError)
    let res_end = execute_tool("ln_end_activity", &json!({
        "activity": "act1",
        "project": "EXTce01107"
    }));
    assert_eq!(res_end["isError"], true);
    let text = res_end["content"][0]["text"].as_str().unwrap();
    assert!(text.contains("PreCommitBoundaryError"), "Expected PreCommitBoundaryError, got: {}", text);

    // 6. ln_adhoc_compile
    let res = execute_tool("ln_adhoc_compile", &json!({
        "package_code": "tx",
        "source_code": "function extern void test() { }"
    }));
    assert_eq!(res["isError"], false);
    let text = res["content"][0]["text"].as_str().unwrap();
    assert!(text.contains("compiled"));
}
