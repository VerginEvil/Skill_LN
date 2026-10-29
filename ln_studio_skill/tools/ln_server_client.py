#!/usr/bin/env python3
"""
ln_studio_skill/tools/ln_server_client.py
Infor LN Studio JCA Server Client, BYOJ Auto-Discovery Resolver, and Transport Layer.

Provides:
1. BYOJ (Bring Your Own JARs) auto-discovery (`resolve_ln_studio_home`, `resolve_ln_studio_jars`)
   locating `JCAAdapter4ERPln*.jar` and `com.infor.ln.studio.common.core_*.jar` from
   `LN_STUDIO_HOME`, environment variables, or local Eclipse LN Studio installations without
   tracking proprietary Infor JARs in Git.
2. JcaTransport interface and MockJcaTransport for offline testing and deterministic CI.
3. HeadlessJavaJcaTransport for interacting with LNStudioJcaBridge.java via JDK 11+.
4. LNStudioServerClient high-level facade for BDE operations (ping, do_bde_call, compile, SCM),
   enforcing protocol-level removal of EndActivity / CloseTask / FinalizeActivity (ADR 0008).
"""

import glob
import json
import os
import subprocess
import sys
import xml.etree.ElementTree as ET
import zipfile
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

PROHIBITED_BDE_METHODS = {
    "endactivity",
    "closetask",
    "finalizeactivity",
    "deliveractivity",
    "commitactivity",
    "completeactivity",
}

PROHIBITED_XML_PATTERNS = (
    "<endactivity",
    "<closetask",
    "<finalizeactivity",
    "<deliveractivity",
    "<end/>",
    "<end>",
    "<deliver/>",
    "<deliver>",
)

STANDARD_STUDIO_SEARCH_PATHS = [
    r"D:\LN Studio\April-2026\InforLNStudio_10_8_0_build0640-x86_64",
    r"D:\LN Studio\InforLNStudio_10_8_0_build0640-x86_64",
    r"C:\Infor\LN Studio\InforLNStudio_10_8_0_build0640-x86_64",
    r"C:\LN Studio\InforLNStudio_10_8_0_build0640-x86_64",
]


class BdeExecutionError(PermissionError):
    """Raised when a BDE execution fails or is prohibited on the LN Server."""

    def __init__(self, message: str, bde: str = "", method: str = "", raw_response: str = ""):
        super().__init__(message)
        self.bde = bde
        self.method = method
        self.raw_response = raw_response


def assert_not_prohibited_activity_closure(bde_name: str, method_name: str, request_xml: str = "") -> None:
    """
    Protocol-level safety check (ADR 0007 / ADR 0008):
    Rejects any attempt to invoke EndActivity, CloseTask, FinalizeActivity, or Deliver.
    """
    b_low = (bde_name or "").strip().lower()
    m_low = (method_name or "").strip().lower()
    if m_low in PROHIBITED_BDE_METHODS or any(p in m_low for p in PROHIBITED_BDE_METHODS) or any(p in b_low for p in PROHIBITED_BDE_METHODS):
        raise BdeExecutionError(
            f"[PROHIBITED_OPERATION] Protocol-level guardrail (ADR 0008): '{bde_name}.{method_name}' "
            f"(EndActivity/CloseTask) is physically prohibited. Use 'prepare-end-activity' for read-only "
            f"verification and complete the activity manually in LN Studio.",
            bde=bde_name,
            method=method_name,
        )
    if request_xml:
        xml_low = request_xml.lower()
        for pat in PROHIBITED_XML_PATTERNS:
            if pat in xml_low:
                raise BdeExecutionError(
                    f"[PROHIBITED_OPERATION] Protocol-level guardrail (ADR 0008): XML payload containing '{pat}' "
                    f"is physically prohibited from executing activity closure.",
                    bde=bde_name,
                    method=method_name,
                )


def resolve_ln_studio_home(explicit_path: Optional[Union[str, Path]] = None) -> Optional[Path]:
    """
    Locates the local Eclipse Infor LN Studio installation directory (`LN_STUDIO_HOME`)
    using explicit parameter, environment variables, `.ln_studio_config.json`, or standard paths.
    """
    candidates: List[Path] = []
    if explicit_path:
        candidates.append(Path(explicit_path))

    for env_var in ("LN_STUDIO_HOME", "LN_STUDIO_PATH", "INFOR_LN_STUDIO_HOME"):
        val = os.environ.get(env_var, "").strip()
        if val:
            candidates.append(Path(val))

    # Check .ln_studio_config.json if present
    skill_root = Path(__file__).resolve().parent.parent
    for cfg_cand in (Path.cwd() / ".ln_studio_config.json", skill_root.parent / ".ln_studio_config.json"):
        if cfg_cand.exists():
            try:
                cfg_data = json.loads(cfg_cand.read_text(encoding="utf-8"))
                for key in ("ln_studio_home", "studio_path"):
                    if cfg_data.get(key):
                        candidates.append(Path(cfg_data[key]))
            except Exception:
                pass

    for std_p in STANDARD_STUDIO_SEARCH_PATHS:
        candidates.append(Path(std_p))

    # Glob search under D:\LN Studio or C:\Infor
    for base_glob in (r"D:\LN Studio\**\InforLNStudio*", r"C:\Infor\**\InforLNStudio*"):
        try:
            for g in glob.glob(base_glob, recursive=True):
                candidates.append(Path(g))
        except Exception:
            pass

    for cand in candidates:
        if not cand.exists():
            continue
        # If user pointed directly to plugins/ or a JCA jar directory, normalize or accept
        if (cand / "plugins").is_dir() or cand.name == "plugins" or list(cand.glob("JCAAdapter4ERPln*.jar")):
            return cand.parent if cand.name == "plugins" else cand

    return candidates[0] if candidates else None


