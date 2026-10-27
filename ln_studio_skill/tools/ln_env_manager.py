#!/usr/bin/env python3
"""
ln_studio_skill/tools/ln_env_manager.py
Infor LN Studio Environment & .ionapi Configuration Manager.

Handles:
1. .ionapi credential import (Desktop & Service Account).
2. Global cloudenv.prefs synchronization for Eclipse LN Studio.
3. Workspace connectivity.prefs synchronization (ProjectServer, dev, rt).
4. OAuth2 token acquisition, silent refresh, and persistent cache outside Git.
5. Multi-workspace discovery and environment listing.
"""

import os
import sys
import json
import time
import urllib.parse
import urllib.request
import urllib.error
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union, Any


@dataclass
class IonapiConfig:
    tenant_id: str
    client_name: str
    device_type: str
    client_id: str
    client_secret: str
    gateway_url: str
    auth_url: str
    token_url: str
    revoke_url: str
    scope: str = "openid"
    saak: Optional[str] = None
    sask: Optional[str] = None

    def has_service_account(self) -> bool:
        return bool(self.saak and self.sask)


def parse_ionapi(ionapi_path: Union[str, Path]) -> IonapiConfig:
    """
    Parses an Infor ION API (.ionapi) JSON credentials file.
    Resolves full URLs for oauth endpoints if relative to pu (Passport URL).
    """
    p = Path(ionapi_path).resolve()
    if not p.exists():
        raise FileNotFoundError(f".ionapi file not found: {p}")

    with open(p, "r", encoding="utf-8") as f:
        data = json.load(f)

    ti = data.get("ti", "")
    cn = data.get("cn", "")
    dt = str(data.get("dt", "11"))
    ci = data.get("ci", "")
    cs = data.get("cs", "")
    iu = data.get("iu", "").rstrip("/")
    pu = data.get("pu", "").rstrip("/")
    oa = data.get("oa", "as/authorization.oauth2").lstrip("/")
    ot = data.get("ot", "as/token.oauth2").lstrip("/")
    or_url = data.get("or", "as/revoke_token.oauth2").lstrip("/")
    sc = data.get("sc", "openid")
    saak = data.get("saak")
    sask = data.get("sask")

    # Resolve authorization, token, and revoke URLs
    auth_url = f"{pu}/{oa}" if not oa.startswith("http") else oa
    token_url = f"{pu}/{ot}" if not ot.startswith("http") else ot
    revoke_url = f"{pu}/{or_url}" if not or_url.startswith("http") else or_url

    return IonapiConfig(
        tenant_id=ti,
        client_name=cn,
        device_type=dt,
        client_id=ci,
        client_secret=cs,
        gateway_url=iu,
        auth_url=auth_url,
        token_url=token_url,
        revoke_url=revoke_url,
        scope=sc,
        saak=saak,
        sask=sask,
    )


