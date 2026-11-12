use serde::{Deserialize, Serialize};
use ln_jca::bde_manager::{BdeExecutionMode, BdeParams, JcaBdeManager};
use ln_jca::client::HttpClient;
use ln_jca::error::JcaError;
use ln_jca::filter::{BdeFilter, BdeSelection};
use crate::xml_tree::parse_xml_to_tree;

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct ApplicationSummary {
    pub name: String,
    pub description: String,
    pub release: String,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct ApplicationDetails {
    pub name: String,
    pub description: String,
    pub release: String,
    pub packages: Vec<String>,
    pub raw_xml: String,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct TaskSummary {
    pub task_name: String,
    pub task_id: String,
    pub description: String,
    pub status: String,
    pub task_type: String,
    pub assigned_to: String,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct SoftwareProjectSummary {
    pub name: String,
    pub project_name: String,
    pub description: String,
    pub project_description: String,
    pub status: String,
    pub project_status: String,
    pub type_of_project: String,
    pub tasks: Vec<TaskSummary>,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct ActivityRelationship {
    pub related_activity_name: String,
    pub relationship_type: String,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct TaskDetails {
    pub task_name: String,
    pub task_id: String,
    pub label_uuid: String,
    pub uuid: String,
    pub task_uuid: String,
    pub task_version_id: String,
    pub task_description: String,
    pub description: String,
    pub task_documentation: String,
    pub task_requirement_id: String,
    pub type_of_task: String,
    pub assigned_to: String,
    pub owner: String,
    pub task_status: String,
    pub status: String,
    pub task_severity: String,
    pub functional_change: String,
    pub relationships: Vec<ActivityRelationship>,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct SoftwareProjectDetails {
    pub name: String,
    pub project_name: String,
    pub description: String,
    pub project_description: String,
    pub project_version_id: String,
    pub base_vrc: String,
    pub work_set_vrc: String,
    pub development_environment: String,
    pub development_repository_address: String,
    pub runtime_repository_address: String,
    pub application_server: String,
    pub application_name: String,
    pub application_release: String,
    pub is_partial_end_allowed: bool,
    pub is_sharing_activities_allowed: bool,
    pub integration_with_pmc: bool,
    pub packages: Vec<String>,
    pub tasks: Vec<TaskDetails>,
    pub raw_xml: String,
}

/// Lists Applications available on Infor LN Server via `Application.List` BDE (`mode = List`).
pub async fn list_applications(client: &HttpClient) -> Result<Vec<ApplicationSummary>, JcaError> {
    let mgr = JcaBdeManager::new(client, "ProjectServer");
    let mut selection = BdeSelection::new();
    selection.add("Application.name");
    selection.add("Application.description");
    selection.add("Application.release");

    let params = BdeParams {
        bde_name: "Application".to_string(),
        method_name: "List".to_string(),
        mode: Some(BdeExecutionMode::List),
        request_xml: Some("<ApplicationListRequest/>".to_string()),
        selection: Some(selection),
        ..Default::default()
    };

    let resp_xml = mgr.execute(&params).await?;
    let tree = parse_xml_to_tree(&resp_xml).map_err(|e| JcaError::Protocol(e))?;

    let mut apps = Vec::new();
    for app_elem in tree.find_all("Application") {
        let name = app_elem.child_text("name")
            .or_else(|| app_elem.child_text("Name"))
            .unwrap_or_default()
            .to_string();
        let desc = app_elem.child_text("description")
            .or_else(|| app_elem.child_text("title"))
            .or_else(|| app_elem.child_text("Description"))
            .unwrap_or_default()
            .to_string();
        let release = app_elem.child_text("release")
            .or_else(|| app_elem.child_text("Release"))
            .or_else(|| app_elem.child_text("releaseID"))
            .unwrap_or_default()
            .to_string();

        if !name.is_empty() {
            apps.push(ApplicationSummary {
                name,
                description: desc,
                release,
            });
        }
    }

    Ok(apps)
}

/// Queries detailed metadata for an Application via `Application.Show` BDE (`mode = Show`).
pub async fn show_application(client: &HttpClient, app_name: &str) -> Result<ApplicationDetails, JcaError> {
    let mgr = JcaBdeManager::new(client, "ProjectServer");
    let req_xml = format!("<Application><name>{app_name}</name></Application>");

    let params = BdeParams {
        bde_name: "Application".to_string(),
        method_name: "Show".to_string(),
        mode: Some(BdeExecutionMode::Show),
        request_xml: Some(req_xml),
        ..Default::default()
    };

    let resp_xml = mgr.execute(&params).await?;
    let tree = parse_xml_to_tree(&resp_xml).map_err(|e| JcaError::Protocol(e))?;

    let app_elem = tree.find_first("Application").unwrap_or(&tree);
    let name = app_elem.child_text("name").unwrap_or(app_name).to_string();
    let desc = app_elem.child_text("description").unwrap_or_default().to_string();
    let release = app_elem.child_text("release")
        .or_else(|| app_elem.child_text("releaseID"))
        .unwrap_or_default()
        .to_string();

    let mut packages = Vec::new();
    for pkg in app_elem.find_all("Package") {
        let txt = pkg.text.trim();
        if !txt.is_empty() && !packages.contains(&txt.to_string()) {
            packages.push(txt.to_string());
        }
    }

    Ok(ApplicationDetails {
        name,
        description: desc,
        release,
        packages,
        raw_xml: resp_xml,
    })
}

/// Lists Software Projects available on Infor LN Server via `SoftwareProject.List` BDE (`mode = List`).
pub async fn list_software_projects(client: &HttpClient) -> Result<Vec<SoftwareProjectSummary>, JcaError> {
    let mgr = JcaBdeManager::new(client, "ProjectServer");
    let mut selection = BdeSelection::new();
    selection.add("projectName");
    selection.add("projectDescription");
    selection.add("projectStatus");
    selection.add("typeOfProject");
    selection.add("Task.taskName");
    selection.add("Task.taskDescription");
    selection.add("Task.taskStatus");
    selection.add("Task.typeOfTask");
    selection.add("Task.assignedTo");

    let params = BdeParams {
        bde_name: "SoftwareProject".to_string(),
        method_name: "List".to_string(),
        mode: Some(BdeExecutionMode::List),
        request_xml: Some("<SoftwareProjectListRequest/>".to_string()),
        selection: Some(selection),
        ..Default::default()
    };

    let resp_xml = mgr.execute(&params).await?;
    let tree = parse_xml_to_tree(&resp_xml).map_err(|e| JcaError::Protocol(e))?;

    let mut projects = Vec::new();
    for p_elem in tree.find_all("SoftwareProject") {
        let name = p_elem.child_text("projectName")
            .or_else(|| p_elem.child_text("name"))
            .or_else(|| p_elem.child_text("Name"))
            .unwrap_or_default()
            .to_string();
        let desc = p_elem.child_text("projectDescription")
            .or_else(|| p_elem.child_text("description"))
            .or_else(|| p_elem.child_text("Description"))
            .unwrap_or_default()
            .to_string();
        let status = p_elem.child_text("projectStatus")
            .or_else(|| p_elem.child_text("status"))
            .or_else(|| p_elem.child_text("Status"))
            .unwrap_or("active")
            .to_string();
        let proj_type = p_elem.child_text("typeOfProject")
            .or_else(|| p_elem.child_text("type"))
            .unwrap_or_default()
            .to_string();

        let mut tasks = Vec::new();
        for t_elem in p_elem.find_all("Task") {
            let t_name = t_elem.child_text("taskName")
                .or_else(|| t_elem.child_text("taskId"))
                .or_else(|| t_elem.child_text("name"))
                .unwrap_or_default()
                .to_string();
            if !t_name.is_empty() {
                tasks.push(TaskSummary {
                    task_name: t_name.clone(),
                    task_id: t_name,
                    description: t_elem.child_text("taskDescription")
                        .or_else(|| t_elem.child_text("description"))
                        .unwrap_or_default()
                        .to_string(),
                    status: t_elem.child_text("taskStatus")
                        .or_else(|| t_elem.child_text("status"))
                        .unwrap_or("open")
                        .to_string(),
                    task_type: t_elem.child_text("typeOfTask")
                        .or_else(|| t_elem.child_text("type"))
                        .unwrap_or_default()
                        .to_string(),
                    assigned_to: t_elem.child_text("assignedTo")
                        .unwrap_or_default()
                        .to_string(),
                });
            }
        }

        if !name.is_empty() {
            projects.push(SoftwareProjectSummary {
                name: name.clone(),
                project_name: name,
                description: desc.clone(),
                project_description: desc,
                status: status.clone(),
                project_status: status,
                type_of_project: proj_type,
                tasks,
            });
        }
    }

    Ok(projects)
}

/// Retrieves full metadata and tasks for a Software Project via `SoftwareProject_V2.Show` BDE (`mode = Show`).
///
/// Invariant: Extracts `labelUUID` (the task's `Label` property) vs `taskUUID`, Base VRC,
/// and repository addresses.
pub async fn get_software_project_details(
    client: &HttpClient,
    project_name: &str,
    filter_expression: Option<&str>,
) -> Result<SoftwareProjectDetails, JcaError> {
    let mgr = JcaBdeManager::new(client, "ProjectServer");
    let req_xml = format!("<SoftwareProject_V2><projectName>{project_name}</projectName></SoftwareProject_V2>");

    let filter = filter_expression.map(BdeFilter::from_raw);

    let params = BdeParams {
        bde_name: "SoftwareProject_V2".to_string(),
        method_name: "Show".to_string(),
        mode: Some(BdeExecutionMode::Show),
        request_xml: Some(req_xml),
        filter,
        ..Default::default()
    };

    let resp_xml = mgr.execute(&params).await?;
    let tree = parse_xml_to_tree(&resp_xml).map_err(|e| JcaError::Protocol(e))?;

    let name = tree.find_text("projectName")
        .or_else(|| tree.find_text("name"))
        .unwrap_or(project_name)
        .to_string();
    let desc = tree.find_text("projectDescription")
        .or_else(|| tree.find_text("description"))
        .unwrap_or_default()
        .to_string();
    let proj_version = tree.find_text("projectVersionID")
        .or_else(|| tree.find_text("baseVRC"))
        .unwrap_or_default()
        .to_string();
    let workset_vrc = tree.find_text("workSetVRC")
        .or_else(|| tree.find_text("workSet"))
        .unwrap_or_default()
        .to_string();
    let dev_env = tree.find_text("developmentEnvironment")
        .unwrap_or_default()
        .to_string();
    let dev_repo = tree.find_text("developmentRepositoryAddress")
        .map(|s| s.to_string())
        .unwrap_or_else(|| format!("{project_name}_dev"));
    let rt_repo = tree.find_text("runtimeRepositoryAddress")
        .map(|s| s.to_string())
        .unwrap_or_else(|| format!("{project_name}_rt"));
    let app_server = tree.find_text("applicationServer")
        .unwrap_or_default()
        .to_string();
    let app_name = tree.find_text("applicationName")
        .unwrap_or_default()
        .to_string();
    let app_release = tree.find_text("applicationRelease")
        .unwrap_or_default()
        .to_string();

    let is_partial_end = tree.find_text("isPartialEndAllowed")
        .map(|v| v.eq_ignore_ascii_case("true") || v.eq_ignore_ascii_case("yes") || v == "1")
        .unwrap_or(true);
    let is_sharing = tree.find_text("isSharingActivitiesAllowed")
        .map(|v| v.eq_ignore_ascii_case("true") || v.eq_ignore_ascii_case("yes") || v == "1")
        .unwrap_or(true);
    let pmc_integration = tree.find_text("integrationWithPMC")
        .map(|v| v.eq_ignore_ascii_case("true") || v.eq_ignore_ascii_case("yes") || v == "1")
        .unwrap_or(false);

    let mut packages = Vec::new();
    for pkg_elem in tree.find_all("Package") {
        let txt = pkg_elem.text.trim();
        if !txt.is_empty() && !packages.contains(&txt.to_string()) {
            packages.push(txt.to_string());
        }
    }
    for pkg_elem in tree.find_all("package") {
        let txt = pkg_elem.text.trim();
        if !txt.is_empty() && !packages.contains(&txt.to_string()) {
            packages.push(txt.to_string());
        }
    }

    let mut tasks = Vec::new();
    for task_elem in tree.find_all("Task") {
        let task_name = task_elem.child_text("taskName")
            .or_else(|| task_elem.child_text("taskId"))
            .or_else(|| task_elem.child_text("name"))
            .unwrap_or_default()
            .to_string();

        let label_uuid = task_elem.child_text("labelUUID")
            .or_else(|| task_elem.child_text("label"))
            .or_else(|| task_elem.child_text("uuid"))
            .or_else(|| task_elem.child_text("UUID"))
            .unwrap_or_default()
            .to_string();

        let task_uuid = task_elem.child_text("taskUUID")
            .unwrap_or_default()
            .to_string();
        let task_v_id = task_elem.child_text("taskVersionID")
            .unwrap_or_default()
            .to_string();
        let task_desc = task_elem.child_text("taskDescription")
            .or_else(|| task_elem.child_text("description"))
            .unwrap_or_default()
            .to_string();
        let task_doc = task_elem.child_text("taskDocumentation")
            .unwrap_or_default()
            .to_string();
        let task_req = task_elem.child_text("taskRequirementID")
            .unwrap_or_default()
            .to_string();
        let type_of_task = task_elem.child_text("typeOfTask")
            .or_else(|| task_elem.child_text("type"))
            .unwrap_or_default()
            .to_string();
        let assigned_to = task_elem.child_text("assignedTo")
            .or_else(|| task_elem.child_text("owner"))
            .unwrap_or_default()
            .to_string();
        let task_status = task_elem.child_text("taskStatus")
            .or_else(|| task_elem.child_text("status"))
            .unwrap_or("open")
            .to_string();
        let task_sev = task_elem.child_text("taskSeverity")
            .unwrap_or_default()
            .to_string();
        let func_change = task_elem.child_text("functionalChange")
            .unwrap_or_default()
            .to_string();

        let mut relationships = Vec::new();
        for rel_elem in task_elem.find_all("ActivityRelationship") {
            let rel_act = rel_elem.child_text("relatedActivityName")
                .or_else(|| rel_elem.child_text("activity"))
                .unwrap_or_default()
                .to_string();
            let rel_type = rel_elem.child_text("relationshipType")
                .or_else(|| rel_elem.child_text("type"))
                .unwrap_or_default()
                .to_string();
            if !rel_act.is_empty() {
                relationships.push(ActivityRelationship {
                    related_activity_name: rel_act,
                    relationship_type: rel_type,
                });
            }
        }

        if !task_name.is_empty() {
            tasks.push(TaskDetails {
                task_name: task_name.clone(),
                task_id: task_name,
                label_uuid: label_uuid.clone(),
                uuid: label_uuid,
                task_uuid,
                task_version_id: task_v_id,
                task_description: task_desc.clone(),
                description: task_desc,
                task_documentation: task_doc,
                task_requirement_id: task_req,
                type_of_task,
                assigned_to: assigned_to.clone(),
                owner: assigned_to,
                task_status: task_status.clone(),
                status: task_status,
                task_severity: task_sev,
                functional_change: func_change,
                relationships,
            });
        }
    }

    Ok(SoftwareProjectDetails {
        name: name.clone(),
        project_name: name,
        description: desc.clone(),
        project_description: desc,
        project_version_id: proj_version.clone(),
        base_vrc: proj_version,
        work_set_vrc: workset_vrc,
        development_environment: dev_env,
        development_repository_address: dev_repo,
        runtime_repository_address: rt_repo,
        application_server: app_server,
        application_name: app_name,
        application_release: app_release,
        is_partial_end_allowed: is_partial_end,
        is_sharing_activities_allowed: is_sharing,
        integration_with_pmc: pmc_integration,
        packages,
        tasks,
        raw_xml: resp_xml,
    })
}
