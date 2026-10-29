#!/usr/bin/env python3
"""
ln_studio_skill/tools/ln_scm_engine.py
Infor LN Studio Authentic BDE SCM Check-Out / Check-In Engine, Verification Receipts,
Anti-Deception Guardrail, Batch Activity SCM, and Extension Modeler Auto-Segregation.

REA Discovered Protocols (from Infor LN Studio 10.8 lnstudio_commoncore.jar & fourglstudio_connectivity.jar):
1. CheckOut: Calls BDE method 'CheckOut' with authentic payload:
     <{bde_name}>
       <name>{comp_name}</name>
       <type>{comp_type}</type>
       <versionID>{base_vrc}</versionID>
       <taskLabel>{activity_guid_or_name}</taskLabel>
       <taskName>{activity_name}</taskName>
       <optionalContent>yes</optionalContent>
     </{bde_name}>
2. CheckIn: Calls BDE method 'CheckIn' with the full component XML containing
   inserted/updated <Version><documentation>{comment}</documentation></Version>.
3. UndoCheckOut: Calls BDE method 'UndoCheckOut' with authentic payload:
     <{bde_name}>
       <name>{comp_name}</name>
       <type>{comp_type}</type>
       <versionID>see Activity ID</versionID>
       <optionalContent>yes</optionalContent>
     </{bde_name}>
4. Context Envelope: Sets <ActivityID> into ControlArea via setadditionalControlAreaElement.
5. Strict Anti-Deception Guardrail: Requires valid server response receipts before updating
   local .admin state or claiming success. Halts immediately on server rejections without rollback.
6. Extension Modeler Auto-Segregation: Segregates tx* extension components to Guide-and-Paste Markdown (ADR 0006).
7. Protocol-Level Safety: Hard-blocks automated End Activity / Deliver (ADR 0007 / ADR 0008).
"""

import os
import sys
import stat
import hashlib
import subprocess
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union, Any

from ln_server_client import LNStudioServerClient, BdeExecutionError
from ln_component_explorer import BDE_TYPE_MAP, _split_component_name
from scm_guardrails import (
    ReadOnlyComponentError,
    is_extension_component,
    assert_file_writable,
    is_project_scm_enabled,
)
from admin_sync import add_component, set_component_status, list_admin_components


# Architectural Dependency Order for SCM and compilation operations
DEPENDENCY_ORDER = [
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
]


class PreCommitBoundaryError(Exception):
    """
    Raised whenever an automated agent or command attempts to execute
    'End Activity', 'Commit Activity', 'CloseTask', or 'FinalizeActivity'.
    Enforces the mandatory human review gate in LN Studio (ADR 0007 / ADR 0008).
    """
    pass


class ServerSCMExecutionError(Exception):
    """
    Raised whenever the Infor LN ERP server rejects an SCM operation,
    returns an XML handling error, lock conflict, or fault response.
    Unsuppressible hard guardrail preventing false assertions (ADR 0011).
    """
    def __init__(self, message: str, raw_response: str = "", component_name: str = "", operation: str = ""):
        super().__init__(message)
        self.raw_response = raw_response
        self.component_name = component_name
        self.operation = operation


