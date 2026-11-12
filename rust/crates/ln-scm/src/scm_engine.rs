use std::collections::HashMap;
use std::fs;
use std::path::{Path, PathBuf};
use std::time::{SystemTime, UNIX_EPOCH};
use regex::Regex;
use serde::{Deserialize, Serialize};
use sha2::{Digest, Sha256};
use thiserror::Error;

use ln_eclipse_compat::{AdminError, AdminFile, PropertyBucket};
use ln_jca::{escape_xml, BdeExecutionMode, BdeParams, HttpClient, JcaBdeManager, JcaError};
use ln_model::dom_surgery::{pre_put_merge_and_guard, PrePutGuardError};
use ln_model::path_resolver::resolve_tde_relative_path;
use crate::explorer::get_bde_type_info;
use crate::xml_tree::parse_xml_to_tree;

/// Architectural Dependency Order for SCM and compilation operations.
pub const DEPENDENCY_ORDER: &[&str] = &[
    "domain",
    "table",
    "label",
    "session",
    "menu",
    "library",
    "function",
    "report",
    "message",
    "question",
    "additional",
    "extension",
];

#[derive(Debug, Error)]
pub enum ScmError {
    #[error("[GET_ONLY_EXTENSION]: Use session ttext1500m000 in LN UI to process extensions ({0})")]
    GetOnlyExtension(String),

    #[error("[READ_ONLY_COMPONENT]: Attempted to write to read-only component '{0}' without checking it out first")]
    ReadOnlyComponent(String),

    #[error("[HARD-BLOCKED] End Activity / Commit Activity is prohibited by ADR 0007 governance. Activity '{activity_id}' in project '{project_name}' has been verified and deployed for testing. Please open Infor LN Studio (Eclipse Workbench) to perform final human review and click 'End Activity'.")]
    PreCommitBoundary {
        project_name: String,
        activity_id: String,
    },

    #[error("[SCM_SERVER_ERROR] Infor LN Server rejected {operation} on '{component_name}': {message}")]
    ServerExecution {
        component_name: String,
        operation: String,
        message: String,
        raw_response: String,
    },

    #[error("Component file not found: {0}")]
    FileNotFound(String),

