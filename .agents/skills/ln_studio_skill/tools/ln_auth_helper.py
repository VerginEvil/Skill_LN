#!/usr/bin/env python3
"""
ln_studio_skill/tools/ln_auth_helper.py
Comprehensive OAuth2 Authentication & Token Acquisition Engine for Infor LN Studio.

Solves the Infor CloudSuite 'oob://localhost/lnstudio' browser protocol mismatch:
1. Multi-Channel Authorization Code Capture:
   - Channel A: Windows 'oob://' Custom URI Scheme Protocol Handler (HKCU registration)
   - Channel B: Zero-dependency Windows Clipboard Auto-Detection (ctypes user32)
   - Channel C: Interactive terminal prompt (accepts URL, raw code, or encoded string)
2. PingFederate / Infor OS Federation Hub Sensitivity Fix:
   - Generates cryptographically secure UUID `state` parameters
   - Suppresses invalid/unconfigured `scope` (e.g. 'openid') that triggers Federation Hub errors
3. Automated Token Exchange & Verification:
   - Exchanges authorization code for Access Token + Refresh Token
   - Automatically synchronizes cloudenv.prefs and workspace connectivity.prefs
   - Pings Infor LN Server via Headless JCA
"""

import os
import sys
import re
import time
import json
import uuid
import ctypes
import tempfile
import threading
import urllib.parse
from pathlib import Path
from typing import Optional, Dict, Any, Tuple

_TOOLS_DIR = Path(__file__).resolve().parent
if str(_TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(_TOOLS_DIR))

from ln_env_manager import IonapiConfig, OAuth2TokenManager, extract_auth_code_from_input


# ==============================================================================
# Windows Clipboard Monitoring (Zero External Dependencies)
# ==============================================================================

def get_windows_clipboard_text() -> Optional[str]:
    """Reads current unicode text from Windows clipboard using standard ctypes."""
    if sys.platform != "win32":
        return None

    user32 = ctypes.windll.user32
    kernel32 = ctypes.windll.kernel32

    user32.GetClipboardData.restype = ctypes.c_void_p
    user32.GetClipboardData.argtypes = [ctypes.c_uint]
    kernel32.GlobalLock.restype = ctypes.c_void_p
    kernel32.GlobalLock.argtypes = [ctypes.c_void_p]
    kernel32.GlobalUnlock.argtypes = [ctypes.c_void_p]

    if not user32.OpenClipboard(0):
        return None
    try:
        CF_UNICODETEXT = 13
        handle = user32.GetClipboardData(CF_UNICODETEXT)
        if not handle:
            return None
        pointer = kernel32.GlobalLock(handle)
        if not pointer:
            return None
        text = ctypes.c_wchar_p(pointer).value
        kernel32.GlobalUnlock(handle)
        return text
    except Exception:
        return None
    finally:
        user32.CloseClipboard()


# ==============================================================================
# Windows 'oob://' Custom URI Scheme Protocol Handler
# ==============================================================================

def get_oob_handler_script() -> Path:
    """Returns the path to the standalone oob protocol handler dispatcher script."""
    return _TOOLS_DIR / "capture_oob.py"


def register_oob_protocol() -> bool:
    """
    Registers 'oob://' custom URI scheme under HKEY_CURRENT_USER\\Software\\Classes\\oob.
    Requires ZERO administrator privileges. Allows Chrome/Edge to forward 'oob://localhost/lnstudio?code=...'
    directly into our Python handler.
    """
    if sys.platform != "win32":
        return False

    try:
        import winreg

        handler_py = get_oob_handler_script()
        python_exe = sys.executable

        key_path = r"Software\Classes\oob"
        with winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path) as key:
            winreg.SetValueEx(key, "", 0, winreg.REG_SZ, "URL:Infor LN Studio OOB Protocol")
            winreg.SetValueEx(key, "URL Protocol", 0, winreg.REG_SZ, "")

        cmd_key_path = r"Software\Classes\oob\shell\open\command"
        with winreg.CreateKey(winreg.HKEY_CURRENT_USER, cmd_key_path) as cmd_key:
            cmd_val = f'"{python_exe}" "{handler_py}" "%1"'
            winreg.SetValueEx(cmd_key, "", 0, winreg.REG_SZ, cmd_val)

        return True
    except Exception as e:
        print(f"[WARN] Failed to register oob:// protocol in registry: {e}", file=sys.stderr)
        return False