class VerificationReceipt(dict):
    """
    Itemized Verification Receipt proving that an SCM operation succeeded on the LN Server.
    Behaves as a dictionary and evaluates truthy in boolean contexts.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__dict__ = self

    def __bool__(self) -> bool:
        return self.get("status") == "SUCCESS"

    def to_dict(self) -> Dict[str, Any]:
        return dict(self)

    def __str__(self) -> str:
        return (
            f"VerificationReceipt(\n"
            f"  Component: {self.get('component_name')} ({self.get('component_type')})\n"
            f"  Operation: {self.get('operation')}\n"
            f"  Status:    {self.get('status')}\n"
            f"  Version:   {self.get('version_id')}\n"
            f"  Activity:  {self.get('activity_name')}\n"
            f"  Server TS: {self.get('server_timestamp')}\n"
            f"  Token:     {self.get('receipt_token')}\n"
            f")"
        )


class CheckedOutPath(type(Path())):
    """Path subclass returned by checkout_component carrying the verification receipt."""
    receipt: Optional[VerificationReceipt] = None


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


def build_activity_context_xml(
    activity_name: str,
    base_vrc: str,
    connection_point: str,
    activity_guid: Optional[str] = None,
    description: str = "",
) -> str:
    """
    Generates authentic <ActivityID> XML envelope discovered via REA in ProjectProperties.class:
    <ActivityID>
      <activityName>{activity_name}</activityName>
      <activityDescription>{description}</activityDescription>
      <activityUUID>{activity_guid}</activityUUID>
      <baseVRC>{base_vrc}</baseVRC>
      <activityContext>{connection_point}</activityContext>
    </ActivityID>
    """
    guid = activity_guid or activity_name
    return (
        f"<ActivityID>"
        f"<activityName>{activity_name}</activityName>"
        f"<activityDescription>{description}</activityDescription>"
        f"<activityUUID>{guid}</activityUUID>"
        f"<baseVRC>{base_vrc}</baseVRC>"
        f"<activityContext>{connection_point}</activityContext>"
        f"</ActivityID>"
    )


def build_checkout_payload(
    bde_name: str,
    comp_name: str,
    comp_type: str,
    base_vrc: str,
    activity_name: str,
    task_label: Optional[str] = None,
) -> str:
    """
    Generates authentic CheckOut request XML discovered via REA in CmCheckOut.class:
    <{bde_name}>
      <name>{comp_name}</name>
      <type>{comp_type}</type>
      <versionID>{base_vrc}</versionID>
      <taskLabel>{task_label}</taskLabel>
      <taskName>{activity_name}</taskName>
      <optionalContent>yes</optionalContent>
    </{bde_name}>
    """
    lbl = task_label or activity_name
    return (
        f"<{bde_name}>\n"
        f"  <name>{comp_name}</name>\n"
        f"  <type>{comp_type}</type>\n"
        f"  <versionID>{base_vrc}</versionID>\n"
        f"  <taskLabel>{lbl}</taskLabel>\n"
        f"  <taskName>{activity_name}</taskName>\n"
        f"  <optionalContent>yes</optionalContent>\n"
        f"</{bde_name}>"
    )


def build_uncheckout_payload(
    bde_name: str,
    comp_name: str,
    comp_type: str,
) -> str:
    """
    Generates authentic UndoCheckOut request XML discovered via REA in CmUnCheckOut.class:
    <{bde_name}>
      <name>{comp_name}</name>
      <type>{comp_type}</type>
      <versionID>see Activity ID</versionID>
      <optionalContent>yes</optionalContent>
    </{bde_name}>
    """
    return (
        f"<{bde_name}>\n"
        f"  <name>{comp_name}</name>\n"
        f"  <type>{comp_type}</type>\n"
        f"  <versionID>see Activity ID</versionID>\n"
        f"  <optionalContent>yes</optionalContent>\n"
        f"</{bde_name}>"
    )


def build_checkin_payload(raw_component_xml: str, comment: str) -> str:
    """
    Generates authentic CheckIn request XML discovered via REA in CmCheckIn.class / BaanSCMConnector.class:
    Inserts or updates <Version><documentation>{comment}</documentation></Version> inside the full
    component XML definition without any artificial <CheckInRequest> wrappers.
    """
    raw = raw_component_xml.strip()
    if not raw:
        raise ValueError("Cannot build CheckIn payload from empty component definition")

    try:
        root = ET.fromstring(raw)
    except ET.ParseError as e:
        raise ValueError(f"Malformed component XML: {e}")

    # Strip XML namespace if present on root tag for consistency
    version_el = root.find("Version")
    if version_el is None:
        version_el = ET.SubElement(root, "Version")

    doc_el = version_el.find("documentation")
    if doc_el is None:
        doc_el = ET.SubElement(version_el, "documentation")
    doc_el.text = comment

    return ET.tostring(root, encoding="utf-8").decode("utf-8")


def parse_scm_receipt(
    response_xml: str,
    comp_name: str,
    comp_type: str,
    operation: str,
    activity_name: str,
    activity_guid: str,
    base_vrc: str = "B61O_a_ext",
) -> VerificationReceipt:
    """
    Verifies that an Infor LN server SCM response represents true success.
    Raises ServerSCMExecutionError immediately if any error indicator is detected.
    Extracts version ID, timestamp, and generates a verification token.
    """
    raw = response_xml.strip() if response_xml else ""
    if not raw:
        raise ServerSCMExecutionError(
            f"Server returned empty response for {operation} on component '{comp_name}'.",
            raw_response=raw,
            component_name=comp_name,
            operation=operation,
        )

    # Detect known server error keywords and exceptions
    error_indicators = [
        "xml handling error",
        "jcabderesultexception",
        "lock conflict",
        "is not checked out",
        "action not allowed",
        "bdeexecutionerror",
    ]
    raw_lower = raw.lower()
    for ind in error_indicators:
        if ind in raw_lower:
            raise ServerSCMExecutionError(
                f"[SCM_SERVER_ERROR] Infor LN Server rejected {operation} on '{comp_name}': {ind}",
                raw_response=raw,
                component_name=comp_name,
                operation=operation,
            )

    try:
        root = ET.fromstring(raw)
    except ET.ParseError as e:
        raise ServerSCMExecutionError(
            f"Invalid XML returned by server for {operation} on '{comp_name}': {e}",
            raw_response=raw,
            component_name=comp_name,
            operation=operation,
        )

    # Check for XML error tags
    tag_clean = root.tag.split("}")[-1] if "}" in root.tag else root.tag
    if tag_clean.lower() in ("error", "fault", "exception"):
        err_msg = root.findtext(".//message") or root.findtext(".//description") or root.text or raw
        raise ServerSCMExecutionError(
            f"[SCM_SERVER_ERROR] Server returned error for {operation} on '{comp_name}': {err_msg}",
            raw_response=raw,
            component_name=comp_name,
            operation=operation,
        )

    # Extract version ID
    version_id = (
        root.findtext(".//versionID")
        or root.findtext(".//Version/versionID")
        or root.findtext(".//revision")
        or root.attrib.get("versionID")
        or base_vrc
    ).strip()

    # Extract or generate server timestamp
    server_ts = (
        root.findtext(".//dateTime")
        or root.findtext(".//timestamp")
        or root.findtext(".//serverTimestamp")
        or datetime.now(timezone.utc).isoformat()
    )

    receipt_token = hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16]

    return VerificationReceipt(
        component_name=comp_name,
        component_type=comp_type,
        operation=operation,
        status="SUCCESS",
        server_timestamp=server_ts,
        version_id=version_id,
        activity_name=activity_name,
        activity_guid=activity_guid,
        receipt_token=receipt_token,
        raw_summary=raw[:200].replace("\n", " ").strip(),
    )


def find_component_file(activity_dir: Path, comp_name: str, comp_type: str) -> Optional[Path]:
    """
    Locates an existing component file in an activity folder across both:
    1. Eclipse standard layout: <pkg>/<type_singular>/<mod>/<comp_name>.<ext> (e.g. tx/table/cmg/txcmg010.tbl)
    2. Skill subfolder layout: <subfolder>/<comp_name>.<ext> (e.g. tables/txcmg010.tbl)
    3. Recursive filename matching.
    """
    info = BDE_TYPE_MAP.get(comp_type.lower())
    ext = info["ext"] if info else f".{comp_type[:3]}"
    subfolder = info["subfolder"] if info else f"{comp_type}s"
    pkg, mod, _ = _split_component_name(comp_name)

    type_singular = comp_type.lower()

    candidates = [
        activity_dir / pkg / type_singular / mod / f"{comp_name}{ext}",
        activity_dir / pkg / subfolder / mod / f"{comp_name}{ext}",
        activity_dir / subfolder / f"{comp_name}{ext}",
        activity_dir / type_singular / f"{comp_name}{ext}",
        activity_dir / f"{comp_name}{ext}",
    ]

    for cand in candidates:
        if cand.exists():
            return cand

    # Case-insensitive recursive glob
    target_name = f"{comp_name}{ext}".lower()
    try:
        for f in activity_dir.rglob(f"*{ext}"):
            if f.name.lower() == target_name:
                return f
    except Exception:
        pass

    return None


def get_target_component_path(activity_dir: Path, comp_name: str, comp_type: str) -> Path:
    """
    Determines the target path for writing a checked-out component.
    Prefers existing file location; otherwise defaults to Eclipse standard layout if activity has pkg directory,
    or skill subfolder layout.
    """
    existing = find_component_file(activity_dir, comp_name, comp_type)
    if existing:
        return existing

    info = BDE_TYPE_MAP.get(comp_type.lower())
    ext = info["ext"] if info else f".{comp_type[:3]}"
    subfolder = info["subfolder"] if info else f"{comp_type}s"
    pkg, mod, _ = _split_component_name(comp_name)

    # If activity directory already contains package folder (e.g. 'tx'), use Eclipse layout
    if pkg and (activity_dir / pkg).is_dir():
        target = activity_dir / pkg / comp_type.lower() / mod / f"{comp_name}{ext}"
    else:
        target = activity_dir / subfolder / f"{comp_name}{ext}"

    target.parent.mkdir(parents=True, exist_ok=True)
    return target


def checkout_component(
    client: LNStudioServerClient,
    comp_type: str,
    comp_name: str,
    activity_dir: Path,
    project_name: str,
    base_vrc: str = "B61O_a_ext",
    dev_connection: Optional[str] = None,
) -> CheckedOutPath:
    """
    Checks out a component on the Infor LN Server via authentic BDE DR_*.CheckOut,
    downloads the authentic component XML, clears the OS Read-Only flag, updates .admin,
    and returns a CheckedOutPath with the VerificationReceipt attached.
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
    task_id = activity_dir.name.split(" ")[0].strip("[]")
    dev_cp = dev_connection or f"{project_name}_dev"

    scm_enabled, reason = is_project_scm_enabled(activity_dir)
    target_file = get_target_component_path(activity_dir, comp_name, comp_type)
    if not scm_enabled:
        if target_file.exists():
            try:
                os.chmod(target_file, stat.S_IWRITE | stat.S_IREAD)
            except Exception:
                pass
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

        receipt = VerificationReceipt(
            component_name=comp_name,
            component_type=comp_type,
            operation="CheckOut",
            status="SUCCESS",
            server_timestamp=datetime.now(timezone.utc).isoformat(),
            version_id=base_vrc,
            activity_name=task_id,
            activity_guid=task_id,
            receipt_token=hashlib.sha256(f"NON_SCM_CKO:{comp_name}:{task_id}".encode()).hexdigest()[:16],
            raw_summary=f"Non-SCM project ({reason}): SCM server lock skipped; component is writable locally.",
            scm_mode="NON_SCM",
        )
        result_path = CheckedOutPath(target_file)
        result_path.receipt = receipt
        return result_path

    req_xml = build_checkout_payload(
        bde_name=bde_name,
        comp_name=comp_name,
        comp_type=comp_type,
        base_vrc=base_vrc,
        activity_name=task_id,
        task_label=task_id,
    )
    context_xml = build_activity_context_xml(
        activity_name=task_id,
        base_vrc=base_vrc,
        connection_point=dev_cp,
        activity_guid=task_id,
    )

    resp_xml = client.do_bde_call(
        bde_name=bde_name,
        method_name="CheckOut",
        request_xml=req_xml,
        connection_point=dev_cp,
        context_xml=context_xml,
    )

    # Parse and verify server receipt BEFORE any local file or .admin modification
    receipt = parse_scm_receipt(
        response_xml=resp_xml,
        comp_name=comp_name,
        comp_type=comp_type,
        operation="CheckOut",
        activity_name=task_id,
        activity_guid=task_id,
        base_vrc=base_vrc,
    )

    # Locate or create target file
    target_file = get_target_component_path(activity_dir, comp_name, comp_type)
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

    result_path = CheckedOutPath(target_file)
    result_path.receipt = receipt
    return result_path


