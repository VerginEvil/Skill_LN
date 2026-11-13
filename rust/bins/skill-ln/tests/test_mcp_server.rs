use std::collections::HashMap;
use std::io::Write;
use std::process::{Command, Stdio};
use std::sync::{Arc, Mutex};
use serde_json::json;
use tokio::io::{AsyncReadExt, AsyncWriteExt};
use tokio::net::TcpListener;

use ln_eclipse_compat::admin::AdminFile;
use ln_model::path_resolver::resolve_tde_relative_path;
use skill_ln::mcp::{
    execute_tool, handle_jsonrpc_request, list_registered_tools,
    JsonRpcRequest,
};

#[tokio::test]
async fn test_mcp_initialize_and_ping() {
    let init_req = JsonRpcRequest {
        jsonrpc: "2.0".to_string(),
        id: Some(json!(1)),
        method: "initialize".to_string(),
        params: Some(json!({
            "protocolVersion": "2024-11-05",
            "clientInfo": {"name": "test-client", "version": "1.0.0"}
        })),
    };

    let res = handle_jsonrpc_request(init_req).await.expect("initialize must return response");
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
    let res_ping = handle_jsonrpc_request(ping_req).await.expect("ping must return response");
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

#[tokio::test]
async fn test_mcp_execute_tools_parity_and_envelope() {
    // 1. ln_list_environments
    let res = execute_tool("ln_list_environments", &json!({})).await;
    assert_eq!(res["isError"], false);
    let text = res["content"][0]["text"].as_str().unwrap();
    assert!(text.contains("workspaces"));

    // 2. ln_explore_projects
    let res = execute_tool("ln_explore_projects", &json!({"mock": true})).await;
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
    })).await;
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
    })).await;
    assert_eq!(res_ext["isError"], true);
    let text = res_ext["content"][0]["text"].as_str().unwrap();
    assert!(text.contains("ReadOnlyComponentError"), "Expected ReadOnlyComponentError, got: {}", text);

    // 5. ln_end_activity (Hard blocked -> PreCommitBoundaryError)
    let res_end = execute_tool("ln_end_activity", &json!({
        "activity": "act1",
        "project": "EXTce01107"
    })).await;
    assert_eq!(res_end["isError"], true);
    let text = res_end["content"][0]["text"].as_str().unwrap();
    assert!(text.contains("PreCommitBoundaryError"), "Expected PreCommitBoundaryError, got: {}", text);

    // 6. ln_adhoc_compile
    let res = execute_tool("ln_adhoc_compile", &json!({
        "package_code": "tx",
        "source_code": "function extern void test() { }",
        "mock": true
    })).await;
    assert_eq!(res["isError"], false);
    let text = res["content"][0]["text"].as_str().unwrap();
    assert!(text.contains("compiled"));
}

#[tokio::test]
async fn test_mcp_create_component_all_12_types_canonical_paths() {
    let dir = tempfile::tempdir().unwrap();
    let act_dir = dir.path().join("dev_act1 [EXTce01108]");
    std::fs::create_dir_all(&act_dir).unwrap();
    std::fs::write(
        act_dir.join(".project"),
        "<projectDescription><name>dev_act1 [EXTce01108]</name></projectDescription>",
    )
    .unwrap();
    AdminFile::default().save_to_path(&act_dir.join(".admin")).unwrap();

    let cases = [
        ("table", "txcmg0001", "tbl"),
        ("session", "txcmg0100m000", "ses"),
        ("domain", "txcmg.dmn1", "dmn"),
        ("library", "txcmg0001lib", "lib"),
        ("menu", "txcmg0001m00", "mnu"),
        ("label", "txcmg0001lbl", "lbl"),
        ("message", "txcmg0001msg", "msg"),
        ("question", "txcmg0001qst", "qst"),
        ("function", "itxcmg0001fn", "fnc"),
        ("additional", "txcmgadd01", "add"),
        ("report", "rtxcmg010011000", "rpt"),
        ("businessobject", "txcmgbod01", "bus"),
    ];

    for (ctype, code, ext) in cases {
        let res = execute_tool(
            "ln_create_component",
            &json!({
                "type": ctype,
                "code": code,
                "description": format!("MCP created {}", code),
                "activity": act_dir.to_string_lossy()
            }),
        )
        .await;
        assert_eq!(
            res["isError"], false,
            "ln_create_component failed for {}: {:?}",
            ctype, res
        );

        let expected_rel = resolve_tde_relative_path(ctype, code, ext).unwrap();
        let full = act_dir.join(&expected_rel);
        assert!(
            full.exists(),
            "Expected canonical path {} for {} ({:?})",
            full.display(),
            ctype,
            res
        );

        let content = std::fs::read_to_string(&full).unwrap();
        assert!(
            content.contains("<?xml") || content.contains("<root>"),
            "Expected valid Single-XML content for {}, got: {}",
            ctype,
            content
        );
        for forbidden in [
            "<DR_Message name=",
            "<DR_Question name=",
            "<DR_Function name=",
            "<DR_Additional name=",
            "<DR_Report name=",
        ] {
            assert!(
                !content.contains(forbidden),
                "Found forbidden attribute stub {} in {}",
                forbidden,
                ctype
            );
        }

        let admin = AdminFile::load_from_path(&act_dir.join(".admin")).unwrap();
        let norm = expected_rel.to_string_lossy().replace('\\', "/");
        assert!(
            admin.get(&norm).is_some(),
            "Missing {} in .admin after creating {}",
            norm,
            ctype
        );
    }

    for legacy_dir in ["messages", "questions", "functions", "additional", "reports"] {
        assert!(
            !act_dir.join(legacy_dir).exists(),
            "Legacy plural directory '{}' must never be created",
            legacy_dir
        );
    }
}

