use std::path::Path;
use serde::{Deserialize, Serialize};

use ln_jca::{BdeExecutionMode, BdeParams, HttpClient, JcaBdeManager};
use crate::build::{parse_compile_diagnostics, CompileDiagnostic};
use crate::scm_engine::{build_activity_context_xml, resolve_activity_scm_metadata, ScmError};
use crate::xml_tree::parse_xml_to_tree;

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct AdHocCompileResult {
    pub success: bool,
    pub package_code: String,
    pub bic_command: String,
    pub diagnostics: Vec<CompileDiagnostic>,
    pub errors: Vec<CompileDiagnostic>,
    pub warnings: Vec<CompileDiagnostic>,
    pub raw_response: String,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct SearchMatch {
    pub component: String,
    pub comp_type: String,
    pub package: String,
    pub line: usize,
    pub snippet: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct SearchServerResult {
    pub pattern: String,
    pub package_code: String,
    pub total_matches: usize,
    pub matches: Vec<SearchMatch>,
    pub raw_response: String,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct CallHierarchyNode {
    pub function: String,
    pub comp_type: String,
    pub source_file: String,
    pub line: usize,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct CallHierarchyResult {
    pub source_file_name: String,
    pub function_name: String,
    pub call_mode: String,
    pub is_valid: bool,
    pub total_nodes: usize,
    pub hierarchy: Vec<CallHierarchyNode>,
    pub raw_response: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct OpenDeclarationResult {
    pub found: bool,
    pub function: String,
    pub component_code: String,
    pub component_type: String,
    pub line_number: usize,
    pub context: String,
    pub raw_response: String,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct RelatedComponent {
    pub name: String,
    pub comp_type: String,
    pub version_id: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct RelatedComponentsResult {
    pub package_code: String,
    pub total_components: usize,
    pub components: Vec<RelatedComponent>,
    pub raw_response: String,
}

fn build_context_envelope(activity_dir: Option<&Path>, project_name: &str) -> (Option<String>, String) {
    let dev_cp = format!("{project_name}_dev");
    if let Some(act_dir) = activity_dir {
        let meta = resolve_activity_scm_metadata(act_dir);
        let cp = if !meta.task_context.is_empty() { meta.task_context } else { dev_cp };
        let ctx = build_activity_context_xml(
            &meta.task_name,
            &meta.base_vrc,
            &cp,
            Some(&meta.label_uuid),
            &meta.task_description,
            None,
        );
        (Some(ctx), cp)
    } else {
        (None, dev_cp)
    }
}

/// Executes Ad-Hoc Server Compilation via `FglStudio.compileSource` in SHOW mode (1).
/// Compiles 4GL code snippet directly on server `bic6.2` without modifying local files or SCM state.
pub async fn compile_source_adhoc(
    client: &HttpClient,
    package_code: &str,
    source_code: &str,
    flags: &str,
    project_name: &str,
    activity_dir: Option<&Path>,
) -> Result<AdHocCompileResult, ScmError> {
    let (context_xml, _dev_cp) = build_context_envelope(activity_dir, project_name);

    let req_xml = format!(
        "<FglStudio>\n\
         \x20\x20<packageCode>{package_code}</packageCode>\n\
         \x20\x20<source><expression><expression><![CDATA[{source_code}]]></expression></expression></source>\n\
         \x20\x20<flags>{flags}</flags>\n\
         </FglStudio>"
    );

    let mgr = JcaBdeManager::new(client, "");
    let params = BdeParams {
        bde_name: "FglStudio".to_string(),
        method_name: "compileSource".to_string(),
        mode: Some(BdeExecutionMode::Show),
        request_xml: Some(req_xml),
        context_xml,
        ..Default::default()
    };

    let resp_xml = mgr.execute(&params).await?;

    let diagnostics = parse_compile_diagnostics(&resp_xml);
    let errors: Vec<_> = diagnostics.iter().filter(|d| d.severity == "error").cloned().collect();
    let warnings: Vec<_> = diagnostics.iter().filter(|d| d.severity == "warning").cloned().collect();

    let mut bic_command = String::new();
    if let Ok(tree) = parse_xml_to_tree(&resp_xml) {
        if let Some(cmd) = tree.find_text("bicCommand") {
            bic_command = cmd.trim().to_string();
        }
    }

    let success = errors.is_empty() && (!resp_xml.to_lowercase().contains("error") || resp_xml.contains("<compileResult"));

    Ok(AdHocCompileResult {
        success,
        package_code: package_code.to_string(),
        bic_command,
        diagnostics,
        errors,
        warnings,
        raw_response: resp_xml,
    })
}

/// Executes Global Server Search via `FglStudio.Searchpattern` in BDE mode (2).
/// Searches regex/text pattern across server components and returns match items.
pub async fn search_server_pattern(
    client: &HttpClient,
    pattern: &str,
    package_code: &str,
    project_name: &str,
    activity_dir: Option<&Path>,
) -> Result<SearchServerResult, ScmError> {
    let (context_xml, _dev_cp) = build_context_envelope(activity_dir, project_name);

    let req_xml = format!(
        "<FglStudio>\n\
         \x20\x20<pattern>{pattern}</pattern>\n\
         \x20\x20<packageCode>{package_code}</packageCode>\n\
         </FglStudio>"
    );

    let mgr = JcaBdeManager::new(client, "");
    let params = BdeParams {
        bde_name: "FglStudio".to_string(),
        method_name: "Searchpattern".to_string(),
        mode: Some(BdeExecutionMode::Bde),
        request_xml: Some(req_xml),
        context_xml,
        ..Default::default()
    };

    let resp_xml = mgr.execute(&params).await?;

    let mut matches = Vec::new();
    if let Ok(tree) = parse_xml_to_tree(&resp_xml) {
        let mut candidates = tree.find_all("match");
        candidates.extend(tree.find_all("item"));
        candidates.extend(tree.find_all("result"));

        for node in candidates {
            let comp = node.attr("component")
                .or_else(|| node.child_text("component"))
                .unwrap_or("")
                .to_string();
            let line_str = node.attr("line")
                .or_else(|| node.child_text("line"))
                .unwrap_or("0");
            let snippet = node.attr("snippet")
                .or_else(|| node.child_text("snippet"))
                .unwrap_or(&node.text)
                .trim()
                .to_string();
            let comp_type = node.attr("type")
                .or_else(|| node.child_text("type"))
                .unwrap_or("")
                .to_string();
            let pkg = node.attr("package")
                .or_else(|| node.child_text("package"))
                .unwrap_or(package_code)
                .to_string();

            let line_no = line_str.parse::<usize>().unwrap_or(0);
            if !comp.is_empty() || !snippet.is_empty() {
                matches.push(SearchMatch {
                    component: comp,
                    comp_type,
                    package: pkg,
                    line: line_no,
                    snippet,
                });
            }
        }
    }

    Ok(SearchServerResult {
        pattern: pattern.to_string(),
        package_code: package_code.to_string(),
        total_matches: matches.len(),
        matches,
        raw_response: resp_xml,
    })
}

/// Queries Function Call Hierarchy & Where-Used via `fglstudio.isValidFunction`
/// and `fglstudio.GetCallHierarchyData` in BDE mode (2).
/// `call_mode` can be `"callers"` (where-used) or `"callees"`.
pub async fn get_call_hierarchy(
    client: &HttpClient,
    source_file_name: &str,
    function_name: &str,
    call_mode: &str,
    project_name: &str,
    activity_dir: Option<&Path>,
) -> Result<CallHierarchyResult, ScmError> {
    let (context_xml, _dev_cp) = build_context_envelope(activity_dir, project_name);

    let mgr = JcaBdeManager::new(client, "");

    // 1. Check if function is valid on server via fglstudio.isValidFunction
    let val_req = format!(
        "<FglStudio>\n\
         \x20\x20<sourceFileName>{source_file_name}</sourceFileName>\n\
         \x20\x20<pattern>{function_name}</pattern>\n\
         </FglStudio>"
    );

    let val_resp = mgr.execute(&BdeParams {
        bde_name: "fglstudio".to_string(),
        method_name: "isValidFunction".to_string(),
        mode: Some(BdeExecutionMode::Bde),
        request_xml: Some(val_req),
        context_xml: context_xml.clone(),
        ..Default::default()
    }).await;

    let is_valid = match val_resp {
        Ok(v) => {
            let lower = v.to_lowercase();
            !lower.contains("false") && !lower.contains("invalid")
        }
        Err(_) => true,
    };

    // 2. Query Call Hierarchy Data via fglstudio.GetCallHierarchyData
    let call_req = format!(
        "<FglStudio>\n\
         \x20\x20<sourceFileName>{source_file_name}</sourceFileName>\n\
         \x20\x20<functionName>{function_name}</functionName>\n\
         \x20\x20<callMode>{call_mode}</callMode>\n\
         </FglStudio>"
    );

    let call_resp = mgr.execute(&BdeParams {
        bde_name: "fglstudio".to_string(),
        method_name: "GetCallHierarchyData".to_string(),
        mode: Some(BdeExecutionMode::Bde),
        request_xml: Some(call_req),
        context_xml,
        ..Default::default()
    }).await?;

    let mut nodes = Vec::new();
    if let Ok(tree) = parse_xml_to_tree(&call_resp) {
        let mut candidates = tree.find_all("node");
        candidates.extend(tree.find_all("caller"));
        candidates.extend(tree.find_all("callee"));
        candidates.extend(tree.find_all("function"));

        for node in candidates {
            let fn_name = node.attr("name")
                .or_else(|| node.child_text("name"))
                .or_else(|| node.attr("function"))
                .unwrap_or("")
                .to_string();
            let fn_type = node.attr("type")
                .or_else(|| node.child_text("type"))
                .unwrap_or("")
                .to_string();
            let fn_file = node.attr("file")
                .or_else(|| node.child_text("file"))
                .or_else(|| node.attr("sourceFileName"))
                .unwrap_or("")
                .to_string();
            let line_str = node.attr("line")
                .or_else(|| node.child_text("line"))
                .unwrap_or("0");
            let line_no = line_str.parse::<usize>().unwrap_or(0);

            if !fn_name.is_empty() || !fn_file.is_empty() {
                nodes.push(CallHierarchyNode {
                    function: fn_name,
                    comp_type: fn_type,
                    source_file: fn_file,
                    line: line_no,
                });
            }
        }
    }

    Ok(CallHierarchyResult {
        source_file_name: source_file_name.to_string(),
        function_name: function_name.to_string(),
        call_mode: call_mode.to_string(),
        is_valid,
        total_nodes: nodes.len(),
        hierarchy: nodes,
        raw_response: call_resp,
    })
}

/// Locates function definition location via `FglStudio.OpenDeclarationFunction` in BDE mode (2).
/// Returns target component code, component type, and line number.
pub async fn open_declaration(
    client: &HttpClient,
    comp_code: &str,
    comp_type: &str,
    function_name: &str,
    context: &str,
    project_name: &str,
    activity_dir: Option<&Path>,
) -> Result<OpenDeclarationResult, ScmError> {
    let (context_xml, _dev_cp) = build_context_envelope(activity_dir, project_name);

    let req_xml = format!(
        "<FglStudio>\n\
         \x20\x20<compCodeFunction>{comp_code}</compCodeFunction>\n\
         \x20\x20<compTypeFunction>{comp_type}</compTypeFunction>\n\
         \x20\x20<function>{function_name}</function>\n\
         \x20\x20<context>{context}</context>\n\
         </FglStudio>"
    );

    let mgr = JcaBdeManager::new(client, "");
    let params = BdeParams {
        bde_name: "FglStudio".to_string(),
        method_name: "OpenDeclarationFunction".to_string(),
        mode: Some(BdeExecutionMode::Bde),
        request_xml: Some(req_xml),
        context_xml,
        ..Default::default()
    };

    let resp_xml = mgr.execute(&params).await?;

    let mut target_comp = String::new();
    let mut target_type = String::new();
    let mut target_line = 0;

    if let Ok(tree) = parse_xml_to_tree(&resp_xml) {
        if let Some(comp) = tree.find_text("compCodeFunction").or_else(|| tree.attr("compCodeFunction")) {
            target_comp = comp.trim().to_string();
        }
        if let Some(ctype) = tree.find_text("compTypeFunction").or_else(|| tree.attr("compTypeFunction")) {
            target_type = ctype.trim().to_string();
        }
        if let Some(linestr) = tree.find_text("lineno").or_else(|| tree.find_text("lineNumber")).or_else(|| tree.attr("lineno")) {
            target_line = linestr.trim().parse::<usize>().unwrap_or(0);
        }
    }

    let found = !target_comp.is_empty() || target_line > 0;
    Ok(OpenDeclarationResult {
        found,
        function: function_name.to_string(),
        component_code: if !target_comp.is_empty() { target_comp } else { comp_code.to_string() },
        component_type: if !target_type.is_empty() { target_type } else { comp_type.to_string() },
        line_number: target_line,
        context: context.to_string(),
        raw_response: resp_xml,
    })
}

/// Discovers includes, libraries, and tables referenced by a 4GL script
/// via `FglStudio.GetScriptComponents` in BDE mode (2).
pub async fn get_related_script_components(
    client: &HttpClient,
    package_code: &str,
    source_code: &str,
    project_name: &str,
    activity_dir: Option<&Path>,
) -> Result<RelatedComponentsResult, ScmError> {
    let (context_xml, _dev_cp) = build_context_envelope(activity_dir, project_name);

    let req_xml = format!(
        "<FglStudio>\n\
         \x20\x20<packageCode>{package_code}</packageCode>\n\
         \x20\x20<source><expression><expression><![CDATA[{source_code}]]></expression></expression></source>\n\
         </FglStudio>"
    );

    let mgr = JcaBdeManager::new(client, "");
    let params = BdeParams {
        bde_name: "FglStudio".to_string(),
        method_name: "GetScriptComponents".to_string(),
        mode: Some(BdeExecutionMode::Bde),
        request_xml: Some(req_xml),
        context_xml,
        ..Default::default()
    };

    let resp_xml = mgr.execute(&params).await?;

    let mut components = Vec::new();
    if let Ok(tree) = parse_xml_to_tree(&resp_xml) {
        let mut candidates = tree.find_all("component");
        candidates.extend(tree.find_all("item"));

        for comp_node in candidates {
            let c_name = comp_node.attr("name")
                .or_else(|| comp_node.child_text("name"))
                .unwrap_or("")
                .to_string();
            let c_type = comp_node.attr("type")
                .or_else(|| comp_node.child_text("type"))
                .unwrap_or("")
                .to_string();
            let c_ver = comp_node.attr("versionID")
                .or_else(|| comp_node.child_text("versionID"))
                .unwrap_or("")
                .to_string();

            if !c_name.is_empty() {
                components.push(RelatedComponent {
                    name: c_name,
                    comp_type: c_type,
                    version_id: c_ver,
                });
            }
        }
    }

    Ok(RelatedComponentsResult {
        package_code: package_code.to_string(),
        total_components: components.len(),
        components,
        raw_response: resp_xml,
    })
}