def resolve_ln_studio_jars(
    studio_path: Optional[Union[str, Path]] = None,
    cache_dir: Optional[Path] = None,
) -> Dict[str, Any]:
    """
    BYOJ (Bring Your Own JARs) Auto-Discovery Resolver (ADR 0008).
    Locates `JCAAdapter4ERPln*.jar`, all JCA connectivity dependency JARs, and
    `lnstudio_commoncore.jar` (extracting it on demand from `com.infor.ln.studio.common.core_*.jar`
    into `~/.ln_studio/jars/` if needed) without bundling proprietary JARs in Git.
    """
    resolved_home = resolve_ln_studio_home(studio_path)
    jar_cache_dir = Path(cache_dir) if cache_dir else (Path.home() / ".ln_studio" / "jars")
    skill_lib_dir = Path(__file__).resolve().parent / "lib"

    jca_adapter_jar: Optional[Path] = None
    jca_lib_jars: List[Path] = []
    commoncore_jar: Optional[Path] = None

    # 1. Check explicit JCA_JAR_PATH env var if set
    env_jca_jar = os.environ.get("JCA_JAR_PATH", "").strip()
    if env_jca_jar and Path(env_jca_jar).exists():
        p = Path(env_jca_jar)
        if p.is_file():
            jca_adapter_jar = p
            jca_lib_jars = list(p.parent.glob("*.jar"))
        elif p.is_dir():
            matches = sorted(p.rglob("JCAAdapter4ERPln*.jar"))
            if matches:
                jca_adapter_jar = matches[0]
                jca_lib_jars = list(jca_adapter_jar.parent.glob("*.jar"))

    # 2. Search inside resolved LN Studio installation
    if resolved_home and resolved_home.exists():
        if not jca_adapter_jar:
            # Direct search in resolved_home or plugins/com.infor.erpln.jca.connectivity_*/lib/
            direct_matches = sorted(resolved_home.glob("JCAAdapter4ERPln*.jar"))
            if not direct_matches and (resolved_home / "plugins").is_dir():
                direct_matches = sorted((resolved_home / "plugins").glob("com.infor.erpln.jca.connectivity_*/lib/JCAAdapter4ERPln*.jar"))
            if not direct_matches:
                direct_matches = sorted(resolved_home.rglob("JCAAdapter4ERPln*.jar"))
            if direct_matches:
                jca_adapter_jar = direct_matches[-1]
                jca_lib_jars = sorted(jca_adapter_jar.parent.glob("*.jar"))

        # Resolve or extract lnstudio_commoncore.jar from com.infor.ln.studio.common.core_*.jar
        plugins_dir = resolved_home / "plugins" if (resolved_home / "plugins").is_dir() else resolved_home
        core_bundles = sorted(plugins_dir.glob("com.infor.ln.studio.common.core_*.jar"))
        if core_bundles:
            bundle_jar = core_bundles[-1]
            try:
                jar_cache_dir.mkdir(parents=True, exist_ok=True)
                extracted_target = jar_cache_dir / "lnstudio_commoncore.jar"
                if not extracted_target.exists():
                    with zipfile.ZipFile(bundle_jar, "r") as zf:
                        if "lnstudio_commoncore.jar" in zf.namelist():
                            extracted_target.write_bytes(zf.read("lnstudio_commoncore.jar"))
                if extracted_target.exists():
                    commoncore_jar = extracted_target
            except Exception:
                pass

    # 3. Fallback check in ~/.ln_studio/jars or untracked local tools/lib/
    if not commoncore_jar:
        for cand in (jar_cache_dir / "lnstudio_commoncore.jar", skill_lib_dir / "lnstudio_commoncore.jar"):
            if cand.exists():
                commoncore_jar = cand
                break

    if not jca_adapter_jar:
        local_jca = sorted(skill_lib_dir.glob("JCAAdapter4ERPln*.jar"))
        if local_jca:
            jca_adapter_jar = local_jca[-1]
            jca_lib_jars = sorted(skill_lib_dir.glob("*.jar"))

    classpath_entries: List[str] = [str(skill_lib_dir)]
    if commoncore_jar:
        classpath_entries.append(str(commoncore_jar))
    for j in jca_lib_jars:
        if str(j) not in classpath_entries:
            classpath_entries.append(str(j))

    sep = ";" if sys.platform == "win32" else ":"
    return {
        "studio_home": str(resolved_home) if resolved_home else None,
        "jca_jar": str(jca_adapter_jar) if jca_adapter_jar else None,
        "jca_adapter_jar": str(jca_adapter_jar) if jca_adapter_jar else None,
        "jca_lib_jars": [str(j) for j in jca_lib_jars],
        "commoncore_jar": str(commoncore_jar) if commoncore_jar else None,
        "classpath": sep.join(classpath_entries),
    }


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
        context_xml: Optional[str] = None,
    ) -> str:
        """Executes a BDE call and returns the XML response string."""
        pass


