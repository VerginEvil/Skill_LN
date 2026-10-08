#!/usr/bin/env python3
"""
tools/ln_studio_bridge.py
Infor LN Studio Window Action Bridge (Refresh, Save, Build).

Detects running Infor LN Studio (Eclipse RCP) window and sends Windows keyboard
commands (F5 Refresh, Ctrl+Shift+S Save All, Ctrl+B Build All) to automate
workspace synchronization and server compilation.
"""

import os
import sys
import time
import ctypes
import argparse
from pathlib import Path
from typing import Optional, List, Tuple

_current_dir = Path(__file__).resolve().parent
_repo_root = _current_dir.parent
for p in (str(_repo_root), str(_current_dir)):
    if p not in sys.path:
        sys.path.insert(0, p)

try:
    from tools.ln_error_reader import read_activity_diagnostics
    from tools.ln_workspace_manager import load_config
except ImportError:
    from ln_error_reader import read_activity_diagnostics
    from ln_workspace_manager import load_config

# Windows API Virtual-Key Codes
VK_CONTROL = 0x11
VK_SHIFT = 0x10
VK_F5 = 0x74
VK_B = 0x42
VK_S = 0x53

KEYEVENTF_KEYUP = 0x0002


def find_ln_studio_windows() -> List[Tuple[int, str]]:
    """
    Enumerates top-level windows and returns list of (hwnd, title)
    for windows matching Infor LN Studio or Eclipse.
    """
    if os.name != "nt":
        return []

    user32 = ctypes.windll.user32
    results = []

    def enum_windows_proc(hwnd, lparam):
        if user32.IsWindowVisible(hwnd):
            length = user32.GetWindowTextLengthW(hwnd)
            if length > 0:
                buff = ctypes.create_unicode_buffer(length + 1)
                user32.GetWindowTextW(hwnd, buff, length + 1)
                title = buff.value
                t_lower = title.lower()
                if "infor ln studio" in t_lower or "eclipse" in t_lower or "baan" in t_lower:
                    results.append((hwnd, title))
        return True

    WNDENUMPROC = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)
    user32.EnumWindows(WNDENUMPROC(enum_windows_proc), 0)
    return results


def activate_window(hwnd: int) -> bool:
    """Brings window to the foreground."""
    user32 = ctypes.windll.user32
    SW_RESTORE = 9
    user32.ShowWindow(hwnd, SW_RESTORE)
    user32.SetForegroundWindow(hwnd)
    time.sleep(0.15)
    return True


def send_key_press(vk_code: int) -> None:
    """Sends a single key down and key up."""
    user32 = ctypes.windll.user32
    user32.keybd_event(vk_code, 0, 0, 0)
    time.sleep(0.05)
    user32.keybd_event(vk_code, 0, KEYEVENTF_KEYUP, 0)
    time.sleep(0.05)


def send_ctrl_key(vk_code: int, with_shift: bool = False) -> None:
    """Sends Ctrl (+ Shift) + Key combination."""
    user32 = ctypes.windll.user32
    user32.keybd_event(VK_CONTROL, 0, 0, 0)
    if with_shift:
        user32.keybd_event(VK_SHIFT, 0, 0, 0)
    time.sleep(0.05)

    user32.keybd_event(vk_code, 0, 0, 0)
    time.sleep(0.05)
    user32.keybd_event(vk_code, 0, KEYEVENTF_KEYUP, 0)
    time.sleep(0.05)

    if with_shift:
        user32.keybd_event(VK_SHIFT, 0, KEYEVENTF_KEYUP, 0)
    user32.keybd_event(VK_CONTROL, 0, KEYEVENTF_KEYUP, 0)
    time.sleep(0.05)


def trigger_refresh(hwnd: int) -> None:
    """Sends F5 (Refresh) to LN Studio."""
    activate_window(hwnd)
    send_key_press(VK_F5)


def trigger_save_all(hwnd: int) -> None:
    """Sends Ctrl+Shift+S (Save All) to LN Studio."""
    activate_window(hwnd)
    send_ctrl_key(VK_S, with_shift=True)


def trigger_build_all(hwnd: int) -> None:
    """Sends Ctrl+B (Build All) to LN Studio."""
    activate_window(hwnd)
    send_ctrl_key(VK_B, with_shift=False)