def uncheckout_component(
    client: LNStudioServerClient,
    comp_type: str,
    comp_name: str,
    activity_dir: Path,
    project_name: str,
    base_vrc: str = "B61O_a_ext",
    dev_connection: Optional[str] = None,
) -> VerificationReceipt:
    """
    Reverts a checked-out component via DR_*.UndoCheckOut, sets the local file to Read-Only,
    and updates .admin with isCheckedOut=False. Returns VerificationReceipt.
    """
    info = BDE_TYPE_MAP.get(comp_type.lower())
    if not info:
        raise ValueError(f"Unsupported component type '{comp_type}'")

    bde_name = info["bde"]
    task_id = activity_dir.name.split(" ")[0].strip("[]")
    dev_cp = dev_connection or f"{project_name}_dev"

    scm_enabled, reason = is_project_scm_enabled(activity_dir)
    if not scm_enabled:
        target_file = find_component_file(activity_dir, comp_name, comp_type)
        if target_file and target_file.exists():
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
        receipt = VerificationReceipt(
            component_name=comp_name,
            component_type=comp_type,
            operation="UndoCheckOut",
            status="SUCCESS",
            server_timestamp=datetime.now(timezone.utc).isoformat(),
            version_id=base_vrc,
            activity_name=task_id,
            activity_guid=task_id,
            receipt_token=hashlib.sha256(f"NON_SCM_UNCKO:{comp_name}:{task_id}".encode()).hexdigest()[:16],
            raw_summary=f"Non-SCM project ({reason}): Reverted local checkout state in .admin.",
            scm_mode="NON_SCM",
        )
        return receipt

    req_xml = build_uncheckout_payload(
        bde_name=bde_name,
        comp_name=comp_name,
        comp_type=comp_type,
    )
    context_xml = build_activity_context_xml(
        activity_name=task_id,
        base_vrc=base_vrc,
        connection_point=dev_cp,
        activity_guid=task_id,
    )

    resp_xml = client.do_bde_call(
        bde_name=bde_name,
        method_name="UndoCheckOut",
        request_xml=req_xml,
        connection_point=dev_cp,
        context_xml=context_xml,
    )

    receipt = parse_scm_receipt(
        response_xml=resp_xml,
        comp_name=comp_name,
        comp_type=comp_type,
        operation="UndoCheckOut",
        activity_name=task_id,
        activity_guid=task_id,
        base_vrc=base_vrc,
    )

    target_file = find_component_file(activity_dir, comp_name, comp_type)
    if target_file and target_file.exists():
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

    return receipt


