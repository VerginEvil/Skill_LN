#!/usr/bin/env python3
"""
ln_studio_skill/tools/ln_env_manager.py
Infor LN Studio Environment & .ionapi Configuration Manager.

Handles:
1. .ionapi credential import (Desktop & Service Account).
2. Global cloudenv.prefs synchronization for Eclipse LN Studio.
3. Workspace connectivity.prefs synchronization (ProjectServer, dev, rt).
4. 3-Tier OAuth2 token lifecycle (`~/.ln_studio/tokens/<workspace>.json`):
   - Tier 1: Cached Active Token (with 5-minute / 300s expiry safety buffer)
   - Tier 2: Silent Refresh via `refresh_token` or Service Account `saak`/`sask`
   - Tier 3: Interactive Browser (`webbrowser.open`) + local loopback listener or `--manual-auth` paste mode
5. Multi-workspace discovery and environment listing.
"""

import http.server
import json
import os
import re
import socket
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
import webbrowser
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

TOKEN_EXPIRY_BUFFER_SECONDS = 300  # 5-minute safety buffer before expires_at
DEFAULT_REDIRECT_URI = "oob://localhost/lnstudio"


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
    redirect_uri: str = DEFAULT_REDIRECT_URI

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
    ru = data.get("ru") or DEFAULT_REDIRECT_URI

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
        redirect_uri=ru,
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


def extract_auth_code_from_input(raw_input_str: str) -> str:
    """
    Extracts the OAuth2 `code` parameter from either a full redirected URL
    (e.g. `oob://localhost/lnstudio?code=ABC123&state=...` or `http://localhost:8765/?code=ABC123`)
    or a raw authorization code string pasted by the user.
    """
    text = raw_input_str.strip()
    if not text:
        raise ValueError("Empty authorization input provided.")

    if "code=" in text:
        parsed = urllib.parse.urlparse(text)
        qs = urllib.parse.parse_qs(parsed.query)
        if "code" in qs and qs["code"]:
            return qs["code"][0].strip()
        # Fallback regex if custom scheme parsing varies
        m = re.search(r"[?&]code=([^&#\s]+)", text)
        if m:
            return urllib.parse.unquote(m.group(1)).strip()

    return text