def trigger_build_and_diagnose(
    activity_name: Optional[str] = None,
    settle_seconds: float = 3.0,
    errors_only: bool = False
) -> int:
    """
    Automates full cycle:
    1. Activate LN Studio window
    2. Refresh (F5)
    3. Build All (Ctrl+B)
    4. Settle wait
    5. Parse and print .markers diagnostics
    """
    windows = find_ln_studio_windows()
    if not windows:
        print("[WARNING] Infor LN Studio window not detected. Changes are saved on disk.", file=sys.stderr)
        print("[NOTE] Launch LN Studio and press F5 / Ctrl+B to trigger server compile.", file=sys.stderr)
        return 0

    hwnd, title = windows[0]
    print(f"[ACTION] Focusing window: '{title}' (hwnd: {hwnd})")

    # Step 1: Refresh
    print("[ACTION] Sending F5 (Refresh)...")
    trigger_refresh(hwnd)
    time.sleep(1.0)

    # Step 2: Build All
    print("[ACTION] Sending Ctrl+B (Build All)...")
    trigger_build_all(hwnd)

    # Step 3: Wait for compilation to complete
    print(f"[ACTION] Waiting {settle_seconds:.1f}s for JCA compilation to settle...")
    time.sleep(settle_seconds)

    # Step 4: Read diagnostics
    print("[ACTION] Inspecting Eclipse problem markers...")
    try:
        diag = read_activity_diagnostics(activity_name=activity_name, errors_only=errors_only)
        print(f"=== Build Diagnostics: {diag['folder']} ===")
        print(f"Errors: {diag['errors_count']} | Warnings: {diag['warnings_count']}")
        print("-" * 65)

        if diag["errors_count"] == 0:
            print("[CLEAN] Compilation clean: 0 errors.")
        else:
            for m in diag["markers"]:
                if m["severity"] == "ERROR":
                    print(f"  [ERROR] {m['file']}:{m['line']} -> {m['message']}")

        return 1 if diag["errors_count"] > 0 else 0
    except Exception as e:
        print(f"[WARN] Could not read diagnostics: {e}")
        return 0


def main():
    parser = argparse.ArgumentParser(description="Infor LN Studio Window Action Bridge")
    parser.add_argument("--list-windows", action="store_true", help="List detected Infor LN Studio windows")
    parser.add_argument("--refresh", action="store_true", help="Send F5 (Refresh)")
    parser.add_argument("--save-all", action="store_true", help="Send Ctrl+Shift+S (Save All)")
    parser.add_argument("--build", action="store_true", help="Send Ctrl+B (Build All)")
    parser.add_argument("--build-and-check", action="store_true", help="Trigger Refresh + Build, wait, and check diagnostics")
    parser.add_argument("--activity", help="Activity name for diagnostics check")
    parser.add_argument("--settle", type=float, default=3.0, help="Wait time in seconds after build (default: 3.0)")
    parser.add_argument("--errors-only", action="store_true", help="Only report errors")

    args = parser.parse_args()

    if args.list_windows:
        wins = find_ln_studio_windows()
        print(f"Detected {len(wins)} LN Studio / Eclipse window(s):")
        for h, t in wins:
            print(f"  hwnd: {h:<10} | title: '{t}'")
        return

    windows = find_ln_studio_windows()
    if not windows:
        print("[WARNING] Infor LN Studio window not detected. Offline mode.", file=sys.stderr)
        if args.build_and_check:
            sys.exit(0)
        return

    hwnd, title = windows[0]

    if args.refresh:
        print(f"[ACTION] Sending F5 (Refresh) to '{title}'")
        trigger_refresh(hwnd)
        return

    if args.save_all:
        print(f"[ACTION] Sending Ctrl+Shift+S (Save All) to '{title}'")
        trigger_save_all(hwnd)
        return

    if args.build:
        print(f"[ACTION] Sending Ctrl+B (Build All) to '{title}'")
        trigger_build_all(hwnd)
        return

    if args.build_and_check:
        code = trigger_build_and_diagnose(
            activity_name=args.activity,
            settle_seconds=args.settle,
            errors_only=args.errors_only
        )
        sys.exit(code)

    parser.print_help()


if __name__ == "__main__":
    main()