def unregister_oob_protocol() -> bool:
    """Unregisters 'oob://' custom URI scheme from HKEY_CURRENT_USER."""
    if sys.platform != "win32":
        return False
    try:
        import winreg
        def delete_key_tree(root, subkey):
            try:
                with winreg.OpenKey(root, subkey, 0, winreg.KEY_ALL_ACCESS) as k:
                    while True:
                        try:
                            child = winreg.EnumKey(k, 0)
                            delete_key_tree(root, f"{subkey}\\{child}")
                        except OSError:
                            break
                winreg.DeleteKey(root, subkey)
            except FileNotFoundError:
                pass

        delete_key_tree(winreg.HKEY_CURRENT_USER, r"Software\Classes\oob")
        return True
    except Exception as e:
        print(f"[WARN] Failed to unregister oob:// protocol: {e}", file=sys.stderr)
        return False


# ==============================================================================
# Multi-Channel Authorization Code Listener
# ==============================================================================

def get_pending_code_file(env_name: str) -> Path:
    """Returns path to the temporary pending auth code file."""
    cache_dir = Path.home() / ".ln_studio" / "tokens"
    cache_dir.mkdir(parents=True, exist_ok=True)
    return cache_dir / f".pending_code_{env_name}.txt"


def build_robust_auth_url(config: IonapiConfig, state: Optional[str] = None) -> Tuple[str, str]:
    """
    Builds authorization URL with strict compliance for Infor PingFederate:
    1. Generates a UUID `state` parameter to prevent Federation Hub errors.
    2. Only includes `scope` if explicitly configured and non-empty.
    """
    eff_state = state or str(uuid.uuid4())
    params = {
        "client_id": config.client_id,
        "response_type": "code",
        "redirect_uri": config.redirect_uri or "oob://localhost/lnstudio",
        "state": eff_state,
    }
    if config.scope and config.scope.strip() and config.scope.strip() != "openid":
        params["scope"] = config.scope.strip()

    sep = "&" if "?" in config.auth_url else "?"
    url = f"{config.auth_url}{sep}{urllib.parse.urlencode(params)}"
    return url, eff_state


def listen_and_capture_auth_code(
    env_name: str,
    auth_url: str,
    expected_state: str,
    timeout: float = 180.0,
) -> str:
    """
    Captures authorization code using 3 concurrent channels:
    Channel 1: Windows Protocol Handler ('oob://') file signal
    Channel 2: Windows Clipboard Auto-Detection
    Channel 3: Terminal manual prompt
    """
    pending_file = get_pending_code_file(env_name)
    if pending_file.exists():
        try:
            pending_file.unlink()
        except Exception:
            pass

    # Ensure Windows oob:// protocol handler is registered
    if sys.platform == "win32":
        register_oob_protocol()

    captured_code_box = [None]
    stop_event = threading.Event()

    # Channel 3: Background terminal prompt thread
    def terminal_input_worker():
        try:
            val = input("\n[Option C] Or paste redirected URL / code here: ").strip()
            if val and not captured_code_box[0]:
                code = extract_auth_code_from_input(val)
                if code:
                    captured_code_box[0] = code
                    stop_event.set()
        except (EOFError, KeyboardInterrupt):
            pass

    # Channel 2: Clipboard monitoring thread
    initial_clip = get_windows_clipboard_text()
    def clipboard_worker():
        nonlocal initial_clip
        while not stop_event.is_set():
            time.sleep(0.4)
            clip = get_windows_clipboard_text()
            if clip and clip != initial_clip:
                initial_clip = clip
                # Check if clipboard text looks like an authorization code or oob redirect URL
                if "oob://localhost/lnstudio" in clip or "code=" in clip:
                    code = extract_auth_code_from_input(clip)
                    if code and len(code) >= 10:
                        print(f"\n[AUTO-DETECT] Detected authorization URL in Clipboard!")
                        captured_code_box[0] = code
                        stop_event.set()
                        return

    # Start clipboard thread on Windows
    clip_thread = None
    if sys.platform == "win32":
        clip_thread = threading.Thread(target=clipboard_worker, daemon=True)
        clip_thread.start()

    prompt_thread = threading.Thread(target=terminal_input_worker, daemon=True)
    prompt_thread.start()

    # Banner explanation
    print("=" * 80)
    print(f"  Infor CloudSuite SSO Login for '{env_name}'")
    print("=" * 80)
    print(f"Authorization URL:\n  {auth_url}\n")
    print("How to complete login (choose any of the 3 automatic ways):")
    print("  1. In the opened browser tab, sign in and click 'Allow'.")
    print("  2. When prompted 'Open Infor LN Studio Auth Helper', click 'Open'. (Auto-captured!)")
    print("  3. OR if the browser shows 'This site can't be reached', simply COPY (Ctrl+C)")
    print("     the URL from the Address Bar! The terminal will auto-detect it immediately.")
    print("=" * 80)

    # Launch system browser
    try:
        import webbrowser
        webbrowser.open(auth_url)
    except Exception:
        pass

    # Channel 1: Main thread polls protocol signal file
    start_time = time.time()
    while time.time() - start_time < timeout:
        if stop_event.is_set() and captured_code_box[0]:
            break

        if pending_file.exists():
            try:
                content = pending_file.read_text(encoding="utf-8").strip()
                if content:
                    print(f"\n[AUTO-DETECT] Captured via Windows 'oob://' Protocol Handler!")
                    captured_code_box[0] = extract_auth_code_from_input(content)
                    pending_file.unlink(missing_ok=True)
                    stop_event.set()
                    break
            except Exception:
                pass

        time.sleep(0.3)

    stop_event.set()
    if not captured_code_box[0]:
        raise TimeoutError(f"OAuth2 login timed out after {timeout} seconds without receiving authorization code.")

    return captured_code_box[0]


