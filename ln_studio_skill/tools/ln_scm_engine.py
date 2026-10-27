#!/usr/bin/env python3
"""
ln_studio_skill/tools/ln_scm_engine.py
Infor LN Studio Pre-Commit SCM Engine & Human-in-the-Loop Guardrail Enforcement.

Handles:
1. Locking server components into an Activity via DR_*.CheckOut.
2. Reverting locks via DR_*.UndoCheckOut.
3. Uploading modified XML to the server Activity workarea via DR_*.Put / DR_Create.
4. Checking in components with comments via DR_*.CheckIn.
5. Strictly intercepting and rejecting check-outs on tx* Extension Modeler components (ADR 0006).
6. Strictly hard-blocking End Activity / Commit Activity (CloseTask / FinalizeActivity) (ADR 0007).
"""

import os
import sys
import stat
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union, Any

from ln_server_client import LNStudioServerClient, BdeExecutionError
from ln_component_explorer import BDE_TYPE_MAP, _split_component_name
from scm_guardrails import (
    ReadOnlyComponentError,
    is_extension_component,
    assert_file_writable,
)
from admin_sync import add_component, set_component_status


class PreCommitBoundaryError(Exception):
    """
    Raised whenever an automated agent or command attempts to execute
    'End Activity', 'Commit Activity', 'CloseTask', or 'FinalizeActivity'.
    Enforces the mandatory human review gate in LN Studio.
    """
    pass


def end_activity_gate(project_name: str, task_id: str) -> None:
    """
    Hard-blocks automated End Activity / Commit Activity per ADR 0007 governance.
    Instructs the developer to perform manual delivery approval in LN Studio.
    """
    raise PreCommitBoundaryError(
        f"[HARD-BLOCKED] End Activity / Commit Activity is prohibited by ADR 0007 governance. "
        f"Activity '{task_id}' in project '{project_name}' has been verified and deployed for testing. "
        f"Please open Infor LN Studio (Eclipse Workbench) to perform final human review and click 'End Activity'."
    )


def checkout_component(
    client: LNStudioServerClient,
    comp_type: str,
    comp_name: str,
    activity_dir: Path,
    project_name: str,
) -> Path:
    """
    Checks out a component on the LN Server via DR_*.CheckOut, downloads the editable XML,
    clears the OS Read-Only attribute, and marks isCheckedOut=True in .admin.
    """
    # 1. ADR 0006 Guardrail: tx* Extension Modeler components cannot be checked out in Studio
    if is_extension_component(comp_name):
        raise ReadOnlyComponentError(
            f"[ERROR] Failure checking-out the component. "
            f"Action on '{comp_name}' is not allowed in LN Studio. "
            f"Use session ttext1500m000 in LN UI to process extensions."
        )

    info = BDE_TYPE_MAP.get(comp_type.lower())
    if not info:
        raise ValueError(f"Unsupported component type '{comp_type}'")

    bde_name = info["bde"]
    ext = info["ext"]
    subfolder = info["subfolder"]
    pkg, mod, _ = _split_component_name(comp_name)

    task_id = activity_dir.name.split(" ")[0].strip("[]")
    dev_cp = f"{project_name}_dev"

    req_xml = (
        f"<{bde_name}>\n"
        f"  <CheckOutRequest>\n"
        f"    <name>{comp_name}</name>\n"
        f"    <package>{pkg}</package>\n"
        f"    <module>{mod}</module>\n"
        f"    <activity>{task_id}</activity>\n"
        f"  </CheckOutRequest>\n"
        f"</{bde_name}>"
    )

    resp_xml = client.do_bde_call(bde_name, "CheckOut", req_xml, connection_point=dev_cp)

    target_dir = activity_dir / subfolder
    target_dir.mkdir(parents=True, exist_ok=True)
    target_file = target_dir / f"{comp_name}{ext}"

    if target_file.exists():
        try:
            os.chmod(target_file, stat.S_IWRITE | stat.S_IREAD)
        except Exception:
            pass

    target_file.write_text(resp_xml, encoding="utf-8")
    try:
        os.chmod(target_file, stat.S_IWRITE | stat.S_IREAD)
    except Exception:
        pass

    # Update .admin SCM cache
    rel_path = target_file.relative_to(activity_dir).as_posix()
    try:
        set_component_status(
            activity_path=activity_dir,
            rel_path=rel_path,
            is_created=False,
            is_checked_out=True,
            is_dirty=True,
        )
    except Exception as e:
        print(f"[WARN] Failed to set isCheckedOut in .admin: {e}", file=sys.stderr)

    return target_file