def put_component(
    client: LNStudioServerClient,
    comp_type: str,
    comp_name: str,
    activity_dir: Path,
    project_name: str,
    base_vrc: str = "B61O_a_ext",
    dev_connection: Optional[str] = None,
) -> VerificationReceipt:
    """
    Uploads modified component XML to the server Activity workarea via DR_*.Put
    without artificial wrappers. Returns VerificationReceipt.
    """
    info = BDE_TYPE_MAP.get(comp_type.lower())
    if not info:
        raise ValueError(f"Unsupported component type '{comp_type}'")

    bde_name = info["bde"]
    task_id = activity_dir.name.split(" ")[0].strip("[]")
    dev_cp = dev_connection or f"{project_name}_dev"

    target_file = find_component_file(activity_dir, comp_name, comp_type)
    if not target_file or not target_file.exists():
        raise FileNotFoundError(f"Component file not found for '{comp_name}' in {activity_dir}")

    content = target_file.read_text(encoding="utf-8")
    context_xml = build_activity_context_xml(
        activity_name=task_id,
        base_vrc=base_vrc,
        connection_point=dev_cp,
        activity_guid=task_id,
    )

    resp_xml = client.do_bde_call(
        bde_name=bde_name,
        method_name="Put",
        request_xml=content,
        connection_point=dev_cp,
        context_xml=context_xml,
    )

    receipt = parse_scm_receipt(
        response_xml=resp_xml,
        comp_name=comp_name,
        comp_type=comp_type,
        operation="Put",
        activity_name=task_id,
        activity_guid=task_id,
        base_vrc=base_vrc,
    )
    return receipt


