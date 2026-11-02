#!/usr/bin/env python3
"""
ln_studio_skill/tools/ln_project_activity_manager.py
Infor LN Studio Remote Project & Activity Explorers + Local Activity Bootstrap.

Handles:
1. Querying Applications, Software Projects, and VRC hierarchies.
2. Browsing remote Activities, tasks, UUIDs, and modified components.
3. Creating new Activities on the LN Server.
4. Cleaning/recovering stuck activities via FglStudio.CleanActivity.
5. Bootstrapping local Eclipse activity project folders (<taskId> [<projectName>])
   with .project, .admin, and properties.index metadata.
"""

import os
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union, Any

from ln_server_client import LNStudioServerClient, BdeExecutionError


def list_applications(client: LNStudioServerClient) -> List[Dict[str, str]]:
    """
    Lists Applications available on Infor LN Server via Application.List BDE (mode='LIST').
    """
    req_xml = "<ApplicationListRequest/>"
    selection = ["Application.name", "Application.description", "Application.release"]
    resp_xml = client.do_bde_call(
        "Application",
        "List",
        req_xml,
        connection_point="ProjectServer",
        mode="LIST",
        selection_fields=selection,
    )
    root = ET.fromstring(resp_xml)
    apps = []
    for app_elem in root.iter("Application"):
        name = app_elem.findtext("name") or app_elem.findtext("Name") or ""
        desc = app_elem.findtext("description") or app_elem.findtext("title") or app_elem.findtext("Description") or ""
        rel = app_elem.findtext("release") or app_elem.findtext("Release") or app_elem.findtext("releaseID") or ""
        if name:
            apps.append({"name": name, "description": desc, "release": rel})
    return apps


def show_application(client: LNStudioServerClient, app_name: str) -> Dict[str, Any]:
    """
    Queries detailed metadata for an Application via Application.Show BDE (mode='SHOW').
    """
    req_xml = f"<Application><name>{app_name}</name></Application>"
    resp_xml = client.do_bde_call(
        "Application",
        "Show",
        req_xml,
        connection_point="ProjectServer",
        mode="SHOW",
    )
    root = ET.fromstring(resp_xml)
    app_elem = root.find(".//Application") or root
    name = app_elem.findtext("name") or app_name
    desc = app_elem.findtext("description") or ""
    release = app_elem.findtext("release") or app_elem.findtext("releaseID") or ""

    packages = []
    for pkg_elem in app_elem.iter("Package"):
        txt = (pkg_elem.text or "").strip()
        if txt:
            packages.append(txt)

    return {
        "name": name,
        "description": desc,
        "release": release,
        "packages": packages,
        "raw_xml": resp_xml,
    }


def list_software_projects(client: LNStudioServerClient) -> List[Dict[str, Any]]:
    """
    Lists Software Projects available on Infor LN Server via SoftwareProject.List BDE (mode='LIST').
    """
    req_xml = "<SoftwareProjectListRequest/>"
    selection = [
        "projectName",
        "projectDescription",
        "projectStatus",
        "typeOfProject",
        "Task.taskName",
        "Task.taskDescription",
        "Task.taskStatus",
        "Task.typeOfTask",
        "Task.assignedTo",
    ]
    resp_xml = client.do_bde_call(
        "SoftwareProject",
        "List",
        req_xml,
        connection_point="ProjectServer",
        mode="LIST",
        selection_fields=selection,
    )
    root = ET.fromstring(resp_xml)
    projs = []
    for p_elem in root.iter("SoftwareProject"):
        name = p_elem.findtext("projectName") or p_elem.findtext("name") or p_elem.findtext("Name") or ""
        desc = p_elem.findtext("projectDescription") or p_elem.findtext("description") or p_elem.findtext("Description") or ""
        status = p_elem.findtext("projectStatus") or p_elem.findtext("status") or p_elem.findtext("Status") or "active"
        proj_type = p_elem.findtext("typeOfProject") or p_elem.findtext("type") or ""

        tasks = []
        for t_elem in p_elem.iter("Task"):
            t_name = t_elem.findtext("taskName") or t_elem.findtext("taskId") or t_elem.findtext("name") or ""
            if t_name:
                tasks.append({
                    "task_name": t_name,
                    "task_id": t_name,
                    "description": t_elem.findtext("taskDescription") or t_elem.findtext("description") or "",
                    "status": t_elem.findtext("taskStatus") or t_elem.findtext("status") or "open",
                    "type": t_elem.findtext("typeOfTask") or "",
                    "assigned_to": t_elem.findtext("assignedTo") or "",
                })

        if name:
            proj_dict = {
                "name": name,
                "projectName": name,
                "description": desc,
                "projectDescription": desc,
                "status": status,
                "projectStatus": status,
                "typeOfProject": proj_type,
            }
            if tasks:
                proj_dict["tasks"] = tasks
            projs.append(proj_dict)
    return projs


