use std::path::{Path, PathBuf};
use serde::{Deserialize, Serialize};
use ln_eclipse_compat::{AdminFile, PropertyBucket};
use ln_jca::bde_manager::{BdeExecutionMode, BdeParams, JcaBdeManager};
use ln_jca::client::HttpClient;
use ln_jca::error::JcaError;
use crate::project::{get_software_project_details, TaskDetails};
use crate::xml_tree::parse_xml_to_tree;

#[derive(Debug, Clone, Default)]
pub struct CreateActivityOptions<'a> {
    pub description: &'a str,
    pub task_documentation: &'a str,
    pub task_requirement_id: &'a str,
    pub type_of_task: &'a str,
    pub assigned_to: &'a str,
    pub severity: &'a str,
    pub functional_change: &'a str,
    pub auto_open: bool,
    pub workspace_path: Option<&'a Path>,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct CreateActivityResult {
    pub task_id: String,
    pub task_name: String,
    pub project: String,
    pub project_name: String,
    pub uuid: String,
    pub label_uuid: String,
    pub task_version_id: String,
    pub status: String,
    pub task_status: String,
    pub workspace_path: Option<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct ModifiedComponent {
    pub name: String,
    pub comp_type: String,
    pub package: String,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct OpenActivityResult {
    pub task_id: String,
    pub task_name: String,
    pub project: String,
    pub project_name: String,
    pub label_uuid: String,
    pub uuid: String,
    pub task_version_id: String,
    pub status: String,
    pub task_status: String,
    pub workspace_path: Option<String>,
    pub modified_components: Vec<ModifiedComponent>,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct ComponentRef {
    pub name: String,
    pub comp_type: String,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct MoveComponentsResult {
    pub success: bool,
    pub moved_components: usize,
    pub target_task: String,
    pub raw_response: String,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct CleanComponentsResult {
    pub success: bool,
    pub cleaned_components: usize,
    pub raw_response: String,
}

/// Lists all remote Activities (Tasks) under a Software Project via `SoftwareProject_V2.Show`.
pub async fn list_remote_activities(client: &HttpClient, project_name: &str) -> Result<Vec<TaskDetails>, JcaError> {
    let details = get_software_project_details(client, project_name, None).await?;
    Ok(details.tasks)
}

/// Retrieves full details for a specific remote activity via `SoftwareProject_V2.Show` with filter.
pub async fn get_remote_activity_details(
    client: &HttpClient,
    project_name: &str,
    task_name: &str,
) -> Result<Option<TaskDetails>, JcaError> {
    let filter = format!("Task.taskName == '{task_name}'");
    if let Ok(details) = get_software_project_details(client, project_name, Some(&filter)).await {
        for t in details.tasks {
            if t.task_name == task_name || t.task_id == task_name {
                return Ok(Some(t));
            }
        }
    }

    // Fallback without filter
    let details = get_software_project_details(client, project_name, None).await?;
    for t in details.tasks {
        if t.task_name == task_name || t.task_id == task_name {
            return Ok(Some(t));
        }
    }

    Ok(None)
}

/// Creates a new Activity on the Infor LN Server via `SoftwareProject_V2.Change` BDE (`CreateSoftwareTaskV2.xml`).
/// Optionally auto-opens the activity and bootstraps the local Eclipse workspace folder.
pub async fn create_remote_activity(
    client: &HttpClient,
    project_name: &str,
    task_id: &str,
    options: CreateActivityOptions<'_>,
) -> Result<CreateActivityResult, JcaError> {
    let mgr = JcaBdeManager::new(client, "ProjectServer");
    let task_desc = if options.description.is_empty() {
        format!("Activity {task_id}")
    } else {
        options.description.to_string()
    };
    let type_of_task = if options.type_of_task.is_empty() { "enhancement" } else { options.type_of_task };
    let severity = if options.severity.is_empty() { "medium" } else { options.severity };
    let functional_change = if options.functional_change.is_empty() { "no" } else { options.functional_change };

    let req_xml = format!(
        "<SoftwareProject_V2 actionType=\"unchanged\">\n\
        \x20 <projectName>{project_name}</projectName>\n\
        \x20 <Task actionType=\"create\">\n\
        \x20   <taskName>{task_id}</taskName>\n\
        \x20   <assignedTo>{}</assignedTo>\n\
        \x20   <taskDescription>{}</taskDescription>\n\
        \x20   <taskDocumentation>{}</taskDocumentation>\n\
        \x20   <taskRequirementID>{}</taskRequirementID>\n\
        \x20   <taskStatus>created</taskStatus>\n\
        \x20   <taskVersionID></taskVersionID>\n\
        \x20   <typeOfTask>{type_of_task}</typeOfTask>\n\
        \x20   <taskUUID></taskUUID>\n\
        \x20   <Assignee actionType=\"createOrChange\"><assigneeName>{}</assigneeName></Assignee>\n\
        \x20   <taskSeverity>{severity}</taskSeverity>\n\
        \x20   <functionalChange>{functional_change}</functionalChange>\n\
        \x20 </Task>\n\
        </SoftwareProject_V2>",
        options.assigned_to,
        task_desc,
        options.task_documentation,
        options.task_requirement_id,
        options.assigned_to,
    );

    let params = BdeParams {
        bde_name: "SoftwareProject_V2".to_string(),
        method_name: "Change".to_string(),
        mode: Some(BdeExecutionMode::Bde),
        request_xml: Some(req_xml),
        ..Default::default()
    };

    let resp_xml = mgr.execute(&params).await?;
    let tree = parse_xml_to_tree(&resp_xml).map_err(|e| JcaError::Protocol(e))?;

    let created_task = tree.find_first("Task");
    let mut label_uuid = String::new();
    let mut task_version_id = String::new();
    let mut status = "created".to_string();

    if let Some(task_node) = created_task {
        label_uuid = task_node.child_text("labelUUID")
            .or_else(|| task_node.child_text("label"))
            .or_else(|| task_node.child_text("uuid"))
            .or_else(|| task_node.child_text("UUID"))
            .unwrap_or_default()
            .to_string();
        task_version_id = task_node.child_text("taskVersionID").unwrap_or_default().to_string();
        status = task_node.child_text("taskStatus")
            .or_else(|| task_node.child_text("status"))
            .unwrap_or(&status)
            .to_string();
    }

    let mut result = CreateActivityResult {
        task_id: task_id.to_string(),
        task_name: task_id.to_string(),
        project: project_name.to_string(),
        project_name: project_name.to_string(),
        uuid: label_uuid.clone(),
        label_uuid: label_uuid.clone(),
        task_version_id: task_version_id.clone(),
        status: status.clone(),
        task_status: status,
        workspace_path: None,
    };

    if options.auto_open {
        if let Some(ws) = options.workspace_path {
            let open_res = open_remote_activity(client, project_name, task_id, Some(ws), false).await?;
            result.label_uuid = open_res.label_uuid;
            result.uuid = open_res.uuid;
            result.task_version_id = open_res.task_version_id;
            result.status = open_res.status;
            result.task_status = open_res.task_status;
            result.workspace_path = open_res.workspace_path;
        }
    }

    Ok(result)
}

/// Opens an Activity on the Infor LN Server:
/// 1. Queries project version (Base VRC), repo addresses, `labelUUID`, and `taskVersionID`.
/// 2. Transitions status to 'opened' via `SoftwareProject.Change` (`ChangeSoftwareTaskStatus.xml`).
/// 3. Bootstraps local Eclipse folder with `.project`, `.admin`, and authentic binary `properties.index`.
/// 4. Queries modified components via `CMLabel.GetModifiedComponents`.
pub async fn open_remote_activity(
    client: &HttpClient,
    project_name: &str,
    task_name: &str,
    workspace_path: Option<&Path>,
    sync_modified: bool,
) -> Result<OpenActivityResult, JcaError> {
    let details = get_remote_activity_details(client, project_name, task_name).await?;
    let proj_info = get_software_project_details(client, project_name, None).await?;

    let mut label_uuid = String::new();
    let mut task_ver_id = String::new();
    if let Some(d) = &details {
        label_uuid = d.label_uuid.clone();
        task_ver_id = d.task_version_id.clone();
    }

    let base_vrc = proj_info.project_version_id.clone();
    let dev_env = proj_info.development_environment.clone();
    let dev_repo = proj_info.development_repository_address.clone();
    let rt_repo = proj_info.runtime_repository_address.clone();

    // Transition status to opened via SoftwareProject.Change
    let change_req = format!(
        "<SoftwareProject actionType=\"unchanged\">\n\
        \x20 <projectName>{project_name}</projectName>\n\
        \x20 <Task actionType=\"change\">\n\
        \x20   <taskName>{task_name}</taskName>\n\
        \x20   <taskStatus>opened</taskStatus>\n\
        \x20   <taskVersionID>{task_ver_id}</taskVersionID>\n\
        \x20 </Task>\n\
        </SoftwareProject>"
    );

    let mgr = JcaBdeManager::new(client, "ProjectServer");
    let change_params = BdeParams {
        bde_name: "SoftwareProject".to_string(),
        method_name: "Change".to_string(),
        mode: Some(BdeExecutionMode::Bde),
        request_xml: Some(change_req),
        ..Default::default()
    };

    let resp_change = mgr.execute(&change_params).await?;
    if let Ok(c_tree) = parse_xml_to_tree(&resp_change) {
        if let Some(upd) = c_tree.find_text("taskVersionID") {
            if !upd.is_empty() {
                task_ver_id = upd.to_string();
            }
        }
    }

    if task_ver_id.is_empty() {
        task_ver_id = "1".to_string();
    }

    let mut act_dir_path = None;
    if let Some(ws_p) = workspace_path {
        let act_dir = bootstrap_local_activity(
            ws_p,
            task_name,
            project_name,
            &label_uuid,
            &dev_repo,
        ).map_err(|e| JcaError::Protocol(format!("Failed to bootstrap local activity: {e}")))?;

        // Update metadata properties.index binary with base_vrc, task_ver_id, dev_env, rt_repo
        let folder_name = format!("{task_name} [{project_name}]");
        let meta_idx = ws_p
            .join(".metadata")
            .join(".plugins")
            .join("org.eclipse.core.resources")
            .join(".projects")
            .join(&folder_name)
            .join(".indexes")
            .join("properties.index");

        let mut bucket = PropertyBucket::load_from_path(&meta_idx).unwrap_or_default();
        bucket.set_property("ProjectName", project_name, "", "");
        bucket.set_property("TaskName", task_name, "", "");
        bucket.set_property("Label", &label_uuid, "", "");
        bucket.set_property("ApplicationRelease", &base_vrc, "", "");
        bucket.set_property("TaskVersionID", &task_ver_id, "", "");
        bucket.set_property("TaskContext", &dev_repo, "", "");
        bucket.set_property("DevelopmentEnvironment", &dev_env, "", "");
        bucket.set_property("DevelopmentTimeRepositoryAddress", &dev_repo, "", "");
        bucket.set_property("RunTimeRepositoryAddress", &rt_repo, "", "");
        bucket.set_property("ApplicationUsesSCM", "yes", "", "");
        bucket.set_property("TaskStatus", "opened", "", "");
        bucket.set_property("repository", "com.infor.ln.studio.apps.core.cmprovider", "org.eclipse.team.core", "");
        let _ = bucket.save_to_path(&meta_idx);

        act_dir_path = Some(act_dir.to_string_lossy().to_string());
    }

    let mut modified_components = Vec::new();
    if !label_uuid.is_empty() {
        if let Ok(comps) = list_activity_modified_components(client, project_name, &label_uuid).await {
            modified_components = comps;
            if sync_modified && workspace_path.is_some() {
                let act_dir = PathBuf::from(act_dir_path.as_ref().unwrap());
                for c in &modified_components {
                    let _ = crate::explorer::get_component(
                        client,
                        &c.comp_type,
                        &c.name,
                        &act_dir,
                        false, // checked out
                        &dev_repo,
                        None,
                        Some(&label_uuid),
                        Some(&base_vrc),
                        None,
                    ).await;
                }
            }
        }
    }

    Ok(OpenActivityResult {
        task_id: task_name.to_string(),
        task_name: task_name.to_string(),
        project: project_name.to_string(),
        project_name: project_name.to_string(),
        label_uuid: label_uuid.clone(),
        uuid: label_uuid,
        task_version_id: task_ver_id,
        status: "opened".to_string(),
        task_status: "opened".to_string(),
        workspace_path: act_dir_path,
        modified_components,
    })
}

/// Queries modified components belonging to an activity via `CMLabel.GetModifiedComponents`.
/// Context XML contains `<ActivityID>{activity_uuid}</ActivityID>`.
pub async fn list_activity_modified_components(
    client: &HttpClient,
    project_name: &str,
    activity_uuid: &str,
) -> Result<Vec<ModifiedComponent>, JcaError> {
    let req_xml = "<CMLabel><timeStampSince>0</timeStampSince><type></type></CMLabel>";
    let context_xml = format!("<ActivityID>{activity_uuid}</ActivityID>");
    let dev_cp = format!("{project_name}_dev");

    let mgr = JcaBdeManager::new(client, &dev_cp);
    let params = BdeParams {
        bde_name: "CMLabel".to_string(),
        method_name: "GetModifiedComponents".to_string(),
        mode: Some(BdeExecutionMode::Bde),
        request_xml: Some(req_xml.to_string()),
        context_xml: Some(context_xml),
        ..Default::default()
    };

    let resp_xml = mgr.execute(&params).await?;
    let tree = parse_xml_to_tree(&resp_xml).map_err(|e| JcaError::Protocol(e))?;

    let mut components = Vec::new();
    for c_elem in tree.find_all("ModifiedComponent") {
        let name = c_elem.child_text("name")
            .or_else(|| c_elem.child_text("componentName"))
            .unwrap_or_default()
            .to_string();
        let c_type = c_elem.child_text("type")
            .or_else(|| c_elem.child_text("componentType"))
            .unwrap_or_default()
            .to_string();
        let pkg = c_elem.child_text("package").unwrap_or_default().to_string();

        if !name.is_empty() {
            components.push(ModifiedComponent {
                name,
                comp_type: c_type,
                package: pkg,
            });
        }
    }

    Ok(components)
}

/// Cleans/recovers a stuck activity on the server via `FglStudio.CleanActivity` BDE call.
///
/// Invariant: Uses `<ActivityID>{labelUUID}</ActivityID>` envelope in ControlArea.
pub async fn clean_remote_activity(
    client: &HttpClient,
    project_name: &str,
    task_id: &str,
    activity_uuid: Option<&str>,
    project_clean: bool,
) -> Result<bool, JcaError> {
    let clean_val = if project_clean { "yes" } else { "no" };
    let req_xml = format!(
        "<FglStudio>\n\
        \x20 <CleanActivity>\n\
        \x20   <ProjectClean>{clean_val}</ProjectClean>\n\
        \x20 </CleanActivity>\n\
        </FglStudio>"
    );

    let mut label_uuid = activity_uuid.unwrap_or_default().to_string();
    if label_uuid.is_empty() {
        if let Ok(Some(details)) = get_remote_activity_details(client, project_name, task_id).await {
            label_uuid = details.label_uuid;
        }
    }

    let context_xml = if !label_uuid.is_empty() {
        Some(format!("<ActivityID>{label_uuid}</ActivityID>"))
    } else {
        None
    };

    let dev_cp = format!("{project_name}_dev");
    let mgr = JcaBdeManager::new(client, &dev_cp);
    let params = BdeParams {
        bde_name: "FglStudio".to_string(),
        method_name: "CleanActivity".to_string(),
        mode: Some(BdeExecutionMode::Bde),
        request_xml: Some(req_xml),
        context_xml,
        ..Default::default()
    };

    let resp_xml = mgr.execute(&params).await?;
    let lower = resp_xml.to_ascii_lowercase();
    Ok(lower.contains("success") || lower.contains("ok") || resp_xml.contains("<Success/>"))
}

/// Initialises a local Eclipse LN Studio activity project folder:
/// `<workspace_path>/<task_id> [<project_name>]`
/// with `.project`, `.admin`, and `.settings/properties.index`.
pub fn bootstrap_local_activity(
    workspace_path: &Path,
    task_id: &str,
    project_name: &str,
    activity_uuid: &str,
    dev_connection: &str,
) -> Result<PathBuf, std::io::Error> {
    let folder_name = format!("{task_id} [{project_name}]");
    let act_dir = workspace_path.join(&folder_name);
    std::fs::create_dir_all(&act_dir)?;

    // 1. Write .project
    let proj_content = format!(
        "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n\
        <projectDescription>\n\
        \t<name>{folder_name}</name>\n\
        \t<comment></comment>\n\
        \t<projects>\n\
        \t</projects>\n\
        \t<buildSpec>\n\
        \t\t<buildCommand>\n\
        \t\t\t<name>com.infor.ln.studio.apps.core.bic</name>\n\
        \t\t\t<arguments>\n\
        \t\t\t</arguments>\n\
        \t\t</buildCommand>\n\
        \t</buildSpec>\n\
        \t<natures>\n\
        \t\t<nature>com.infor.ln.studio.apps.core.fourglStudio</nature>\n\
        \t</natures>\n\
        </projectDescription>\n"
    );
    std::fs::write(act_dir.join(".project"), proj_content)?;

    // 2. Write .admin
    let admin_path = act_dir.join(".admin");
    if !admin_path.exists() {
        let admin_file = AdminFile::new();
        let _ = admin_file.save_to_path(&admin_path);
    }

    // 3. Write binary PropertyBucket to workspace metadata
    let meta_idx = workspace_path
        .join(".metadata")
        .join(".plugins")
        .join("org.eclipse.core.resources")
        .join(".projects")
        .join(&folder_name)
        .join(".indexes")
        .join("properties.index");

    let mut bucket = PropertyBucket::load_from_path(&meta_idx).unwrap_or_default();
    let dev_conn = if dev_connection.is_empty() {
        format!("{project_name}_dev")
    } else {
        dev_connection.to_string()
    };
    bucket.set_property("ProjectName", project_name, "", "");
    bucket.set_property("TaskName", task_id, "", "");
    bucket.set_property("Label", activity_uuid, "", "");
    bucket.set_property("DevelopmentTimeRepositoryAddress", &dev_conn, "", "");
    bucket.set_property("RunTimeRepositoryAddress", &format!("{project_name}_rt"), "", "");
    bucket.set_property("ApplicationUsesSCM", "yes", "", "");
    bucket.set_property("TaskStatus", "opened", "", "");
    bucket.set_property("repository", "com.infor.ln.studio.apps.core.cmprovider", "org.eclipse.team.core", "");
    let _ = bucket.save_to_path(&meta_idx);

    // 4. Write Eclipse persistent project properties (.settings/properties.index)
    let settings_dir = act_dir.join(".settings");
    std::fs::create_dir_all(&settings_dir)?;
    let props_index = settings_dir.join("properties.index");
    let props_content = format!(
        "version=1\n\
        activityUUID={activity_uuid}\n\
        softwareProject={project_name}\n\
        connectionPoint={dev_conn}\n\
        taskId={task_id}\n"
    );
    std::fs::write(props_index, props_content)?;

    Ok(act_dir)
}

/// Moves components from source activity to target activity on server via `FglStudio.MoveComponent` (BDE mode 2).
/// Updates local activity files and `.admin` metadata.
pub async fn move_activity_components(
    client: &HttpClient,
    components: &[ComponentRef],
    source_activity_dir: &Path,
    target_task_name: &str,
    target_task_uuid: &str,
    target_base_vrc: &str,
    target_context: &str,
    target_activity_dir: Option<&Path>,
) -> Result<MoveComponentsResult, JcaError> {
    let (context_xml, dev_cp) = resolve_activity_context(source_activity_dir);

    let mut comp_items = Vec::new();
    for c in components {
        comp_items.push(format!("<Component><type>{}</type><name>{}</name></Component>", c.comp_type, c.name));
    }
    let comps_xml = comp_items.join("");

    let req_xml = format!(
        "<FglStudio>\n\
        \x20 <TargetActivityID>\n\
        \x20   <taskName>{target_task_name}</taskName>\n\
        \x20   <labelUUID>{target_task_uuid}</labelUUID>\n\
        \x20   <baseVRC>{target_base_vrc}</baseVRC>\n\
        \x20   <taskContext>{target_context}</taskContext>\n\
        \x20 </TargetActivityID>\n\
        \x20 <ComponentList>\n\
        \x20   <Components>{comps_xml}</Components>\n\
        \x20 </ComponentList>\n\
        </FglStudio>"
    );

    let mgr = JcaBdeManager::new(client, &dev_cp);
    let params = BdeParams {
        bde_name: "FglStudio".to_string(),
        method_name: "MoveComponent".to_string(),
        mode: Some(BdeExecutionMode::Bde),
        request_xml: Some(req_xml),
        context_xml,
        ..Default::default()
    };

    let resp_xml = mgr.execute(&params).await?;

    // Update local filesystem and .admin files
    let mut moved_count = 0;
    let mut src_admin = AdminFile::load_from_path(&source_activity_dir.join(".admin")).unwrap_or_default();
    let mut tgt_admin = target_activity_dir.and_then(|d| AdminFile::load_from_path(&d.join(".admin")).ok());

    for c in components {
        if let Some(src_file) = find_component_file(source_activity_dir, &c.name, &c.comp_type) {
            if let Ok(rel_p) = src_file.strip_prefix(source_activity_dir) {
                let rel_str = rel_p.to_string_lossy().replace('\\', "/");
                if let Some(tgt_dir) = target_activity_dir {
                    let dest_file = tgt_dir.join(rel_p);
                    if let Some(parent) = dest_file.parent() {
                        let _ = std::fs::create_dir_all(parent);
                    }
                    if let Ok(bytes) = std::fs::read(&src_file) {
                        let _ = std::fs::write(&dest_file, bytes);
                        if let Some(ta) = tgt_admin.as_mut() {
                            ta.after_create(&rel_str);
                        }
                    }
                }
                src_admin.after_uncheckout(&rel_str);
                let _ = std::fs::remove_file(&src_file);
                moved_count += 1;
            }
        }
    }

    let _ = src_admin.save_to_path(&source_activity_dir.join(".admin"));
    if let (Some(tgt_dir), Some(ta)) = (target_activity_dir, tgt_admin) {
        let _ = ta.save_to_path(&tgt_dir.join(".admin"));
    }

    let lower = resp_xml.to_ascii_lowercase();
    let success = !lower.contains("error") || lower.contains("ok");

    Ok(MoveComponentsResult {
        success,
        moved_components: moved_count,
        target_task: target_task_name.to_string(),
        raw_response: resp_xml,
    })
}

/// Cleans components from activity workarea via `FglStudio.CleanComponents` (BDE mode 2).
/// Deletes files from local workspace and removes them from `.admin`.
pub async fn clean_activity_components(
    client: &HttpClient,
    components: &[ComponentRef],
    activity_dir: &Path,
) -> Result<CleanComponentsResult, JcaError> {
    let (context_xml, dev_cp) = resolve_activity_context(activity_dir);

    let mut comp_items = Vec::new();
    for c in components {
        comp_items.push(format!("<Component><type>{}</type><name>{}</name></Component>", c.comp_type, c.name));
    }
    let comps_xml = comp_items.join("");

    let req_xml = format!(
        "<FglStudio>\n\
        \x20 <CleanComponents>\n\
        \x20   <ComponentList>\n\
        \x20     <Components>{comps_xml}</Components>\n\
        \x20   </ComponentList>\n\
        \x20 </CleanComponents>\n\
        </FglStudio>"
    );

    let mgr = JcaBdeManager::new(client, &dev_cp);
    let params = BdeParams {
        bde_name: "FglStudio".to_string(),
        method_name: "CleanComponents".to_string(),
        mode: Some(BdeExecutionMode::Bde),
        request_xml: Some(req_xml),
        context_xml,
        ..Default::default()
    };

    let resp_xml = mgr.execute(&params).await?;

    let mut cleaned_count = 0;
    let mut admin_file = AdminFile::load_from_path(&activity_dir.join(".admin")).unwrap_or_default();

    for c in components {
        if let Some(comp_file) = find_component_file(activity_dir, &c.name, &c.comp_type) {
            if let Ok(rel_p) = comp_file.strip_prefix(activity_dir) {
                let rel_str = rel_p.to_string_lossy().replace('\\', "/");
                admin_file.remove(&rel_str);
                let _ = std::fs::remove_file(&comp_file);
                cleaned_count += 1;
            }
        }
    }

    let _ = admin_file.save_to_path(&activity_dir.join(".admin"));

    let lower = resp_xml.to_ascii_lowercase();
    let success = !lower.contains("error") || lower.contains("ok");

    Ok(CleanComponentsResult {
        success,
        cleaned_components: cleaned_count,
        raw_response: resp_xml,
    })
}

/// Resolves the Activity `<ActivityID>` XML envelope and effective connection point from `.settings/properties.index`.
pub fn resolve_activity_context(activity_dir: &Path) -> (Option<String>, String) {
    let settings_file = activity_dir.join(".settings").join("properties.index");
    if settings_file.exists() {
        if let Ok(content) = std::fs::read_to_string(&settings_file) {
            let mut uuid = String::new();
            let mut cp = String::new();
            for line in content.lines() {
                if let Some(val) = line.strip_prefix("activityUUID=") {
                    uuid = val.trim().to_string();
                } else if let Some(val) = line.strip_prefix("connectionPoint=") {
                    cp = val.trim().to_string();
                }
            }
            let ctx = if !uuid.is_empty() {
                Some(format!("<ActivityID><activityUUID>{uuid}</activityUUID></ActivityID>"))
            } else {
                None
            };
            let eff_cp = if !cp.is_empty() { cp } else { "ProjectServer".to_string() };
            return (ctx, eff_cp);
        }
    }
    (None, "ProjectServer".to_string())
}

/// Helper to locate a component file on disk inside an activity directory.
pub fn find_component_file(activity_dir: &Path, comp_name: &str, comp_type: &str) -> Option<PathBuf> {
    let info = crate::explorer::get_bde_type_info(comp_type);
    let ext = info.map(|i| i.ext).unwrap_or(".xml");

    if let Ok(rel) = ln_model::path_resolver::resolve_tde_relative_path(comp_type, comp_name, ext) {
        let p = activity_dir.join(rel);
        if p.exists() {
            return Some(p);
        }
    }

    // Fallback: search recursively for {comp_name}{ext}
    let filename = format!("{comp_name}{ext}");
    find_file_recursive(activity_dir, &filename)
}

fn find_file_recursive(dir: &Path, filename: &str) -> Option<PathBuf> {
    if let Ok(entries) = std::fs::read_dir(dir) {
        for entry in entries.flatten() {
            let p = entry.path();
            if p.is_dir() {
                if let Some(found) = find_file_recursive(&p, filename) {
                    return Some(found);
                }
            } else if p.file_name().and_then(|n| n.to_str()).map(|n| n.eq_ignore_ascii_case(filename)).unwrap_or(false) {
                return Some(p);
            }
        }
    }
    None
}
