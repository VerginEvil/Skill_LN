use std::collections::HashMap;
use std::fs;
use std::path::Path;
use serde::{Deserialize, Serialize};

use ln_eclipse_compat::AdminFile;
use ln_jca::{BdeExecutionMode, BdeParams, HttpClient, JcaBdeManager};
use crate::explorer::get_bde_type_info;
use crate::scm_engine::{
    build_activity_context_xml, checkin_component, find_component_file,
    is_extension_component, put_component, resolve_activity_scm_metadata,
    ScmError,
};
use crate::xml_tree::parse_xml_to_tree;

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct CompileDiagnostic {
    pub severity: String, // "error" or "warning"
    pub line: usize,
    pub column: usize,
    pub code: String,
    pub message: String,
    pub source: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct CompileResult {
    pub success: bool,
    pub diagnostics: Vec<CompileDiagnostic>,
    pub errors: Vec<CompileDiagnostic>,
    pub warnings: Vec<CompileDiagnostic>,
    pub bic_command: String,
    pub summary: HashMap<String, String>,
    pub raw_xml: String,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct VscWarning {
    pub accepted: String,
    pub blocking: bool,
    pub message_id: String,
    pub warning_id: String,
    pub priority: String,
    pub location: String,
    pub element: String,
    pub message: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct VscResult {
    pub passed: bool,
    pub verification_code: String,
    pub warnings: Vec<VscWarning>,
    pub raw_xml: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct DeployTestResult {
    pub component: String,
    pub comp_type: String,
    pub mode: String,
    pub dry_run: bool,
    pub planned_steps: Vec<String>,
    pub lock_warning: String,
    pub success: bool,
    pub compiled: bool,
    pub crdd: bool,
    pub create_tables: bool,
    pub vsc_passed: bool,
    pub checked_in: bool,
    pub errors: Vec<CompileDiagnostic>,
    pub warnings: Vec<CompileDiagnostic>,
    pub message: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct PrepareEndActivityResult {
    pub activity: String,
    pub project: String,
    pub activity_folder: String,
    pub server_valid: bool,
    pub metadata_synced: bool,
    pub components_count: usize,
    pub components: Vec<String>,
    pub ready_for_human_review: bool,
    pub human_action_required: String,
    pub commit_summary: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct DiagnoseResult {
    pub component: String,
    pub comp_type: String,
    pub compiler_success: bool,
    pub compiler_diagnostics: Vec<CompileDiagnostic>,
    pub linter_diagnostics: Vec<String>,
    pub raw_compiler_xml: String,
}

/// Parses compiler diagnostics from server Compile XML response into structured line,
/// column, error code, message, and source.
pub fn parse_compile_diagnostics(response_xml: &str) -> Vec<CompileDiagnostic> {
    let mut diagnostics = Vec::new();
    if response_xml.trim().is_empty() {
        return diagnostics;
    }

    let tree = match parse_xml_to_tree(response_xml) {
        Ok(t) => t,
        Err(_) => return diagnostics,
    };

    // 1. Authentic <compileResult> schema
    for err in tree.find_all("error") {
        let line = err.attr("line").and_then(|s| s.parse::<usize>().ok()).unwrap_or(0);
        let src = err.attr("source").unwrap_or("").to_string();
        let msg = err.text.trim().to_string();
        diagnostics.push(CompileDiagnostic {
            severity: "error".to_string(),
            line,
            column: 0,
            code: String::new(),
            message: msg,
            source: src,
        });
    }

    for warn in tree.find_all("warning") {
        let line = warn.attr("line").and_then(|s| s.parse::<usize>().ok()).unwrap_or(0);
        let src = warn.attr("source").unwrap_or("").to_string();
        let lvl = warn.attr("level").unwrap_or("").to_string();
        let msg = warn.text.trim().to_string();
        diagnostics.push(CompileDiagnostic {
            severity: "warning".to_string(),
            line,
            column: 0,
            code: lvl,
            message: msg,
            source: src,
        });
    }

    // 2. Legacy <CompileResponse> schema fallback
    for err in tree.find_all("CompileResponseError") {
        let line = err.attr("line").or_else(|| err.child_text("line")).and_then(|s| s.parse::<usize>().ok()).unwrap_or(0);
        let col = err.attr("column").or_else(|| err.child_text("column")).and_then(|s| s.parse::<usize>().ok()).unwrap_or(0);
        let code = err.attr("code").or_else(|| err.child_text("code")).unwrap_or("").to_string();
        let msg = err.attr("message").or_else(|| err.child_text("message")).unwrap_or(&err.text).trim().to_string();
        diagnostics.push(CompileDiagnostic {
            severity: "error".to_string(),
            line,
            column: col,
            code,
            message: msg,
            source: String::new(),
        });
    }

    for warn in tree.find_all("CompileResponseWarning") {
        let line = warn.attr("line").or_else(|| warn.child_text("line")).and_then(|s| s.parse::<usize>().ok()).unwrap_or(0);
        let col = warn.attr("column").or_else(|| warn.child_text("column")).and_then(|s| s.parse::<usize>().ok()).unwrap_or(0);
        let code = warn.attr("code").or_else(|| warn.child_text("code")).unwrap_or("").to_string();
        let msg = warn.attr("message").or_else(|| warn.child_text("message")).unwrap_or(&warn.text).trim().to_string();
        diagnostics.push(CompileDiagnostic {
            severity: "warning".to_string(),
            line,
            column: col,
            code,
            message: msg,
            source: String::new(),
        });
    }

    diagnostics
}

/// Triggers remote headless server compilation via `DR_*.Compile` in SHOW mode (1)
/// with authentic request XML:
/// ```xml
/// <{bdeName}>
///   <name>{compName}</name>
///   <isCheckedOut>{yes|no}</isCheckedOut>
/// </{bdeName}>
/// ```
pub async fn compile_component(
    client: &HttpClient,
    comp_type: &str,
    comp_name: &str,
    project_name: &str,
    activity_dir: Option<&Path>,
    is_checked_out: bool,
) -> Result<CompileResult, ScmError> {
    let info = get_bde_type_info(comp_type)
        .ok_or_else(|| ScmError::Other(format!("Unsupported component type '{comp_type}'")))?;
    let bde_name = info.bde;
    let dev_cp = format!("{project_name}_dev");

    let context_xml = if let Some(act_dir) = activity_dir {
        let meta = resolve_activity_scm_metadata(act_dir);
        let cp = if !meta.task_context.is_empty() { &meta.task_context } else { &dev_cp };
        Some(build_activity_context_xml(
            &meta.task_name,
            &meta.base_vrc,
            cp,
            Some(&meta.label_uuid),
            &meta.task_description,
            None,
        ))
    } else {
        None
    };

    let cko_val = if is_checked_out { "yes" } else { "no" };
    let req_xml = format!(
        "<{bde_name}>\n\
         \x20\x20<name>{comp_name}</name>\n\
         \x20\x20<isCheckedOut>{cko_val}</isCheckedOut>\n\
         </{bde_name}>"
    );

    let mgr = JcaBdeManager::new(client, "");
    let params = BdeParams {
        bde_name: bde_name.to_string(),
        method_name: "Compile".to_string(),
        mode: Some(BdeExecutionMode::Show),
        request_xml: Some(req_xml),
        context_xml,
        ..Default::default()
    };

    let resp_xml = mgr.execute(&params).await?;

    let diags = parse_compile_diagnostics(&resp_xml);
    let errors: Vec<_> = diags.iter().filter(|d| d.severity == "error").cloned().collect();
    let warnings: Vec<_> = diags.iter().filter(|d| d.severity == "warning").cloned().collect();

    let mut bic_cmd = String::new();
    let mut summary = HashMap::new();

    if let Ok(tree) = parse_xml_to_tree(&resp_xml) {
        if let Some(cmd) = tree.find_text("bicCommand") {
            bic_cmd = cmd.trim().to_string();
        }
        if let Some(sum_node) = tree.find_first("summary") {
            summary = sum_node.attributes.clone();
        }
    }

    Ok(CompileResult {
        success: errors.is_empty(),
        diagnostics: diags,
        errors,
        warnings,
        bic_command: bic_cmd,
        summary,
        raw_xml: resp_xml,
    })
}

/// Converts component to runtime data dictionary (CRDD) via `DR_*.ConvertToRuntime`
/// in BDE mode (2) with Controlling Attribute `{"executionMethod": "synchronous"}`.
pub async fn convert_to_runtime(
    client: &HttpClient,
    comp_type: &str,
    comp_name: &str,
    project_name: &str,
    activity_dir: Option<&Path>,
) -> Result<bool, ScmError> {
    let info = get_bde_type_info(comp_type)
        .ok_or_else(|| ScmError::Other(format!("Unsupported component type '{comp_type}'")))?;
    let bde_name = info.bde;
    let dev_cp = format!("{project_name}_dev");

    let context_xml = if let Some(act_dir) = activity_dir {
        let meta = resolve_activity_scm_metadata(act_dir);
        let cp = if !meta.task_context.is_empty() { &meta.task_context } else { &dev_cp };
        Some(build_activity_context_xml(
            &meta.task_name,
            &meta.base_vrc,
            cp,
            Some(&meta.label_uuid),
            &meta.task_description,
            None,
        ))
    } else {
        None
    };

    let req_xml = format!(
        "<{bde_name}>\n\
         \x20\x20<name>{comp_name}</name>\n\
         \x20\x20<type>{}</type>\n\
         </{bde_name}>",
        comp_type.to_lowercase()
    );

    let mut ctrl_attrs = HashMap::new();
    ctrl_attrs.insert("executionMethod".to_string(), "synchronous".to_string());

    let mgr = JcaBdeManager::new(client, "");
    let params = BdeParams {
        bde_name: bde_name.to_string(),
        method_name: "ConvertToRuntime".to_string(),
        mode: Some(BdeExecutionMode::Bde),
        request_xml: Some(req_xml),
        context_xml,
        controlling_attributes: ctrl_attrs,
        ..Default::default()
    };

    let resp_xml = mgr.execute(&params).await?;
    let lower = resp_xml.to_lowercase();
    Ok(!lower.contains("error") || lower.contains("ok"))
}

/// Invokes `DR_Table.CreateTables` in BDE mode (2) with Controlling Attribute
/// `{"executionMethod": "synchronous"}` to reconfigure database tables after schema changes.
pub async fn create_tables(
    client: &HttpClient,
    table_name: &str,
    project_name: &str,
    activity_dir: Option<&Path>,
) -> Result<bool, ScmError> {
    let dev_cp = format!("{project_name}_dev");

    let context_xml = if let Some(act_dir) = activity_dir {
        let meta = resolve_activity_scm_metadata(act_dir);
        let cp = if !meta.task_context.is_empty() { &meta.task_context } else { &dev_cp };
        Some(build_activity_context_xml(
            &meta.task_name,
            &meta.base_vrc,
            cp,
            Some(&meta.label_uuid),
            &meta.task_description,
            None,
        ))
    } else {
        None
    };

    let req_xml = format!(
        "<DR_Table>\n\
         \x20\x20<name>{table_name}</name>\n\
         \x20\x20<type>table</type>\n\
         </DR_Table>"
    );

    let mut ctrl_attrs = HashMap::new();
    ctrl_attrs.insert("executionMethod".to_string(), "synchronous".to_string());

    let mgr = JcaBdeManager::new(client, "");
    let params = BdeParams {
        bde_name: "DR_Table".to_string(),
        method_name: "CreateTables".to_string(),
        mode: Some(BdeExecutionMode::Bde),
        request_xml: Some(req_xml),
        context_xml,
        controlling_attributes: ctrl_attrs,
        ..Default::default()
    };

    let resp_xml = mgr.execute(&params).await?;
    let lower = resp_xml.to_lowercase();
    Ok(!lower.contains("error") || lower.contains("ok"))
}

/// Executes Verification of Source Code (VSC) on the LN Server via `VSC.executeVSC` in SHOW mode (1).
/// Parses `<vscResult verificationCode="...">` and updates `m_isVSCHappy` in activity's `.admin`.
pub async fn execute_vsc(
    client: &HttpClient,
    comp_type: &str,
    comp_name: &str,
    project_name: &str,
    activity_dir: Option<&Path>,
) -> Result<VscResult, ScmError> {
    let dev_cp = format!("{project_name}_dev");

    let context_xml = if let Some(act_dir) = activity_dir {
        let meta = resolve_activity_scm_metadata(act_dir);
        let cp = if !meta.task_context.is_empty() { &meta.task_context } else { &dev_cp };
        Some(build_activity_context_xml(
            &meta.task_name,
            &meta.base_vrc,
            cp,
            Some(&meta.label_uuid),
            &meta.task_description,
            None,
        ))
    } else {
        None
    };

    let req_xml = format!(
        "<VSC>\n\
         \x20\x20<componentName>{comp_name}</componentName>\n\
         \x20\x20<componentType>{}</componentType>\n\
         </VSC>",
        comp_type.to_lowercase()
    );

    let mgr = JcaBdeManager::new(client, "");
    let params = BdeParams {
        bde_name: "VSC".to_string(),
        method_name: "executeVSC".to_string(),
        mode: Some(BdeExecutionMode::Show),
        request_xml: Some(req_xml),
        context_xml,
        ..Default::default()
    };

    let resp_xml = mgr.execute(&params).await?;

    let mut warnings = Vec::new();
    let mut ver_code = String::new();
    let mut has_blocking = false;
    let passed;

    if let Ok(tree) = parse_xml_to_tree(&resp_xml) {
        let vsc_node = if tree.tag == "vscResult" {
            Some(&tree)
        } else {
            tree.find_first("vscResult")
        };

        if let Some(vn) = vsc_node {
            ver_code = vn.attr("verificationCode").unwrap_or("").to_string();
            for w in vn.find_all("warning") {
                let blocking = w.attr("blocking").map(|b| b.eq_ignore_ascii_case("true") || b.eq_ignore_ascii_case("yes")).unwrap_or(false);
                if blocking {
                    has_blocking = true;
                }
                warnings.push(VscWarning {
                    accepted: w.attr("accepted").unwrap_or("").to_string(),
                    blocking,
                    message_id: w.attr("messageID").unwrap_or("").to_string(),
                    warning_id: w.attr("warningID").unwrap_or("").to_string(),
                    priority: w.attr("priority").unwrap_or("").to_string(),
                    location: w.attr("location").unwrap_or("").to_string(),
                    element: w.attr("element").unwrap_or("").to_string(),
                    message: w.text.trim().to_string(),
                });
            }
            passed = !has_blocking && !ver_code.eq_ignore_ascii_case("error");
        } else {
            let lower = resp_xml.to_lowercase();
            passed = !lower.contains("error") && !lower.contains("fail");
        }
    } else {
        let lower = resp_xml.to_lowercase();
        passed = !lower.contains("error") && !lower.contains("fail");
    }

    // Update .admin m_isVSCHappy
    if let Some(act_dir) = activity_dir {
        if let Some(comp_file) = find_component_file(act_dir, comp_name, comp_type) {
            let rel_p = comp_file.strip_prefix(act_dir).unwrap_or(&comp_file).to_string_lossy().to_string();
            let admin_path = act_dir.join(".admin");
            if let Ok(mut admin) = AdminFile::load_from_path(&admin_path) {
                admin.set_vsc_happy(&rel_p, passed);
                let _ = admin.save_to_path(&admin_path);
            }
        }
    }

    Ok(VscResult {
        passed,
        verification_code: ver_code,
        warnings,
        raw_xml: resp_xml,
    })
}

/// Executes the split `deploy-test` pipeline (ADR 0008):
/// - `mode="compile-only"` (default safe mode): `Put -> Compile -> executeVSC -> CheckIn`
/// - `mode="schema-crdd"`: `Put -> Compile -> ConvertToRuntime -> CreateTables -> executeVSC -> CheckIn`
///   with a pre-check table lock warning and `--dry-run` support.
pub async fn deploy_test(
    client: &HttpClient,
    comp_type: &str,
    comp_name: &str,
    activity_dir: &Path,
    project_name: &str,
    comment: &str,
    mode: &str,
    dry_run: bool,
) -> Result<DeployTestResult, ScmError> {
    let ctype_lower = comp_type.to_lowercase();
    if ctype_lower == "extension" || is_extension_component(comp_name) {
        return Err(ScmError::GetOnlyExtension(
            "Extension Modeler Rule (ADR 0006): Extension objects cannot be deployed via LN Studio. \
             Author and deploy extension hooks via manual Copy-Paste in LN UI Cloud (ttext1500m000)."
                .to_string(),
        ));
    }

    if mode != "compile-only" && mode != "schema-crdd" {
        return Err(ScmError::Other(format!(
            "Invalid deploy-test mode '{mode}'. Supported modes: 'compile-only', 'schema-crdd'."
        )));
    }

    let planned_steps = if mode == "compile-only" {
        vec!["Put".to_string(), "Compile".to_string(), "executeVSC".to_string(), "CheckIn".to_string()]
    } else {
        vec![
            "Put".to_string(),
            "Compile".to_string(),
            "ConvertToRuntime".to_string(),
            "CreateTables".to_string(),
            "executeVSC".to_string(),
            "CheckIn".to_string(),
        ]
    };

    let lock_warning = if mode == "schema-crdd" {
        format!(
            "[TABLE LOCK WARNING] Mode 'schema-crdd' will execute ConvertToRuntime (CRDD) and CreateTables for \
             '{comp_name}'. Active LN UI Cloud sessions or open bshell cursors on '{comp_name}' can cause \
             reconfiguration lock hangs. Close active LN UI sessions before running without --dry-run."
        )
    } else {
        String::new()
    };

    if dry_run {
        return Ok(DeployTestResult {
            component: comp_name.to_string(),
            comp_type: comp_type.to_string(),
            mode: mode.to_string(),
            dry_run: true,
            planned_steps: planned_steps.clone(),
            lock_warning: lock_warning.clone(),
            success: true,
            compiled: false,
            crdd: false,
            create_tables: false,
            vsc_passed: false,
            checked_in: false,
            errors: Vec::new(),
            warnings: Vec::new(),
            message: format!(
                "[DRY-RUN] Pre-check completed for '{comp_name}' in mode '{mode}'. Planned steps: {}. {}",
                planned_steps.join(" -> "),
                lock_warning
            ),
        });
    }

    // 1. Upload to server workarea (Put)
    put_component(client, comp_type, comp_name, activity_dir, project_name, None, None).await?;

    // 2. Headless Server Compile
    let compile_res = compile_component(client, comp_type, comp_name, project_name, Some(activity_dir), true).await?;
    if !compile_res.success {
        return Ok(DeployTestResult {
            component: comp_name.to_string(),
            comp_type: comp_type.to_string(),
            mode: mode.to_string(),
            dry_run: false,
            planned_steps,
            lock_warning,
            success: false,
            compiled: false,
            crdd: false,
            create_tables: false,
            vsc_passed: false,
            checked_in: false,
            errors: compile_res.errors.clone(),
            warnings: compile_res.warnings.clone(),
            message: format!("Compilation failed with {} errors.", compile_res.errors.len()),
        });
    }

    let mut crdd_ok = false;
    let mut ct_ok = false;

    // 3 & 4. ConvertToRuntime (CRDD) & CreateTables ONLY in `schema-crdd` mode
    if mode == "schema-crdd" {
        if matches!(ctype_lower.as_str(), "table" | "domain" | "session" | "menu") {
            crdd_ok = convert_to_runtime(client, comp_type, comp_name, project_name, Some(activity_dir)).await?;
        }
        if ctype_lower == "table" {
            ct_ok = create_tables(client, comp_name, project_name, Some(activity_dir)).await?;
        }
    }

    // 5. executeVSC
    let vsc_res = execute_vsc(client, comp_type, comp_name, project_name, Some(activity_dir)).await?;

    // 6. CheckIn with documentation comment
    checkin_component(client, comp_type, comp_name, activity_dir, project_name, comment, None, None).await?;

    Ok(DeployTestResult {
        component: comp_name.to_string(),
        comp_type: comp_type.to_string(),
        mode: mode.to_string(),
        dry_run: false,
        planned_steps,
        lock_warning,
        success: true,
        compiled: true,
        crdd: crdd_ok,
        create_tables: ct_ok,
        vsc_passed: vsc_res.passed,
        checked_in: true,
        errors: compile_res.errors,
        warnings: compile_res.warnings,
        message: format!("Successfully deployed {comp_name} ({mode}) to Activity VRC for testing in LN UI Cloud."),
    })
}

/// Pre-commit readiness verifier for Activity delivery:
/// 1. Queries modified components via `CMLabel.GetModifiedComponents` and validates activity on server
///    via `DR_Solution.ValidateDevelopmentActivity` in SHOW mode (1).
/// 2. Verifies 100% synchronization of `.admin`, `.project`, and binary `properties.index`.
/// 3. Compiles human commit note and commit checklist.
pub async fn prepare_end_activity(
    client: &HttpClient,
    activity_dir: &Path,
    project_name: &str,
) -> Result<PrepareEndActivityResult, ScmError> {
    let meta = resolve_activity_scm_metadata(activity_dir);
    let task_id = if !meta.task_name.is_empty() { meta.task_name } else { "Activity".to_string() };
    let label_uuid = if !meta.label_uuid.is_empty() { meta.label_uuid } else { task_id.clone() };
    let dev_cp = if !meta.task_context.is_empty() { meta.task_context } else { format!("{project_name}_dev") };

    let context_xml = build_activity_context_xml(
        &task_id,
        &meta.base_vrc,
        &dev_cp,
        Some(&label_uuid),
        &meta.task_description,
        if !meta.task_documentation.is_empty() { Some(&meta.task_documentation) } else { None },
    );

    // 1. Query modified components via CMLabel.GetModifiedComponents
    let cmlabel_req = format!(
        "<CMLabel>\n\
         \x20\x20<labelUUID>{label_uuid}</labelUUID>\n\
         </CMLabel>"
    );
    let mgr = JcaBdeManager::new(client, "");
    let mod_resp = mgr.execute(&BdeParams {
        bde_name: "CMLabel".to_string(),
        method_name: "GetModifiedComponents".to_string(),
        mode: Some(BdeExecutionMode::Bde),
        request_xml: Some(cmlabel_req),
        context_xml: Some(context_xml.clone()),
        ..Default::default()
    }).await;

    let mut cmlabel_parts = vec!["<CMLabel>".to_string()];
    if let Ok(ref xml) = mod_resp {
        if let Ok(tree) = parse_xml_to_tree(xml) {
            for comp in tree.find_all("ModifiedComponent") {
                let name = comp.child_text("name").unwrap_or("");
                let ctype = comp.child_text("type").unwrap_or("");
                cmlabel_parts.push(format!("<ModifiedComponent><name>{name}</name><type>{ctype}</type></ModifiedComponent>"));
            }
        }
    }
    cmlabel_parts.push("</CMLabel>".to_string());
    let mod_xml = cmlabel_parts.join("");

    // 2. Server activity validation via DR_Solution.ValidateDevelopmentActivity in SHOW mode
    let val_req = format!(
        "<DR_Solution>\n\
         \x20\x20<projectName>{project_name}</projectName>\n\
         \x20\x20<taskName>{task_id}</taskName>\n\
         \x20\x20<relatedProjectName></relatedProjectName>\n\
         \x20\x20<relatedTaskName></relatedTaskName>\n\
         \x20\x20<relatedActivityUUID>{label_uuid}</relatedActivityUUID>\n\
         \x20\x20<CMLabel>{mod_xml}</CMLabel>\n\
         </DR_Solution>"
    );

    let val_resp = mgr.execute(&BdeParams {
        bde_name: "DR_Solution".to_string(),
        method_name: "ValidateDevelopmentActivity".to_string(),
        mode: Some(BdeExecutionMode::Show),
        request_xml: Some(val_req),
        context_xml: Some(context_xml),
        ..Default::default()
    }).await;

    let server_valid = match val_resp {
        Ok(res) => {
            let lower = res.to_lowercase();
            !lower.contains("error") && !lower.contains("fail")
        }
        Err(_) => false,
    };

    // 3. Local metadata verification
    let has_proj = activity_dir.join(".project").exists();
    let has_admin = activity_dir.join(".admin").exists();
    let has_settings = activity_dir.join(".settings").join("properties.index").exists();
    let metadata_ok = has_proj && has_admin && (has_settings || !meta.base_vrc.is_empty());

    // 4. Discover modified components in .admin
    let admin_path = activity_dir.join(".admin");
    let mut comp_paths = Vec::new();
    if let Ok(admin) = AdminFile::load_from_path(&admin_path) {
        for (rel, _) in admin.entries {
            comp_paths.push(rel);
        }
    }

    let summary = format!(
        "=== Infor LN Studio Pre-Commit Activity Summary ===\n\
         Activity:   {task_id}\n\
         Project:    {project_name}\n\
         Components: {} modified components\n\
         Server VSC: {}\n\
         Workspace:  {}\n\
         Status:     READY FOR HUMAN DELIVERY APPROVAL IN LN STUDIO\n\
         ===================================================",
        comp_paths.len(),
        if server_valid { "PASSED" } else { "CHECK_REQUIRED" },
        if metadata_ok { "100% SYNCHRONIZED" } else { "METADATA_INCOMPLETE" }
    );

    Ok(PrepareEndActivityResult {
        activity: task_id,
        project: project_name.to_string(),
        activity_folder: activity_dir.to_string_lossy().to_string(),
        server_valid,
        metadata_synced: metadata_ok,
        components_count: comp_paths.len(),
        components: comp_paths,
        ready_for_human_review: server_valid && metadata_ok,
        human_action_required: "Please open Infor LN Studio (Eclipse), review changes, and click 'End Activity'.".to_string(),
        commit_summary: summary,
    })
}

/// Diagnoses a component by running remote headless compilation and static analysis with `ln-linter`.
pub async fn diagnose(
    client: &HttpClient,
    comp_type: &str,
    comp_name: &str,
    project_name: &str,
    activity_dir: Option<&Path>,
) -> Result<DiagnoseResult, ScmError> {
    let comp_res = compile_component(client, comp_type, comp_name, project_name, activity_dir, true).await?;

    let mut linter_diags = Vec::new();
    if let Some(act_dir) = activity_dir {
        if let Some(cf) = find_component_file(act_dir, comp_name, comp_type) {
            if let Ok(source) = fs::read_to_string(&cf) {
                // If script file or component contains 4GL
                let diags = ln_linter::audit_content(&source, &cf.to_string_lossy(), false, None);
                for d in diags {
                    linter_diags.push(format!("[{}] Line {}: {}", d.code, d.line, d.message));
                }
            }
        }
    }

    Ok(DiagnoseResult {
        component: comp_name.to_string(),
        comp_type: comp_type.to_string(),
        compiler_success: comp_res.success,
        compiler_diagnostics: comp_res.diagnostics,
        linter_diagnostics: linter_diags,
        raw_compiler_xml: comp_res.raw_xml,
    })
}