def get_software_project_details(
    client: LNStudioServerClient,
    project_name: str,
    filter_expression: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Retrieves full metadata and tasks for a Software Project via SoftwareProject_V2.Show BDE (mode='SHOW').
    Extracts projectVersionID (Base VRC), development/runtime repository addresses, packages,
    and task list with labelUUID vs taskUUID distinction.
    """
    req_xml = f"<SoftwareProject_V2><projectName>{project_name}</projectName></SoftwareProject_V2>"
    resp_xml = client.do_bde_call(
        "SoftwareProject_V2",
        "Show",
        req_xml,
        connection_point="ProjectServer",
        mode="SHOW",
        filter_expression=filter_expression,
    )
    root = ET.fromstring(resp_xml)

    name = root.findtext(".//projectName") or root.findtext(".//name") or project_name
    desc = root.findtext(".//projectDescription") or root.findtext(".//description") or ""
    proj_version = root.findtext(".//projectVersionID") or root.findtext(".//baseVRC") or ""
    workset_vrc = root.findtext(".//workSetVRC") or root.findtext(".//workSet") or ""
    dev_env = root.findtext(".//developmentEnvironment") or ""
    dev_repo = root.findtext(".//developmentRepositoryAddress") or f"{project_name}_dev"
    rt_repo = root.findtext(".//runtimeRepositoryAddress") or f"{project_name}_rt"
    app_server = root.findtext(".//applicationServer") or ""
    app_name = root.findtext(".//applicationName") or ""
    app_release = root.findtext(".//applicationRelease") or ""

    is_partial_end = (root.findtext(".//isPartialEndAllowed") or "true").lower() in ("true", "yes", "1")
    is_sharing = (root.findtext(".//isSharingActivitiesAllowed") or "true").lower() in ("true", "yes", "1")
    pmc_integration = (root.findtext(".//integrationWithPMC") or "false").lower() in ("true", "yes", "1")

    packages = []
    for pkg_elem in root.iter("Package"):
        txt = (pkg_elem.text or "").strip()
        if txt:
            packages.append(txt)
    for pkg_elem in root.iter("package"):
        txt = (pkg_elem.text or "").strip()
        if txt and txt not in packages:
            packages.append(txt)

    tasks = []
    for task_elem in root.iter("Task"):
        task_name = task_elem.findtext("taskName") or task_elem.findtext("taskId") or task_elem.findtext("name") or ""
        label_uuid = task_elem.findtext("labelUUID") or task_elem.findtext("label") or task_elem.findtext("uuid") or ""
        task_uuid = task_elem.findtext("taskUUID") or ""
        task_v_id = task_elem.findtext("taskVersionID") or ""
        task_desc = task_elem.findtext("taskDescription") or task_elem.findtext("description") or ""
        task_doc = task_elem.findtext("taskDocumentation") or ""
        task_req = task_elem.findtext("taskRequirementID") or ""
        type_of_task = task_elem.findtext("typeOfTask") or task_elem.findtext("type") or ""
        assigned_to = task_elem.findtext("assignedTo") or task_elem.findtext("owner") or ""
        task_status = task_elem.findtext("taskStatus") or task_elem.findtext("status") or "open"
        task_sev = task_elem.findtext("taskSeverity") or ""
        func_change = task_elem.findtext("functionalChange") or ""

        # Activity relationships
        relationships = []
        for rel_elem in task_elem.iter("ActivityRelationship"):
            rel_act = rel_elem.findtext("relatedActivityName") or rel_elem.findtext("activity") or ""
            rel_type = rel_elem.findtext("relationshipType") or rel_elem.findtext("type") or ""
            if rel_act:
                relationships.append({"relatedActivityName": rel_act, "relationshipType": rel_type})

        if task_name:
            tasks.append({
                "taskName": task_name,
                "task_id": task_name,
                "labelUUID": label_uuid,
                "uuid": label_uuid,
                "taskUUID": task_uuid,
                "taskVersionID": task_v_id,
                "taskDescription": task_desc,
                "description": task_desc,
                "taskDocumentation": task_doc,
                "taskRequirementID": task_req,
                "typeOfTask": type_of_task,
                "assignedTo": assigned_to,
                "owner": assigned_to,
                "taskStatus": task_status,
                "status": task_status,
                "taskSeverity": task_sev,
                "functionalChange": func_change,
                "relationships": relationships,
            })

    return {
        "name": name,
        "projectName": name,
        "description": desc,
        "projectDescription": desc,
        "projectVersionID": proj_version,
        "baseVRC": proj_version,
        "workSetVRC": workset_vrc,
        "developmentEnvironment": dev_env,
        "developmentRepositoryAddress": dev_repo,
        "runtimeRepositoryAddress": rt_repo,
        "applicationServer": app_server,
        "applicationName": app_name,
        "applicationRelease": app_release,
        "isPartialEndAllowed": is_partial_end,
        "isSharingActivitiesAllowed": is_sharing,
        "integrationWithPMC": pmc_integration,
        "packages": packages,
        "tasks": tasks,
        "raw_xml": resp_xml,
    }


def list_remote_activities(client: LNStudioServerClient, project_name: str) -> List[Dict[str, Any]]:
    """
    Lists all remote Activities (Tasks) under a Software Project via SoftwareProject_V2.Show.
    """
    details = get_software_project_details(client, project_name)
    return details.get("tasks", [])


def get_remote_activity_details(
    client: LNStudioServerClient,
    project_name: str,
    task_name: str,
) -> Optional[Dict[str, Any]]:
    """
    Retrieves full details for a specific remote activity via SoftwareProject_V2.Show with filter.
    """
    filter_expr = f"Task.taskName == '{task_name}'"
    try:
        details = get_software_project_details(client, project_name, filter_expression=filter_expr)
        for t in details.get("tasks", []):
            if t["taskName"] == task_name or t["task_id"] == task_name:
                return t
    except Exception:
        pass

    # Fallback without filter
    details = get_software_project_details(client, project_name)
    for t in details.get("tasks", []):
        if t["taskName"] == task_name or t["task_id"] == task_name:
            return t
    return None


def create_remote_activity(
    client: LNStudioServerClient,
    project_name: str,
    task_id: str,
    description: str = "",
    task_documentation: str = "",
    task_requirement_id: str = "",
    type_of_task: str = "enhancement",
    assigned_to: str = "",
    severity: str = "medium",
    functional_change: str = "no",
    auto_open: bool = False,
    workspace_path: Optional[Union[str, Path]] = None,
) -> Dict[str, Any]:
    """
    Creates a new Activity on the Infor LN Server via SoftwareProject_V2.Change BDE (CreateSoftwareTaskV2.xml).
    Optionally auto-opens the activity and bootstraps the local Eclipse workspace folder.
    """
    task_desc = description or f"Activity {task_id}"
    req_xml = (
        f'<SoftwareProject_V2 actionType="unchanged">\n'
        f'  <projectName>{project_name}</projectName>\n'
        f'  <Task actionType="create">\n'
        f'    <taskName>{task_id}</taskName>\n'
        f'    <assignedTo>{assigned_to}</assignedTo>\n'
        f'    <taskDescription>{task_desc}</taskDescription>\n'
        f'    <taskDocumentation>{task_documentation}</taskDocumentation>\n'
        f'    <taskRequirementID>{task_requirement_id}</taskRequirementID>\n'
        f'    <taskStatus>created</taskStatus>\n'
        f'    <taskVersionID></taskVersionID>\n'
        f'    <typeOfTask>{type_of_task}</typeOfTask>\n'
        f'    <taskUUID></taskUUID>\n'
        f'    <Assignee actionType="createOrChange"><assigneeName>{assigned_to}</assigneeName></Assignee>\n'
        f'    <taskSeverity>{severity}</taskSeverity>\n'
        f'    <functionalChange>{functional_change}</functionalChange>\n'
        f'  </Task>\n'
        f'</SoftwareProject_V2>'
    )
    resp_xml = client.do_bde_call("SoftwareProject_V2", "Change", req_xml, connection_point="ProjectServer", mode="BDE")
    root = ET.fromstring(resp_xml)

    created_task = root.find(".//Task")
    uuid_str = ""
    label_uuid = ""
    task_version_id = ""
    status = "created"
    if created_task is not None:
        label_uuid = (
            created_task.findtext("labelUUID")
            or created_task.findtext("label")
            or created_task.findtext("uuid")
            or created_task.findtext("UUID")
            or ""
        )
        uuid_str = label_uuid
        task_version_id = created_task.findtext("taskVersionID") or ""
        status = created_task.findtext("taskStatus") or created_task.findtext("status") or status

    res: Dict[str, Any] = {
        "task_id": task_id,
        "taskName": task_id,
        "project": project_name,
        "projectName": project_name,
        "uuid": uuid_str,
        "labelUUID": label_uuid,
        "taskVersionID": task_version_id,
        "status": status,
        "taskStatus": status,
    }

    if auto_open and workspace_path:
        open_res = open_remote_activity(
            client=client,
            project_name=project_name,
            task_name=task_id,
            workspace_path=workspace_path,
        )
        res.update(open_res)

    return res


def open_remote_activity(
    client: LNStudioServerClient,
    project_name: str,
    task_name: str,
    workspace_path: Optional[Union[str, Path]] = None,
    sync_modified: bool = True,
) -> Dict[str, Any]:
    """
    Opens an Activity on the Infor LN Server:
    1. Queries project version (Base VRC), repo addresses, labelUUID, and taskVersionID.
    2. Transitions status to 'opened' via SoftwareProject.Change (ChangeSoftwareTaskStatus.xml).
    3. Bootstraps local Eclipse folder with .project, .admin, and authentic binary properties.index.
    4. Queries modified components via CMLabel.GetModifiedComponents.
    """
    details = get_remote_activity_details(client, project_name, task_name)
    proj_info = get_software_project_details(client, project_name)

    label_uuid = ""
    task_ver_id = ""
    if details:
        label_uuid = details.get("labelUUID") or details.get("uuid") or ""
        task_ver_id = details.get("taskVersionID") or ""

    base_vrc = proj_info.get("projectVersionID") or proj_info.get("baseVRC") or ""
    dev_env = proj_info.get("developmentEnvironment") or ""
    dev_repo = proj_info.get("developmentRepositoryAddress") or f"{project_name}_dev"
    rt_repo = proj_info.get("runtimeRepositoryAddress") or f"{project_name}_rt"

    change_req = (
        f'<SoftwareProject actionType="unchanged">\n'
        f'  <projectName>{project_name}</projectName>\n'
        f'  <Task actionType="change">\n'
        f'    <taskName>{task_name}</taskName>\n'
        f'    <taskStatus>opened</taskStatus>\n'
        f'    <taskVersionID>{task_ver_id}</taskVersionID>\n'
        f'  </Task>\n'
        f'</SoftwareProject>'
    )
    resp_change = client.do_bde_call("SoftwareProject", "Change", change_req, connection_point="ProjectServer", mode="BDE")
    c_root = ET.fromstring(resp_change)
    upd_ver_elem = c_root.find(".//taskVersionID")
    if upd_ver_elem is None:
        upd_ver_elem = c_root.find(".//Task/taskVersionID")
    if upd_ver_elem is not None and upd_ver_elem.text:
        task_ver_id = upd_ver_elem.text.strip()
    elif task_ver_id and task_ver_id.isdigit():
        task_ver_id = str(int(task_ver_id) + 1)
    else:
        task_ver_id = task_ver_id or "1"

    act_dir = None
    if workspace_path:
        ws_p = Path(workspace_path)
        act_dir = bootstrap_local_activity(
            workspace_path=ws_p,
            task_id=task_name,
            project_name=project_name,
            activity_uuid=label_uuid,
            dev_connection=dev_repo,
        )

        folder_name = f"{task_name} [{project_name}]"
        meta_idx = ws_p / ".metadata" / ".plugins" / "org.eclipse.core.resources" / ".projects" / folder_name / ".indexes" / "properties.index"
        from properties_index import PropertyBucket
        bucket = PropertyBucket()
        bucket.set_project_properties({
            "ProjectName": project_name,
            "TaskName": task_name,
            "Label": label_uuid,
            "ApplicationRelease": base_vrc,
            "TaskVersionID": task_ver_id,
            "TaskContext": dev_repo,
            "DevelopmentEnvironment": dev_env,
            "DevelopmentTimeRepositoryAddress": dev_repo,
            "RunTimeRepositoryAddress": rt_repo,
            "ApplicationUsesSCM": "yes",
            "TaskStatus": "opened",
        })
        bucket.set_property("repository", "com.infor.ln.studio.apps.core.cmprovider", qualifier="org.eclipse.team.core")
        bucket.save(meta_idx)

    modified_components = []
    if label_uuid:
        try:
            modified_components = list_activity_modified_components(client, project_name, label_uuid)
        except Exception:
            pass

    return {
        "task_id": task_name,
        "taskName": task_name,
        "project": project_name,
        "projectName": project_name,
        "labelUUID": label_uuid,
        "uuid": label_uuid,
        "taskVersionID": task_ver_id,
        "status": "opened",
        "taskStatus": "opened",
        "workspace_path": str(act_dir) if act_dir else None,
        "modified_components": modified_components,
    }


def list_activity_modified_components(
    client: LNStudioServerClient,
    project_name: str,
    activity_uuid: str,
) -> List[Dict[str, Any]]:
    """
    Queries modified components belonging to an activity via CMLabel.GetModifiedComponents.
    Context XML contains <ActivityID>{activity_uuid}</ActivityID>.
    """
    req_xml = "<CMLabel><timeStampSince>0</timeStampSince><type></type></CMLabel>"
    context_xml = f"<ActivityID>{activity_uuid}</ActivityID>"
    dev_cp = f"{project_name}_dev"
    resp_xml = client.do_bde_call(
        "CMLabel",
        "GetModifiedComponents",
        req_xml,
        connection_point=dev_cp,
        context_xml=context_xml,
        mode="BDE",
    )
    root = ET.fromstring(resp_xml)
    components = []
    for c_elem in root.iter("ModifiedComponent"):
        c_name = c_elem.findtext("name") or c_elem.findtext("componentName") or ""
        c_type = c_elem.findtext("type") or c_elem.findtext("componentType") or ""
        c_pkg = c_elem.findtext("package") or ""
        if c_name:
            components.append({
                "name": c_name,
                "type": c_type,
                "package": c_pkg,
            })
    return components


def clean_remote_activity(
    client: LNStudioServerClient,
    project_name: str,
    task_id: str,
    activity_uuid: Optional[str] = None,
    project_clean: bool = False,
) -> bool:
    """
    Cleans/recovers a stuck activity on the server via FglStudio.CleanActivity BDE call.
    Uses exact payload <FglStudio><CleanActivity><ProjectClean>{yes|no}</ProjectClean></CleanActivity></FglStudio>
    with <ActivityID> set in ControlArea.
    """
    clean_val = "yes" if project_clean else "no"
    req_xml = (
        f"<FglStudio>\n"
        f"  <CleanActivity>\n"
        f"    <ProjectClean>{clean_val}</ProjectClean>\n"
        f"  </CleanActivity>\n"
        f"</FglStudio>"
    )
    label_uuid = activity_uuid
    if not label_uuid:
        try:
            details = get_remote_activity_details(client, project_name, task_id)
            if details:
                label_uuid = details.get("labelUUID") or details.get("uuid")
        except Exception:
            pass

    context_xml = f"<ActivityID>{label_uuid}</ActivityID>" if label_uuid else None
    dev_cp = f"{project_name}_dev"
    resp_xml = client.do_bde_call(
        "FglStudio",
        "CleanActivity",
        req_xml,
        connection_point=dev_cp,
        context_xml=context_xml,
        mode="BDE",
    )
    return "success" in resp_xml.lower() or "ok" in resp_xml.lower() or "<Success/>" in resp_xml


def bootstrap_local_activity(
    workspace_path: Path,
    task_id: str,
    project_name: str,
    activity_uuid: str = "",
    dev_connection: str = "",
) -> Path:
    """
    Initializes a local Eclipse LN Studio activity project folder:
    `<workspace_path>/<task_id> [<project_name>]`
    with .project, .admin, and .settings/properties.index.
    """
    folder_name = f"{task_id} [{project_name}]"
    act_dir = workspace_path / folder_name
    act_dir.mkdir(parents=True, exist_ok=True)

    # 1. Write .project
    proj_content = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<projectDescription>\n'
        f'\t<name>{folder_name}</name>\n'
        '\t<comment></comment>\n'
        '\t<projects>\n'
        '\t</projects>\n'
        '\t<buildSpec>\n'
        '\t\t<buildCommand>\n'
        '\t\t\t<name>com.infor.ln.studio.apps.core.bic</name>\n'
        '\t\t\t<arguments>\n'
        '\t\t\t</arguments>\n'
        '\t\t</buildCommand>\n'
        '\t</buildSpec>\n'
        '\t<natures>\n'
        '\t\t<nature>com.infor.ln.studio.apps.core.fourglStudio</nature>\n'
        '\t</natures>\n'
        '</projectDescription>\n'
    )
    (act_dir / ".project").write_text(proj_content, encoding="utf-8")

    # 2. Write .admin
    from admin_sync import write_admin_file
    admin_path = act_dir / ".admin"
    if not admin_path.exists():
        write_admin_file(admin_path, {})

    # 3. Write binary PropertyBucket to workspace metadata
    from properties_index import PropertyBucket
    meta_idx = workspace_path / ".metadata" / ".plugins" / "org.eclipse.core.resources" / ".projects" / folder_name / ".indexes" / "properties.index"
    try:
        bucket = PropertyBucket()
        bucket.set_project_properties({
            "ProjectName": project_name,
            "TaskName": task_id,
            "Label": activity_uuid,
            "DevelopmentTimeRepositoryAddress": dev_connection or f"{project_name}_dev",
            "RunTimeRepositoryAddress": f"{project_name}_rt",
            "ApplicationUsesSCM": "yes",
            "TaskStatus": "opened",
        })
        bucket.set_property("repository", "com.infor.ln.studio.apps.core.cmprovider", qualifier="org.eclipse.team.core")
        bucket.save(meta_idx)
    except Exception:
        pass

    # 4. Write Eclipse persistent project properties (.settings/properties.index)
    settings_dir = act_dir / ".settings"
    settings_dir.mkdir(parents=True, exist_ok=True)
    props_index = settings_dir / "properties.index"
    props_lines = [
        "version=1\n",
        f"activityUUID={activity_uuid}\n",
        f"softwareProject={project_name}\n",
        f"connectionPoint={dev_connection or f'{project_name}_dev'}\n",
        f"taskId={task_id}\n",
    ]
    props_index.write_text("".join(props_lines), encoding="utf-8")

    return act_dir