def checkin_component(
    client: LNStudioServerClient,
    comp_type: str,
    comp_name: str,
    activity_dir: Path,
    project_name: str,
    comment: str = "Automated check-in for LN UI Cloud testing",
    base_vrc: str = "B61O_a_ext",
    dev_connection: Optional[str] = None,
) -> VerificationReceipt:
    """
    Uploads and checks in a component via DR_*.CheckIn with a comment embedded in
    <Version><documentation>, sets local file to Read-Only, and updates .admin.
    Returns VerificationReceipt.
    """
    if is_extension_component(comp_name):
        raise ReadOnlyComponentError(
            f"[ERROR] Failure checking-in the component. "
            f"Action on '{comp_name}' is not allowed in LN Studio. "
            f"Use session ttext1500m000 in LN UI to process extensions."
        )

    info = BDE_TYPE_MAP.get(comp_type.lower())
    if not info:
        raise ValueError(f"Unsupported component type '{comp_type}'")

    bde_name = info["bde"]
    task_id = activity_dir.name.split(" ")[0].strip("[]")
    dev_cp = dev_connection or f"{project_name}_dev"

    target_file = find_component_file(activity_dir, comp_name, comp_type)
    if not target_file or not target_file.exists():
        raise FileNotFoundError(f"Component file not found for '{comp_name}' in {activity_dir}")

    content = target_file.read_text(encoding="utf-8")
    req_xml = build_checkin_payload(content, comment)

    scm_enabled, reason = is_project_scm_enabled(activity_dir)
    if not scm_enabled:
        target_file.write_text(req_xml, encoding="utf-8")
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
        receipt = VerificationReceipt(
            component_name=comp_name,
            component_type=comp_type,
            operation="CheckIn",
            status="SUCCESS",
            server_timestamp=datetime.now(timezone.utc).isoformat(),
            version_id=base_vrc,
            activity_name=task_id,
            activity_guid=task_id,
            receipt_token=hashlib.sha256(f"NON_SCM_CKI:{comp_name}:{comment}".encode()).hexdigest()[:16],
            raw_summary=f"Non-SCM project ({reason}): Embedded check-in documentation '{comment}' into component definition.",
            scm_mode="NON_SCM",
        )
        return receipt

    context_xml = build_activity_context_xml(
        activity_name=task_id,
        base_vrc=base_vrc,
        connection_point=dev_cp,
        activity_guid=task_id,
    )

    resp_xml = client.do_bde_call(
        bde_name=bde_name,
        method_name="CheckIn",
        request_xml=req_xml,
        connection_point=dev_cp,
        context_xml=context_xml,
    )

    # Verify server response receipt BEFORE updating local file permissions or .admin
    receipt = parse_scm_receipt(
        response_xml=resp_xml,
        comp_name=comp_name,
        comp_type=comp_type,
        operation="CheckIn",
        activity_name=task_id,
        activity_guid=task_id,
        base_vrc=base_vrc,
    )

    # Set to Read-Only upon verified server success
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
    except Exception as e:
        print(f"[WARN] Failed to set isCheckedOut=False in .admin: {e}", file=sys.stderr)

    return receipt