#[derive(Default)]
struct McpMockJcaState {
    next_conid: usize,
    bde_calls: Vec<String>,
    non_numeric_conid_seen: bool,
    disconnects: usize,
}

fn form_decode(input: &str) -> HashMap<String, String> {
    let mut map = HashMap::new();
    for pair in input.split('&') {
        if let Some((k, v)) = pair.split_once('=') {
            let dec = |s: &str| {
                let s = s.replace('+', " ");
                let mut out = String::new();
                let mut chars = s.bytes().peekable();
                while let Some(b) = chars.next() {
                    if b == b'%' {
                        let h1 = chars.next().unwrap_or(b'0');
                        let h2 = chars.next().unwrap_or(b'0');
                        if let Ok(val) = u8::from_str_radix(&format!("{}{}", h1 as char, h2 as char), 16) {
                            out.push(val as char);
                        }
                    } else {
                        out.push(b as char);
                    }
                }
                out
            };
            map.insert(dec(k), dec(v));
        }
    }
    map
}

async fn start_mcp_mock_jca() -> (String, Arc<Mutex<McpMockJcaState>>) {
    let listener = TcpListener::bind("127.0.0.1:0").await.unwrap();
    let addr = listener.local_addr().unwrap();
    let state = Arc::new(Mutex::new(McpMockJcaState::default()));
    let state_clone = state.clone();

    tokio::spawn(async move {
        loop {
            let Ok((mut stream, _)) = listener.accept().await else {
                break;
            };
            let st = state_clone.clone();
            tokio::spawn(async move {
                let mut buf = vec![0u8; 65536];
                let n = stream.read(&mut buf).await.unwrap_or(0);
                if n == 0 {
                    return;
                }
                let raw = String::from_utf8_lossy(&buf[..n]);
                let req_line = raw.lines().next().unwrap_or("");
                let query = req_line
                    .split_whitespace()
                    .nth(1)
                    .and_then(|u| u.split_once('?').map(|(_, q)| q))
                    .unwrap_or("");
                let body = raw.split("\r\n\r\n").nth(1).unwrap_or("");
                let mut params = form_decode(query);
                params.extend(form_decode(body));
                let method = params.get("method").map(String::as_str).unwrap_or("");

                let (status, resp_xml) = match method {
                    "ping" => ("200 OK", "pong".to_string()),
                    "connect" | "share" => {
                        let mut s = st.lock().unwrap();
                        let id = s.next_conid;
                        s.next_conid += 1;
                        (
                            "200 OK",
                            format!("<ConnectResponse><SessionID>mcp_s</SessionID><conid>{id}</conid></ConnectResponse>"),
                        )
                    }
                    "disconnect" => {
                        st.lock().unwrap().disconnects += 1;
                        ("200 OK", "<DisconnectResponse/>".to_string())
                    }
                    "bdecall" => {
                        let conid = params.get("conid").cloned().unwrap_or_default();
                        let bde = params.get("bdename").cloned().unwrap_or_default();
                        let bde_m = params.get("bdemethod").cloned().unwrap_or_default();
                        let mut s = st.lock().unwrap();
                        if conid.is_empty() || !conid.chars().all(|c| c.is_ascii_digit()) {
                            s.non_numeric_conid_seen = true;
                            (
                                "500 Internal Server Error",
                                "<error><info>null</info><message>POST request failed</message><reason>0</reason></error>".to_string(),
                            )
                        } else {
                            s.bde_calls.push(format!("{}.{}", bde, bde_m));
                            let xml = match (bde.as_str(), bde_m.as_str()) {
                                ("SoftwareProject", "List") => "<SoftwareProjectListResponse><DataArea><SoftwareProject><projectName>LIVE_PROJ_88</projectName><projectDescription>Live Stateful Project</projectDescription><projectStatus>active</projectStatus><typeOfProject>standard</typeOfProject><Task><taskName>LIVE_TASK_99</taskName><taskStatus>opened</taskStatus><typeOfTask>feature</typeOfTask><assignedTo>u</assignedTo></Task></SoftwareProject></DataArea></SoftwareProjectListResponse>".to_string(),
                                ("SoftwareProject_V2", "Show") => "<SoftwareProject_V2ShowResponse><DataArea><SoftwareProject_V2><projectName>LIVE_PROJ_88</projectName><projectDescription>Live Stateful Project</projectDescription><projectVersionID>B61O_a_ext</projectVersionID><developmentEnvironment>DEV</developmentEnvironment><developmentRepositoryAddress>LIVE_PROJ_88_dev</developmentRepositoryAddress><runtimeRepositoryAddress>LIVE_PROJ_88_rt</runtimeRepositoryAddress><integrationWithPMC>false</integrationWithPMC><Package>tx</Package><Task><taskName>LIVE_TASK_99</taskName><labelUUID>uuid-lbl-99</labelUUID><taskUUID>uuid-tsk-99</taskUUID><taskVersionID>1</taskVersionID><taskDescription>Live Task</taskDescription><typeOfTask>feature</typeOfTask><assignedTo>u</assignedTo><taskStatus>opened</taskStatus><taskSeverity>medium</taskSeverity><functionalChange>no</functionalChange></Task></SoftwareProject_V2></DataArea></SoftwareProject_V2ShowResponse>".to_string(),
                                ("StudioComponent", "GetProjectSource") | ("StudioComponent", "GetActivitySource") => "<StudioComponentResponse><DataArea><DR_Table xmlns=\"http://www.infor.com/businessline/application/dr\" version=\"1.0\"><description>Item</description><name>tcibd001</name><Column><name>item</name></Column><Source><expression><![CDATA[function extern void dummy() {}]]></expression></Source></DR_Table></DataArea></StudioComponentResponse>".to_string(),
                                ("FglStudio", "compileSource") => "<FglStudioShowResponse><DataArea><compileResult><summary totalErrors=\"0\" totalWarnings=\"0\"/></compileResult></DataArea></FglStudioShowResponse>".to_string(),
                                (_, "GetRevisions") => "<FglStudioResponse><DataArea><revisions><revision number=\"7\" versionID=\"B61O_a_ext\" date=\"2026-01-01\" time=\"00:00:00\" author=\"dev\" comment=\"Live rev\" task=\"LIVE_TASK_99\"/></revisions></DataArea></FglStudioResponse>".to_string(),
                                _ => format!("<{}Response><DataArea><Ok/></DataArea></{}Response>", bde, bde),
                            };
                            ("200 OK", xml)
                        }
                    }
                    "show" => ("200 OK", "<show><ok>true</ok></show>".to_string()),
                    _ => ("200 OK", "<ok>true</ok>".to_string()),
                };

                let reply = format!(
                    "HTTP/1.1 {}\r\nContent-Type: text/xml\r\nContent-Length: {}\r\nConnection: close\r\n\r\n{}",
                    status,
                    resp_xml.len(),
                    resp_xml
                );
                let _ = stream.write_all(reply.as_bytes()).await;
            });
        }
    });

    (format!("http://{}", addr), state)
}

