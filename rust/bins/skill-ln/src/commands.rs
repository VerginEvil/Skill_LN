use std::path::{Path, PathBuf};
use std::time::Duration;
use serde_json::json;

use ln_model::generators::{
    additional::{generate_additional_xml, AdditionalFileSpec},
    business_object::{generate_business_object_xml, BusinessObjectSpec},
    domain::{generate_domain_xml, DomainSpec},
    function::{generate_function_xml, FunctionSpec},
    label::generate_label_xml,
    library::{generate_library_xml, LibrarySpec},
    menu::{generate_menu_xml, MenuSpec},
    message::{generate_message_xml, MessageSpec},
    question::{generate_question_xml, QuestionSpec},
    report::{generate_report_xml, ReportSpec},
    session::{generate_session_xml, SessionSpec},
    table::{generate_table_xml, TableSpec},
};
use ln_model::path_resolver::{resolve_tde_relative_path, split_component_name};
use ln_scm::activity::{
    bootstrap_local_activity, clean_activity_components, clean_remote_activity,
    create_remote_activity, get_remote_activity_details, list_remote_activities,
    move_activity_components, open_remote_activity, ComponentRef, CreateActivityOptions,
};
use ln_scm::build::{compile_component, deploy_test, prepare_end_activity};
use ln_scm::code_intel::{
    compile_source_adhoc, get_call_hierarchy, get_related_script_components, open_declaration,
    search_server_pattern,
};
use ln_scm::context::{ActivityDotProject, WorkspaceContext};
use ln_scm::explorer::{
    browse_components, clone_component, get_component, inspect_component, sync_reference,
};
use ln_scm::project::{
    get_software_project_details, list_applications, list_software_projects, show_application,
};
use ln_scm::revision_diff::{
    diff_component, generate_report_on_server, list_component_revisions,
};
use ln_scm::scm_engine::{
    checkin_activity, checkin_component, checkout_activity, checkout_component,
    discover_dirty_components, is_extension_component, segregate_extension_components,
    uncheckout_component,
};

use crate::cli::Commands;

pub(crate) type DynErr = Box<dyn std::error::Error + Send + Sync>;

pub(crate) fn infer_app_and_version(act_dir: &Path) -> (String, String) {
    if let Ok(meta) = ActivityDotProject::from_activity_dir(act_dir) {
        let app = if meta.project_name.is_empty() {
            "EXTce01108".to_string()
        } else {
            meta.project_name
        };
        let ver = if meta.application_release.is_empty() {
            "B61O_a_ext".to_string()
        } else {
            meta.application_release
        };
        return (app, ver);
    }
    ("EXTce01108".to_string(), "B61O_a_ext".to_string())
}

pub(crate) fn write_generated_tde_file(
    act_dir: &Path,
    comp_type: &str,
    code: &str,
    ext: &str,
    xml: &str,
) -> Result<PathBuf, DynErr> {
    let rel = resolve_tde_relative_path(comp_type, code, ext)?;
    let full = act_dir.join(&rel);
    if let Some(p) = full.parent() {
        std::fs::create_dir_all(p)?;
    }
    std::fs::write(&full, xml)?;

    let admin_path = act_dir.join(".admin");
    if admin_path.exists() {
        let mut admin = ln_eclipse_compat::admin::AdminFile::load_from_path(&admin_path)?;
        let norm = rel.to_string_lossy().replace('\\', "/");
        admin.after_create(&norm);
        admin.save_to_path(&admin_path)?;
    }
    Ok(full)
}

fn merge_spec_defaults(
    code: &str,
    desc: &str,
    spec_val: Option<&serde_json::Value>,
) -> serde_json::Value {
    let mut map = match spec_val {
        Some(serde_json::Value::Object(m)) => m.clone(),
        _ => serde_json::Map::new(),
    };
    map.entry("code".to_string())
        .or_insert_with(|| serde_json::Value::String(code.to_string()));
    map.entry("name".to_string())
        .or_insert_with(|| serde_json::Value::String(code.to_string()));
    map.entry("description".to_string())
        .or_insert_with(|| serde_json::Value::String(desc.to_string()));
    serde_json::Value::Object(map)
}

/// Generates a Single-XML TDE component for any of the 12 component types and optionally writes + registers `.admin`.
pub(crate) fn create_single_xml_component(
    act_dir: &Path,
    comp_type: &str,
    code: &str,
    desc: &str,
    spec_val: Option<&serde_json::Value>,
    dry_run: bool,
) -> Result<(PathBuf, String, String), DynErr> {
    let norm_type = match comp_type.trim().to_lowercase().as_str() {
        "bod" | "bus" => "businessobject",
        other => other,
    }
    .to_string();
    let (app, ver) = infer_app_and_version(act_dir);
    let merged = merge_spec_defaults(code, desc, spec_val);

    let (ext, xml) = match norm_type.as_str() {
        "table" => {
            let spec: TableSpec = serde_json::from_value(merged)?;
            (".tbl", generate_table_xml(&spec, &app, &ver, None, None))
        }
        "session" => {
            let spec: SessionSpec = serde_json::from_value(merged)?;
            (".ses", generate_session_xml(&spec, &app, &ver, None, None))
        }
        "domain" => {
            let spec: DomainSpec = serde_json::from_value(merged)?;
            (".dmn", generate_domain_xml(&spec, &ver, &app))
        }
        "library" => {
            let spec: LibrarySpec = serde_json::from_value(merged)?;
            (".lib", generate_library_xml(&spec, &app, &ver, None))
        }
        "menu" => {
            let spec: MenuSpec = serde_json::from_value(merged)?;
            (".mnu", generate_menu_xml(&spec, &app, &ver, None))
        }
        "label" => {
            let len = merged.get("length").and_then(|v| v.as_u64()).map(|n| n as usize);
            (".lbl", generate_label_xml(code, desc, &ver, &app, len, None))
        }
        "message" => {
            let spec: MessageSpec = serde_json::from_value(merged)?;
            (".msg", generate_message_xml(&spec, &app, &ver))
        }
        "question" => {
            let spec: QuestionSpec = serde_json::from_value(merged)?;
            (".qst", generate_question_xml(&spec, &app, &ver))
        }
        "function" => {
            let spec: FunctionSpec = serde_json::from_value(merged)?;
            (".fnc", generate_function_xml(&spec, &app, &ver))
        }
        "additional" => {
            let spec: AdditionalFileSpec = serde_json::from_value(merged)?;
            (".add", generate_additional_xml(&spec, &app, &ver))
        }
        "report" => {
            let spec: ReportSpec = serde_json::from_value(merged)?;
            (".rpt", generate_report_xml(&spec, &app, &ver, None))
        }
        "businessobject" => {
            let spec: BusinessObjectSpec = serde_json::from_value(merged)?;
            (".bus", generate_business_object_xml(&spec, &app, &ver, None))
        }
        other => {
            return Err(format!("Unsupported component type: '{}'", other).into());
        }
    };

    let rel = resolve_tde_relative_path(&norm_type, code, ext)?;
    let rel_str = rel.to_string_lossy().replace('\\', "/");
    let full = if dry_run {
        act_dir.join(&rel)
    } else {
        write_generated_tde_file(act_dir, &norm_type, code, ext, &xml)?
    };
    Ok((full, rel_str, xml))
}

pub(crate) async fn resolve_ctx_and_client(
    workspace: Option<&Path>,
    activity: Option<&Path>,
) -> Result<(WorkspaceContext, ln_jca::client::HttpClient), DynErr> {
    let ctx = WorkspaceContext::discover(workspace, activity)?;
    let client = ctx.build_authenticated_client().await?;
    Ok((ctx, client))
}