# =========================================================================
# Ticket 03 & 04: Batch Activity SCM, Dirty Discovery & Extension Segregation
# =========================================================================

def get_component_type_from_extension(ext: str) -> Optional[str]:
    """Infers component type from file extension."""
    norm_ext = ext.lower()
    for c_type, info in BDE_TYPE_MAP.items():
        if info["ext"] == norm_ext:
            return c_type
    return None


def discover_dirty_components(activity_dir: Path) -> List[Dict[str, Any]]:
    """
    Scans the activity workspace directory and returns a sorted list of dirty / modified components
    in architectural dependency order.
    Inspects:
    1. .admin cache (isCheckedOut=True or isDirty=True)
    2. Writable files on disk across managed component directories
    3. Git status (if workspace is inside a git repository)
    """
    found_map: Dict[str, Dict[str, Any]] = {}

    # 1. Inspect .admin cache
    try:
        admin_comps = list_admin_components(activity_dir)
        for c in admin_comps:
            if c.get("isCheckedOut") or c.get("isDirty"):
                rel_p = c["path"]
                full_p = activity_dir / rel_p
                ext = full_p.suffix.lower()
                comp_type = get_component_type_from_extension(ext)
                if comp_type:
                    comp_name = full_p.stem
                    found_map[comp_name] = {
                        "name": comp_name,
                        "type": comp_type,
                        "path": full_p,
                        "rel_path": rel_p,
                        "is_extension": is_extension_component(comp_name) or comp_type == "extension",
                    }
    except Exception:
        pass

    # 2. Inspect filesystem for writable or modified component files
    valid_exts = {info["ext"] for info in BDE_TYPE_MAP.values()}
    for root, dirs, files in os.walk(activity_dir):
        # Skip .metadata and RemoteSystemsTempFiles
        if any(ignored in root for ignored in (".metadata", "RemoteSystemsTempFiles", ".git")):
            continue
        for f in files:
            p = Path(root) / f
            ext = p.suffix.lower()
            if ext in valid_exts:
                comp_type = get_component_type_from_extension(ext)
                comp_name = p.stem
                if comp_type and comp_name not in found_map:
                    # Check writable status or modification
                    try:
                        is_writable = (p.stat().st_mode & stat.S_IWRITE) != 0
                    except Exception:
                        is_writable = False

                    if is_writable:
                        found_map[comp_name] = {
                            "name": comp_name,
                            "type": comp_type,
                            "path": p,
                            "rel_path": p.relative_to(activity_dir).as_posix(),
                            "is_extension": is_extension_component(comp_name) or comp_type == "extension",
                        }

    # 3. Inspect git status if workspace is a git repo
    try:
        git_res = subprocess.run(
            ["git", "status", "--porcelain", str(activity_dir)],
            capture_output=True,
            text=True,
            check=False,
        )
        if git_res.returncode == 0:
            for line in git_res.stdout.splitlines():
                if len(line) >= 4:
                    status_flag = line[:2]
                    git_rel = line[3:].strip().strip('"')
                    git_p = Path(git_rel)
                    ext = git_p.suffix.lower()
                    if ext in valid_exts:
                        comp_type = get_component_type_from_extension(ext)
                        comp_name = git_p.stem
                        if comp_type and comp_name not in found_map:
                            found_map[comp_name] = {
                                "name": comp_name,
                                "type": comp_type,
                                "path": activity_dir / git_rel if not git_p.is_absolute() else git_p,
                                "rel_path": git_rel,
                                "is_extension": is_extension_component(comp_name) or comp_type == "extension",
                            }
    except Exception:
        pass

    # Sort in architectural dependency order
    def _order_key(item: Dict[str, Any]) -> int:
        c_type = item.get("type", "").lower()
        if c_type in DEPENDENCY_ORDER:
            return DEPENDENCY_ORDER.index(c_type)
        return 99

    ordered_list = sorted(found_map.values(), key=_order_key)
    return ordered_list