class OAuth2TokenManager:
    """
    Implements the 3-Tier Automated OAuth2 Token Lifecycle (ADR 0008):
    1. Cached Active Token: Read from `~/.ln_studio/tokens/<workspace>.json` (with 5-minute / 300s safety buffer).
    2. Silent Refresh: Automatic HTTP POST to `.ionapi` token endpoint (`ot`) using cached `refresh_token`
       or Service Account credentials (`saak`/`sask`).
    3. Interactive Browser Fallback & Manual Paste Mode (`--manual-auth`):
       Launches `webbrowser.open` to `.ionapi` authorization URL (`oa`), spins up a local loopback
       listener (if http localhost redirect) or prompts user to paste redirected URL/code.
    """

    SAFETY_BUFFER_SECONDS = TOKEN_EXPIRY_BUFFER_SECONDS  # 300 seconds (5 minutes)

    def __init__(self, cache_dir: Optional[Path] = None):
        if cache_dir:
            self.cache_dir = Path(cache_dir).resolve()
        else:
            self.cache_dir = Path.home() / ".ln_studio" / "tokens"
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def _get_token_path(self, env_name: str) -> Path:
        safe_name = re.sub(r"[^a-zA-Z0-9_.-]", "_", env_name)
        return self.cache_dir / f"{safe_name}.json"

    def load_token(self, env_name: str) -> Optional[Dict[str, Any]]:
        path = self._get_token_path(env_name)
        if path.exists():
            try:
                with open(path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                return None
        return None

    def save_token(self, env_name: str, token_data: Dict[str, Any]) -> Path:
        path = self._get_token_path(env_name)
        path.parent.mkdir(parents=True, exist_ok=True)
        if "expires_at" not in token_data and "expires_in" in token_data:
            token_data["expires_at"] = time.time() + float(token_data["expires_in"])
        token_data["updated_at"] = time.time()
        with open(path, "w", encoding="utf-8") as f:
            json.dump(token_data, f, indent=2)
        return path

    def build_authorization_url(
        self,
        config: IonapiConfig,
        redirect_uri: Optional[str] = None,
    ) -> str:
        eff_redirect = redirect_uri or config.redirect_uri or DEFAULT_REDIRECT_URI
        params = {
            "client_id": config.client_id,
            "response_type": "code",
            "redirect_uri": eff_redirect,
            "scope": config.scope or "openid",
        }
        sep = "&" if "?" in config.auth_url else "?"
        return f"{config.auth_url}{sep}{urllib.parse.urlencode(params)}"

    def get_access_token(
        self,
        env_name: str,
        config: IonapiConfig,
        interactive: bool = False,
        manual_auth: bool = False,
        input_fn: Optional[Callable[[str], str]] = None,
        loopback_timeout: float = 120.0,
    ) -> str:
        """
        Executes the 3-Tier Automated Token Lifecycle:
        Tier 1: Check `~/.ln_studio/tokens/<workspace>.json` with a 5-minute (300s) safety buffer.
        Tier 2: Silently refresh via `refresh_token` or `saak`/`sask` Service Account credentials.
        Tier 3: Interactive Browser (`webbrowser.open`) + local loopback listener or `--manual-auth` paste fallback.
        """
        # Tier 1: Cached Active Token (5-minute / 300s safety buffer)
        cached = self.load_token(env_name)
        now = time.time()
        if cached and "access_token" in cached:
            expires_at = float(cached.get("expires_at", 0))
            if expires_at - now > self.SAFETY_BUFFER_SECONDS:
                return cached["access_token"]

            # Tier 2a: Silent Refresh using cached refresh_token
            refresh_tok = cached.get("refresh_token")
            if refresh_tok:
                try:
                    refreshed = self.refresh_access_token(config, refresh_tok)
                    if refreshed and "access_token" in refreshed:
                        if "refresh_token" not in refreshed:
                            refreshed["refresh_token"] = refresh_tok
                        if "expires_at" not in refreshed and "expires_in" in refreshed:
                            refreshed["expires_at"] = time.time() + float(refreshed["expires_in"])
                        self.save_token(env_name, refreshed)
                        return refreshed["access_token"]
                except Exception:
                    # Fall through to Service Account or Tier 3 Interactive Fallback
                    pass

        # Tier 2b: Silent Service Account (`saak`/`sask`) Password Grant
        if config.has_service_account():
            token_resp = self.acquire_service_account_token(config)
            if "expires_at" not in token_resp and "expires_in" in token_resp:
                token_resp["expires_at"] = time.time() + float(token_resp["expires_in"])
            self.save_token(env_name, token_resp)
            return token_resp["access_token"]

        # Tier 3: Interactive Browser Fallback & Manual Paste Mode
        if manual_auth or interactive or input_fn is not None:
            token_resp = self.acquire_interactive_token(
                env_name=env_name,
                config=config,
                manual_auth=manual_auth,
                input_fn=input_fn,
                loopback_timeout=loopback_timeout,
            )
            return token_resp["access_token"]

        auth_url = self.build_authorization_url(config)
        raise PermissionError(
            f"No valid token or refresh token for environment '{env_name}'. "
            f"Run 'connect' with --interactive or --manual-auth, or authenticate via browser: {auth_url}"
        )

    def acquire_interactive_token(
        self,
        env_name: str,
        config: IonapiConfig,
        manual_auth: bool = False,
        redirect_uri: Optional[str] = None,
        input_fn: Optional[Callable[[str], str]] = None,
        loopback_timeout: float = 120.0,
    ) -> Dict[str, Any]:
        """
        Tier 3 Interactive Browser & Manual Paste OAuth2 flow:
        - If `manual_auth=True`: prints the authorization URL and prompts user to paste redirected URL or code.
        - Otherwise: opens system browser (`webbrowser.open`) and either captures `?code=...` on a temporary
          local loopback HTTP server (when `redirect_uri` is `http://localhost:<port>`) or falls back to
          prompting the user to paste the `oob://localhost/lnstudio?code=...` redirect URL / code.
        """
        eff_redirect = redirect_uri or config.redirect_uri or DEFAULT_REDIRECT_URI
        auth_url = self.build_authorization_url(config, redirect_uri=eff_redirect)
        prompt_fn = input_fn or input

        captured_code: Optional[str] = None

        if not manual_auth:
            # Check if redirect_uri is a local HTTP loopback endpoint
            parsed_redir = urllib.parse.urlparse(eff_redirect)
            is_http_loopback = (
                parsed_redir.scheme == "http"
                and parsed_redir.hostname in ("localhost", "127.0.0.1")
            )
            if is_http_loopback:
                port = parsed_redir.port or 8765
                captured_code = self._run_loopback_listener_with_browser(
                    auth_url=auth_url,
                    port=port,
                    timeout=loopback_timeout,
                )
            else:
                try:
                    webbrowser.open(auth_url)
                except Exception:
                    pass

        if not captured_code:
            print(
                f"\n[OAuth2 Login Required for '{env_name}']\n"
                f"Authorization URL:\n  {auth_url}\n"
                f"After signing in, copy the redirected URL (e.g. oob://localhost/lnstudio?code=...) or authorization code.",
                file=sys.stderr,
            )
            raw_pasted = prompt_fn("Paste redirected URL or authorization code: ")
            captured_code = extract_auth_code_from_input(raw_pasted)

        token_resp = self.exchange_authorization_code(
            config=config,
            code=captured_code,
            redirect_uri=eff_redirect,
        )
        if "expires_at" not in token_resp and "expires_in" in token_resp:
            token_resp["expires_at"] = time.time() + float(token_resp["expires_in"])
        self.save_token(env_name, token_resp)
        return token_resp

    def _run_loopback_listener_with_browser(
        self,
        auth_url: str,
        port: int = 8765,
        timeout: float = 120.0,
    ) -> Optional[str]:
        """Spins up a temporary one-shot HTTP loopback server on `127.0.0.1:<port>` to catch `?code=...`."""
        captured: Dict[str, Optional[str]] = {"code": None}
        done_event = threading.Event()

        class _OAuthCallbackHandler(http.server.BaseHTTPRequestHandler):
            def do_GET(self):
                parsed = urllib.parse.urlparse(self.path)
                qs = urllib.parse.parse_qs(parsed.query)
                if "code" in qs and qs["code"]:
                    captured["code"] = qs["code"][0]
                    body = b"<html><body><h2>Infor LN Studio OAuth2 Login Successful!</h2><p>You may close this tab and return to your terminal.</p></body></html>"
                    self.send_response(200)
                else:
                    body = b"<html><body><h2>OAuth2 callback received without code.</h2></body></html>"
                    self.send_response(400)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
                done_event.set()

            def log_message(self, format: str, *args: Any) -> None:
                return  # Silence console logging

        try:
            server = http.server.HTTPServer(("127.0.0.1", port), _OAuthCallbackHandler)
            server.timeout = timeout
        except OSError:
            try:
                webbrowser.open(auth_url)
            except Exception:
                pass
            return None

        srv_thread = threading.Thread(target=server.handle_request, daemon=True)
        srv_thread.start()
        try:
            webbrowser.open(auth_url)
        except Exception:
            pass

        done_event.wait(timeout=timeout)
        try:
            server.server_close()
        except Exception:
            pass
        return captured["code"]

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
        redirect_uri: str = DEFAULT_REDIRECT_URI,
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
