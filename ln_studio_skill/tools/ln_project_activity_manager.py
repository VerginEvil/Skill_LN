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
    Lists Applications available on Infor LN Server via Application.List BDE.
    """
    req_xml = "<ApplicationListRequest/>"
    resp_xml = client.do_bde_call("Application", "List", req_xml, connection_point="ProjectServer")
    root = ET.fromstring(resp_xml)
    apps = []
    for app_elem in root.iter("Application"):
        name = app_elem.findtext("name") or app_elem.findtext("Name") or ""
        desc = app_elem.findtext("description") or app_elem.findtext("title") or app_elem.findtext("Description") or ""
        if name:
            apps.append({"name": name, "description": desc})
    return apps


def list_software_projects(client: LNStudioServerClient) -> List[Dict[str, str]]:
    """
    Lists Software Projects available on Infor LN Server via SoftwareProject.List BDE.
    """
    req_xml = "<SoftwareProjectListRequest/>"
    resp_xml = client.do_bde_call("SoftwareProject", "List", req_xml, connection_point="ProjectServer")
    root = ET.fromstring(resp_xml)
    projs = []
    for p_elem in root.iter("SoftwareProject"):
        name = p_elem.findtext("name") or p_elem.findtext("Name") or ""
        desc = p_elem.findtext("description") or p_elem.findtext("Description") or ""
        status = p_elem.findtext("status") or p_elem.findtext("Status") or "active"
        if name:
            projs.append({"name": name, "description": desc, "status": status})
    return projs


def get_software_project_details(client: LNStudioServerClient, project_name: str) -> Dict[str, Any]:
    """
    Retrieves VRC hierarchy and assigned packages for a Software Project via SoftwareProject_V2.Show BDE.
    """
    req_xml = f"<SoftwareProject_V2><name>{project_name}</name></SoftwareProject_V2>"
    resp_xml = client.do_bde_call("SoftwareProject_V2", "Show", req_xml, connection_point="ProjectServer")
    root = ET.fromstring(resp_xml)

    name = root.findtext(".//name") or project_name
    desc = root.findtext(".//description") or ""
    base_vrc = root.findtext(".//baseVRC") or ""
    workset_vrc = root.findtext(".//workSetVRC") or root.findtext(".//workSet") or ""

    packages = []
    for pkg_elem in root.iter("Package"):
        txt = (pkg_elem.text or "").strip()
        if txt:
            packages.append(txt)

    return {
        "name": name,
        "description": desc,
        "baseVRC": base_vrc,
        "workSetVRC": workset_vrc,
        "packages": packages,
        "raw_xml": resp_xml,
    }


def list_remote_activities(client: LNStudioServerClient, project_name: str) -> List[Dict[str, str]]:
    """
    Lists all remote Activities (Tasks) under a Software Project via SoftwareProject_V2.Show.
    """
    req_xml = f"<SoftwareProject_V2><name>{project_name}</name></SoftwareProject_V2>"
    resp_xml = client.do_bde_call("SoftwareProject_V2", "Show", req_xml, connection_point="ProjectServer")
    root = ET.fromstring(resp_xml)

    activities = []
    for task_elem in root.iter("Task"):
        task_id = task_elem.findtext("taskId") or task_elem.findtext("TaskId") or task_elem.findtext("name") or ""
        uuid_str = task_elem.findtext("uuid") or task_elem.findtext("UUID") or ""
        desc = task_elem.findtext("description") or task_elem.findtext("Description") or ""
        owner = task_elem.findtext("owner") or task_elem.findtext("Owner") or ""
        status = task_elem.findtext("status") or task_elem.findtext("Status") or "open"

        if task_id:
            activities.append({
                "task_id": task_id,
                "uuid": uuid_str,
                "description": desc,
                "owner": owner,
                "status": status,
            })
    return activities


def create_remote_activity(
    client: LNStudioServerClient,
    project_name: str,
    task_id: str,
    description: str,
) -> Dict[str, str]:
    """
    Creates a new Activity on the Infor LN Server via SoftwareProject_V2.Change BDE with action='create'.
    """
    req_xml = (
        f"<SoftwareProject_V2>\n"
        f"  <name>{project_name}</name>\n"
        f"  <Tasks action=\"create\">\n"
        f"    <Task>\n"
        f"      <taskId>{task_id}</taskId>\n"
        f"      <description>{description}</description>\n"
        f"    </Task>\n"
        f"  </Tasks>\n"
        f"</SoftwareProject_V2>"
    )
    resp_xml = client.do_bde_call("SoftwareProject_V2", "Change", req_xml, connection_point="ProjectServer")
    root = ET.fromstring(resp_xml)

    created_task = root.find(".//Task")
    uuid_str = ""
    status = "created"
    if created_task is not None:
        uuid_str = created_task.findtext("uuid") or created_task.findtext("UUID") or ""
        status = created_task.findtext("status") or status

    return {
        "task_id": task_id,
        "project": project_name,
        "uuid": uuid_str,
        "status": status,
    }


def clean_remote_activity(
    client: LNStudioServerClient,
    project_name: str,
    task_id: str,
) -> bool:
    """
    Cleans/recovers a stuck activity on the server via FglStudio.CleanActivity BDE call.
    """
    req_xml = (
        f"<FglStudio>\n"
        f"  <CleanActivityRequest>\n"
        f"    <project>{project_name}</project>\n"
        f"    <task>{task_id}</task>\n"
        f"  </CleanActivityRequest>\n"
        f"</FglStudio>"
    )
    dev_cp = f"{project_name}_dev"
    resp_xml = client.do_bde_call("FglStudio", "CleanActivity", req_xml, connection_point=dev_cp)
    return "success" in resp_xml.lower() or "ok" in resp_xml.lower()


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

    # 3. Write Eclipse persistent project properties (.settings/properties.index)
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