class MockJcaTransport(JcaTransport):
    """
    In-memory mock JCA transport for 100% offline testing and deterministic behavior.
    Enforces protocol-level removal of EndActivity / CloseTask.
    """

    def __init__(self):
        self.responses: Dict[Tuple[str, str], str] = {}
        self.errors: Dict[Tuple[str, str], str] = {}
        self.handlers: Dict[Tuple[str, str], Any] = {}
        self.call_history: List[Dict[str, Any]] = []
        self.ping_result = True

    def register_response(self, bde_name: str, method_name: str, response_xml: str) -> None:
        self.responses[(bde_name, method_name)] = response_xml

    def register_error(self, bde_name: str, method_name: str, error_message: str) -> None:
        self.errors[(bde_name, method_name)] = error_message

    def register_handler(self, bde_name: str, method_name: str, callback: Any) -> None:
        self.handlers[(bde_name, method_name)] = callback

    def ping(self) -> bool:
        return self.ping_result

    def do_bde_call(
        self,
        bde_name: str,
        method_name: str,
        request_xml: str,
        connection_point: str = "ProjectServer",
        context_xml: Optional[str] = None,
    ) -> str:
        assert_not_prohibited_activity_closure(bde_name, method_name, request_xml)

        self.call_history.append({
            "bde": bde_name,
            "method": method_name,
            "request": request_xml,
            "connection_point": connection_point,
            "context_xml": context_xml,
        })

        key = (bde_name, method_name)
        if key in self.handlers:
            return self.handlers[key](request_xml, connection_point, context_xml)

        if key in self.errors:
            raise BdeExecutionError(
                self.errors[key],
                bde=bde_name,
                method=method_name,
                raw_response=f"<Error>{self.errors[key]}</Error>",
            )

        if key in self.responses:
            return self.responses[key]

        return f"<{bde_name}Response><status>success</status><method>{method_name}</method></{bde_name}Response>"


class HeadlessJavaJcaTransport(JcaTransport):
    """
    Production JCA transport using LNStudioJcaBridge.java executed via bundled JDK 11+.
    Uses BYOJ auto-discovery (`resolve_ln_studio_jars`) to locate `JCAAdapter4ERPln*.jar`.
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

        if jdk_path:
            self.jdk_path = Path(jdk_path)
        else:
            env_jdk = os.environ.get("JAVA_HOME", "").strip()
            self.jdk_path = Path(env_jdk) if env_jdk else Path(r"D:\LN Studio\jdk-11.0.16.1")

        self.jar_info = resolve_ln_studio_jars(studio_path=studio_path)
        self.studio_path = Path(self.jar_info["studio_home"]) if self.jar_info.get("studio_home") else None
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
        self.jar_info = resolve_ln_studio_jars(studio_path=self.studio_path)
        return self.jar_info["classpath"]

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
        context_xml: Optional[str] = None,
    ) -> str:
        assert_not_prohibited_activity_closure(bde_name, method_name, request_xml)

        if not self.jar_info.get("jca_adapter_jar"):
            raise RuntimeError(
                "BYOJ Error: Could not locate 'JCAAdapter4ERPln*.jar'. "
                "Please set the LN_STUDIO_HOME environment variable to your Infor LN Studio installation directory."
            )

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
        if context_xml:
            cmd.extend(["--context", context_xml])
        if self.workspace_path:
            cmd.extend(["--workspace", str(self.workspace_path)])

        res = subprocess.run(cmd, input=request_xml, capture_output=True, text=True)
        if res.returncode == 3:
            raise PermissionError(res.stderr.strip() or "EndActivity is physically blocked by LNStudioJcaBridge.")
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

    def __init__(
        self,
        transport: Optional[JcaTransport] = None,
        workspace_dir: Optional[Union[str, Path]] = None,
    ):
        self.workspace_dir = Path(workspace_dir) if workspace_dir else None
        self.transport: JcaTransport = transport if transport is not None else MockJcaTransport()

    def ping(self) -> bool:
        return self.transport.ping()

    def do_bde_call(
        self,
        bde_name: str,
        method_name: str,
        request_xml: str,
        connection_point: str = "ProjectServer",
        context_xml: Optional[str] = None,
    ) -> str:
        assert_not_prohibited_activity_closure(bde_name, method_name, request_xml)
        return self.transport.do_bde_call(
            bde_name=bde_name,
            method_name=method_name,
            request_xml=request_xml,
            connection_point=connection_point,
            context_xml=context_xml,
        )
