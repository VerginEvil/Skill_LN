#!/usr/bin/env python3
"""
ln_studio_skill/tools/capture_oob.py
Windows 'oob://' Protocol Handler Callback Dispatcher.

Invoked automatically by Windows when a web browser navigates to 'oob://localhost/lnstudio?code=...'.
Extracts the authorization code, writes it to pending token signal files, and displays a clean
success page in the browser.
"""

import os
import sys
import tempfile
import urllib.parse
import webbrowser
from pathlib import Path


def main():
    if len(sys.argv) < 2:
        sys.exit(0)

    raw_uri = sys.argv[1].strip()
    if not raw_uri:
        sys.exit(0)

    # Parse code parameter
    parsed = urllib.parse.urlparse(raw_uri)
    qs = urllib.parse.parse_qs(parsed.query)
    code = qs.get("code", [""])[0].strip()

    if not code and "code=" in raw_uri:
        import re
        m = re.search(r"[?&]code=([^&#\s]+)", raw_uri)
        if m:
            code = urllib.parse.unquote(m.group(1)).strip()

    if not code:
        sys.exit(0)

    # Deliver to all pending code listeners in ~/.ln_studio/tokens/
    cache_dir = Path.home() / ".ln_studio" / "tokens"
    cache_dir.mkdir(parents=True, exist_ok=True)

    delivered = False
    for p_file in cache_dir.glob(".pending_code_*.txt"):
        try:
            p_file.write_text(code, encoding="utf-8")
            delivered = True
        except Exception:
            pass

    # Also write a global fallback pending code
    global_file = cache_dir / ".pending_code_global.txt"
    try:
        global_file.write_text(code, encoding="utf-8")
    except Exception:
        pass

    # Display friendly confirmation page in browser
    html_content = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Infor LN Studio - Login Successful</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
               background: #f4f6f8; color: #1a202c; display: flex; align-items: center; justify-content: center; height: 80vh; margin: 0; }
        .card { background: white; padding: 40px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.08); text-align: center; max-width: 480px; }
        .check { width: 64px; height: 64px; border-radius: 50%; background: #ebfbee; color: #2b8a3e; font-size: 36px; line-height: 64px; margin: 0 auto 20px; }
        h1 { font-size: 24px; margin-bottom: 12px; color: #2b8a3e; }
        p { color: #4a5568; line-height: 1.5; font-size: 16px; }
    </style>
</head>
<body>
    <div class="card">
        <div class="check">&#10003;</div>
        <h1>Authentication Successful!</h1>
        <p>Infor LN Studio authorization code has been captured by the automation assistant.<br><br><b>You can close this tab and return to your terminal.</b></p>
    </div>
</body>
</html>"""

    try:
        tmp_html = Path(tempfile.gettempdir()) / "ln_studio_login_success.html"
        tmp_html.write_text(html_content, encoding="utf-8")
        webbrowser.open(tmp_html.as_uri())
    except Exception:
        pass

    sys.exit(0)


if __name__ == "__main__":
    main()