pub(crate) fn resolve_activity_path(
    ctx: &WorkspaceContext,
    activity_arg: Option<&str>,
    project_arg: Option<&str>,
) -> (Option<PathBuf>, String, String) {
    let mut act_path: Option<PathBuf> = None;
    let mut meta: Option<ActivityDotProject> = None;

    if let Some(a) = activity_arg.filter(|s| !s.trim().is_empty()) {
        let direct = PathBuf::from(a);
        if direct.exists() && direct.is_dir() {
            meta = ActivityDotProject::from_activity_dir(&direct).ok();
            act_path = Some(direct);
        } else if let Ok((p, m)) = ctx.resolve_activity(Some(a)) {
            meta = Some(m);
            act_path = Some(p);
        }
    }

    if act_path.is_none() {
        if let Some(def) = &ctx.default_activity_dir {
            meta = ActivityDotProject::from_activity_dir(def).ok();
            act_path = Some(def.clone());
        }
    }

    let project_name = project_arg
        .filter(|s| !s.trim().is_empty())
        .map(|s| s.to_string())
        .or_else(|| meta.as_ref().map(|m| m.project_name.clone()).filter(|s| !s.is_empty()))
        .unwrap_or_else(|| "EXTce01108".to_string());

    let dev_cp = meta
        .as_ref()
        .map(|m| m.dev_repo_address.clone())
        .filter(|s| !s.is_empty())
        .unwrap_or_else(|| format!("{project_name}_dev"));

    (act_path, project_name, dev_cp)
}

fn parse_component_refs(raw: &str) -> Vec<ComponentRef> {
    raw.split(',')
        .map(|s| s.trim())
        .filter(|s| !s.is_empty())
        .map(|item| {
            if let Some((ct, name)) = item.split_once(':') {
                ComponentRef {
                    comp_type: ct.trim().to_lowercase(),
                    name: name.trim().to_string(),
                }
            } else {
                let comp_type = if item.contains("m0") {
                    "session"
                } else if item.contains("dll") {
                    "library"
                } else if item.contains('.') {
                    "domain"
                } else {
                    "table"
                };
                ComponentRef {
                    comp_type: comp_type.to_string(),
                    name: item.to_string(),
                }
            }
        })
        .collect()
}