# ==============================================================================
# High-Level Login Orchestrator
# ==============================================================================

def execute_login(
    env_name: str,
    config: IonapiConfig,
    workspace_name: Optional[str] = None,
    ping_after: bool = True,
    timeout: float = 180.0,
) -> Dict[str, Any]:
    """
    Executes a clean, self-contained, end-to-end OAuth2 login flow:
    1. Generates robust PingFederate-safe SSO URL.
    2. Runs multi-channel auto-capture (Windows oob protocol + clipboard + prompt).
    3. Exchanges authorization code for Access Token + Refresh Token.
    4. Saves token cache to ~/.ln_studio/tokens/<env>.json.
    5. Synchronizes Eclipse connectivity preferences if workspace specified.
    6. Verifies live connection via JCA ping.
    """
    token_mgr = OAuth2TokenManager()
    auth_url, state = build_robust_auth_url(config)

    code = listen_and_capture_auth_code(
        env_name=env_name,
        auth_url=auth_url,
        expected_state=state,
        timeout=timeout,
    )

    print(f"\n[OK] Exchanging authorization code for OAuth2 tokens...")
    token_resp = token_mgr.exchange_authorization_code(
        config=config,
        code=code,
        redirect_uri=config.redirect_uri or "oob://localhost/lnstudio",
    )

    saved_path = token_mgr.save_token(env_name, token_resp)
    print(f"[SUCCESS] OAuth2 Access Token & Refresh Token saved to: {saved_path}")

    # Synchronize workspace connectivity if provided
    from ln_workspace_manager import get_workspace_root
    from ln_env_manager import sync_cloudenv_prefs, sync_connectivity_prefs

    from ln_workspace_manager import get_studio_installation_path
    studio_path = get_studio_installation_path()
    cloudenv_prefs = studio_path / "configuration" / ".settings" / "com.infor.erpln.jca.connectivity.cloudenv.prefs"
    sync_cloudenv_prefs(cloudenv_prefs, env_name, config)

    ws_root = get_workspace_root()
    ws = workspace_name or env_name
    if ws_root and (ws_root / ws).exists():
        ws_path = ws_root / ws
        conn_prefs = ws_path / ".metadata" / ".plugins" / "org.eclipse.core.runtime" / ".settings" / "com.infor.erpln.jca.connectivity.prefs"
        sync_connectivity_prefs(conn_prefs, env_name, config)
        print(f"[OK] Synchronized workspace connectivity.prefs in '{ws_path}'")

    if ping_after:
        from ln_server_client import HeadlessJavaJcaTransport, LNStudioServerClient
        print(f"[...] Pinging Infor LN Server for '{env_name}'...")
        transport = HeadlessJavaJcaTransport(
            gateway_url=config.gateway_url,
            tenant_id=config.tenant_id,
            access_token=token_resp["access_token"],
            studio_path=studio_path,
        )
        client = LNStudioServerClient(transport=transport)
        if client.ping():
            print(f"[SUCCESS] Live JCA Ping verified for '{env_name}'! Connection is fully ready.")
        else:
            print(f"[WARN] JCA Ping returned false.", file=sys.stderr)

    return token_resp