#[tokio::test]
async fn test_mcp_tools_against_stateful_mock_jca_server() {
    let (endpoint, state) = start_mcp_mock_jca().await;
    let dir = tempfile::tempdir().unwrap();
    let act_dir = dir.path().join("live_act [LIVE_PROJ_88]");
    std::fs::create_dir_all(&act_dir).unwrap();
    std::fs::write(
        act_dir.join(".project"),
        "<projectDescription><name>live_act [LIVE_PROJ_88]</name></projectDescription>",
    )
    .unwrap();

    // 1. ln_connect
    let res = execute_tool(
        "ln_connect",
        &json!({
            "endpoint": endpoint,
            "access_token": "tok-mcp",
            "workspace": dir.path().to_string_lossy()
        }),
    )
    .await;
    assert_eq!(res["isError"], false, "ln_connect failed: {:?}", res);

    // 2. ln_explore_projects (NO mock flag -> hits stateful JCA server)
    let res = execute_tool(
        "ln_explore_projects",
        &json!({
            "endpoint": endpoint,
            "access_token": "tok-mcp",
            "workspace": dir.path().to_string_lossy()
        }),
    )
    .await;
    assert_eq!(res["isError"], false, "ln_explore_projects failed: {:?}", res);
    let txt = res["content"][0]["text"].as_str().unwrap();
    assert!(txt.contains("LIVE_PROJ_88"), "Expected LIVE_PROJ_88 from live mock JCA, got: {}", txt);

    // 3. ln_explore_activities
    let res = execute_tool(
        "ln_explore_activities",
        &json!({
            "project": "LIVE_PROJ_88",
            "endpoint": endpoint,
            "access_token": "tok-mcp",
            "workspace": dir.path().to_string_lossy()
        }),
    )
    .await;
    assert_eq!(res["isError"], false, "ln_explore_activities failed: {:?}", res);
    let txt = res["content"][0]["text"].as_str().unwrap();
    assert!(txt.contains("LIVE_TASK_99"), "Expected LIVE_TASK_99, got: {}", txt);

    // 4. ln_adhoc_compile
    let res = execute_tool(
        "ln_adhoc_compile",
        &json!({
            "package_code": "tx",
            "source_code": "function extern void ok() {}",
            "endpoint": endpoint,
            "access_token": "tok-mcp",
            "workspace": dir.path().to_string_lossy()
        }),
    )
    .await;
    assert_eq!(res["isError"], false, "ln_adhoc_compile failed: {:?}", res);

    // 5. ln_version_diff (list_revisions)
    let res = execute_tool(
        "ln_version_diff",
        &json!({
            "action": "list_revisions",
            "comp_type": "table",
            "comp_name": "tcibd001",
            "project": "LIVE_PROJ_88",
            "endpoint": endpoint,
            "access_token": "tok-mcp",
            "workspace": dir.path().to_string_lossy()
        }),
    )
    .await;
    assert_eq!(res["isError"], false, "ln_version_diff failed: {:?}", res);

    let st = state.lock().unwrap();
    assert!(!st.non_numeric_conid_seen, "JCA server rejected non-numeric conid");
    assert!(st.bde_calls.iter().any(|b| b == "SoftwareProject.List"));
    assert!(st.bde_calls.iter().any(|b| b == "FglStudio.compileSource"));
    assert!(st.disconnects >= 1, "Expected cleanup disconnect calls");
}

