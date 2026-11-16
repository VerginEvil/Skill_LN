#!/usr/bin/env python3
"""
ln_studio_skill/tools/properties_index.py
Byte-accurate reader, writer, and manager for Eclipse binary PropertyBucket (`properties.index`).

Matches org.eclipse.core.internal.properties.PropertyBucket and Bucket serialization
format (DataOutputStream / DataInputStream big-endian):
- byte version = 1 (0x01)
- int entryCount (number of resource paths in bucket)
- for each resource:
  - UTF path ("" for project root)
  - unsignedShort propCount
  - for each property:
    - tag: byte 2 (QNAME) if qualifier is unseen in this file:
      - UTF qualifier
      - records 0-based qualifier index in file-scoped list
    - tag: byte 1 (INDEX) if qualifier was already seen:
      - int index (4-byte big-endian signed integer)
    - UTF localName
    - UTF value
"""

import os
import io
import sys
import struct
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Any, Union


# Eclipse PropertyBucket binary protocol constants
VERSION: int = 1
TAG_INDEX: int = 1
TAG_QNAME: int = 2


def _read_utf(stream: io.BytesIO) -> str:
    """Reads a DataInputStream-compatible UTF-8 string (2-byte unsigned length + bytes)."""
    raw_len = stream.read(2)
    if len(raw_len) < 2:
        raise EOFError("Unexpected EOF while reading UTF string length")
    length, = struct.unpack(">H", raw_len)
    data = stream.read(length)
    if len(data) < length:
        raise EOFError(f"Unexpected EOF while reading UTF data: expected {length} bytes, got {len(data)}")
    return data.decode("utf-8")


def _write_utf(stream: io.BytesIO, text: str) -> None:
    """Writes a DataOutputStream-compatible UTF-8 string."""
    encoded = text.encode("utf-8")
    if len(encoded) > 65535:
        raise ValueError(f"UTF string exceeds maximum length 65535: {len(encoded)} bytes")
    stream.write(struct.pack(">H", len(encoded)))
    stream.write(encoded)


