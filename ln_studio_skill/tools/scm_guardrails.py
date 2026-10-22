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
from typing import Optional, Tuple


class ReadOnlyComponentError(Exception):
    """Raised when an operation attempts to write to a read-only or checked-in component."""
    pass


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


def assert_file_writable(path: Path, activity_path: Optional[Path] = None) -> None:
    """
    Asserts that the target path can be safely written to.
    Aborts immediately with ReadOnlyComponentError if the file is Read-Only
    or checked in without check-out in .admin.
    """
    if not path.exists():
        # Parent directory must be checked if writing a new file
        parent = path.parent
        if parent.exists() and not os.access(parent, os.W_OK):
            raise ReadOnlyComponentError(
                f"[ERROR] Parent directory is not writable: '{parent}'. "
                f"Cannot create component '{path.name}'."
            )
        return

    if is_file_readonly(path):
        raise ReadOnlyComponentError(
            f"[ERROR] Target file is Read-Only on disk (checked-in): '{path}'. "
            f"Please Check-out the component in LN Studio (Eclipse Workbench) before modifying it."
        )

    checked_in, rel = is_tracked_checked_in(path, activity_path)
    if checked_in:
        raise ReadOnlyComponentError(
            f"[ERROR] Component '{rel or path.name}' is checked in (isCheckedOut=false) in .admin SCM cache: '{path}'. "
            f"Please Check-out the component in LN Studio (Eclipse Workbench) before modifying it."
        )