def _read_prefs_file(path: Path) -> Dict[str, str]:
    """Reads Eclipse .prefs file into key-value map, unescaping \\: and \\=."""
    props = {}
    if not path.exists():
        return props

    with open(path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                # Find unescaped '='
                parts = line.split("=", 1)
                k = parts[0].strip().replace(r"\:", ":").replace(r"\=", "=")
                v = parts[1].strip().replace(r"\:", ":").replace(r"\=", "=")
                props[k] = v
    return props


def _write_prefs_file(path: Path, props: Dict[str, str]) -> None:
    """Writes key-value map to Eclipse .prefs file with proper \\: escaping."""
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = []
    for k in sorted(props.keys()):
        # Escape colons and equals in keys/values as Eclipse expects
        v = props[k]
        escaped_v = v.replace(":", r"\:")
        lines.append(f"{k}={escaped_v}\n")

    with open(path, "w", encoding="utf-8") as f:
        f.writelines(lines)


def sync_cloudenv_prefs(prefs_path: Path, env_name: str, config: IonapiConfig) -> None:
    """
    Synchronizes an environment entry into global com.infor.erpln.jca.connectivity.cloudenv.prefs.
    If the environment already exists, updates it in place; otherwise appends it.
    """
    props = _read_prefs_file(prefs_path)
    count = int(props.get("EnvironmentsCount", "0"))

    # Check if env_name already exists
    target_idx = None
    for i in range(count):
        if props.get(f"EnvironmentName{i}") == env_name:
            target_idx = i
            break

    if target_idx is None:
        target_idx = count
        count += 1
        props["EnvironmentsCount"] = str(count)

    props[f"EnvironmentName{target_idx}"] = env_name
    props[f"TenantID{target_idx}"] = config.tenant_id
    props[f"GatewayURL{target_idx}"] = config.gateway_url
    props[f"AuthorizationCodeURL{target_idx}"] = config.auth_url
    props[f"RequestTokenURL{target_idx}"] = config.token_url
    props[f"RevokeTokenURL{target_idx}"] = config.revoke_url
    props[f"ClientID{target_idx}"] = config.client_id
    props[f"ClientSecret{target_idx}"] = config.client_secret
    props[f"AppScope{target_idx}"] = config.scope or ""
    props["eclipse.preferences.version"] = "1"

    _write_prefs_file(prefs_path, props)


def read_connectivity_prefs(prefs_path: Path) -> Dict[str, Dict[str, str]]:
    """
    Reads workspace com.infor.erpln.jca.connectivity.prefs and groups properties
    by connection Name (e.g. 'ProjectServer', 'EXTce01107_dev', 'EXTce01107_rt').
    """
    props = _read_prefs_file(prefs_path)
    count = int(props.get("ConfigurationCount", "0"))
    configs_by_name = {}

    for i in range(count):
        name = props.get(f"Name{i}")
        if not name:
            continue
        cfg = {"_index": str(i)}
        # Gather all indexed attributes for index i
        for k, v in props.items():
            if k.endswith(str(i)):
                attr_name = k[:-len(str(i))]
                if attr_name:
                    cfg[attr_name] = v
        configs_by_name[name] = cfg

    return configs_by_name


def sync_connectivity_prefs(
    prefs_path: Path,
    env_name: str,
    config: IonapiConfig,
    project_name: Optional[str] = None,
) -> None:
    """
    Synchronizes workspace com.infor.erpln.jca.connectivity.prefs.
    Ensures ProjectServer (Name1) is configured for http_oauth2 against the given CloudEnvironment,
    and configures shared dev/rt connection points if project_name is provided.
    """
    props = _read_prefs_file(prefs_path)
    count = int(props.get("ConfigurationCount", "8"))
    if count < 8:
        count = 8
    props["ConfigurationCount"] = str(count)
    props["eclipse.preferences.version"] = "1"

    # Default connections if empty
    if not props.get("Name0"):
        props["Name0"] = "Debug"
        props["Description0"] = "Debug Server"
        props["State0"] = "initial"
        props["Company0"] = "0"
        props["Port0"] = "0"
        props["MaxConnections0"] = "1"
        props["MaxReferences0"] = "-1"
        props["IsStatic0"] = "true"

    # ProjectServer (Index 1)
    props["Name1"] = "ProjectServer"
    props["Description1"] = "Project Server"
    props["ActivationType1"] = "http_oauth2"
    props["CloudEnvironment1"] = env_name
    props["HostName1"] = f"{config.gateway_url}/{config.tenant_id}/LN/webservice"
    props["Company1"] = "0"
    props["Port1"] = "0"
    props["MaxConnections1"] = "1"
    props["MaxReferences1"] = "-1"
    props["IsStatic1"] = "true"
    props["IsFixedCompany1"] = "true"
    props["State1"] = "valid"
    props["http_oauth21"] = "true"
    props["http_basic1"] = "true"
    props["bw1"] = "true"
    props["baanlogin1"] = "true"

    # Standard shared points (RuntimeRepositoryConnection, TestServerConnection, TestBdeEventConnection)
    for idx, (name, desc) in enumerate([
        ("RuntimeRepositoryConnection", "Runtime Repository"),
        ("TestServerConnection", "Test Server Connection"),
        ("TestBdeEventConnection", "Test BDE Event Connection"),
    ], start=2):
        props[f"Name{idx}"] = name
        props[f"Description{idx}"] = desc
        props[f"Company{idx}"] = "0"
        props[f"Port{idx}"] = "0"
        props[f"MaxConnections{idx}"] = "1"
        props[f"MaxReferences{idx}"] = "-1"
        props[f"IsStatic{idx}"] = "true"
        props[f"SharedWith{idx}"] = "ProjectServer"
        props[f"State{idx}"] = "valid"
        props[f"ActivationType{idx}"] = "bw"
        props[f"http_oauth2{idx}"] = "true"
        props[f"http_basic{idx}"] = "true"
        props[f"bw{idx}"] = "true"
        props[f"baanlogin{idx}"] = "true"

    # Dev and RT connection points for project_name
    if project_name:
        dev_name = f"{project_name}_dev"
        rt_name = f"{project_name}_rt"

        props["Name6"] = dev_name
        props["Description6"] = f"Development Address {dev_name}"
        props["ActivationType6"] = "bw"
        props["SharedWith6"] = "ProjectServer"
        props["Company6"] = "0"
        props["Port6"] = "0"
        props["MaxConnections6"] = "1"
        props["MaxReferences6"] = "-1"
        props["IsFixedCompany6"] = "true"
        props["State6"] = "valid"
        props["http_oauth26"] = "true"
        props["http_basic6"] = "true"
        props["bw6"] = "true"

        props["Name7"] = rt_name
        props["Description7"] = f"Runtime Address {rt_name}"
        props["ActivationType7"] = "bw"
        props["SharedWith7"] = "ProjectServer"
        props["Company7"] = "0"
        props["Port7"] = "0"
        props["MaxConnections7"] = "1"
        props["MaxReferences7"] = "-1"
        props["State7"] = "valid"
        props["http_oauth27"] = "true"
        props["http_basic7"] = "true"
        props["bw7"] = "true"

    _write_prefs_file(prefs_path, props)


def list_configured_environments(workspace_root: Optional[Path] = None) -> Dict[str, Dict[str, Any]]:
    """
    Scans workspaces under workspace_root and reads their JCA connectivity.prefs.
    Returns a dict mapping workspace_name -> { cloud_env, tenant_id, gateway_url, dev_point, rt_point, path }.
    """
    from ln_workspace_manager import get_workspace_root

    root = workspace_root or get_workspace_root()
    if not root or not root.exists():
        return {}

    results = {}
    for entry in sorted(root.iterdir()):
        if not entry.is_dir() or entry.name.startswith("."):
            continue

        prefs_file = entry / ".metadata" / ".plugins" / "org.eclipse.core.runtime" / ".settings" / "com.infor.erpln.jca.connectivity.prefs"
        if not prefs_file.exists():
            continue

        conns = read_connectivity_prefs(prefs_file)
        ps = conns.get("ProjectServer", {})
        cloud_env = ps.get("CloudEnvironment", "")
        host_name = ps.get("HostName", "")

        # Extract TenantID from HostName: https://.../<TenantID>/LN/webservice
        tenant_id = ""
        gateway_url = ""
        if host_name:
            parts = host_name.split("/")
            if len(parts) >= 4:
                tenant_id = parts[-3] if parts[-2:] == ["LN", "webservice"] else ""
                gateway_url = "/".join(parts[:-3])

        dev_point = ""
        rt_point = ""
        for name in conns.keys():
            if name.endswith("_dev"):
                dev_point = name
            elif name.endswith("_rt"):
                rt_point = name

        results[entry.name] = {
            "workspace": entry.name,
            "cloud_env": cloud_env,
            "tenant_id": tenant_id,
            "gateway_url": gateway_url,
            "host_name": host_name,
            "dev_point": dev_point,
            "rt_point": rt_point,
            "workspace_path": str(entry),
        }

    return results


class OAuth2TokenManager:
    """
    Manages OAuth2 access/refresh token caching and silent renewal.
    Caches tokens outside git at .cache/tokens/<env_name>.json.
    """

    def __init__(self, cache_dir: Optional[Path] = None):
        if cache_dir:
            self.cache_dir = Path(cache_dir).resolve()
        else:
            self.cache_dir = Path(__file__).resolve().parent.parent / ".cache" / "tokens"
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def _get_token_path(self, env_name: str) -> Path:
        return self.cache_dir / f"{env_name}.json"

    def load_token(self, env_name: str) -> Optional[Dict[str, Any]]:
        path = self._get_token_path(env_name)
        if path.exists():
            try:
                with open(path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                return None
        return None

    def save_token(self, env_name: str, token_data: Dict[str, Any]) -> None:
        path = self._get_token_path(env_name)
        if "expires_at" not in token_data and "expires_in" in token_data:
            token_data["expires_at"] = time.time() + float(token_data["expires_in"])
        with open(path, "w", encoding="utf-8") as f:
            json.dump(token_data, f, indent=2)

    def get_access_token(self, env_name: str, config: IonapiConfig) -> str:
        """
        Returns a valid access token.
        1. Checks cache for unexpired token (buffer 60 seconds).
        2. Silently refreshes via refresh_token if expired.
        3. Authenticates via service account (saak/sask) password grant if configured.
        4. Otherwise prompts/captures desktop authorization code.
        """
        cached = self.load_token(env_name)
        now = time.time()
        if cached:
            expires_at = cached.get("expires_at", 0)
            if expires_at - now > 60:
                return cached["access_token"]

            # Try silent refresh
            refresh_tok = cached.get("refresh_token")
            if refresh_tok:
                refreshed = self.refresh_access_token(config, refresh_tok)
                if refreshed and "access_token" in refreshed:
                    if "refresh_token" not in refreshed:
                        refreshed["refresh_token"] = refresh_tok
                    self.save_token(env_name, refreshed)
                    return refreshed["access_token"]

        # If Service Account is present, use password grant
        if config.has_service_account():
            token_resp = self.acquire_service_account_token(config)
            self.save_token(env_name, token_resp)
            return token_resp["access_token"]

        # Desktop login flow (oob redirect catcher or manual auth code)
        raise PermissionError(
            f"No valid token or refresh token for environment '{env_name}'. "
            f"Please run 'connect' with .ionapi or authenticate via browser: {config.auth_url}"
        )

    def refresh_access_token(self, config: IonapiConfig, refresh_token: str) -> Dict[str, Any]:
        """Exchanges refresh_token for a new access_token at token_url."""
        payload = urllib.parse.urlencode({
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            "client_id": config.client_id,
            "client_secret": config.client_secret,
        }).encode("utf-8")

        req = urllib.request.Request(
            config.token_url,
            data=payload,
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": "JCAWebClient (LNStudio)",
            },
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data

    def acquire_service_account_token(self, config: IonapiConfig) -> Dict[str, Any]:
        """Acquires access_token via password grant using saak/sask credentials."""
        payload = urllib.parse.urlencode({
            "grant_type": "password",
            "username": config.saak,
            "password": config.sask,
            "client_id": config.client_id,
            "client_secret": config.client_secret,
            "scope": config.scope or "openid",
        }).encode("utf-8")

        req = urllib.request.Request(
            config.token_url,
            data=payload,
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": "JCAWebClient (LNStudio)",
            },
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data

    def exchange_authorization_code(
        self,
        config: IonapiConfig,
        code: str,
        redirect_uri: str = "oob://localhost/lnstudio",
    ) -> Dict[str, Any]:
        """Exchanges authorization code for access and refresh tokens."""
        payload = urllib.parse.urlencode({
            "grant_type": "authorization_code",
            "code": code,
            "client_id": config.client_id,
            "client_secret": config.client_secret,
            "redirect_uri": redirect_uri,
        }).encode("utf-8")

        req = urllib.request.Request(
            config.token_url,
            data=payload,
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": "JCAWebClient (LNStudio)",
            },
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data