    #[error("PrePutGuard error: {0}")]
    PrePutGuard(#[from] PrePutGuardError),

    #[error("JCA error: {0}")]
    Jca(#[from] JcaError),

    #[error("Admin error: {0}")]
    Admin(#[from] AdminError),

    #[error("IO error: {0}")]
    Io(#[from] std::io::Error),

    #[error("XML parse error: {0}")]
    Xml(String),

    #[error("{0}")]
    Other(String),
}

/// Itemized Verification Receipt proving that an SCM operation succeeded on the LN Server.
#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct VerificationReceipt {
    pub component_name: String,
    pub component_type: String,
    pub operation: String,
    pub status: String,
    pub server_timestamp: String,
    pub version_id: String,
    pub activity_name: String,
    pub activity_guid: String,
    pub receipt_token: String,
    pub raw_summary: String,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub scm_mode: Option<String>,
}

#[derive(Debug, Clone)]
pub struct CheckedOutComponent {
    pub path: PathBuf,
    pub receipt: VerificationReceipt,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct DiscoveredComponent {
    pub name: String,
    pub comp_type: String,
    pub path: PathBuf,
    pub is_extension: bool,
    pub is_checked_out: bool,
    pub is_dirty: bool,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct BatchScmResult {
    pub activity: String,
    pub processed_count: usize,
    pub receipts: Vec<VerificationReceipt>,
    pub segregated_extensions: Vec<DiscoveredComponent>,
    pub extension_guide_markdown: String,
    pub f5_refresh_prompt: String,
}

#[derive(Debug, Clone, Default)]
pub struct ScmMetadata {
    pub label_uuid: String,
    pub base_vrc: String,
    pub task_name: String,
    pub task_description: String,
    pub task_documentation: String,
    pub task_context: String,
    pub development_time_repository_address: String,
    pub development_environment: String,
    pub scm_enabled: bool,
}

/// Generates current UTC ISO 8601 string: YYYY-MM-DDTHH:MM:SSZ
pub fn iso8601_now() -> String {
    let now = SystemTime::now().duration_since(UNIX_EPOCH).unwrap_or_default().as_secs();
    let sec = now % 60;
    let min = (now / 60) % 60;
    let hour = (now / 3600) % 24;

    // Approximate days calculation for UTC timestamp
    let mut days = (now / 86400) as i64;
    // Epoch is 1970-01-01 (Thursday)
    let mut year = 1970;
    loop {
        let is_leap = (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
        let year_days = if is_leap { 366 } else { 365 };
        if days < year_days {
            break;
        }
        days -= year_days;
        year += 1;
    }

    let is_leap = (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
    let month_days = [
        31, if is_leap { 29 } else { 28 }, 31, 30, 31, 30,
        31, 31, 30, 31, 30, 31
    ];

    let mut month = 1;
    for &mdays in &month_days {
        if days < mdays {
            break;
        }
        days -= mdays;
        month += 1;
    }
    let day = days + 1;

    format!("{year:04}-{month:02}-{day:02}T{hour:02}:{min:02}:{sec:02}Z")
}

/// Sets or clears the OS Read-Only attribute on a file.
pub fn set_file_readonly(path: &Path, readonly: bool) -> std::io::Result<()> {
    if !path.exists() {
        return Ok(());
    }
    let mut perms = fs::metadata(path)?.permissions();
    perms.set_readonly(readonly);
    fs::set_permissions(path, perms)?;
    Ok(())
}

/// Checks whether a file exists and has the OS Read-Only flag set.
pub fn is_file_readonly(path: &Path) -> bool {
    if !path.exists() {
        return false;
    }
    if let Ok(meta) = fs::metadata(path) {
        meta.permissions().readonly()
    } else {
        false
    }
}

/// Checks if a component path or identifier represents an Infor LN Extension Modeler component
/// (txess*, txest*, txesb*, txesm*, txesr*, .eso, .eto, .ere, or in library/es* subfolders).
pub fn is_extension_component(name_or_path: &str) -> bool {
    let lower = name_or_path.to_lowercase();
    let p = Path::new(&lower);
    let stem = p.file_stem().and_then(|s| s.to_str()).unwrap_or(&lower);
    let fname = p.file_name().and_then(|s| s.to_str()).unwrap_or(&lower);

    let ext_prefixes = ["txess", "txest", "txesb", "txesm", "txesr"];
    for prefix in &ext_prefixes {
        if fname.starts_with(prefix) || stem.starts_with(prefix) {
            return true;
        }
    }
    if fname.ends_with(".eso") || fname.ends_with(".eto") || fname.ends_with(".ere") {
        return true;
    }

    let posix = lower.replace('\\', "/");
    for ext_type in &["ess", "est", "esb", "esm", "esr"] {
        if posix.contains(&format!("/library/{}/", ext_type))
            || posix.ends_with(&format!("/library/{}", ext_type))
            || posix.contains(&format!("library/{}/", ext_type))
        {
            return true;
        }
    }

    for comp in p.components() {
        if let std::path::Component::Normal(c) = comp {
            if let Some(s) = c.to_str() {
                if matches!(s, "ess" | "est" | "esb" | "esm" | "esr") {
                    return true;
                }
            }
        }
    }

    false
}

/// Enforces the Extension Modeler SCM Boundary (`[GET_ONLY_EXTENSION]` — ADR 0006 & ADR 0020).
pub fn assert_not_extension_for_scm(comp_name: &str, comp_type: &str) -> Result<(), ScmError> {
    let ctype = comp_type.to_lowercase();
    if is_extension_component(comp_name)
        || ctype == "extension"
        || matches!(ctype.as_str(), "ess" | "est" | "esb" | "esm" | "esr")
    {
        return Err(ScmError::GetOnlyExtension(format!(
            "[GET_ONLY_EXTENSION]: Use session ttext1500m000 in LN UI to process extensions (component '{}').",
            comp_name
        )));
    }
    Ok(())
}

/// Resolves SCM metadata for an activity workspace folder.
pub fn resolve_activity_scm_metadata(activity_dir: &Path) -> ScmMetadata {
    let mut meta = ScmMetadata {
        base_vrc: "B61O_a_ext".to_string(),
        scm_enabled: true,
        ..Default::default()
    };

    // 1. Try reading binary PropertyBucket from .metadata or workspace root
    let folder_name = activity_dir.file_name().and_then(|n| n.to_str()).unwrap_or("");
    let mut parent = activity_dir.parent();
    while let Some(p) = parent {
        let meta_idx = p
            .join(".metadata")
            .join(".plugins")
            .join("org.eclipse.core.resources")
            .join(".projects")
            .join(folder_name)
            .join("properties.index");
        if meta_idx.exists() {
            if let Ok(bucket) = PropertyBucket::load_from_path(&meta_idx) {
                for (_res, map) in &bucket.entries {
                    for ((_qual, name), val) in map {
                        match name.as_str() {
                            "Label" => meta.label_uuid = val.clone(),
                            "ApplicationRelease" | "baseVRC" => meta.base_vrc = val.clone(),
                            "TaskName" => meta.task_name = val.clone(),
                            "TaskDescription" => meta.task_description = val.clone(),
                            "TaskDocumentation" => meta.task_documentation = val.clone(),
                            "DevelopmentTimeRepositoryAddress" => {
                                meta.development_time_repository_address = val.clone();
                                if meta.task_context.is_empty() {
                                    meta.task_context = val.clone();
                                }
                            }
                            "TaskContext" => {
                                if meta.task_context.is_empty() {
                                    meta.task_context = val.clone();
                                }
                            }
                            "DevelopmentEnvironment" => meta.development_environment = val.clone(),
                            "ApplicationUsesSCM" | "ApplicationUseSCM" => {
                                if val.eq_ignore_ascii_case("no") || val.eq_ignore_ascii_case("false") {
                                    meta.scm_enabled = false;
                                }
                            }
                            _ => {}
                        }
                    }
                }
                break;
            }
        }
        parent = p.parent();
    }

    // 2. Fallback to reading text properties.index in .settings/
    let settings_idx = activity_dir.join(".settings").join("properties.index");
    if settings_idx.exists() {
        if let Ok(content) = fs::read_to_string(&settings_idx) {
            for line in content.lines() {
                if let Some((k, v)) = line.split_once('=') {
                    let k = k.trim();
                    let v = v.trim();
                    match k {
                        "activityUUID" | "Label" => if meta.label_uuid.is_empty() { meta.label_uuid = v.to_string(); },
                        "ApplicationRelease" | "baseVRC" => if meta.base_vrc.is_empty() { meta.base_vrc = v.to_string(); },
                        "TaskName" | "taskName" => if meta.task_name.is_empty() { meta.task_name = v.to_string(); },
                        "TaskDescription" => if meta.task_description.is_empty() { meta.task_description = v.to_string(); },
                        "TaskDocumentation" => if meta.task_documentation.is_empty() { meta.task_documentation = v.to_string(); },
                        "connectionPoint" | "TaskContext" => if meta.task_context.is_empty() { meta.task_context = v.to_string(); },
                        "DevelopmentTimeRepositoryAddress" => if meta.development_time_repository_address.is_empty() { meta.development_time_repository_address = v.to_string(); },
                        "ApplicationUsesSCM" | "ApplicationUseSCM" => {
                            if v.eq_ignore_ascii_case("no") || v.eq_ignore_ascii_case("false") {
                                meta.scm_enabled = false;
                            }
                        }
                        _ => {}
                    }
                }
            }
        }
    }

    // 3. Fallback to folder name parsing "<task> [<project>]"
    if meta.task_name.is_empty() {
        if let Some(space_idx) = folder_name.find(' ') {
            meta.task_name = folder_name[..space_idx].trim_matches(|c| c == '[' || c == ']').to_string();
        } else {
            meta.task_name = folder_name.trim_matches(|c| c == '[' || c == ']').to_string();
        }
    }
    if meta.label_uuid.is_empty() {
        meta.label_uuid = meta.task_name.clone();
    }
    if meta.task_context.is_empty() {
        if folder_name.contains('[') && folder_name.contains(']') {
            let start = folder_name.find('[').unwrap();
            let end = folder_name.find(']').unwrap();
            let proj = folder_name[start + 1..end].trim();
            meta.task_context = format!("{proj}_dev");
        }
    }
    if meta.development_time_repository_address.is_empty() {
        meta.development_time_repository_address = meta.task_context.clone();
    }

    meta
}

/// Checks if SCM is enabled for this activity.
pub fn is_project_scm_enabled(activity_dir: &Path) -> (bool, String) {
    let meta = resolve_activity_scm_metadata(activity_dir);
    if !meta.scm_enabled {
        (false, "ApplicationUsesSCM=no".to_string())
    } else {
        (true, "SCM enabled".to_string())
    }
}

/// Generates authentic `<ActivityID>` XML envelope:
pub fn build_activity_context_xml(
    activity_name: &str,
    base_vrc: &str,
    connection_point: &str,
    activity_guid: Option<&str>,
    description: &str,
    documentation: Option<&str>,
) -> String {
    let guid = activity_guid.unwrap_or(activity_name);
    let mut parts = format!(
        "<ActivityID>\
           <activityName>{activity_name}</activityName>\
           <activityDescription>{description}</activityDescription>\
           <activityUUID>{guid}</activityUUID>\
           <baseVRC>{base_vrc}</baseVRC>\
           <activityContext>{connection_point}</activityContext>"
    );
    if let Some(doc) = documentation {
        parts.push_str(&format!("<documentation>{doc}</documentation>"));
    }
    parts.push_str("</ActivityID>");
    parts
}

/// Generates authentic CheckOut request XML:
pub fn build_checkout_payload(
    bde_name: &str,
    comp_name: &str,
    comp_type: &str,
    base_vrc: &str,
    activity_name: &str,
    task_label: Option<&str>,
) -> String {
    let lbl = task_label.unwrap_or(activity_name);
    format!(
        "<{bde_name}>\n\
         \x20\x20<name>{comp_name}</name>\n\
         \x20\x20<type>{comp_type}</type>\n\
         \x20\x20<versionID>{base_vrc}</versionID>\n\
         \x20\x20<taskLabel>{lbl}</taskLabel>\n\
         \x20\x20<taskName>{activity_name}</taskName>\n\
         \x20\x20<optionalContent>yes</optionalContent>\n\
         </{bde_name}>"
    )
}

/// Generates authentic UndoCheckOut request XML:
pub fn build_uncheckout_payload(
    bde_name: &str,
    comp_name: &str,
    comp_type: &str,
) -> String {
    format!(
        "<{bde_name}>\n\
         \x20\x20<name>{comp_name}</name>\n\
         \x20\x20<type>{comp_type}</type>\n\
         \x20\x20<versionID>see Activity ID</versionID>\n\
         \x20\x20<optionalContent>yes</optionalContent>\n\
         </{bde_name}>"
    )
}

/// Generates authentic CheckIn request XML by injecting/updating
/// `<Version><documentation>{comment}</documentation></Version>`.
pub fn build_checkin_payload(raw_xml: &str, comment: &str) -> Result<String, ScmError> {
    let raw = raw_xml.trim();
    if raw.is_empty() {
        return Err(ScmError::Other("Cannot build CheckIn payload from empty component definition".to_string()));
    }

    let escaped_comment = escape_xml(comment);

    // If <Version> tag is already present in raw_xml
    if let Some(v_start) = raw.find("<Version>") {
        if let Some(v_end_rel) = raw[v_start..].find("</Version>") {
            let v_end = v_start + v_end_rel;
            let version_block = &raw[v_start..v_end];
            if version_block.contains("<documentation>") {
                // Replace existing documentation
                let re = Regex::new(r"(?s)<documentation>.*?</documentation>").unwrap();
                let new_v = re.replace(version_block, format!("<documentation>{}</documentation>", escaped_comment));
                let mut out = String::with_capacity(raw.len() + escaped_comment.len());
                out.push_str(&raw[..v_start]);
                out.push_str(&new_v);
                out.push_str(&raw[v_end..]);
                return Ok(out);
            } else {
                // Insert <documentation> into existing <Version>
                let insert_pos = v_start + "<Version>".len();
                let mut out = String::with_capacity(raw.len() + escaped_comment.len() + 32);
                out.push_str(&raw[..insert_pos]);
                out.push_str(&format!("<documentation>{}</documentation>", escaped_comment));
                out.push_str(&raw[insert_pos..]);
                return Ok(out);
            }
        }
    }

    // Insert <Version><documentation>...</documentation></Version> before closing root tag
    if let Some(last_close) = raw.rfind("</") {
        let version_tag = format!("  <Version><documentation>{}</documentation></Version>\n", escaped_comment);
        let mut out = String::with_capacity(raw.len() + version_tag.len());
        out.push_str(&raw[..last_close]);
        out.push_str(&version_tag);
        out.push_str(&raw[last_close..]);
        Ok(out)
    } else {
        Ok(format!("{}\n<Version><documentation>{}</documentation></Version>", raw, escaped_comment))
    }
}

/// Verifies that an Infor LN server SCM response represents true success.
/// Raises ServerExecution error immediately if any error indicator is detected.
pub fn parse_scm_receipt(
    response_xml: &str,
    comp_name: &str,
    comp_type: &str,
    operation: &str,
    activity_name: &str,
    activity_guid: &str,
    base_vrc: &str,
) -> Result<VerificationReceipt, ScmError> {
    let raw = response_xml.trim();
    if raw.is_empty() {
        return Err(ScmError::ServerExecution {
            component_name: comp_name.to_string(),
            operation: operation.to_string(),
            message: format!("Server returned empty response for {operation} on '{comp_name}'"),
            raw_response: String::new(),
        });
    }

    // 1. Detect known server error keywords and exceptions
    let error_indicators = [
        "xml handling error",
        "jcabderesultexception",
        "lock conflict",
        "is not checked out",
        "action not allowed",
        "bdeexecutionerror",
    ];
    let raw_lower = raw.to_lowercase();
    for ind in error_indicators {
        if raw_lower.contains(ind) {
            return Err(ScmError::ServerExecution {
                component_name: comp_name.to_string(),
                operation: operation.to_string(),
                message: format!("[SCM_SERVER_ERROR] Infor LN Server rejected {operation} on '{comp_name}': {ind}"),
                raw_response: raw.to_string(),
            });
        }
    }

    // 2. Parse XML and check root tag
    let tree = parse_xml_to_tree(raw).map_err(|e| ScmError::ServerExecution {
        component_name: comp_name.to_string(),
        operation: operation.to_string(),
        message: format!("Invalid XML returned by server for {operation} on '{comp_name}': {e}"),
        raw_response: raw.to_string(),
    })?;

    let root_tag = tree.tag.to_lowercase();
    if root_tag == "error" || root_tag == "fault" || root_tag == "exception" {
        let msg = tree.find_text("message")
            .or_else(|| tree.find_text("description"))
            .unwrap_or(raw);
        return Err(ScmError::ServerExecution {
            component_name: comp_name.to_string(),
            operation: operation.to_string(),
            message: format!("[SCM_SERVER_ERROR] Server returned error for {operation} on '{comp_name}': {msg}"),
            raw_response: raw.to_string(),
        });
    }

    // 3. Extract version ID
    let version_id = tree.find_text("versionID")
        .or_else(|| tree.find_text("revision"))
        .or_else(|| tree.attr("versionID"))
        .unwrap_or(base_vrc)
        .trim()
        .to_string();

    // 4. Extract server timestamp
    let server_ts = tree.find_text("dateTime")
        .or_else(|| tree.find_text("timestamp"))
        .or_else(|| tree.find_text("serverTimestamp"))
        .map(|s| s.to_string())
        .unwrap_or_else(iso8601_now);

    // 5. Generate receipt token: first 16 hex chars of SHA-256
    let mut hasher = Sha256::new();
    hasher.update(raw.as_bytes());
    let hash_result = hasher.finalize();
    let receipt_token = format!("{:x}", hash_result)[..16].to_string();

    let raw_summary = if raw.len() > 200 {
        raw[..200].replace('\n', " ").trim().to_string()
    } else {
        raw.replace('\n', " ").trim().to_string()
    };

    Ok(VerificationReceipt {
        component_name: comp_name.to_string(),
        component_type: comp_type.to_string(),
        operation: operation.to_string(),
        status: "SUCCESS".to_string(),
        server_timestamp: server_ts,
        version_id,
        activity_name: activity_name.to_string(),
        activity_guid: activity_guid.to_string(),
        receipt_token,
        raw_summary,
        scm_mode: None,
    })
}

// Re-export find_component_file from activity
pub use crate::activity::find_component_file;

/// Determines the target path for writing a component (defaults to Native Single-XML TDE layout).
pub fn get_target_component_path(activity_dir: &Path, comp_name: &str, comp_type: &str) -> PathBuf {
    if let Some(existing) = find_component_file(activity_dir, comp_name, comp_type) {
        return existing;
    }
    let info = get_bde_type_info(comp_type);
    let ext = info.map(|i| i.ext).unwrap_or(".xml");
    let rel = resolve_tde_relative_path(comp_type, comp_name, ext)
        .unwrap_or_else(|_| PathBuf::from(format!("{comp_name}{ext}")));
    let p = activity_dir.join(rel);
    if let Some(parent) = p.parent() {
        let _ = fs::create_dir_all(parent);
    }
    p
}

/// Hard-blocks automated End Activity / Commit Activity per ADR 0007 governance.
pub fn end_activity_gate(project_name: &str, task_id: &str) -> Result<(), ScmError> {
    Err(ScmError::PreCommitBoundary {
        project_name: project_name.to_string(),
        activity_id: task_id.to_string(),
    })
}

/// Checks out a component on the Infor LN Server via authentic BDE `DR_*.CheckOut`,
/// downloads authentic XML, clears OS Read-Only flag, updates `.admin`, and returns `VerificationReceipt`.
pub async fn checkout_component(
    client: &HttpClient,
    comp_type: &str,
    comp_name: &str,
    activity_dir: &Path,
    project_name: &str,
    base_vrc: Option<&str>,
    dev_connection: Option<&str>,
) -> Result<CheckedOutComponent, ScmError> {
    // 1. ADR 0006 & ADR 0020 Guardrail: Extension Modeler components blocked from SCM checkout
    assert_not_extension_for_scm(comp_name, comp_type)?;

    let info = get_bde_type_info(comp_type)
        .ok_or_else(|| ScmError::Other(format!("Unsupported component type '{comp_type}'")))?;
    let bde_name = info.bde;

    let meta = resolve_activity_scm_metadata(activity_dir);
    let task_id = if !meta.task_name.is_empty() { meta.task_name } else { "Activity".to_string() };
    let label_uuid = if !meta.label_uuid.is_empty() { meta.label_uuid } else { task_id.clone() };
    let eff_base_vrc = base_vrc.unwrap_or(if !meta.base_vrc.is_empty() { &meta.base_vrc } else { "B61O_a_ext" });
    let default_dev_cp = format!("{project_name}_dev");
    let dev_cp = dev_connection.unwrap_or(if !meta.task_context.is_empty() { &meta.task_context } else { &default_dev_cp });

    let (scm_enabled, reason) = is_project_scm_enabled(activity_dir);
    let target_file = get_target_component_path(activity_dir, comp_name, comp_type);

    if !scm_enabled {
        let _ = set_file_readonly(&target_file, false);
        let rel_path = target_file.strip_prefix(activity_dir).unwrap_or(&target_file).to_string_lossy().to_string();
        let admin_path = activity_dir.join(".admin");
        let mut admin = AdminFile::load_from_path(&admin_path).unwrap_or_default();
        admin.after_checkout(&rel_path);
        let _ = admin.save_to_path(&admin_path);

        let mut hasher = Sha256::new();
        hasher.update(format!("NON_SCM_CKO:{comp_name}:{task_id}").as_bytes());
        let token = format!("{:x}", hasher.finalize())[..16].to_string();

        let receipt = VerificationReceipt {
            component_name: comp_name.to_string(),
            component_type: comp_type.to_string(),
            operation: "CheckOut".to_string(),
            status: "SUCCESS".to_string(),
            server_timestamp: iso8601_now(),
            version_id: eff_base_vrc.to_string(),
            activity_name: task_id,
            activity_guid: label_uuid,
            receipt_token: token,
            raw_summary: format!("Non-SCM project ({reason}): SCM server lock skipped; component is writable locally."),
            scm_mode: Some("NON_SCM".to_string()),
        };

        return Ok(CheckedOutComponent {
            path: target_file,
            receipt,
        });
    }

    let req_xml = build_checkout_payload(
        bde_name,
        comp_name,
        comp_type,
        eff_base_vrc,
        &task_id,
        Some(&label_uuid),
    );
    let context_xml = build_activity_context_xml(
        &task_id,
        eff_base_vrc,
        dev_cp,
        Some(&label_uuid),
        &meta.task_description,
        None,
    );

    let mgr = JcaBdeManager::new(client, "");
    let params = BdeParams {
        bde_name: bde_name.to_string(),
        method_name: "CheckOut".to_string(),
        mode: Some(BdeExecutionMode::Bde),
        request_xml: Some(req_xml),
        context_xml: Some(context_xml),
        ..Default::default()
    };

    let resp_xml = mgr.execute(&params).await?;

    // Parse and verify server receipt BEFORE modifying local file or .admin
    let receipt = parse_scm_receipt(
        &resp_xml,
        comp_name,
        comp_type,
        "CheckOut",
        &task_id,
        &label_uuid,
        eff_base_vrc,
    )?;

    // Write verified server content to target file and clear OS Read-Only attribute
    let _ = set_file_readonly(&target_file, false);
    fs::write(&target_file, &resp_xml)?;
    let _ = set_file_readonly(&target_file, false);

    // Update .admin SCM cache
    let rel_path = target_file.strip_prefix(activity_dir).unwrap_or(&target_file).to_string_lossy().to_string();
    let admin_path = activity_dir.join(".admin");
    let mut admin = AdminFile::load_from_path(&admin_path).unwrap_or_default();
    admin.after_checkout(&rel_path);
    let _ = admin.save_to_path(&admin_path);

    Ok(CheckedOutComponent {
        path: target_file,
        receipt,
    })
}

/// Reverts a checked-out component via `DR_*.UndoCheckOut`, sets local file to Read-Only,
/// and updates `.admin` with `after_uncheckout`. Returns `VerificationReceipt`.
pub async fn uncheckout_component(
    client: &HttpClient,
    comp_type: &str,
    comp_name: &str,
    activity_dir: &Path,
    project_name: &str,
    base_vrc: Option<&str>,
    dev_connection: Option<&str>,
) -> Result<VerificationReceipt, ScmError> {
    let info = get_bde_type_info(comp_type)
        .ok_or_else(|| ScmError::Other(format!("Unsupported component type '{comp_type}'")))?;
    let bde_name = info.bde;

    let meta = resolve_activity_scm_metadata(activity_dir);
    let task_id = if !meta.task_name.is_empty() { meta.task_name } else { "Activity".to_string() };
    let label_uuid = if !meta.label_uuid.is_empty() { meta.label_uuid } else { task_id.clone() };
    let eff_base_vrc = base_vrc.unwrap_or(if !meta.base_vrc.is_empty() { &meta.base_vrc } else { "B61O_a_ext" });
    let default_dev_cp = format!("{project_name}_dev");
    let dev_cp = dev_connection.unwrap_or(if !meta.task_context.is_empty() { &meta.task_context } else { &default_dev_cp });

    let (scm_enabled, reason) = is_project_scm_enabled(activity_dir);
    let target_file = find_component_file(activity_dir, comp_name, comp_type);

    if !scm_enabled {
        if let Some(ref tf) = target_file {
            let _ = set_file_readonly(tf, true);
            let rel_path = tf.strip_prefix(activity_dir).unwrap_or(tf).to_string_lossy().to_string();
            let admin_path = activity_dir.join(".admin");
            let mut admin = AdminFile::load_from_path(&admin_path).unwrap_or_default();
            admin.after_uncheckout(&rel_path);
            let _ = admin.save_to_path(&admin_path);
        }

        let mut hasher = Sha256::new();
        hasher.update(format!("NON_SCM_UNCKO:{comp_name}:{task_id}").as_bytes());
        let token = format!("{:x}", hasher.finalize())[..16].to_string();

        return Ok(VerificationReceipt {
            component_name: comp_name.to_string(),
            component_type: comp_type.to_string(),
            operation: "UndoCheckOut".to_string(),
            status: "SUCCESS".to_string(),
            server_timestamp: iso8601_now(),
            version_id: eff_base_vrc.to_string(),
            activity_name: task_id,
            activity_guid: label_uuid,
            receipt_token: token,
            raw_summary: format!("Non-SCM project ({reason}): Reverted local checkout state in .admin."),
            scm_mode: Some("NON_SCM".to_string()),
        });
    }

    let req_xml = build_uncheckout_payload(bde_name, comp_name, comp_type);
    let context_xml = build_activity_context_xml(
        &task_id,
        eff_base_vrc,
        dev_cp,
        Some(&label_uuid),
        &meta.task_description,
        None,
    );

    let mgr = JcaBdeManager::new(client, "");
    let params = BdeParams {
        bde_name: bde_name.to_string(),
        method_name: "UndoCheckOut".to_string(),
        mode: Some(BdeExecutionMode::Bde),
        request_xml: Some(req_xml),
        context_xml: Some(context_xml),
        ..Default::default()
    };

    let resp_xml = mgr.execute(&params).await?;

    let receipt = parse_scm_receipt(
        &resp_xml,
        comp_name,
        comp_type,
        "UndoCheckOut",
        &task_id,
        &label_uuid,
        eff_base_vrc,
    )?;

    if let Some(ref tf) = target_file {
        let _ = set_file_readonly(tf, true);
        let rel_path = tf.strip_prefix(activity_dir).unwrap_or(tf).to_string_lossy().to_string();
        let admin_path = activity_dir.join(".admin");
        let mut admin = AdminFile::load_from_path(&admin_path).unwrap_or_default();
        admin.after_uncheckout(&rel_path);
        let _ = admin.save_to_path(&admin_path);
    }

    Ok(receipt)
}

/// Uploads modified component XML to server Activity workarea via `DR_*.Put`
/// with Pre-Put Script Merge & Non-Empty Source Guardrail (`ln-model`), updating `.admin` via `after_put`.
pub async fn put_component(
    client: &HttpClient,
    comp_type: &str,
    comp_name: &str,
    activity_dir: &Path,
    project_name: &str,
    base_vrc: Option<&str>,
    dev_connection: Option<&str>,
) -> Result<VerificationReceipt, ScmError> {
    assert_not_extension_for_scm(comp_name, comp_type)?;

    let info = get_bde_type_info(comp_type)
        .ok_or_else(|| ScmError::Other(format!("Unsupported component type '{comp_type}'")))?;
    let bde_name = info.bde;

    let target_file = find_component_file(activity_dir, comp_name, comp_type)
        .ok_or_else(|| ScmError::FileNotFound(format!("Component file not found for '{comp_name}' in {:?}", activity_dir)))?;

    if is_file_readonly(&target_file) {
        return Err(ScmError::ReadOnlyComponent(comp_name.to_string()));
    }

    let meta = resolve_activity_scm_metadata(activity_dir);
    let task_id = if !meta.task_name.is_empty() { meta.task_name } else { "Activity".to_string() };
    let label_uuid = if !meta.label_uuid.is_empty() { meta.label_uuid } else { task_id.clone() };
    let eff_base_vrc = base_vrc.unwrap_or(if !meta.base_vrc.is_empty() { &meta.base_vrc } else { "B61O_a_ext" });
    let default_dev_cp = format!("{project_name}_dev");
    let dev_cp = dev_connection.unwrap_or(if !meta.task_context.is_empty() { &meta.task_context } else { &default_dev_cp });

    // Pre-Put Script Merge & Non-Empty Source Guardrail
    let content = pre_put_merge_and_guard(&target_file, comp_name, comp_type, activity_dir)?;

    let context_xml = build_activity_context_xml(
        &task_id,
        eff_base_vrc,
        dev_cp,
        Some(&label_uuid),
        &meta.task_description,
        None,
    );

    let mgr = JcaBdeManager::new(client, "");
    let params = BdeParams {
        bde_name: bde_name.to_string(),
        method_name: "Put".to_string(),
        mode: Some(BdeExecutionMode::Bde),
        request_xml: Some(content),
        context_xml: Some(context_xml),
        ..Default::default()
    };

    let resp_xml = mgr.execute(&params).await?;

    let receipt = parse_scm_receipt(
        &resp_xml,
        comp_name,
        comp_type,
        "Put",
        &task_id,
        &label_uuid,
        eff_base_vrc,
    )?;

    // Update .admin after_put
    let rel_path = target_file.strip_prefix(activity_dir).unwrap_or(&target_file).to_string_lossy().to_string();
    let admin_path = activity_dir.join(".admin");
    let mut admin = AdminFile::load_from_path(&admin_path).unwrap_or_default();
    admin.after_put(&rel_path);
    let _ = admin.save_to_path(&admin_path);

    Ok(receipt)
}

/// Checks in a component via `DR_*.CheckIn` with Pre-Put Script Merge & Non-Empty Source Guardrail,
/// sets local file to Read-Only, and updates `.admin` via `after_checkin`. Returns `VerificationReceipt`.
pub async fn checkin_component(
    client: &HttpClient,
    comp_type: &str,
    comp_name: &str,
    activity_dir: &Path,
    project_name: &str,
    comment: &str,
    base_vrc: Option<&str>,
    dev_connection: Option<&str>,
) -> Result<VerificationReceipt, ScmError> {
    assert_not_extension_for_scm(comp_name, comp_type)?;

    let info = get_bde_type_info(comp_type)
        .ok_or_else(|| ScmError::Other(format!("Unsupported component type '{comp_type}'")))?;
    let bde_name = info.bde;

    let target_file = find_component_file(activity_dir, comp_name, comp_type)
        .ok_or_else(|| ScmError::FileNotFound(format!("Component file not found for '{comp_name}' in {:?}", activity_dir)))?;

    let meta = resolve_activity_scm_metadata(activity_dir);
    let task_id = if !meta.task_name.is_empty() { meta.task_name } else { "Activity".to_string() };
    let label_uuid = if !meta.label_uuid.is_empty() { meta.label_uuid } else { task_id.clone() };
    let eff_base_vrc = base_vrc.unwrap_or(if !meta.base_vrc.is_empty() { &meta.base_vrc } else { "B61O_a_ext" });
    let default_dev_cp = format!("{project_name}_dev");
    let dev_cp = dev_connection.unwrap_or(if !meta.task_context.is_empty() { &meta.task_context } else { &default_dev_cp });

    // Pre-Put Script Merge & Non-Empty Source Guardrail
    let content = pre_put_merge_and_guard(&target_file, comp_name, comp_type, activity_dir)?;
    let req_xml = build_checkin_payload(&content, comment)?;

    let (scm_enabled, reason) = is_project_scm_enabled(activity_dir);
    if !scm_enabled {
        fs::write(&target_file, &req_xml)?;
        let _ = set_file_readonly(&target_file, true);
        let rel_path = target_file.strip_prefix(activity_dir).unwrap_or(&target_file).to_string_lossy().to_string();
        let admin_path = activity_dir.join(".admin");
        let mut admin = AdminFile::load_from_path(&admin_path).unwrap_or_default();
        admin.after_checkin(&rel_path);
        let _ = admin.save_to_path(&admin_path);

        let mut hasher = Sha256::new();
        hasher.update(format!("NON_SCM_CKI:{comp_name}:{comment}").as_bytes());
        let token = format!("{:x}", hasher.finalize())[..16].to_string();

        return Ok(VerificationReceipt {
            component_name: comp_name.to_string(),
            component_type: comp_type.to_string(),
            operation: "CheckIn".to_string(),
            status: "SUCCESS".to_string(),
            server_timestamp: iso8601_now(),
            version_id: eff_base_vrc.to_string(),
            activity_name: task_id,
            activity_guid: label_uuid,
            receipt_token: token,
            raw_summary: format!("Non-SCM project ({reason}): Embedded check-in documentation into component definition."),
            scm_mode: Some("NON_SCM".to_string()),
        });
    }

    let context_xml = build_activity_context_xml(
        &task_id,
        eff_base_vrc,
        dev_cp,
        Some(&label_uuid),
        &meta.task_description,
        Some(comment),
    );

    let mgr = JcaBdeManager::new(client, "");
    let params = BdeParams {
        bde_name: bde_name.to_string(),
        method_name: "CheckIn".to_string(),
        mode: Some(BdeExecutionMode::Bde),
        request_xml: Some(req_xml),
        context_xml: Some(context_xml),
        ..Default::default()
    };

    let resp_xml = mgr.execute(&params).await?;

    let receipt = parse_scm_receipt(
        &resp_xml,
        comp_name,
        comp_type,
        "CheckIn",
        &task_id,
        &label_uuid,
        eff_base_vrc,
    )?;

    // Set OS Read-Only upon verified server success
    let _ = set_file_readonly(&target_file, true);

    let rel_path = target_file.strip_prefix(activity_dir).unwrap_or(&target_file).to_string_lossy().to_string();
    let admin_path = activity_dir.join(".admin");
    let mut admin = AdminFile::load_from_path(&admin_path).unwrap_or_default();
    admin.after_checkin(&rel_path);
    let _ = admin.save_to_path(&admin_path);

    Ok(receipt)
}

/// Infers component type from file extension.
pub fn get_component_type_from_extension(ext: &str) -> Option<String> {
    let norm = ext.to_lowercase();
    for &ct in DEPENDENCY_ORDER {
        if let Some(info) = get_bde_type_info(ct) {
            if info.ext.to_lowercase() == norm {
                return Some(ct.to_string());
            }
        }
    }
    match norm.as_str() {
        ".tbl" => Some("table".to_string()),
        ".ses" => Some("session".to_string()),
        ".lib" => Some("library".to_string()),
        ".dmn" => Some("domain".to_string()),
        ".lbl" => Some("label".to_string()),
        ".mnu" => Some("menu".to_string()),
        ".rpt" => Some("report".to_string()),
        ".msg" => Some("message".to_string()),
        ".qst" | ".que" => Some("question".to_string()),
        ".fnc" | ".fun" => Some("function".to_string()),
        ".add" => Some("additional".to_string()),
        _ => None,
    }
}

/// Scans the activity workspace directory and returns modified / dirty components.
pub fn discover_dirty_components(activity_dir: &Path) -> Vec<DiscoveredComponent> {
    let mut map: HashMap<String, DiscoveredComponent> = HashMap::new();

    // 1. Inspect .admin cache
    let admin_path = activity_dir.join(".admin");
    if let Ok(admin) = AdminFile::load_from_path(&admin_path) {
        for (rel_path, comp) in &admin.entries {
            if comp.is_checked_out || comp.is_dirty {
                let full = activity_dir.join(rel_path);
                let ext = full.extension().and_then(|e| e.to_str()).map(|e| format!(".{}", e)).unwrap_or_default();
                if let Some(c_type) = get_component_type_from_extension(&ext) {
                    let stem = full.file_stem().and_then(|s| s.to_str()).unwrap_or("").to_string();
                    let is_ext = is_extension_component(&stem) || c_type == "extension";
                    map.insert(stem.clone(), DiscoveredComponent {
                        name: stem,
                        comp_type: c_type,
                        path: full,
                        is_extension: is_ext,
                        is_checked_out: comp.is_checked_out,
                        is_dirty: comp.is_dirty,
                    });
                }
            }
        }
    }

    // 2. Discover writable files on disk across managed extensions
    scan_writable_components(activity_dir, activity_dir, &mut map);

    let mut result: Vec<DiscoveredComponent> = map.into_values().collect();
    result.sort_by_key(|c| {
        let ct = c.comp_type.to_lowercase();
        DEPENDENCY_ORDER.iter().position(|&d| d == ct).unwrap_or(99)
    });

    result
}

fn scan_writable_components(root: &Path, current: &Path, map: &mut HashMap<String, DiscoveredComponent>) {
    if let Ok(entries) = fs::read_dir(current) {
        for entry in entries.flatten() {
            let p = entry.path();
            if p.is_dir() {
                if let Some(name) = p.file_name().and_then(|n| n.to_str()) {
                    if !name.starts_with('.') {
                        scan_writable_components(root, &p, map);
                    }
                }
            } else if p.is_file() {
                let ext = p.extension().and_then(|e| e.to_str()).map(|e| format!(".{}", e)).unwrap_or_default();
                if let Some(c_type) = get_component_type_from_extension(&ext) {
                    let stem = p.file_stem().and_then(|s| s.to_str()).unwrap_or("").to_string();
                    if !map.contains_key(&stem) && !is_file_readonly(&p) {
                        let is_ext = is_extension_component(&stem) || c_type == "extension";
                        map.insert(stem.clone(), DiscoveredComponent {
                            name: stem,
                            comp_type: c_type,
                            path: p,
                            is_extension: is_ext,
                            is_checked_out: true,
                            is_dirty: true,
                        });
                    }
                }
            }
        }
    }
}

/// Segregates components into standard SCM components vs Extension Modeler components (ADR 0006).
pub fn segregate_extension_components(
    components: Vec<DiscoveredComponent>,
) -> (Vec<DiscoveredComponent>, Vec<DiscoveredComponent>) {
    let mut standard = Vec::new();
    let mut extensions = Vec::new();

    for c in components {
        if c.is_extension || is_extension_component(&c.name) || c.comp_type.eq_ignore_ascii_case("extension") {
            extensions.push(c);
        } else {
            standard.push(c);
        }
    }

    (standard, extensions)
}

/// Generates Guide-and-Paste Markdown documentation for LN UI session `ttext1500m000` (ADR 0006).
pub fn format_extension_guide_markdown(segregated: &[DiscoveredComponent]) -> String {
    if segregated.is_empty() {
        return String::new();
    }

    let mut lines = Vec::new();
    lines.push("### Infor LN Extension Modeler Guide-and-Paste (ADR 0006)".to_string());
    lines.push("The following extension components are segregated from LN Studio BDE SCM.".to_string());
    lines.push("Please open Infor LN UI, navigate to session `ttext1500m000` (Extension Modeler), and paste the code:\n".to_string());

    for ext in segregated {
        let code = fs::read_to_string(&ext.path).unwrap_or_default();
        lines.push(format!("#### Extension Component: `{}`", ext.name));
        lines.push("- **Target Session**: `ttext1500m000`".to_string());
        lines.push(format!("- **File Location**: `{}`", ext.path.to_string_lossy()));
        lines.push("```4gl".to_string());
        lines.push(code.trim().to_string());
        lines.push("```\n".to_string());
    }

    lines.join("\n")
}

/// Batch Check-Out for all components in an activity.
/// Iterates in architectural dependency order and halts immediately on first failure.
pub async fn checkout_activity(
    client: &HttpClient,
    activity_dir: &Path,
    project_name: &str,
    base_vrc: Option<&str>,
    dev_connection: Option<&str>,
    filter_components: Option<&[(String, String)]>,
) -> Result<BatchScmResult, ScmError> {
    let meta = resolve_activity_scm_metadata(activity_dir);
    let task_id = if !meta.task_name.is_empty() { meta.task_name } else { "Activity".to_string() };

    let comps = if let Some(fc) = filter_components {
        let mut list = Vec::new();
        for (c_type, c_name) in fc {
            let target_file = get_target_component_path(activity_dir, c_name, c_type);
            let is_ext = is_extension_component(c_name) || c_type == "extension";
            list.push(DiscoveredComponent {
                name: c_name.clone(),
                comp_type: c_type.clone(),
                path: target_file,
                is_extension: is_ext,
                is_checked_out: false,
                is_dirty: false,
            });
        }
        list
    } else {
        let dirty = discover_dirty_components(activity_dir);
        if dirty.is_empty() {
            // Find all managed components on disk
            let mut all_map = HashMap::new();
            scan_all_managed_components(activity_dir, activity_dir, &mut all_map);
            let mut all: Vec<_> = all_map.into_values().collect();
            all.sort_by_key(|c| {
                let ct = c.comp_type.to_lowercase();
                DEPENDENCY_ORDER.iter().position(|&d| d == ct).unwrap_or(99)
            });
            all
        } else {
            dirty
        }
    };

    let (standard, extensions) = segregate_extension_components(comps);
    let mut receipts = Vec::new();

    for comp in &standard {
        let res = checkout_component(
            client,
            &comp.comp_type,
            &comp.name,
            activity_dir,
            project_name,
            base_vrc,
            dev_connection,
        ).await?;
        receipts.push(res.receipt);
    }

    let guide_md = format_extension_guide_markdown(&extensions);

    Ok(BatchScmResult {
        activity: task_id,
        processed_count: receipts.len(),
        receipts,
        segregated_extensions: extensions,
        extension_guide_markdown: guide_md,
        f5_refresh_prompt: "Please press F5 (Refresh) in Infor LN Studio (Eclipse) to display updated server checkout status.".to_string(),
    })
}

/// Batch Check-In for all modified components in an activity with a single comment.
/// Automatically segregates Extension Modeler components (ADR 0006).
/// Iterates in architectural dependency order and halts immediately on first failure.
pub async fn checkin_activity(
    client: &HttpClient,
    activity_dir: &Path,
    project_name: &str,
    comment: &str,
    base_vrc: Option<&str>,
    dev_connection: Option<&str>,
    filter_components: Option<&[(String, String)]>,
) -> Result<BatchScmResult, ScmError> {
    let meta = resolve_activity_scm_metadata(activity_dir);
    let task_id = if !meta.task_name.is_empty() { meta.task_name } else { "Activity".to_string() };

    let comps = if let Some(fc) = filter_components {
        let mut list = Vec::new();
        for (c_type, c_name) in fc {
            let target_file = get_target_component_path(activity_dir, c_name, c_type);
            let is_ext = is_extension_component(c_name) || c_type == "extension";
            list.push(DiscoveredComponent {
                name: c_name.clone(),
                comp_type: c_type.clone(),
                path: target_file,
                is_extension: is_ext,
                is_checked_out: true,
                is_dirty: true,
            });
        }
        list
    } else {
        discover_dirty_components(activity_dir)
    };

    let (standard, extensions) = segregate_extension_components(comps);
    let mut receipts = Vec::new();

    for comp in &standard {
        let r = checkin_component(
            client,
            &comp.comp_type,
            &comp.name,
            activity_dir,
            project_name,
            comment,
            base_vrc,
            dev_connection,
        ).await?;
        receipts.push(r);
    }

    let guide_md = format_extension_guide_markdown(&extensions);

    Ok(BatchScmResult {
        activity: task_id,
        processed_count: receipts.len(),
        receipts,
        segregated_extensions: extensions,
        extension_guide_markdown: guide_md,
        f5_refresh_prompt: "Please press F5 (Refresh) in Infor LN Studio (Eclipse) to display updated server checkin status.".to_string(),
    })
}

fn scan_all_managed_components(root: &Path, current: &Path, map: &mut HashMap<String, DiscoveredComponent>) {
    if let Ok(entries) = fs::read_dir(current) {
        for entry in entries.flatten() {
            let p = entry.path();
            if p.is_dir() {
                if let Some(name) = p.file_name().and_then(|n| n.to_str()) {
                    if !name.starts_with('.') {
                        scan_all_managed_components(root, &p, map);
                    }
                }
            } else if p.is_file() {
                let ext = p.extension().and_then(|e| e.to_str()).map(|e| format!(".{}", e)).unwrap_or_default();
                if let Some(c_type) = get_component_type_from_extension(&ext) {
                    let stem = p.file_stem().and_then(|s| s.to_str()).unwrap_or("").to_string();
                    if !map.contains_key(&stem) {
                        let is_ext = is_extension_component(&stem) || c_type == "extension";
                        map.insert(stem.clone(), DiscoveredComponent {
                            name: stem,
                            comp_type: c_type,
                            path: p,
                            is_extension: is_ext,
                            is_checked_out: false,
                            is_dirty: false,
                        });
                    }
                }
            }
        }
    }
}