def segregate_extension_components(
    components: List[Dict[str, Any]],
) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    """
    Segregates standard LN Studio components from Extension Modeler components (ADR 0006).
    Returns (standard_components, extension_components).
    """
    standard = []
    extensions = []
    for c in components:
        comp_name = c["name"]
        comp_type = c.get("type", "")
        if is_extension_component(comp_name) or comp_type == "extension":
            extensions.append(c)
        else:
            standard.append(c)
    return standard, extensions


def format_extension_guide_markdown(
    segregated_components: List[Dict[str, Any]],
    activity_dir: Path,
) -> str:
    """
    Generates Guide-and-Paste Markdown documentation for LN UI session ttext1500m000
    for segregated Extension Modeler components (ADR 0006).
    """
    if not segregated_components:
        return ""

    lines = [
        "### Infor LN Extension Modeler Guide-and-Paste (ADR 0006)",
        "The following extension components are segregated from LN Studio BDE SCM.",
        "Please open Infor LN UI, navigate to session `ttext1500m000` (Extension Modeler), and paste the code:\n",
    ]

    for ext_comp in segregated_components:
        comp_name = ext_comp["name"]
        comp_path = ext_comp.get("path")
        code = ""
        if comp_path and Path(comp_path).exists():
            try:
                code = Path(comp_path).read_text(encoding="utf-8")
            except Exception:
                code = ""

        lines.append(f"#### Extension Component: `{comp_name}`")
        lines.append(f"- **Target Session**: `ttext1500m000`")
        lines.append(f"- **File Location**: `{comp_path}`")
        lines.append("```4gl")
        lines.append(code.strip())
        lines.append("```\n")

    return "\n".join(lines)


