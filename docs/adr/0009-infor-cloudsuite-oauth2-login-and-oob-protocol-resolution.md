# ADR 0009: Infor CloudSuite SSO OAuth2 Engine, Windows 'oob://' Protocol Handler, and Self-Contained Login CLI

- **Status**: Accepted
- **Date**: 2026-10-29
- **Target Skills**: `ln_studio_skill`
- **Prior ADRs**:
  - [`docs/adr/0008-semantic-ast-auditor-oauth-dd-cache-and-byoj-hardening.md`](0008-semantic-ast-auditor-oauth-dd-cache-and-byoj-hardening.md) *(OAuth2 3-tier lifecycle foundation)*

---

## 1. Context & Problem Statement

In real-world testing with Infor LN CloudSuite environments (e.g. `SCS_TST`, tenant `SLNBGS786BCXMXWQ_TST`, client `SLNBGS786BCXMXWQ_TST~L871tflFMmNqtUSvKdCMbXwlmqfTN5tp6Hs7AUlS2JU`):
1. **The "Login ได้แต่ไม่ได้ Token" Failure**:
   - Infor Desktop Client OAuth (`dt=11`) redirects to `oob://localhost/lnstudio?code=...`.
   - Web browsers (Chrome, Edge) do not recognize custom URI scheme `oob://` and abort with `net::ERR_ABORTED` or "This site can’t be reached".
   - Users perceive this as a server crash or authentication failure, failing to acquire tokens.
2. **PingFederate Policy Constraints**:
   - `grant_type=password` is disallowed (`HTTP 400: Unsupported grant type password. Expected one of authorization_code`).
   - PingFederate requires an explicit UUID `state` parameter to avoid CSRF and session confusion.
3. **Infor OS Federation Hub Error on Unconfigured Scopes**:
   - Passing `scope=openid` on native desktop client registrations triggers a runtime crash in Infor OS Federation Hub (`"InforOS Federation Hub service has encountered an error"`).

---

## 2. Settled Architectural Decisions

### Decision 1: Multi-Channel OAuth2 Receiver Engine (`ln_auth_helper.py`)
1. **Channel 1 (Windows Registry Protocol Handler)**:
   - Registers custom protocol `oob` under `HKCU\Software\Classes\oob` (user-level, requiring zero administrator privileges).
   - Directs `oob://` launches to `capture_oob.py`, which extracts `code` and `state`, signals the waiting login process via filesystem lock/signal, and serves an immediate clean green confirmation page in the user's browser.
2. **Channel 2 (Windows Clipboard Auto-Detection)**:
   - Zero-dependency background thread using 64-bit safe `ctypes.windll.user32` polls clipboard changes.
   - If the user copies the browser URL bar or authorization code, it is instantly captured without pressing Enter.
3. **Channel 3 (Terminal Interactive Prompt)**:
   - Clean manual prompt fallback for headless or restricted console environments.

### Decision 2: Self-Contained CLI `login` & MCP Tool `ln_login`
- Added CLI subcommand: `python ln_studio_skill/tools/ln_component_builder.py login --workspace <ws> [--ionapi <file>]`.
- Added MCP tool `ln_login` enabling AI assistants to check token status, register protocol handler, or initiate login.
