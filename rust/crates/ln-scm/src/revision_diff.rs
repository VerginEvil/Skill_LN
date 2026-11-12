use std::collections::HashMap;
use std::fs;
use std::path::Path;
use serde::{Deserialize, Serialize};

use ln_eclipse_compat::AdminFile;
use ln_jca::{BdeExecutionMode, BdeParams, HttpClient, JcaBdeManager};
use ln_model::dom_surgery::extract_script;
use crate::explorer::{fetch_component_xml, get_bde_type_info};
use crate::scm_engine::{build_activity_context_xml, find_component_file, resolve_activity_scm_metadata, ScmError};
use crate::xml_tree::parse_xml_to_tree;

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct RevisionMetadata {
    pub number: usize,
    pub version_id: String,
    pub date: String,
    pub time: String,
    pub author: String,
    pub comment: String,
    pub task: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ComponentRevisionsResult {
    pub component_name: String,
    pub component_type: String,
    pub version_id: String,
    pub total_revisions: usize,
    pub revisions: Vec<RevisionMetadata>,
    pub raw_response: String,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct StructuralElement {
    pub tag: String,
    pub name: String,
    pub attributes: HashMap<String, String>,
    pub text: String,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct ModifiedElement {
    pub key: String,
    pub local: StructuralElement,
    pub remote: StructuralElement,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct StructuralDiff {
    pub added_elements: Vec<StructuralElement>,
    pub removed_elements: Vec<StructuralElement>,
    pub modified_elements: Vec<ModifiedElement>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ComponentDiffResult {
    pub component_name: String,
    pub component_type: String,
    pub target_version: String,
    pub target_revision: usize,
    pub has_script_changes: bool,
    pub script_diff: String,
    pub has_structural_changes: bool,
    pub structural_diff: StructuralDiff,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ServerReportResult {
    pub success: bool,
    pub report_name: String,
    pub table_name: String,
    pub version_id: String,
    pub output_file: Option<String>,
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

/// Generates a standard unified diff between two text strings using the Longest Common Subsequence (LCS).
pub fn generate_unified_diff(
    original: &str,
    modified: &str,
    from_file: &str,
    to_file: &str,
) -> String {
    let orig_lines: Vec<&str> = original.lines().collect();
    let mod_lines: Vec<&str> = modified.lines().collect();

    if orig_lines == mod_lines {
        return String::new();
    }

    let n = orig_lines.len();
    let m = mod_lines.len();

    // Compute LCS matrix
    let mut dp = vec![vec![0u32; m + 1]; n + 1];
    for i in 0..n {
        for j in 0..m {
            if orig_lines[i] == mod_lines[j] {
                dp[i + 1][j + 1] = dp[i][j] + 1;
            } else {
                dp[i + 1][j + 1] = dp[i + 1][j].max(dp[i][j + 1]);
            }
        }
    }

    // Backtrack to find edit sequence
    #[derive(Debug, PartialEq, Eq)]
    enum DiffOp<'a> {
        Equal(&'a str),
        Delete(&'a str),
        Insert(&'a str),
    }

    let mut ops = Vec::new();
    let mut i = n;
    let mut j = m;

    while i > 0 || j > 0 {
        if i > 0 && j > 0 && orig_lines[i - 1] == mod_lines[j - 1] {
            ops.push(DiffOp::Equal(orig_lines[i - 1]));
            i -= 1;
            j -= 1;
        } else if j > 0 && (i == 0 || dp[i][j - 1] >= dp[i - 1][j]) {
            ops.push(DiffOp::Insert(mod_lines[j - 1]));
            j -= 1;
        } else if i > 0 && (j == 0 || dp[i][j - 1] < dp[i - 1][j]) {
            ops.push(DiffOp::Delete(orig_lines[i - 1]));
            i -= 1;
        }
    }
    ops.reverse();

    // Format into unified diff
    let mut out = String::new();
    out.push_str(&format!("--- {from_file}\n"));
    out.push_str(&format!("+++ {to_file}\n"));
    out.push_str(&format!("@@ -1,{} +1,{} @@\n", n, m));

    for op in ops {
        match op {
            DiffOp::Equal(line) => {
                out.push(' ');
                out.push_str(line);
                out.push('\n');
            }
            DiffOp::Delete(line) => {
                out.push('-');
                out.push_str(line);
                out.push('\n');
            }
            DiffOp::Insert(line) => {
                out.push('+');
                out.push_str(line);
                out.push('\n');
            }
        }
    }

    out
}

/// Extracts structural elements (fields, forms, options, indices, hooks) from component XML.
pub fn extract_structural_elements(xml_str: &str) -> HashMap<String, StructuralElement> {
    let mut elements = HashMap::new();
    if xml_str.trim().is_empty() {
        return elements;
    }

    if let Ok(tree) = parse_xml_to_tree(xml_str) {
        for child in &tree.children {
            if child.tag == "expression" || child.tag.ends_with("Script") || child.tag == "ControlArea" {
                continue;
            }
            let name = child.attr("name")
                .or_else(|| child.child_text("name"))
                .unwrap_or(&child.tag)
                .to_string();
            let key = format!("{}::{}", child.tag, name);
            elements.insert(key, StructuralElement {
                tag: child.tag.clone(),
                name,
                attributes: child.attributes.clone(),
                text: child.text.trim().to_string(),
            });
        }
    }

    elements
}

/// Queries server-side revision history via `FglStudio.GetRevisions` in BDE mode (2).
/// Returns list of revision metadata dictionaries.
pub async fn list_component_revisions(
    client: &HttpClient,
    comp_type: &str,
    comp_name: &str,
    version_id: &str,
    project_name: &str,
    activity_dir: Option<&Path>,
) -> Result<ComponentRevisionsResult, ScmError> {
    let (context_xml, _dev_cp) = build_context_envelope(activity_dir, project_name);

    let req_xml = format!(
        "<FglStudio>\n\
         \x20\x20<compType>{comp_type}</compType>\n\
         \x20\x20<compCode>{comp_name}</compCode>\n\
         \x20\x20<versionID>{version_id}</versionID>\n\
         </FglStudio>"
    );

    let mgr = JcaBdeManager::new(client, "");
    let params = BdeParams {
        bde_name: "FglStudio".to_string(),
        method_name: "GetRevisions".to_string(),
        mode: Some(BdeExecutionMode::Bde),
        request_xml: Some(req_xml),
        context_xml,
        ..Default::default()
    };

    let resp_xml = mgr.execute(&params).await?;

    let mut revisions = Vec::new();
    if let Ok(tree) = parse_xml_to_tree(&resp_xml) {
        let mut candidates = tree.find_all("revision");
        candidates.extend(tree.find_all("item"));

        for r_node in candidates {
            let num_str = r_node.attr("number")
                .or_else(|| r_node.child_text("number"))
                .unwrap_or("0");
            let v_id = r_node.attr("versionID")
                .or_else(|| r_node.child_text("versionID"))
                .unwrap_or(version_id)
                .to_string();
            let date_str = r_node.attr("date")
                .or_else(|| r_node.child_text("date"))
                .unwrap_or("")
                .to_string();
            let time_str = r_node.attr("time")
                .or_else(|| r_node.child_text("time"))
                .unwrap_or("")
                .to_string();
            let author = r_node.attr("author")
                .or_else(|| r_node.attr("user"))
                .or_else(|| r_node.child_text("author"))
                .or_else(|| r_node.child_text("user"))
                .unwrap_or("")
                .to_string();
            let comment = r_node.attr("comment")
                .or_else(|| r_node.child_text("comment"))
                .unwrap_or(&r_node.text)
                .trim()
                .to_string();
            let task = r_node.attr("task")
                .or_else(|| r_node.attr("taskName"))
                .or_else(|| r_node.child_text("task"))
                .unwrap_or("")
                .to_string();

            let num = num_str.parse::<usize>().unwrap_or(0);
            revisions.push(RevisionMetadata {
                number: num,
                version_id: v_id,
                date: date_str,
                time: time_str,
                author,
                comment,
                task,
            });
        }
    }

    revisions.sort_by(|a, b| b.number.cmp(&a.number));

    Ok(ComponentRevisionsResult {
        component_name: comp_name.to_string(),
        component_type: comp_type.to_string(),
        version_id: version_id.to_string(),
        total_revisions: revisions.len(),
        revisions,
        raw_response: resp_xml,
    })
}

/// Retrieves the raw component XML of a historical server revision
/// via `DR_*.GetRevision` (or `StudioComponent.GetRevision`) in BDE mode (2).
pub async fn get_component_revision(
    client: &HttpClient,
    comp_type: &str,
    comp_name: &str,
    version_id: &str,
    rev_number: usize,
    project_name: &str,
    activity_dir: Option<&Path>,
) -> Result<String, ScmError> {
    let info = get_bde_type_info(comp_type);
    let bde_name = info.map(|i| i.bde).unwrap_or("StudioComponent");
    let (context_xml, _dev_cp) = build_context_envelope(activity_dir, project_name);

    let req_xml = format!(
        "<{bde_name}>\n\
         \x20\x20<name>{comp_name}</name>\n\
         \x20\x20<type>{}</type>\n\
         \x20\x20<versionID>{version_id}</versionID>\n\
         \x20\x20<number>{rev_number}</number>\n\
         \x20\x20<optionalContent>yes</optionalContent>\n\
         </{bde_name}>",
        comp_type.to_lowercase()
    );

    let mgr = JcaBdeManager::new(client, "");
    let params = BdeParams {
        bde_name: bde_name.to_string(),
        method_name: "GetRevision".to_string(),
        mode: Some(BdeExecutionMode::Bde),
        request_xml: Some(req_xml.clone()),
        context_xml: context_xml.clone(),
        ..Default::default()
    };

    match mgr.execute(&params).await {
        Ok(res) => Ok(res),
        Err(_) => {
            // Fallback to StudioComponent.GetRevision
            let fb_params = BdeParams {
                bde_name: "StudioComponent".to_string(),
                method_name: "GetRevision".to_string(),
                mode: Some(BdeExecutionMode::Bde),
                request_xml: Some(req_xml),
                context_xml,
                ..Default::default()
            };
            let fb_res = mgr.execute(&fb_params).await?;
            Ok(fb_res)
        }
    }
}

/// Diffs local workarea component against a server revision or base copy.
/// Produces:
/// 1. Unified 4GL script diff
/// 2. Structural XML elements diff (added, removed, modified)
pub async fn diff_component(
    client: &HttpClient,
    comp_type: &str,
    comp_name: &str,
    activity_dir: &Path,
    target_version_id: Option<&str>,
    target_rev_number: Option<usize>,
    project_name: &str,
) -> Result<ComponentDiffResult, ScmError> {
    // 1. Locate local file
    let local_file = find_component_file(activity_dir, comp_name, comp_type)
        .ok_or_else(|| ScmError::FileNotFound(format!("Component '{comp_name}' ({comp_type}) not found in {:?}", activity_dir)))?;

    let local_xml = fs::read_to_string(&local_file).unwrap_or_default();

    // Check standalone script file priority (.4gl, .dal, .src)
    let script_candidates = [
        activity_dir.join("scripts").join(format!("{comp_name}.4gl")),
        activity_dir.join("scripts").join(format!("{comp_name}.src")),
        activity_dir.join("dal").join(format!("{comp_name}.dal")),
        local_file.with_extension("4gl"),
        local_file.with_extension("dal"),
    ];
    let mut local_script = String::new();
    for sc in &script_candidates {
        if sc.exists() {
            if let Ok(c) = fs::read_to_string(sc) {
                local_script = c;
                break;
            }
        }
    }
    if local_script.is_empty() {
        local_script = extract_script(&local_xml).unwrap_or_default();
    }

    // 2. Fetch remote revision
    let meta = resolve_activity_scm_metadata(activity_dir);
    let version_id = target_version_id.unwrap_or(if !meta.base_vrc.is_empty() { &meta.base_vrc } else { "B61O_a_ext" });
    let rev_num = target_rev_number.unwrap_or(0);

    let remote_xml = if rev_num > 0 {
        get_component_revision(
            client,
            comp_type,
            comp_name,
            version_id,
            rev_num,
            project_name,
            Some(activity_dir),
        ).await.unwrap_or_default()
    } else {
        let (context_xml, dev_cp) = build_context_envelope(Some(activity_dir), project_name);
        match fetch_component_xml(
            client,
            comp_type,
            comp_name,
            &dev_cp,
            context_xml.as_deref(),
            Some(version_id),
        ).await {
            Ok(xml) => xml,
            Err(_) => {
                get_component_revision(
                    client,
                    comp_type,
                    comp_name,
                    version_id,
                    1,
                    project_name,
                    Some(activity_dir),
                ).await.unwrap_or_default()
            }
        }
    };

    let remote_script = extract_script(&remote_xml).unwrap_or_default();

    // 3. Unified Script Diff
    let from_header = format!("server/{comp_name} (rev {})", if rev_num > 0 { rev_num.to_string() } else { "base".to_string() });
    let to_header = format!("local/{comp_name}");
    let script_diff_text = generate_unified_diff(&remote_script, &local_script, &from_header, &to_header);

    // 4. Structural XML Diff
    let local_elements = extract_structural_elements(&local_xml);
    let remote_elements = extract_structural_elements(&remote_xml);

    let mut added = Vec::new();
    let mut removed = Vec::new();
    let mut modified = Vec::new();

    for (k, v) in &local_elements {
        if !remote_elements.contains_key(k) {
            added.push(v.clone());
        } else if v != &remote_elements[k] {
            modified.push(ModifiedElement {
                key: k.clone(),
                local: v.clone(),
                remote: remote_elements[k].clone(),
            });
        }
    }

    for (k, v) in &remote_elements {
        if !local_elements.contains_key(k) {
            removed.push(v.clone());
        }
    }

    let has_script = !script_diff_text.trim().is_empty();
    let has_structural = !added.is_empty() || !removed.is_empty() || !modified.is_empty();

    Ok(ComponentDiffResult {
        component_name: comp_name.to_string(),
        component_type: comp_type.to_string(),
        target_version: version_id.to_string(),
        target_revision: rev_num,
        has_script_changes: has_script,
        script_diff: script_diff_text,
        has_structural_changes: has_structural,
        structural_diff: StructuralDiff {
            added_elements: added,
            removed_elements: removed,
            modified_elements: modified,
        },
    })
}

/// Invokes Server Report Wizard via `DR_Report.Generate` in BDE mode (2).
/// Generates standard report layout and script, saves `.rpt` locally, and updates `.admin`.
pub async fn generate_report_on_server(
    client: &HttpClient,
    report_name: &str,
    table_name: &str,
    version_id: &str,
    description: &str,
    report_size: &str,
    report_type: &str,
    used_index: &str,
    input_fields: Option<&[String]>,
    overwrite: bool,
    project_name: &str,
    activity_dir: Option<&Path>,
) -> Result<ServerReportResult, ScmError> {
    let (context_xml, _dev_cp) = build_context_envelope(activity_dir, project_name);

    let mut fields_xml = String::new();
    if let Some(fields) = input_fields {
        for f in fields {
            fields_xml.push_str(&format!("<field>{f}</field>"));
        }
    }

    let ovw_str = if overwrite { "yes" } else { "no" };
    let req_xml = format!(
        "<DR_Report>\n\
         \x20\x20<name>{report_name}</name>\n\
         \x20\x20<versionID>{version_id}</versionID>\n\
         \x20\x20<table>{table_name}</table>\n\
         \x20\x20<description>{description}</description>\n\
         \x20\x20<overwrite>{ovw_str}</overwrite>\n\
         \x20\x20<reportSize>{report_size}</reportSize>\n\
         \x20\x20<reportType>{report_type}</reportType>\n\
         \x20\x20<usedIndex>{used_index}</usedIndex>\n\
         \x20\x20<inputFields>{fields_xml}</inputFields>\n\
         </DR_Report>"
    );

    let mgr = JcaBdeManager::new(client, "");
    let params = BdeParams {
        bde_name: "DR_Report".to_string(),
        method_name: "Generate".to_string(),
        mode: Some(BdeExecutionMode::Bde),
        request_xml: Some(req_xml),
        context_xml,
        ..Default::default()
    };

    let resp_xml = mgr.execute(&params).await?;

    let mut output_path = None;
    if let Some(act_dir) = activity_dir {
        let pkg = if report_name.len() >= 2 { &report_name[..2] } else { "tx" };
        let mod_code = if report_name.len() >= 5 { &report_name[2..5] } else { "gen" };
        let rpt_dir = act_dir.join(pkg).join("report").join(mod_code);
        let _ = fs::create_dir_all(&rpt_dir);
        let rpt_file = rpt_dir.join(format!("{report_name}.rpt"));

        let file_content = if resp_xml.contains("<DR_Report") {
            resp_xml.clone()
        } else {
            format!(
                "<DR_Report name=\"{report_name}\" versionID=\"{version_id}\" table=\"{table_name}\">\n\
                 \x20\x20<description>{description}</description>\n\
                 \x20\x20<reportSize>{report_size}</reportSize>\n\
                 \x20\x20<reportType>{report_type}</reportType>\n\
                 \x20\x20<expression><![CDATA[| 4GL Report script for {report_name}]]></expression>\n\
                 </DR_Report>"
            )
        };

        fs::write(&rpt_file, file_content)?;

        let rel_admin = format!("{pkg}/report/{mod_code}/{report_name}.rpt");
        let admin_path = act_dir.join(".admin");
        if let Ok(mut admin) = AdminFile::load_from_path(&admin_path) {
            admin.after_create(&rel_admin);
            let _ = admin.save_to_path(&admin_path);
        }

        output_path = Some(rpt_file.to_string_lossy().to_string());
    }

    let success = !resp_xml.to_lowercase().contains("error") || resp_xml.contains("<DR_Report");

    Ok(ServerReportResult {
        success,
        report_name: report_name.to_string(),
        table_name: table_name.to_string(),
        version_id: version_id.to_string(),
        output_file: output_path,
        raw_response: resp_xml,
    })
}