def checkout_activity(
    client: LNStudioServerClient,
    activity_dir: Path,
    project_name: str,
    base_vrc: str = "B61O_a_ext",
    dev_connection: Optional[str] = None,
    components: Optional[List[Tuple[str, str]]] = None,
) -> Dict[str, Any]:
    """
    Batch Check-Out for all components in an activity.
    Iterates in architectural dependency order.
    Halts immediately on first failure without blind rollback.
    """
    task_id = activity_dir.name.split(" ")[0].strip("[]")
    dev_cp = dev_connection or f"{project_name}_dev"

    if components:
        comp_list = []
        for c_type, c_name in components:
            comp_list.append({
                "name": c_name,
                "type": c_type,
                "is_extension": is_extension_component(c_name) or c_type == "extension",
            })
    else:
        comp_list = discover_dirty_components(activity_dir)
        if not comp_list:
            # Check all managed files in activity
            all_found = []
            for root, _, files in os.walk(activity_dir):
                for f in files:
                    ext = Path(f).suffix.lower()
                    c_type = get_component_type_from_extension(ext)
                    if c_type:
                        c_name = Path(f).stem
                        all_found.append({
                            "name": c_name,
                            "type": c_type,
                            "path": Path(root) / f,
                            "is_extension": is_extension_component(c_name) or c_type == "extension",
                        })
            comp_list = all_found

    def _order_key(item: Dict[str, Any]) -> int:
        c_type = item.get("type", "").lower()
        return DEPENDENCY_ORDER.index(c_type) if c_type in DEPENDENCY_ORDER else 99
    comp_list = sorted(comp_list, key=_order_key)

    standard_comps, extension_comps = segregate_extension_components(comp_list)
    receipts: List[VerificationReceipt] = []

    for comp in standard_comps:
        c_name = comp["name"]
        c_type = comp["type"]
        try:
            path_res = checkout_component(
                client=client,
                comp_type=c_type,
                comp_name=c_name,
                activity_dir=activity_dir,
                project_name=project_name,
                base_vrc=base_vrc,
                dev_connection=dev_cp,
            )
            if hasattr(path_res, "receipt") and path_res.receipt:
                receipts.append(path_res.receipt)
        except Exception as e:
            # Halt immediately on first failure without rolling back already successful check-outs
            raise ServerSCMExecutionError(
                f"Batch CheckOut halted on '{c_name}' ({c_type}): {e}. "
                f"Successfully checked out {len(receipts)} components prior to failure.",
                component_name=c_name,
                operation="CheckOut",
            ) from e

    # Touch timestamps to assist LN Studio UI cache
    try:
        activity_dir.touch(exist_ok=True)
    except Exception:
        pass

    return {
        "activity": task_id,
        "checked_out_count": len(receipts),
        "receipts": [r.to_dict() for r in receipts],
        "segregated_extensions": extension_comps,
        "extension_guide_markdown": format_extension_guide_markdown(extension_comps, activity_dir),
        "f5_refresh_prompt": "Please press F5 (Refresh) in Infor LN Studio (Eclipse) to display updated server checkout status.",
    }


def checkin_activity(
    client: LNStudioServerClient,
    activity_dir: Path,
    project_name: str,
    comment: str = "Automated activity check-in",
    base_vrc: str = "B61O_a_ext",
    dev_connection: Optional[str] = None,
    components: Optional[List[Tuple[str, str]]] = None,
) -> Dict[str, Any]:
    """
    Batch Check-In for all modified components in an activity with a single comment.
    Automatically segregates Extension Modeler components (ADR 0006).
    Iterates standard components in architectural dependency order.
    Halts immediately on first failure without blind rollback.
    """
    task_id = activity_dir.name.split(" ")[0].strip("[]")
    dev_cp = dev_connection or f"{project_name}_dev"

    if components:
        comp_list = []
        for c_type, c_name in components:
            comp_list.append({
                "name": c_name,
                "type": c_type,
                "is_extension": is_extension_component(c_name) or c_type == "extension",
            })
    else:
        comp_list = discover_dirty_components(activity_dir)

    def _order_key(item: Dict[str, Any]) -> int:
        c_type = item.get("type", "").lower()
        return DEPENDENCY_ORDER.index(c_type) if c_type in DEPENDENCY_ORDER else 99
    comp_list = sorted(comp_list, key=_order_key)

    standard_comps, extension_comps = segregate_extension_components(comp_list)
    receipts: List[VerificationReceipt] = []

    for comp in standard_comps:
        c_name = comp["name"]
        c_type = comp["type"]
        try:
            receipt = checkin_component(
                client=client,
                comp_type=c_type,
                comp_name=c_name,
                activity_dir=activity_dir,
                project_name=project_name,
                comment=comment,
                base_vrc=base_vrc,
                dev_connection=dev_cp,
            )
            receipts.append(receipt)
        except Exception as e:
            # Halt immediately on first failure without reverting already successful check-ins
            raise ServerSCMExecutionError(
                f"Batch CheckIn halted on '{c_name}' ({c_type}): {e}. "
                f"Successfully checked in {len(receipts)} components prior to failure.",
                component_name=c_name,
                operation="CheckIn",
            ) from e

    # Touch timestamps to assist LN Studio UI cache
    try:
        activity_dir.touch(exist_ok=True)
    except Exception:
        pass

    return {
        "activity": task_id,
        "checked_in_count": len(receipts),
        "receipts": [r.to_dict() for r in receipts],
        "segregated_extensions": extension_comps,
        "extension_guide_markdown": format_extension_guide_markdown(extension_comps, activity_dir),
        "f5_refresh_prompt": "Please press F5 (Refresh) in Infor LN Studio (Eclipse) to display updated server check-in status.",
    }