def uncheckout_component(
    client: LNStudioServerClient,
    comp_type: str,
    comp_name: str,
    activity_dir: Path,
    project_name: str,
) -> bool:
    """
    Reverts a checked-out component via DR_*.UndoCheckOut, sets the local file to Read-Only,
    and updates .admin with isCheckedOut=False.
    """
    info = BDE_TYPE_MAP.get(comp_type.lower())
    if not info:
        raise ValueError(f"Unsupported component type '{comp_type}'")

    bde_name = info["bde"]
    ext = info["ext"]
    subfolder = info["subfolder"]
    pkg, mod, _ = _split_component_name(comp_name)
    dev_cp = f"{project_name}_dev"

    req_xml = (
        f"<{bde_name}>\n"
        f"  <UndoCheckOutRequest>\n"
        f"    <name>{comp_name}</name>\n"
        f"    <package>{pkg}</package>\n"
        f"    <module>{mod}</module>\n"
        f"  </UndoCheckOutRequest>\n"
        f"</{bde_name}>"
    )

    client.do_bde_call(bde_name, "UndoCheckOut", req_xml, connection_point=dev_cp)

    target_file = activity_dir / subfolder / f"{comp_name}{ext}"
    if target_file.exists():
        try:
            os.chmod(target_file, stat.S_IREAD)
        except Exception:
            pass

        rel_path = target_file.relative_to(activity_dir).as_posix()
        try:
            set_component_status(
                activity_path=activity_dir,
                rel_path=rel_path,
                is_created=False,
                is_checked_out=False,
                is_dirty=False,
            )
        except Exception:
            pass

    return True


def put_component(
    client: LNStudioServerClient,
    comp_type: str,
    comp_name: str,
    activity_dir: Path,
    project_name: str,
) -> bool:
    """
    Uploads modified component XML to the server Activity workarea via DR_*.Put.
    """
    info = BDE_TYPE_MAP.get(comp_type.lower())
    if not info:
        raise ValueError(f"Unsupported component type '{comp_type}'")

    bde_name = info["bde"]
    ext = info["ext"]
    subfolder = info["subfolder"]
    pkg, mod, _ = _split_component_name(comp_name)
    dev_cp = f"{project_name}_dev"

    target_file = activity_dir / subfolder / f"{comp_name}{ext}"
    if not target_file.exists():
        raise FileNotFoundError(f"Component file not found: {target_file}")

    content = target_file.read_text(encoding="utf-8")
    req_xml = (
        f"<{bde_name}>\n"
        f"  <PutRequest>\n"
        f"    <name>{comp_name}</name>\n"
        f"    <package>{pkg}</package>\n"
        f"    <module>{mod}</module>\n"
        f"    <content><![CDATA[{content}]]></content>\n"
        f"  </PutRequest>\n"
        f"</{bde_name}>"
    )

    client.do_bde_call(bde_name, "Put", req_xml, connection_point=dev_cp)
    return True


def checkin_component(
    client: LNStudioServerClient,
    comp_type: str,
    comp_name: str,
    activity_dir: Path,
    project_name: str,
    comment: str = "Automated check-in for LN UI Cloud testing",
) -> bool:
    """
    Uploads and checks in a component via DR_*.CheckIn with a comment, sets the local file to Read-Only,
    and updates .admin with isCheckedOut=False and isDirty=False.
    """
    info = BDE_TYPE_MAP.get(comp_type.lower())
    if not info:
        raise ValueError(f"Unsupported component type '{comp_type}'")

    bde_name = info["bde"]
    ext = info["ext"]
    subfolder = info["subfolder"]
    pkg, mod, _ = _split_component_name(comp_name)
    dev_cp = f"{project_name}_dev"

    target_file = activity_dir / subfolder / f"{comp_name}{ext}"
    content = ""
    if target_file.exists():
        content = target_file.read_text(encoding="utf-8")

    req_xml = (
        f"<{bde_name}>\n"
        f"  <CheckInRequest>\n"
        f"    <name>{comp_name}</name>\n"
        f"    <package>{pkg}</package>\n"
        f"    <module>{mod}</module>\n"
        f"    <comment>{comment}</comment>\n"
        f"    <content><![CDATA[{content}]]></content>\n"
        f"  </CheckInRequest>\n"
        f"</{bde_name}>"
    )

    client.do_bde_call(bde_name, "CheckIn", req_xml, connection_point=dev_cp)

    if target_file.exists():
        try:
            os.chmod(target_file, stat.S_IREAD)
        except Exception:
            pass

        rel_path = target_file.relative_to(activity_dir).as_posix()
        try:
            set_component_status(
                activity_path=activity_dir,
                rel_path=rel_path,
                is_created=False,
                is_checked_out=False,
                is_dirty=False,
            )
        except Exception:
            pass

    return True