#[test]
fn test_mcp_stdio_child_process_roundtrip() {
    let mut child = Command::new(env!("CARGO_BIN_EXE_skill-ln"))
        .arg("mcp-stdio")
        .stdin(Stdio::piped())
        .stdout(Stdio::piped())
        .stderr(Stdio::piped())
        .spawn()
        .expect("Failed to spawn skill-ln mcp-stdio");

    let reqs = concat!(
        r#"{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","clientInfo":{"name":"roundtrip","version":"1.0"}}}"#,
        "\n",
        r#"{"jsonrpc":"2.0","id":2,"method":"tools/list","params":{}}"#,
        "\n",
        r#"{"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"ln_list_environments","arguments":{}}}"#,
        "\n"
    );

    {
        let stdin = child.stdin.as_mut().unwrap();
        stdin.write_all(reqs.as_bytes()).unwrap();
    }
    let output = child.wait_with_output().unwrap();
    assert!(output.status.success(), "mcp-stdio exited non-zero: {}", String::from_utf8_lossy(&output.stderr));

    let stdout_str = String::from_utf8_lossy(&output.stdout);
    let lines: Vec<serde_json::Value> = stdout_str
        .lines()
        .filter(|l| !l.trim().is_empty())
        .map(|l| serde_json::from_str(l).expect("valid json-rpc response line"))
        .collect();
    assert_eq!(lines.len(), 3, "Expected 3 responses, got: {}", stdout_str);
    assert_eq!(lines[0]["result"]["serverInfo"]["name"], "infor-ln-studio-mcp");
    assert_eq!(lines[1]["result"]["tools"].as_array().unwrap().len(), 25);
    assert_eq!(lines[2]["result"]["isError"], false);
}