pub async fn execute_command(cmd: Commands) -> Result<(), DynErr> {
    match cmd {
        Commands::Workspace { list: _, activities } => {
            println!("=== Infor LN Customer Workspaces ===");
            let mut roots = Vec::new();
            if let Ok(ws_env) = std::env::var("LN_WORKSPACE") {
                let p = PathBuf::from(ws_env);
                if p.exists() {
                    roots.push(p);
                }
            }
            if let Some(docs) = dirs::document_dir() {
                let ws_base = docs.join("workspace_lnstudio");
                if ws_base.exists() {
                    if let Ok(entries) = std::fs::read_dir(&ws_base) {
                        for e in entries.flatten() {
                            let p = e.path();
                            if p.is_dir() && p.join(".metadata").exists() && !roots.contains(&p) {
                                roots.push(p);
                            }
                        }
                    }
                }
            }
            if roots.is_empty() {
                if let Ok(ctx) = WorkspaceContext::discover(None, None) {
                    roots.push(ctx.workspace_dir);
                }
            }
            for ws in &roots {
                println!("  - Workspace: {} ({})", ws.file_name().unwrap_or_default().to_string_lossy(), ws.display());
                if activities {
                    if let Ok(entries) = std::fs::read_dir(ws) {
                        for e in entries.flatten() {
                            let p = e.path();
                            if p.is_dir() && p.join(".project").exists() {
                                println!("      * Activity: {}", e.file_name().to_string_lossy());
                            }
                        }
                    }
                }
            }
            if roots.is_empty() {
                println!("  (no Eclipse LN Studio workspaces discovered; set LN_WORKSPACE)");
            }
        }

        Commands::Environments { workspace_root } => {
            let ws_override = workspace_root.as_deref().map(Path::new);
            let ctx = WorkspaceContext::discover(ws_override, None)?;
            let settings_dir = ctx
                .workspace_dir
                .join(".metadata/.plugins/org.eclipse.core.runtime/.settings");
            let conn_file = settings_dir.join("com.infor.erpln.jca.connectivity.prefs");
            let conns = ln_auth::read_connectivity_prefs(&conn_file).unwrap_or_default();
            let auth_rep = ln_auth::check_auth_status(&ctx.env_name, None, None);

            println!("=== Configured Environments ===");
            println!("  Environment: {}", ctx.env_name);
            println!("  Endpoint:    {}", ctx.endpoint_url);
            println!("  Company:     {}", ctx.company);
            println!("  TokenState:  {}", auth_rep.status);
            for (name, props) in conns {
                let st = props.get("State").map(|s| s.as_str()).unwrap_or("");
                println!("  - Connection: {} [{}]", name, st);
            }
        }

        Commands::Login {
            workspace,
            ionapi,
            status,
            check_only,
            json: is_json,
            register_protocol,
        } => {
            if register_protocol {
                #[cfg(target_os = "windows")]
                let ok = std::process::Command::new("reg")
                    .args(["add", r"HKCU\Software\Classes\oob", "/ve", "/d", "URL:oob Protocol", "/f"])
                    .status()
                    .map_or(false, |s| s.success());
                #[cfg(not(target_os = "windows"))]
                let ok = true;

                if is_json {
                    println!("{}", json!({ "status": if ok { "success" } else { "error" }, "protocol_registered": ok }));
                } else if ok {
                    println!("[SUCCESS] Registered oob:// protocol handler in Windows Registry");
                } else {
                    eprintln!("[ERROR] Failed to register oob:// protocol handler");
                }
                return Ok(());
            }

            let ws = workspace.as_deref().unwrap_or("SCS_TST");
            let home = dirs::home_dir().unwrap_or_else(|| PathBuf::from("."));
            let tok_dir = home.join(".ln_studio").join("tokens");
            let tok_mgr = ln_auth::OAuth2TokenManager::new(Some(tok_dir.clone()));

            if status || check_only {
                let st = tok_mgr.check_token_status(ws);
                let is_valid = matches!(st, ln_auth::TokenStatus::Valid { .. });
                let exp = match st {
                    ln_auth::TokenStatus::Valid { expires_in, .. } => expires_in,
                    ln_auth::TokenStatus::NeedsRefresh { expires_in, .. } => expires_in,
                    ln_auth::TokenStatus::Expired { expires_in } => expires_in,
                    ln_auth::TokenStatus::Missing => 0.0,
                };
                let st_name = match st {
                    ln_auth::TokenStatus::Valid { .. } => "valid",
                    ln_auth::TokenStatus::NeedsRefresh { .. } => "needs_refresh",
                    ln_auth::TokenStatus::Expired { .. } => "expired",
                    ln_auth::TokenStatus::Missing => "missing",
                };

                if is_json {
                    println!("{}", json!({ "status": st_name, "valid": is_valid, "expires_in": exp }));
                } else {
                    println!("Auth Status for '{}':", ws);
                    println!("  Valid: {}", is_valid);
                    println!("  Expires in: {}s", exp);
                    println!("  Status: {}", st_name);
                }
                return Ok(());
            }

            if let Some(ionapi_path) = ionapi {
                let cfg = ln_auth::IonapiConfig::load_from_path(Path::new(&ionapi_path))?;
                if let Some(cached) = tok_mgr.load_token(ws) {
                    if let Some(rt) = cached.refresh_token {
                        if let Ok(new_tok) = tok_mgr.refresh_access_token(&cfg, &rt).await {
                            tok_mgr.save_token(ws, new_tok)?;
                            if is_json {
                                println!("{}", json!({ "workspace": ws, "status": "refreshed" }));
                            } else {
                                println!("[SUCCESS] Refreshed OAuth2 token for '{}'.", ws);
                            }
                            return Ok(());
                        }
                    }
                }
                if cfg.saak.is_some() && cfg.sask.is_some() {
                    let tok = tok_mgr.acquire_service_account_token(&cfg).await?;
                    tok_mgr.save_token(ws, tok)?;
                    if is_json {
                        println!("{}", json!({ "workspace": ws, "status": "authenticated" }));
                    } else {
                        println!("[SUCCESS] Acquired service account OAuth2 token for '{}'.", ws);
                    }
                    return Ok(());
                }
                let auth_url = tok_mgr.build_authorization_url(&cfg, None, None);
                let banner = ln_auth::format_auth_alert_banner(ws, Some(&auth_url));
                return Err(banner.into());
            }

            let rep = ln_auth::check_auth_status(ws, Some(tok_dir), None);
            if rep.access_token.is_some() {
                if is_json {
                    println!("{}", json!({ "workspace": ws, "status": rep.status, "expires_in": rep.expires_in }));
                } else {
                    println!("[AUTH] Workspace '{}' token valid ({:?}s remaining).", ws, rep.expires_in);
                }
            } else if let Some(banner) = rep.alert_banner {
                return Err(banner.into());
            }
        }

        Commands::Connect { ionapi, workspace, manual_auth: _ } => {
            let ws = workspace.clone().unwrap_or_else(|| "SCS_TST".to_string());
            let path = PathBuf::from(&ionapi);
            if !path.exists() {
                return Err(format!(".ionapi file not found at: {}", ionapi).into());
            }
            let cfg = ln_auth::IonapiConfig::load_from_path(&path)?;
            let home = dirs::home_dir().unwrap_or_else(|| PathBuf::from("."));
            let prefs_path = home.join(".ln_studio").join("com.infor.erpln.jca.connectivity.cloudenv.prefs");
            ln_auth::sync_cloudenv_prefs(&prefs_path, &ws, &cfg)?;

            if let Ok(ctx) = WorkspaceContext::discover(workspace.as_deref().map(Path::new), None) {
                let conn_prefs = ctx
                    .workspace_dir
                    .join(".metadata/.plugins/org.eclipse.core.runtime/.settings/com.infor.erpln.jca.connectivity.prefs");
                if conn_prefs.exists() {
                    let _ = ln_auth::sync_connectivity_prefs(&conn_prefs, &ws, &cfg, None);
                }
                if std::env::var("LN_JCA_ENDPOINT").is_ok() {
                    let started = std::time::Instant::now();
                    let client = ctx.build_authenticated_client().await?;
                    let resp = client.connect(&ln_jca::client::ConnectOptions {
                        company: Some(ctx.company.clone()),
                        ..Default::default()
                    }).await?;
                    let ping_res = client.ping().await;
                    let latency_ms = started.elapsed().as_millis();
                    let _ = client.disconnect_all().await;
                    ping_res?;
                    println!(
                        "[SUCCESS] Connected & verified JCA ping (conid={}, latency={}ms) for '{}'.",
                        resp.conid, latency_ms, ws
                    );
                    return Ok(());
                }
            }
            println!("[SUCCESS] Imported .ionapi and synchronized preferences for workspace '{}'.", ws);
        }

        Commands::Daemon { status, stop, restart, token: _ } => {
            let ws_dir = WorkspaceContext::discover(None, None)
                .ok()
                .map(|c| c.workspace_dir);
            let client = ln_daemon::DaemonClient::new(ws_dir.as_deref());

            if stop {
                if client.get_info().is_ok() {
                    let _ = client.send_rpc("shutdown", json!({}), Duration::from_secs(2)).await;
                }
                let reg_file = ln_daemon::get_daemon_reg_file(ws_dir.as_deref());
                if reg_file.exists() {
                    let _ = std::fs::remove_file(&reg_file);
                }
                println!("[DAEMON] Stopped Single-Leader daemon.");
            } else if restart {
                if client.get_info().is_ok() {
                    let _ = client.send_rpc("shutdown", json!({}), Duration::from_secs(2)).await;
                }
                println!("[DAEMON] Single-Leader daemon reset; next RPC call starts a fresh leader.");
            } else {
                let _ = status;
                match client.get_info() {
                    Ok(info) => {
                        let alive = client.send_rpc("ping", json!({}), Duration::from_secs(2)).await.is_ok();
                        println!("=== Single-Leader Daemon Status ===");
                        println!("  Running:   {}", alive);
                        println!("  PID:       {}", info.pid);
                        println!("  Port:      {}", info.port);
                        println!("  Workspace: {}", info.workspace);
                    }
                    Err(e) => {
                        println!("[DAEMON] Inactive ({})", e);
                    }
                }
            }
        }

        Commands::Project { app, project } => {
            let (_ctx, client) = resolve_ctx_and_client(None, None).await?;
            let res: Result<(), DynErr> = async {
                if let Some(p) = project {
                    let det = get_software_project_details(&client, &p, None).await?;
                    println!("=== Software Project '{}' ===", det.project_name);
                    println!("  Description: {}", det.project_description);
                    println!("  VRC:         {}", det.project_version_id);
                    println!("  DevRepo:     {}", det.development_repository_address);
                } else if let Some(a) = app {
                    let det = show_application(&client, &a).await?;
                    println!("=== Application '{}' (release {}) ===", det.name, det.release);
                    println!("  Packages: {:?}", det.packages);
                } else {
                    let apps = list_applications(&client).await?;
                    println!("=== Infor LN Applications ===");
                    for a in &apps {
                        println!("  - {} ({}) - {}", a.name, a.release, a.description);
                    }
                    let projs = list_software_projects(&client).await?;
                    println!("=== Infor LN Software Projects ===");
                    for p in &projs {
                        println!("  - {} [{}] ({})", p.name, p.status, p.description);
                    }
                }
                Ok(())
            }
            .await;
            let _ = client.disconnect_all().await;
            res?;
        }

        Commands::ProjectInfo { project } => {
            let (_ctx, client) = resolve_ctx_and_client(None, None).await?;
            let res: Result<(), DynErr> = async {
                let det = get_software_project_details(&client, &project, None).await?;
                println!("=== Software Project Details ===");
                println!("  Project:     {}", det.project_name);
                println!("  Description: {}", det.project_description);
                println!("  Base VRC:    {}", det.project_version_id);
                println!("  Dev Env:     {}", det.development_environment);
                println!("  Dev Repo:    {}", det.development_repository_address);
                println!("  RT Repo:     {}", det.runtime_repository_address);
                println!("  Packages:    {:?}", det.packages);
                println!("  Tasks:       {}", det.tasks.len());
                Ok(())
            }
            .await;
            let _ = client.disconnect_all().await;
            res?;
        }

        Commands::Activity { project, activity } => {
            let (_ctx, client) = resolve_ctx_and_client(None, None).await?;
            let res: Result<(), DynErr> = async {
                if let Some(act) = activity {
                    if let Some(t) = get_remote_activity_details(&client, &project, &act).await? {
                        println!("=== Activity '{}' ({}) ===", t.task_name, t.task_status);
                        println!("  LabelUUID:   {}", t.label_uuid);
                        println!("  Description: {}", t.task_description);
                        println!("  AssignedTo:  {}", t.assigned_to);
                    } else {
                        return Err(format!("Activity '{}' not found in project '{}'", act, project).into());
                    }
                } else {
                    let list = list_remote_activities(&client, &project).await?;
                    println!("=== Activities under Project '{}' ===", project);
                    for t in list {
                        println!("  - {} [{}] ({}) label={}", t.task_name, t.task_status, t.assigned_to, t.label_uuid);
                    }
                }
                Ok(())
            }
            .await;
            let _ = client.disconnect_all().await;
            res?;
        }

        Commands::NewActivity { project, task, desc, user, workspace } => {
            let ws_override = workspace.as_deref().map(Path::new);
            if let Ok((ctx, client)) = resolve_ctx_and_client(ws_override, None).await {
                let opts = CreateActivityOptions {
                    description: desc.as_deref().unwrap_or(&task),
                    assigned_to: user.as_deref().unwrap_or(""),
                    auto_open: true,
                    workspace_path: Some(&ctx.workspace_dir),
                    ..Default::default()
                };
                let res = create_remote_activity(&client, &project, &task, opts).await;
                let _ = client.disconnect_all().await;
                let created = res?;
                println!(
                    "[SUCCESS] Created remote activity '{}' under '{}' (label={}, status={}) at: {:?}",
                    created.task_name, created.project_name, created.label_uuid, created.status, created.workspace_path
                );
            } else {
                let ws = workspace.unwrap_or_else(|| ".".to_string());
                let act_path = bootstrap_local_activity(
                    Path::new(&ws),
                    &task,
                    &project,
                    "",
                    &format!("{project}_dev"),
                )?;
                println!("[SUCCESS] Bootstrapped local activity '{}' under project '{}' at: {:?}", task, project, act_path);
            }
        }

        Commands::OpenActivity { project, task, no_sync_modified, workspace } => {
            let ws_override = workspace.as_deref().map(Path::new);
            let (ctx, client) = resolve_ctx_and_client(ws_override, None).await?;
            let res = open_remote_activity(
                &client,
                &project,
                &task,
                Some(&ctx.workspace_dir),
                !no_sync_modified,
            )
            .await;
            let _ = client.disconnect_all().await;
            let opened = res?;
            println!(
                "[SUCCESS] Opened activity '{}' under '{}' (label={}, modified={}) at: {:?}",
                opened.task_name, opened.project_name, opened.label_uuid, opened.modified_components.len(), opened.workspace_path
            );
        }

        Commands::CleanActivity { project, task } => {
            let (_ctx, client) = resolve_ctx_and_client(None, None).await?;
            let res = clean_remote_activity(&client, &project, &task, None, false).await;
            let _ = client.disconnect_all().await;
            let ok = res?;
            println!("[SUCCESS] Cleaned activity '{}' under project '{}' (result={}).", task, project, ok);
        }

        Commands::MoveComponents { source_activity, target_task, components } => {
            let act_dir = PathBuf::from(&source_activity);
            let (ctx, client) = resolve_ctx_and_client(None, Some(&act_dir)).await?;
            let (src_opt, proj_name, dev_cp) = resolve_activity_path(&ctx, Some(&source_activity), None);
            let src_dir = src_opt.ok_or("Source activity directory could not be resolved")?;
            let meta = ActivityDotProject::from_activity_dir(&src_dir).ok();
            let base_vrc = meta
                .as_ref()
                .map(|m| m.application_release.clone())
                .filter(|s| !s.is_empty())
                .unwrap_or_else(|| "B61O_a_ext".to_string());
            let refs = parse_component_refs(&components);
            let res: Result<(), DynErr> = async {
                let target_details = get_remote_activity_details(&client, &proj_name, &target_task)
                    .await?
                    .ok_or_else(|| format!("Target task '{}' not found in project '{}'", target_task, proj_name))?;
                let mv = move_activity_components(
                    &client,
                    &refs,
                    &src_dir,
                    &target_task,
                    &target_details.label_uuid,
                    &base_vrc,
                    &dev_cp,
                    None,
                )
                .await?;
                println!("[SUCCESS] Moved {} component(s) to '{}' (ok={}).", mv.moved_components, mv.target_task, mv.success);
                Ok(())
            }
            .await;
            let _ = client.disconnect_all().await;
            res?;
        }

        Commands::CleanComponents { activity, components } => {
            let act_path = PathBuf::from(&activity);
            let (ctx, client) = resolve_ctx_and_client(None, Some(&act_path)).await?;
            let (act_opt, _, _) = resolve_activity_path(&ctx, Some(&activity), None);
            let dir = act_opt.ok_or("Activity directory could not be resolved")?;
            let refs = parse_component_refs(&components);
            let res = clean_activity_components(&client, &refs, &dir).await;
            let _ = client.disconnect_all().await;
            let clean_res = res?;
            println!("[SUCCESS] Cleaned {} component(s) from '{}' (ok={}).", clean_res.cleaned_components, dir.display(), clean_res.success);
        }

        Commands::Explorer { comp_type, filter, project, workspace } => {
            let ws_p = workspace.as_deref().map(Path::new);
            let (ctx, client) = resolve_ctx_and_client(ws_p, None).await?;
            let (_, proj_name, dev_cp) = resolve_activity_path(&ctx, None, project.as_deref());
            let filt = filter.as_deref().unwrap_or("");
            let pkg: String = filt.chars().take(2).take_while(|c| c.is_ascii_alphabetic()).collect();
            let res = browse_components(&client, &pkg, &comp_type, filt, &dev_cp).await;
            let _ = client.disconnect_all().await;
            let items = res?;
            println!("=== Component Explorer ({}) in '{}' [count={}] ===", comp_type, proj_name, items.len());
            for it in items {
                println!("  - {} [v={}] co={} {}", it.name, it.version_id, it.is_checked_out, it.description);
            }
        }

        Commands::GetComponent { comp_type, name, inspect, export_script, activity, project, workspace } => {
            let ws_p = workspace.as_deref().map(Path::new);
            let act_p = activity.as_deref().map(Path::new);
            let (ctx, client) = resolve_ctx_and_client(ws_p, act_p).await?;
            let (act_opt, proj_name, dev_cp) = resolve_activity_path(&ctx, activity.as_deref(), project.as_deref());
            let dd_cache = ctx.workspace_dir.join(".ln_dd_cache.json");

            let res: Result<(), DynErr> = async {
                if inspect {
                    let info = inspect_component(&client, &comp_type, &name, &dev_cp, Some(&dd_cache), None, None).await?;
                    println!("=== Inspected Component {}:{} ({}) ===", info.comp_type, info.name, info.description);
                    println!("  Package/Module: {}/{} | Fields: {} | Script Bytes: {}", info.package, info.module, info.fields.len(), info.script.len());
                    if let Some(out) = export_script {
                        let out_p = PathBuf::from(&out);
                        if let Some(p) = out_p.parent() {
                            std::fs::create_dir_all(p)?;
                        }
                        std::fs::write(&out_p, &info.script)?;
                    }
                } else {
                    let dir = act_opt.unwrap_or_else(|| ctx.workspace_dir.clone());
                    let exp_p = export_script.as_deref().map(Path::new);
                    let meta = ActivityDotProject::from_activity_dir(&dir).ok();
                    let label_uuid = meta.as_ref().map(|m| m.label.as_str()).filter(|s| !s.is_empty());
                    let base_vrc = meta.as_ref().map(|m| m.application_release.as_str()).filter(|s| !s.is_empty());
                    let saved = get_component(
                        &client,
                        &comp_type,
                        &name,
                        &dir,
                        true,
                        &dev_cp,
                        Some(&dd_cache),
                        label_uuid,
                        base_vrc,
                        exp_p,
                    )
                    .await?;
                    println!("[SUCCESS] Downloaded {}:{} (project={}) to: {:?}", comp_type, name, proj_name, saved);
                }
                Ok(())
            }
            .await;
            let _ = client.disconnect_all().await;
            res?;
        }

        Commands::SyncReference { comp_type, name, workspace_dir, dd_cache } => {
            let ws_p = workspace_dir.as_deref().map(Path::new);
            let (ctx, client) = resolve_ctx_and_client(ws_p, None).await?;
            let (_, _, dev_cp) = resolve_activity_path(&ctx, None, None);
            let dd_p = dd_cache.as_deref().map(Path::new);
            let res = sync_reference(&client, &comp_type, &name, &ctx.workspace_dir, dd_p, &dev_cp).await;
            let _ = client.disconnect_all().await;
            let sr = res?;
            println!("[SUCCESS] Synchronized {} {} reference(s) matching '{}' into '{}' (dd_indexed={:?}).", sr.synced_count, sr.comp_type, sr.pattern, sr.reference_dir, sr.dd_indexed);
        }

        Commands::CloneComponent { source_type, source_name, target_name, activity, target_desc: _ } => {
            let act_path = PathBuf::from(&activity);
            if source_type.eq_ignore_ascii_case("extension") || is_extension_component(&source_name) {
                return Err("Extension Modeler components cannot be cloned (ADR 0006).".into());
            }
            if let Ok((ctx, client)) = resolve_ctx_and_client(None, Some(&act_path)).await {
                let (_, _, dev_cp) = resolve_activity_path(&ctx, Some(&activity), None);
                let label_uuid = ActivityDotProject::from_activity_dir(&act_path)
                    .ok()
                    .map(|m| m.label)
                    .filter(|s| !s.is_empty());
                let res = clone_component(
                    &client,
                    &source_type,
                    &source_name,
                    &target_name,
                    &act_path,
                    true,
                    &dev_cp,
                    label_uuid.as_deref(),
                )
                .await;
                let _ = client.disconnect_all().await;
                let saved = res?;
                println!("[SUCCESS] Cloned {}:{} -> {}:{} at {:?}", source_type, source_name, source_type, target_name, saved);
            } else {
                let src_file = ln_scm::activity::find_component_file(&act_path, &source_name, &source_type)
                    .ok_or_else(|| format!("Local source component {}:{} not found in '{}' and no JCA endpoint configured", source_type, source_name, activity))?;
                let raw_xml = std::fs::read_to_string(&src_file)?;
                let (src_pkg, src_mod, _) = split_component_name(&source_name);
                let (dst_pkg, dst_mod, _) = split_component_name(&target_name);
                let cloned = ln_model::clone_component_xml(
                    &raw_xml,
                    &source_name,
                    &target_name,
                    &src_pkg,
                    &dst_pkg,
                    if src_mod.is_empty() { None } else { Some(src_mod.as_str()) },
                    if dst_mod.is_empty() { None } else { Some(dst_mod.as_str()) },
                );
                let ext = src_file.extension().and_then(|s| s.to_str()).map(|s| format!(".{s}")).unwrap_or_else(|| ".tbl".into());
                let out_path = write_generated_tde_file(&act_path, &source_type, &target_name, &ext, &cloned)?;
                println!("[SUCCESS] Cloned offline {}:{} -> {}:{} at {:?}", source_type, source_name, source_type, target_name, out_path);
            }
        }

        Commands::CheckoutComponent { comp_type, name, activity, project, workspace, comment: _ } => {
            if comp_type.eq_ignore_ascii_case("extension") || is_extension_component(&name) {
                return Err("ReadOnlyComponentError: Extension Modeler component is Read-Only Get per ADR 0006. SCM Check-Out is blocked.".into());
            }
            let act_path = PathBuf::from(&activity);
            let (ctx, client) = resolve_ctx_and_client(workspace.as_deref().map(Path::new), Some(&act_path)).await?;
            let (act_opt, proj_name, dev_cp) = resolve_activity_path(&ctx, Some(&activity), project.as_deref());
            let dir = act_opt.unwrap_or(act_path);
            let res = checkout_component(&client, &comp_type, &name, &dir, &proj_name, None, Some(&dev_cp)).await;
            let _ = client.disconnect_all().await;
            let co = res?;
            println!("[SUCCESS] Checked out {}:{} -> {:?} (status={}).", comp_type, name, co.path, co.receipt.status);
        }

        Commands::UncheckoutComponent { comp_type, name, activity, project, workspace } => {
            let act_path = PathBuf::from(&activity);
            let (ctx, client) = resolve_ctx_and_client(workspace.as_deref().map(Path::new), Some(&act_path)).await?;
            let (act_opt, proj_name, dev_cp) = resolve_activity_path(&ctx, Some(&activity), project.as_deref());
            let dir = act_opt.unwrap_or(act_path);
            let res = uncheckout_component(&client, &comp_type, &name, &dir, &proj_name, None, Some(&dev_cp)).await;
            let _ = client.disconnect_all().await;
            let receipt = res?;
            println!("[SUCCESS] Reverted check-out for {}:{} (status={}).", comp_type, name, receipt.status);
        }

        Commands::CheckinComponent { comp_type, name, activity, project, workspace, comment } => {
            if comp_type.eq_ignore_ascii_case("extension") || is_extension_component(&name) {
                return Err("ReadOnlyComponentError: Extension Modeler component is Read-Only Get per ADR 0006. SCM Check-In is blocked.".into());
            }
            let act_path = PathBuf::from(&activity);
            let (ctx, client) = resolve_ctx_and_client(workspace.as_deref().map(Path::new), Some(&act_path)).await?;
            let (act_opt, proj_name, dev_cp) = resolve_activity_path(&ctx, Some(&activity), project.as_deref());
            let dir = act_opt.unwrap_or(act_path);
            let cmt = comment.as_deref().unwrap_or("Checked in by skill-ln");
            let res = checkin_component(&client, &comp_type, &name, &dir, &proj_name, cmt, None, Some(&dev_cp)).await;
            let _ = client.disconnect_all().await;
            let receipt = res?;
            println!("[SUCCESS] Checked in {}:{} from '{}' (version={}).", comp_type, name, dir.display(), receipt.version_id);
        }

        Commands::CheckoutActivity { activity, project, workspace } => {
            let act_path = PathBuf::from(&activity);
            let (ctx, client) = resolve_ctx_and_client(workspace.as_deref().map(Path::new), Some(&act_path)).await?;
            let (act_opt, proj_name, dev_cp) = resolve_activity_path(&ctx, Some(&activity), project.as_deref());
            let dir = act_opt.unwrap_or(act_path);
            let res = checkout_activity(&client, &dir, &proj_name, None, Some(&dev_cp), None).await;
            let _ = client.disconnect_all().await;
            let batch = res?;
            println!("[SUCCESS] Checked out {} component(s) in '{}' (extensions segregated={}).", batch.processed_count, batch.activity, batch.segregated_extensions.len());
            if !batch.extension_guide_markdown.is_empty() {
                println!("{}", batch.extension_guide_markdown);
            }
        }

        Commands::CheckinActivity { activity, project, workspace, comment } => {
            let act_path = PathBuf::from(&activity);
            let (ctx, client) = resolve_ctx_and_client(workspace.as_deref().map(Path::new), Some(&act_path)).await?;
            let (act_opt, proj_name, dev_cp) = resolve_activity_path(&ctx, Some(&activity), project.as_deref());
            let dir = act_opt.unwrap_or(act_path);
            let cmt = comment.as_deref().unwrap_or("Batch check-in via skill-ln");
            let res = checkin_activity(&client, &dir, &proj_name, cmt, None, Some(&dev_cp), None).await;
            let _ = client.disconnect_all().await;
            let batch = res?;
            println!("[SUCCESS] Checked in {} component(s) in '{}' (extensions segregated={}).", batch.processed_count, batch.activity, batch.segregated_extensions.len());
            if !batch.extension_guide_markdown.is_empty() {
                println!("{}", batch.extension_guide_markdown);
            }
        }

        Commands::EndActivity { task, project } => {
            return Err(format!(
                "PreCommitBoundaryError: Direct end-activity for task '{}' under project '{}' is physically hard-blocked per ADR 0007. Delivery must be finalized in Infor LN Studio UI.",
                task, project
            ).into());
        }

        Commands::PrepareEndActivity { activity, project, workspace } => {
            let act_path = PathBuf::from(&activity);
            let (ctx, client) = resolve_ctx_and_client(workspace.as_deref().map(Path::new), Some(&act_path)).await?;
            let (act_opt, proj_name, _) = resolve_activity_path(&ctx, Some(&activity), project.as_deref());
            let dir = act_opt.unwrap_or(act_path);
            let res = prepare_end_activity(&client, &dir, &proj_name).await;
            let _ = client.disconnect_all().await;
            let prep = res?;
            println!("{}", prep.commit_summary);
        }

        Commands::CompileSource { package, source_file, code, flags } => {
            let src = if let Some(c) = code {
                c
            } else if let Some(sf) = source_file {
                std::fs::read_to_string(&sf)?
            } else {
                return Err("Either --code or --source-file must be provided".into());
            };
            let (ctx, client) = resolve_ctx_and_client(None, None).await?;
            let (act_opt, proj_name, _) = resolve_activity_path(&ctx, None, None);
            let res = compile_source_adhoc(&client, &package, &src, flags.as_deref().unwrap_or(""), &proj_name, act_opt.as_deref()).await;
            let _ = client.disconnect_all().await;
            let comp = res?;
            println!("=== Ad-Hoc Server Compile ({}) success={} ===", comp.package_code, comp.success);
            println!("  Errors: {}, Warnings: {}", comp.errors.len(), comp.warnings.len());
            for d in &comp.diagnostics {
                println!("  [{}] line {}: {}", d.severity, d.line, d.message);
            }
        }

        Commands::SearchServer { pattern, package } => {
            let (ctx, client) = resolve_ctx_and_client(None, None).await?;
            let (act_opt, proj_name, _) = resolve_activity_path(&ctx, None, None);
            let res = search_server_pattern(&client, &pattern, package.as_deref().unwrap_or(""), &proj_name, act_opt.as_deref()).await;
            let _ = client.disconnect_all().await;
            let sr = res?;
            println!("=== Server Search Results ('{}', {} matches) ===", sr.pattern, sr.total_matches);
            for m in &sr.matches {
                println!("  - {}:{} (line {}): {}", m.package, m.component, m.line, m.snippet);
            }
        }

        Commands::CallHierarchy { source_file, function, mode } => {
            let (ctx, client) = resolve_ctx_and_client(None, None).await?;
            let (act_opt, proj_name, _) = resolve_activity_path(&ctx, None, None);
            let res = get_call_hierarchy(&client, &source_file, &function, &mode, &proj_name, act_opt.as_deref()).await;
            let _ = client.disconnect_all().await;
            let ch = res?;
            println!("=== Call Hierarchy: {} ({}, valid={}) [{}] ===", ch.function_name, ch.call_mode, ch.is_valid, ch.total_nodes);
            for n in &ch.hierarchy {
                println!("  - {} ({}) {}:{}", n.function, n.comp_type, n.source_file, n.line);
            }
        }

        Commands::OpenDeclaration { comp, comp_type, function } => {
            let (ctx, client) = resolve_ctx_and_client(None, None).await?;
            let (act_opt, proj_name, _) = resolve_activity_path(&ctx, None, None);
            let res = open_declaration(&client, &comp, &comp_type, &function, "script", &proj_name, act_opt.as_deref()).await;
            let _ = client.disconnect_all().await;
            let decl = res?;
            println!("=== Symbol Declaration (found={}) ===", decl.found);
            println!("  Function: {} -> {}:{} line {}", decl.function, decl.component_type, decl.component_code, decl.line_number);
        }

        Commands::RelatedComponents { package, source_file, code } => {
            let src = if let Some(c) = code {
                c
            } else if let Some(sf) = source_file {
                std::fs::read_to_string(&sf)?
            } else {
                String::new()
            };
            let (ctx, client) = resolve_ctx_and_client(None, None).await?;
            let (act_opt, proj_name, _) = resolve_activity_path(&ctx, None, None);
            let res = get_related_script_components(&client, &package, &src, &proj_name, act_opt.as_deref()).await;
            let _ = client.disconnect_all().await;
            let rel = res?;
            println!("=== Related Components for Package '{}' ({}) ===", rel.package_code, rel.total_components);
            for c in &rel.components {
                println!("  - {}:{} ({})", c.comp_type, c.name, c.version_id);
            }
        }

        Commands::Revisions { comp_type, name, version } => {
            let (ctx, client) = resolve_ctx_and_client(None, None).await?;
            let (act_opt, proj_name, _) = resolve_activity_path(&ctx, None, None);
            let ver = version.as_deref().unwrap_or("B61O_a_ext");
            let res = list_component_revisions(&client, &comp_type, &name, ver, &proj_name, act_opt.as_deref()).await;
            let _ = client.disconnect_all().await;
            let revs = res?;
            println!("=== Revision History for {}:{} ({} revisions) ===", revs.component_type, revs.component_name, revs.total_revisions);
            for r in &revs.revisions {
                println!("  Rev {}: {} {} {} - {}", r.number, r.date, r.time, r.author, r.comment);
            }
        }

        Commands::DiffComponent { comp_type, name, activity, revision } => {
            let act_path = PathBuf::from(&activity);
            let (ctx, client) = resolve_ctx_and_client(None, Some(&act_path)).await?;
            let (act_opt, proj_name, _) = resolve_activity_path(&ctx, Some(&activity), None);
            let dir = act_opt.unwrap_or(act_path);
            let rev_usize = revision.map(|r| r.max(0) as usize);
            let res = diff_component(&client, &comp_type, &name, &dir, None, rev_usize, &proj_name).await;
            let _ = client.disconnect_all().await;
            let d = res?;
            println!("=== Component Diff: {}:{} (rev={:?}, script_changed={}) ===", d.component_type, d.component_name, d.target_revision, d.has_script_changes);
            if !d.script_diff.is_empty() {
                println!("{}", d.script_diff);
            }
        }

        Commands::GenerateReportServer { code, table, paper_width, report_type, activity } => {
            let act_opt_p = activity.as_deref().map(Path::new);
            let (ctx, client) = resolve_ctx_and_client(None, act_opt_p).await?;
            let (act_opt, proj_name, _) = resolve_activity_path(&ctx, activity.as_deref(), None);
            let res = generate_report_on_server(
                &client,
                &code,
                &table,
                "B61O_a_ext",
                &code,
                &paper_width,
                &report_type,
                "1",
                None,
                true,
                &proj_name,
                act_opt.as_deref(),
            )
            .await;
            let _ = client.disconnect_all().await;
            let gen = res?;
            println!("[SUCCESS] Generated report '{}' at {:?} (ok={}).", gen.report_name, gen.output_file, gen.success);
        }

        Commands::Table { spec, output_dir, dry_run } => {
            let yaml_content = std::fs::read_to_string(&spec)?;
            let out_path = PathBuf::from(output_dir.unwrap_or_else(|| ".".to_string()));
            let _res = ln_model::compile_schema_to_tde(&yaml_content, &out_path, !dry_run, None)?;
            println!("[SUCCESS] Table component generation complete for: {}", spec);
        }

        Commands::Domain { spec, output_dir, dry_run } => {
            let yaml_content = std::fs::read_to_string(&spec)?;
            let out_path = PathBuf::from(output_dir.unwrap_or_else(|| ".".to_string()));
            let _res = ln_model::compile_schema_to_tde(&yaml_content, &out_path, !dry_run, None)?;
            println!("[SUCCESS] Domain component generation complete for: {}", spec);
        }

        Commands::Session { spec, output_dir, dry_run } => {
            let yaml_content = std::fs::read_to_string(&spec)?;
            let out_path = PathBuf::from(output_dir.unwrap_or_else(|| ".".to_string()));
            let _res = ln_model::compile_schema_to_tde(&yaml_content, &out_path, !dry_run, None)?;
            println!("[SUCCESS] Session component generation complete for: {}", spec);
        }

        Commands::Library { spec, output_dir, dry_run } => {
            let yaml_content = std::fs::read_to_string(&spec)?;
            let out_path = PathBuf::from(output_dir.unwrap_or_else(|| ".".to_string()));
            let _res = ln_model::compile_schema_to_tde(&yaml_content, &out_path, !dry_run, None)?;
            println!("[SUCCESS] Library component generation complete for: {}", spec);
        }

        Commands::Menu { spec, output_dir, dry_run } => {
            let yaml_content = std::fs::read_to_string(&spec)?;
            let out_path = PathBuf::from(output_dir.unwrap_or_else(|| ".".to_string()));
            let _res = ln_model::compile_schema_to_tde(&yaml_content, &out_path, !dry_run, None)?;
            println!("[SUCCESS] Menu component generation complete for: {}", spec);
        }

        Commands::Component { spec, output_dir, dry_run } => {
            let yaml_content = std::fs::read_to_string(&spec)?;
            let out_path = PathBuf::from(output_dir.unwrap_or_else(|| ".".to_string()));
            let _res = ln_model::compile_schema_to_tde(&yaml_content, &out_path, !dry_run, None)?;
            println!("[SUCCESS] Full schema component generation complete for: {}", spec);
        }

        Commands::Pipeline { spec, output_dir, auto_fix: _, skip_build: _ } => {
            let yaml_content = std::fs::read_to_string(&spec)?;
            let out_path = PathBuf::from(output_dir.unwrap_or_else(|| ".".to_string()));
            let _res = ln_model::compile_schema_to_tde(&yaml_content, &out_path, true, None)?;
            println!("[SUCCESS] Pipeline completed for '{}'.", spec);
        }

        Commands::Message { code, severity, text, activity } => {
            let act_path = PathBuf::from(&activity);
            let (app, ver) = infer_app_and_version(&act_path);
            let spec = MessageSpec {
                code: code.clone(),
                description: Some(text.clone().unwrap_or_else(|| code.clone())),
                version_id: Some(ver.clone()),
                application: Some(app.clone()),
                severity,
                text,
                language: 2,
            };
            let xml = generate_message_xml(&spec, &app, &ver);
            let saved = write_generated_tde_file(&act_path, "message", &code, ".msg", &xml)?;
            println!("[SUCCESS] Generated message Single-XML at: {:?}", saved);
        }

        Commands::Question { code, domain, text, activity } => {
            let act_path = PathBuf::from(&activity);
            let (app, ver) = infer_app_and_version(&act_path);
            let spec = QuestionSpec {
                code: code.clone(),
                description: Some(text.clone().unwrap_or_else(|| code.clone())),
                version_id: Some(ver.clone()),
                application: Some(app.clone()),
                severity: "2".to_string(),
                domain: domain.unwrap_or_else(|| "tcyesno".to_string()),
                default_answer: "yes".to_string(),
                text,
                language: 2,
            };
            let xml = generate_question_xml(&spec, &app, &ver);
            let saved = write_generated_tde_file(&act_path, "question", &code, ".qst", &xml)?;
            println!("[SUCCESS] Generated question Single-XML at: {:?}", saved);
        }

        Commands::Function { code, script_file, activity } => {
            let act_path = PathBuf::from(&activity);
            let (app, ver) = infer_app_and_version(&act_path);
            let script = match script_file {
                Some(p) => Some(std::fs::read_to_string(&p)?),
                None => None,
            };
            let spec = FunctionSpec {
                code: code.clone(),
                description: Some(code.clone()),
                version_id: Some(ver.clone()),
                application: Some(app.clone()),
                script,
            };
            let xml = generate_function_xml(&spec, &app, &ver);
            let saved = write_generated_tde_file(&act_path, "function", &code, ".fnc", &xml)?;
            println!("[SUCCESS] Generated include function Single-XML at: {:?}", saved);
        }

        Commands::Additional { code, content_file, activity } => {
            let act_path = PathBuf::from(&activity);
            let (app, ver) = infer_app_and_version(&act_path);
            let content = match content_file {
                Some(p) => Some(std::fs::read_to_string(&p)?),
                None => None,
            };
            let spec = AdditionalFileSpec {
                code: code.clone(),
                description: Some(code.clone()),
                version_id: Some(ver.clone()),
                application: Some(app.clone()),
                content,
                keyword1: None,
                keyword2: None,
                keyword3: None,
            };
            let xml = generate_additional_xml(&spec, &app, &ver);
            let saved = write_generated_tde_file(&act_path, "additional", &code, ".add", &xml)?;
            println!("[SUCCESS] Generated additional file Single-XML at: {:?}", saved);
        }

        Commands::Report { code, paper_width, activity } => {
            let act_path = PathBuf::from(&activity);
            let (app, ver) = infer_app_and_version(&act_path);
            let width = paper_width.parse::<usize>().unwrap_or(132);
            let spec = ReportSpec {
                code: code.clone(),
                description: Some(code.clone()),
                version_id: Some(ver.clone()),
                application: Some(app.clone()),
                paper_width: width,
                input_fields: Vec::new(),
                layouts: Vec::new(),
                script: None,
            };
            let xml = generate_report_xml(&spec, &app, &ver, None);
            let saved = write_generated_tde_file(&act_path, "report", &code, ".rpt", &xml)?;
            println!("[SUCCESS] Generated report Single-XML at: {:?}", saved);
        }

        Commands::Inject { source, target } => {
            let script = std::fs::read_to_string(&source)?;
            let xml = std::fs::read_to_string(&target)?;
            let updated = ln_model::inject_script(&xml, &script)?;
            std::fs::write(&target, updated)?;
            println!("[SUCCESS] Injected 4GL script from '{}' into '{}'.", source, target);
        }

        Commands::Extract { source, output } => {
            let xml = std::fs::read_to_string(&source)?;
            let script = ln_model::extract_script(&xml)
                .ok_or_else(|| "No <expression> script found in XML")?;
            std::fs::write(&output, script)?;
            println!("[SUCCESS] Extracted 4GL script from '{}' into '{}'.", source, output);
        }

        Commands::CheckScript { file_path, strict: _, json: is_json } => {
            let p = PathBuf::from(&file_path);
            let diags = ln_linter::Auditor4GL::new().audit_path(&p, None)?;

            if is_json {
                println!("{}", serde_json::to_string_pretty(&diags)?);
            } else {
                println!("=== 4GL Audit Report: {} ===", file_path);
                println!("  Violations: {}", diags.len());
                for d in &diags {
                    println!("    [{:?}] {}:{}: {} ({})", d.severity, d.file, d.line, d.message, d.code);
                }
            }
        }

        Commands::Validate { activity_path, strict, fix, json: is_json } => {
            let act = activity_path.unwrap_or_else(|| ".".to_string());
            let report = ln_model::validate_activity(Path::new(&act), strict, fix);
            if is_json {
                println!("{}", serde_json::to_string_pretty(&report)?);
            } else {
                let has_errors = report
                    .diagnostics
                    .iter()
                    .any(|d| d.severity == ln_model::validator::ValidationSeverity::Error);
                println!("=== Activity Validation Report: {} ===", act);
                println!("  Status: {}", if has_errors { "FAIL" } else { "PASS" });
                println!("  Files Scanned: {}", report.files_scanned);
                println!("  Diagnostics: {}", report.diagnostics.len());
                println!("  Repaired Items: {}", report.repaired_items.len());
            }
        }

        Commands::SyncAdmin { activity } => {
            let act_path = PathBuf::from(&activity);
            let admin_path = act_path.join(".admin");
            let mut admin = if admin_path.exists() {
                ln_eclipse_compat::admin::AdminFile::load_from_path(&admin_path)?
            } else {
                ln_eclipse_compat::admin::AdminFile::new()
            };

            let mut count = 0;
            fn scan_dir(
                dir: &Path,
                base: &Path,
                admin: &mut ln_eclipse_compat::admin::AdminFile,
                count: &mut usize,
            ) {
                if let Ok(entries) = std::fs::read_dir(dir) {
                    for e in entries.flatten() {
                        let p = e.path();
                        if p.is_dir() {
                            scan_dir(&p, base, admin, count);
                        } else if p.is_file() {
                            let rel = p.strip_prefix(base).unwrap_or(&p).to_string_lossy().to_string();
                            if ln_eclipse_compat::admin::is_managed_extension(&rel) {
                                admin.insert(ln_eclipse_compat::admin::AdministrationComponent::new(&rel));
                                *count += 1;
                            }
                        }
                    }
                }
            }
            scan_dir(&act_path, &act_path, &mut admin, &mut count);
            admin.save_to_path(&admin_path)?;
            println!("[SUCCESS] Synchronized .admin for '{}' (registered {} components).", activity, count);
        }

        Commands::Diagnose { activity, errors_only } => {
            let act_path = PathBuf::from(&activity);
            let markers_path = act_path.join(".markers");
            if markers_path.exists() {
                let mf = ln_eclipse_compat::markers::MarkersFile::load_from_path(&markers_path)?;
                println!("=== Problem Markers in '{}' ===", activity);
                for m in &mf.markers {
                    let is_err = matches!(m.severity, ln_eclipse_compat::markers::MarkerSeverity::Error);
                    if !errors_only || is_err {
                        println!("  - [{:?}] {}: {}", m.severity, m.resource_path, m.message);
                    }
                }
            } else {
                println!("[DIAGNOSE] No .markers file found in '{}'. Workspace clean.", activity);
            }
        }

        Commands::Build { activity, ui_bridge: _ } => {
            let act_path = PathBuf::from(&activity);
            let (ctx, client) = resolve_ctx_and_client(None, Some(&act_path)).await?;
            let (act_opt, proj_name, _) = resolve_activity_path(&ctx, Some(&activity), None);
            let dir = act_opt.unwrap_or(act_path);
            let discovered = discover_dirty_components(&dir);
            let (standard, extensions) = segregate_extension_components(discovered);

            let res: Result<(), DynErr> = async {
                let mut compiled_count = 0usize;
                for c in &standard {
                    let comp_res = compile_component(&client, &c.comp_type, &c.name, &proj_name, Some(&dir), true).await?;
                    compiled_count += 1;
                    if !comp_res.success {
                        return Err(format!("Compile failed for {}:{} ({} errors)", c.comp_type, c.name, comp_res.errors.len()).into());
                    }
                }
                let prep = prepare_end_activity(&client, &dir, &proj_name).await?;
                println!(
                    "[SUCCESS] JCA build completed for '{}' (compiled={}, segregated_extensions={}, server_vsc={}).",
                    prep.activity, compiled_count, extensions.len(), prep.server_valid
                );
                Ok(())
            }
            .await;
            let _ = client.disconnect_all().await;
            res?;
        }

        Commands::NewExtension { comp_type, target, output } => {
            let out_p = output.as_deref().map(Path::new);
            let saved = ln_scm::extension::new_extension(&comp_type, &target, out_p, "Skill_LN", None)?;
            println!("[SUCCESS] Scaffolded extension script at: {:?}", saved);
        }

        Commands::ImportExtension { source, output } => {
            let src_p = Path::new(&source);
            let out_p = output.as_deref().map(Path::new);
            let saved = ln_scm::extension::import_extension(src_p, out_p, None, None)?;
            println!("[SUCCESS] Imported extension script to: {:?}", saved);
        }

        Commands::ExtensionHooks { script_path, list: _, hook: _, copy: _ } => {
            let code = std::fs::read_to_string(&script_path)?;
            let hooks = ln_scm::extension::parse_extension_hooks(&code);
            println!("=== Extension Hooks in '{}' ===", script_path);
            for h in hooks {
                println!("  - Hook: {} ({} lines)", h.name, h.lines.len());
            }
        }

        Commands::DeployTest { comp_type, name, activity, mode, dry_run } => {
            let act_path = PathBuf::from(&activity);
            let (ctx, client) = resolve_ctx_and_client(None, Some(&act_path)).await?;
            let (act_opt, proj_name, _) = resolve_activity_path(&ctx, Some(&activity), None);
            let dir = act_opt.unwrap_or(act_path);
            let res = deploy_test(
                &client,
                &comp_type,
                &name,
                &dir,
                &proj_name,
                "Deploy test via skill-ln CLI",
                &mode,
                dry_run,
            )
            .await;
            let _ = client.disconnect_all().await;
            let dt = res?;
            println!("[SUCCESS] Test deployment pipeline completed for {}:{} (mode={}, dry_run={}).", comp_type, name, mode, dt.dry_run);
            println!("  Compile: {}", dt.compiled);
            println!("  VSC:     {}", dt.vsc_passed);
            println!("  CheckIn: {}", dt.checked_in);
        }

        Commands::McpSetup { client, apply } => {
            let home = dirs::home_dir().unwrap_or_else(|| PathBuf::from("."));
            let cfg = json!({
                "mcpServers": {
                    "infor-ln-studio": {
                        "command": "skill-ln",
                        "args": ["mcp-stdio"]
                    }
                }
            });

            if apply {
                let cfg_path = match client.as_str() {
                    "claude" => home.join("AppData").join("Roaming").join("Claude").join("claude_desktop_config.json"),
                    "cursor" => PathBuf::from(".cursor").join("mcp.json"),
                    "antigravity" => home.join(".gemini").join("antigravity").join("mcp").join("ln_studio.json"),
                    _ => PathBuf::from("mcp_config.json"),
                };
                if let Some(p) = cfg_path.parent() {
                    std::fs::create_dir_all(p)?;
                }
                std::fs::write(&cfg_path, serde_json::to_string_pretty(&cfg)?)?;
                println!("[SUCCESS] Registered skill-ln MCP server in '{}' config: {:?}", client, cfg_path);
            } else {
                println!("{}", serde_json::to_string_pretty(&cfg)?);
            }
        }

        Commands::McpStdio => {
            crate::mcp::run_stdio_server().await?;
        }

        Commands::Audit4gl { path, rule, json: is_json, dd_cache: _ } => {
            let p = PathBuf::from(&path);
            let diags = ln_linter::Auditor4GL::new().audit_path(&p, rule.as_deref())?;

            if is_json {
                println!("{}", serde_json::to_string_pretty(&diags)?);
            } else {
                println!("=== 4GL Audit Report: {} ===", path);
                println!("  Violations: {}", diags.len());
                for d in &diags {
                    println!("    [{:?}] {}:{}: {} ({})", d.severity, d.file, d.line, d.message, d.code);
                }
            }
        }

        Commands::FnSearch { query, category: _, limit, json: is_json } => {
            let results = ln_kb::search_functions(&query);
            if is_json {
                println!("{}", serde_json::to_string_pretty(&results)?);
            } else {
                println!("=== Function Search: '{}' (found {}) ===", query, results.len());
                for r in results.into_iter().take(limit) {
                    println!("  - {}: {} ({})", r.name, r.syntax, r.return_type);
                }
            }
        }

        Commands::DocSearch { query, limit, json: is_json } => {
            let (results, _) = ln_kb::search_docs(&query, None, None, limit);
            if is_json {
                println!("{}", serde_json::to_string_pretty(&results)?);
            } else {
                println!("=== Documentation Search: '{}' (found {}) ===", query, results.len());
                for r in results {
                    let snippet = r.hits.first().map(|h| h.snippet.as_str()).unwrap_or("");
                    println!("  - {}: {} ({})", r.rel_path, r.title, snippet);
                }
            }
        }

        Commands::VerifyStudioBuild { studio_home, json: is_json } => {
            let report = ln_verify::verify_studio_build(Path::new(&studio_home))?;
            if is_json {
                println!("{}", serde_json::to_string_pretty(&report)?);
            } else {
                println!("{}", report.summary_markdown);
            }
        }
    }

    Ok(())
}