class PropertyBucket:
    """
    In-memory representation of an Eclipse PropertyBucket (`properties.index`).
    Maintains properties per resource path (e.g. `""` for the project root).
    """

    def __init__(self, version: int = VERSION):
        self.version = version
        # Map: resource_path -> dict of (qualifier, local_name) -> value
        self.entries: Dict[str, Dict[Tuple[str, str], str]] = {}

    def get_property(
        self,
        local_name: str,
        qualifier: str = "",
        resource_path: str = "",
    ) -> Optional[str]:
        """Gets a property value by qualifier and local name on a resource path."""
        res_props = self.entries.get(resource_path)
        if res_props is None:
            return None
        return res_props.get((qualifier, local_name))

    def set_property(
        self,
        local_name: str,
        value: str,
        qualifier: str = "",
        resource_path: str = "",
    ) -> None:
        """Sets a property value by qualifier and local name on a resource path."""
        if resource_path not in self.entries:
            self.entries[resource_path] = {}
        self.entries[resource_path][(qualifier, local_name)] = str(value)

    def delete_property(
        self,
        local_name: str,
        qualifier: str = "",
        resource_path: str = "",
    ) -> bool:
        """Deletes a property. Returns True if deleted, False if not present."""
        if resource_path in self.entries:
            key = (qualifier, local_name)
            if key in self.entries[resource_path]:
                del self.entries[resource_path][key]
                return True
        return False

    def get_project_properties(self, resource_path: str = "") -> Dict[str, str]:
        """Returns all unqualified project properties (qualifier="")."""
        res_props = self.entries.get(resource_path, {})
        return {name: val for (q, name), val in res_props.items() if q == ""}

    def set_project_properties(self, props: Dict[str, str], resource_path: str = "") -> None:
        """Bulk updates unqualified project properties (qualifier="")."""
        for name, val in props.items():
            self.set_property(name, val, qualifier="", resource_path=resource_path)

    def get_studio_settings(self, resource_path: str = "") -> Dict[str, str]:
        """Returns all LN Studio project settings (qualifier="IStudio_Core")."""
        res_props = self.entries.get(resource_path, {})
        return {name: val for (q, name), val in res_props.items() if q == "IStudio_Core"}

    def set_studio_settings(self, settings: Dict[str, str], resource_path: str = "") -> None:
        """Bulk updates LN Studio project settings (qualifier="IStudio_Core")."""
        for name, val in settings.items():
            self.set_property(name, val, qualifier="IStudio_Core", resource_path=resource_path)

    @classmethod
    def decode(cls, data: bytes) -> "PropertyBucket":
        """Decodes raw binary bytes of a PropertyBucket."""
        stream = io.BytesIO(data)
        raw_v = stream.read(1)
        if not raw_v:
            return cls(version=VERSION)
        version, = struct.unpack("b", raw_v)
        entry_count, = struct.unpack(">I", stream.read(4))

        bucket = cls(version=version)
        qualifier_table: List[str] = []

        for _ in range(entry_count):
            path = _read_utf(stream)
            prop_count, = struct.unpack(">H", stream.read(2))
            bucket.entries[path] = {}

            for _ in range(prop_count):
                tag, = struct.unpack("b", stream.read(1))
                if tag == TAG_QNAME:
                    qualifier = _read_utf(stream)
                    qualifier_table.append(qualifier)
                elif tag == TAG_INDEX:
                    q_idx, = struct.unpack(">i", stream.read(4))
                    if q_idx < 0 or q_idx >= len(qualifier_table):
                        raise IndexError(f"Qualifier index {q_idx} out of range (size {len(qualifier_table)})")
                    qualifier = qualifier_table[q_idx]
                else:
                    raise ValueError(f"Unknown PropertyBucket qualifier tag: {tag}")

                local_name = _read_utf(stream)
                val = _read_utf(stream)
                bucket.entries[path][(qualifier, local_name)] = val

        return bucket

    def encode(self) -> bytes:
        """Encodes this PropertyBucket to byte-accurate Eclipse binary format."""
        stream = io.BytesIO()
        stream.write(struct.pack("b", self.version))
        stream.write(struct.pack(">I", len(self.entries)))

        qualifier_index: List[str] = []

        for path, props in self.entries.items():
            _write_utf(stream, path)
            stream.write(struct.pack(">H", len(props)))

            for (qualifier, local_name), value in props.items():
                if qualifier not in qualifier_index:
                    stream.write(struct.pack("b", TAG_QNAME))
                    _write_utf(stream, qualifier)
                    qualifier_index.append(qualifier)
                else:
                    stream.write(struct.pack("b", TAG_INDEX))
                    q_idx = qualifier_index.index(qualifier)
                    stream.write(struct.pack(">i", q_idx))

                _write_utf(stream, local_name)
                _write_utf(stream, value)

        return stream.getvalue()

    def save(self, file_path: Union[str, Path]) -> None:
        """Encodes and saves bucket to disk, creating parent directories if needed."""
        target = Path(file_path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(self.encode())

    @classmethod
    def load(cls, file_path: Union[str, Path]) -> "PropertyBucket":
        """Loads and decodes PropertyBucket from disk file."""
        target = Path(file_path)
        if not target.exists():
            return cls(version=VERSION)
        return cls.decode(target.read_bytes())


def read_properties_index(file_path: Union[str, Path]) -> PropertyBucket:
    """Convenience function to read a PropertyBucket from file."""
    return PropertyBucket.load(file_path)


def write_properties_index(file_path: Union[str, Path], bucket: PropertyBucket) -> None:
    """Convenience function to write a PropertyBucket to file."""
    bucket.save(file_path)


def find_project_properties_index(activity_path: Union[str, Path]) -> Optional[Path]:
    """
    Finds the active `properties.index` file for an activity project folder.
    Checks:
    1. <workspace>/.metadata/.plugins/org.eclipse.core.resources/.projects/<project>/.indexes/properties.index
    2. <activity>/.settings/properties.index
    3. <activity>/properties.index
    """
    act = Path(activity_path).resolve()
    # If passed a file within the activity, resolve to activity folder
    if act.is_file():
        act = act.parent

    # Try upward traversal to find workspace .metadata
    curr = act
    for _ in range(4):
        metadata_cand = curr / ".metadata" / ".plugins" / "org.eclipse.core.resources" / ".projects" / act.name / ".indexes" / "properties.index"
        if metadata_cand.exists():
            return metadata_cand
        if (curr / ".metadata").exists():
            # Workspace root reached
            cand = curr / ".metadata" / ".plugins" / "org.eclipse.core.resources" / ".projects" / act.name / ".indexes" / "properties.index"
            return cand
        curr = curr.parent

    # Local activity candidates
    settings_cand = act / ".settings" / "properties.index"
    if settings_cand.exists():
        return settings_cand
    root_cand = act / "properties.index"
    if root_cand.exists():
        return root_cand

    # Default to expected Eclipse metadata location if workspace parent has .metadata
    ws_parent = act.parent
    if (ws_parent / ".metadata").exists():
        return ws_parent / ".metadata" / ".plugins" / "org.eclipse.core.resources" / ".projects" / act.name / ".indexes" / "properties.index"

    return None


def is_workspace_locked(workspace_path: Union[str, Path]) -> Dict[str, Any]:
    """
    Checks whether <workspace>/.metadata/.lock exists and is locked by an active Eclipse/LN Studio instance.
    Returns structured status:
    {
        "locked": bool,
        "exists": bool,
        "lock_file": str,
        "reason": Optional[str]
    }
    """
    ws = Path(workspace_path).resolve()
    lock_file = ws / ".metadata" / ".lock"
    if not lock_file.exists():
        return {
            "locked": False,
            "exists": False,
            "lock_file": str(lock_file),
            "reason": None,
        }

    try:
        with open(lock_file, "r+b") as f:
            if sys.platform == "win32":
                try:
                    import msvcrt
                    # Attempt non-blocking lock of 1 byte to test for existing locks
                    msvcrt.locking(f.fileno(), msvcrt.LK_NBLCK, 1)
                    msvcrt.locking(f.fileno(), msvcrt.LK_UNLCK, 1)
                except (PermissionError, OSError) as e:
                    return {
                        "locked": True,
                        "exists": True,
                        "lock_file": str(lock_file),
                        "reason": f"File is locked by active process: {e}",
                    }
        return {
            "locked": False,
            "exists": True,
            "lock_file": str(lock_file),
            "reason": None,
        }
    except (PermissionError, OSError) as e:
        return {
            "locked": True,
            "exists": True,
            "lock_file": str(lock_file),
            "reason": f"File is locked by active process: {e}",
        }
