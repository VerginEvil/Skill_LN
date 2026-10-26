#!/usr/bin/env python3
"""
ln_studio_skill/tools/scm_guardrails.py
Human-in-the-Loop SCM and Read-Only Protection Guardrails for Infor LN Studio.

Enforces strict Read-Only and SCM check-out protection across all file generation,
script injection, and synchronization operations. Prevents silent corruption of
checked-in components and guides developers to perform Check-out in LN Studio.
"""

import os
import stat
from pathlib import Path
from typing import Optional, Tuple, Union


class ReadOnlyComponentError(Exception):
    """Raised when an operation attempts to write to a read-only or checked-in component."""
    pass


def is_extension_component(path: Union[Path, str]) -> bool:
    """
    Checks if a component path represents an Infor LN Extension Modeler component
    (txess*, txest*, txesb*, txesm*, txesr*, or components located in
    /library/ess/, /library/est/, /library/esb/, /library/esm/, /library/esr/).
    """
    p = Path(path)
    name = p.name.lower()
    stem = p.stem.lower()

    # 1. Official Extension Modeler component prefixes
    ext_prefixes = ("txess", "txest", "txesb", "txesm", "txesr")
    if name.startswith(ext_prefixes) or stem.startswith(ext_prefixes):
        return True

    # 2. Directory path check for Studio extension library subfolders
    posix = p.as_posix().lower()
    for ext_type in ("ess", "est", "esb", "esm", "esr"):
        if f"/library/{ext_type}/" in posix or posix.endswith(f"/library/{ext_type}") or f"library/{ext_type}" in posix:
            return True

    # 3. Path parts check (handles OS-specific separators)
    parts = [part.lower() for part in p.parts]
    if "library" in parts:
        idx = parts.index("library")
        if idx + 1 < len(parts) and parts[idx + 1] in ("ess", "est", "esb", "esm", "esr"):
            return True

    return False


def is_file_readonly(path: Path) -> bool:
    """
    Checks if a file exists and has the OS Read-Only attribute set.
    """
    if not path.exists():
        return False

    # Check write access via standard os.access
    if not os.access(path, os.W_OK):
        return True

    # Windows-specific attribute check
    try:
        attrs = path.stat().st_file_attributes
        if attrs & stat.FILE_ATTRIBUTE_READONLY:
            return True
    except AttributeError:
        pass

    return False


def find_activity_root(path: Path) -> Optional[Path]:
    """
    Walks up the directory tree to find an Activity root folder
    (identified by having .admin, .project, or matching '<act> [<proj>]').
    """
    curr = path.resolve()
    if curr.is_file():
        curr = curr.parent

    while curr and curr != curr.parent:
        if (curr / ".admin").exists() or (curr / ".project").exists():
            return curr
        curr = curr.parent

    return None


def is_tracked_checked_in(path: Path, activity_path: Optional[Path] = None) -> Tuple[bool, Optional[str]]:
    """
    Checks if the component file is tracked in the activity's .admin SCM cache
    and marked checked-in (isCheckedOut=false and isCreated=false).
    """
    act_path = activity_path or find_activity_root(path)
    if not act_path or not (act_path / ".admin").exists():
        return False, None

    try:
        from admin_sync import list_admin_components
        comps = list_admin_components(act_path)
        try:
            rel = path.resolve().relative_to(act_path.resolve()).as_posix()
        except ValueError:
            return False, None

        for c in comps:
            if c["path"].lower() == rel.lower():
                # If not created and not checked out, it is checked-in on the server
                if not c.get("isCheckedOut", False) and not c.get("isCreated", False):
                    return True, rel
    except Exception:
        pass

    return False, None


def assert_file_writable(path: Union[Path, str], activity_path: Optional[Path] = None) -> None:
    """
    Asserts that the target path can be safely written to.
    Aborts immediately with ReadOnlyComponentError if:
    - The component is an Extension Modeler component (tx*, ess, est, esb, esm, esr)
      which is Read-Only in LN Studio.
    - The target directory or file is not writable.
    - The file is Read-Only on disk.
    - The file is checked in without check-out in .admin SCM cache.
    """
    p = Path(path)

    # 1. Extension Modeler Read-Only Guardrail (ADR 0006)
    if is_extension_component(p):
        comp_name = p.stem if p.suffix else p.name
        raise ReadOnlyComponentError(
            f"[ERROR] Failure checking-out the component. "
            f"Action on '{comp_name}' is not allowed in LN Studio. "
            f"Use session ttext1500m000 in LN UI to process extensions."
        )

    if not p.exists():
        # Parent directory must be checked if writing a new file
        parent = p.parent
        if parent.exists() and not os.access(parent, os.W_OK):
            raise ReadOnlyComponentError(
                f"[ERROR] Parent directory is not writable: '{parent}'. "
                f"Cannot create component '{p.name}'."
            )
        return

    if is_file_readonly(p):
        raise ReadOnlyComponentError(
            f"[ERROR] Target file is Read-Only on disk (checked-in): '{p}'. "
            f"Please Check-out the component in LN Studio (Eclipse Workbench) before modifying it."
        )

    checked_in, rel = is_tracked_checked_in(p, activity_path)
    if checked_in:
        raise ReadOnlyComponentError(
            f"[ERROR] Component '{rel or p.name}' is checked in (isCheckedOut=false) in .admin SCM cache: '{p}'. "
            f"Please Check-out the component in LN Studio (Eclipse Workbench) before modifying it."
        )
