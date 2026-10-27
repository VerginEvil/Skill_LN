#!/usr/bin/env python3
"""
ln_studio_skill/tools/ln_server_client.py
Infor LN Studio JCA Server Client and Transport Layer.

Provides:
1. JcaTransport interface and MockJcaTransport for offline testing and deterministic CI.
2. HeadlessJavaJcaTransport for interacting with LNStudioJcaBridge.java via JDK 11.
3. LNStudioServerClient high-level facade for BDE operations (ping, do_bde_call, compile, SCM).
"""

import os
import sys
import json
import subprocess
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union, Any


class BdeExecutionError(Exception):
    """Raised when a BDE execution fails on the LN Server."""
    def __init__(self, message: str, bde: str = "", method: str = "", raw_response: str = ""):
        super().__init__(message)
        self.bde = bde
        self.method = method
        self.raw_response = raw_response


class JcaTransport(ABC):
    """Abstract interface for JCA Transport."""

    @abstractmethod
    def ping(self) -> bool:
        """Pings the LN Server over JCA."""
        pass

    @abstractmethod
    def do_bde_call(
        self,
        bde_name: str,
        method_name: str,
        request_xml: str,
        connection_point: str = "ProjectServer",
    ) -> str:
        """Executes a BDE call and returns the XML response string."""
        pass


class MockJcaTransport(JcaTransport):
    """
    In-memory mock JCA transport for 100% offline testing and deterministic behavior.
    """

    def __init__(self):
        self.responses: Dict[Tuple[str, str], str] = {}
        self.errors: Dict[Tuple[str, str], str] = {}
        self.call_history: List[Dict[str, str]] = []
        self.ping_result = True

    def register_response(self, bde_name: str, method_name: str, response_xml: str) -> None:
        self.responses[(bde_name, method_name)] = response_xml

    def register_error(self, bde_name: str, method_name: str, error_message: str) -> None:
        self.errors[(bde_name, method_name)] = error_message

    def ping(self) -> bool:
        return self.ping_result

    def do_bde_call(
        self,
        bde_name: str,
        method_name: str,
        request_xml: str,
        connection_point: str = "ProjectServer",
    ) -> str:
        self.call_history.append({
            "bde": bde_name,
            "method": method_name,
            "request": request_xml,
            "connection_point": connection_point,
        })

        key = (bde_name, method_name)
        if key in self.errors:
            raise BdeExecutionError(
                self.errors[key],
                bde=bde_name,
                method=method_name,
                raw_response=f"<Error>{self.errors[key]}</Error>",
            )

        if key in self.responses:
            return self.responses[key]

        # Generic default response
        return f"<{bde_name}Response><status>success</status><method>{method_name}</method></{bde_name}Response>"


class HeadlessJavaJcaTransport(JcaTransport):
    """
    Production JCA transport using LNStudioJcaBridge.java executed via bundled JDK 11.
    """

    def __init__(
        self,
        gateway_url: str,
        tenant_id: str,
        access_token: str,
        jdk_path: Optional[Union[str, Path]] = None,
        studio_path: Optional[Union[str, Path]] = None,
        workspace_path: Optional[Union[str, Path]] = None,
    ):
        self.gateway_url = gateway_url.rstrip("/")
        self.tenant_id = tenant_id
        self.access_token = access_token

        # Resolve JDK path
        if jdk_path:
            self.jdk_path = Path(jdk_path)
        else:
            self.jdk_path = Path(r"D:\LN Studio\jdk-11.0.16.1")

        # Resolve Studio installation path
        if studio_path:
            self.studio_path = Path(studio_path)
        else:
            self.studio_path = Path(r"D:\LN Studio\April-2026\InforLNStudio_10_8_0_build0640-x86_64")

        self.workspace_path = Path(workspace_path) if workspace_path else None
        self._ensure_bridge_compiled()

    def _get_java_exe(self) -> str:
        java_bin = self.jdk_path / "bin" / "java.exe"
        if java_bin.exists():
            return str(java_bin)
        return "java"

    def _get_javac_exe(self) -> str:
        javac_bin = self.jdk_path / "bin" / "javac.exe"
        if javac_bin.exists():
            return str(javac_bin)
        return "javac"

    def _get_classpath(self) -> str:
        skill_root = Path(__file__).resolve().parent.parent
        lib_dir = skill_root / "tools" / "lib"

        conn_plugin_dir = self.studio_path / "plugins" / "com.infor.erpln.jca.connectivity_10.8.12.v0-20250703-1423" / "lib"

        jars = [
            str(lib_dir),
            str(lib_dir / "lnstudio_commoncore.jar"),
        ]

        if conn_plugin_dir.exists():
            for j in conn_plugin_dir.glob("*.jar"):
                jars.append(str(j))

        return ";".join(jars) if sys.platform == "win32" else ":".join(jars)

    def _ensure_bridge_compiled(self) -> None:
        skill_root = Path(__file__).resolve().parent.parent
        java_src = skill_root / "tools" / "lib" / "LNStudioJcaBridge.java"
        class_file = skill_root / "tools" / "lib" / "LNStudioJcaBridge.class"

        if not java_src.exists():
            return

        if not class_file.exists() or java_src.stat().st_mtime > class_file.stat().st_mtime:
            javac = self._get_javac_exe()
            cp = self._get_classpath()
            cmd = [javac, "-cp", cp, str(java_src)]
            res = subprocess.run(cmd, capture_output=True, text=True)
            if res.returncode != 0:
                print(f"[WARN] Failed to compile LNStudioJcaBridge.java: {res.stderr}", file=sys.stderr)

    def ping(self) -> bool:
        java_exe = self._get_java_exe()
        cp = self._get_classpath()
        cmd = [
            java_exe,
            "-cp",
            cp,
            "LNStudioJcaBridge",
            "--ping",
            "--backend",
            self.gateway_url,
            "--tenant",
            self.tenant_id,
            "--token",
            self.access_token,
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        return res.returncode == 0 and "PING_OK" in res.stdout

    def do_bde_call(
        self,
        bde_name: str,
        method_name: str,
        request_xml: str,
        connection_point: str = "ProjectServer",
    ) -> str:
        java_exe = self._get_java_exe()
        cp = self._get_classpath()
        cmd = [
            java_exe,
            "-cp",
            cp,
            "LNStudioJcaBridge",
            "--bde",
            bde_name,
            "--method",
            method_name,
            "--backend",
            self.gateway_url,
            "--tenant",
            self.tenant_id,
            "--token",
            self.access_token,
            "--cp",
            connection_point,
        ]
        if self.workspace_path:
            cmd.extend(["--workspace", str(self.workspace_path)])

        res = subprocess.run(cmd, input=request_xml, capture_output=True, text=True)
        if res.returncode != 0:
            raise BdeExecutionError(
                f"BDE call {bde_name}.{method_name} failed: {res.stderr or res.stdout}",
                bde=bde_name,
                method=method_name,
                raw_response=res.stdout,
            )
        return res.stdout


class LNStudioServerClient:
    """
    Unified client for communicating with Infor LN Server via JCA.
    """

    def __init__(self, transport: JcaTransport):
        self.transport = transport

    def ping(self) -> bool:
        return self.transport.ping()

    def do_bde_call(
        self,
        bde_name: str,
        method_name: str,
        request_xml: str,
        connection_point: str = "ProjectServer",
    ) -> str:
        return self.transport.do_bde_call(
            bde_name=bde_name,
            method_name=method_name,
            request_xml=request_xml,
            connection_point=connection_point,
        )
