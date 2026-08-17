# Broker MCP — Session Startup Checklist

Run this **before any trading activity** each Claude Code session. All three MCPs must be green before you ask for market data or trade suggestions.

> **Where everything else lives:** [`CLAUDE.md`](../CLAUDE.md) is the repo index — it has a **⚡ Fast Load** table (which docs to read for which kind of ask), the **§8 map** of the live operating manual, and the current **Known Blockers**. There is no README.
>
> **Read [`mcp-usage-log.md`](./mcp-usage-log.md) §1 before trusting any capability.** As of 17-Aug-2026: Dhan's Data API is not entitled (**no IV/Greeks from any source** — §7 there lists the sanctioned substitutes), Kite is data-only, and all execution is manual in the Kotak Neo app.

---

## 1. Kite (Zerodha) — Order Execution

**Status:** Active in `.mcp.json` · Supports order placement ⚠️

**Steps:**
```
1. Say: "Login to Zerodha" (or just ask for quotes/positions — Claude will trigger auth)
2. Claude returns an auth link → open it in your browser
3. On Zerodha's site: enter credentials + complete TOTP (2FA)
4. Browser redirects back → session is active for the day
5. Verify: ask "Show my Zerodha available margin"
```

**Troubleshoot `-32000` error:**
- This means the session expired or MCP lost connection
- Simply say "Login to Zerodha" again — a fresh auth link will be generated
- If MCP server itself fails to start, restart Claude Code (it relaunches the MCP process)

**Session duration:** Valid for one trading day. Re-login required every new Claude Code session.

---

## 2. Kotak Neo — Research & Account Data

**Status:** Active in `.mcp.json` · Read-only (no order placement)

**Steps:**
```
1. Say: "Login to Kotak Neo" (UCC = V6PZT)
2. Claude calls get_login → you receive a login link
3. Open Kotak Neo mobile app → Profile → Web Login → Scan QR code on the link
4. Type "DONE" in chat
5. Claude calls validate_login → session active
6. Verify: ask "What is my available margin on Kotak Neo?"
```

**Session duration:** Ephemeral — expires when Claude Code session ends. Repeat every session.

---

## 3. Dhan — Full Option Chain + Greeks + Order Placement

**Status:** HTTP transport in `~/.claude.json` (not `.mcp.json`) · Connected · Supports order placement ⚠️

**Steps:**
```
1. Say: "Login to Dhan"
2. Claude calls mcp__dhan__login → returns browser consent URL
   (https://auth.dhan.co/consent-login?consentId=...)
3. Open URL in browser → log in with Dhan credentials
4. Browser redirects to https://mcp.dhan.co/auth/callback?tokenId=...
5a. If Claude says "token already consumed" → session is active (auto-bound) ✅
5b. If not auto-bound → copy tokenId from URL → say: "complete_login with tokenId <value>"
6. Verify: ask "Show my Dhan funds"
```

> **Architecture note:** Dhan is primarily used for **option chain + Greeks** (the only MCP with pre-calculated Delta/Theta/Gamma/Vega + OI per strike). It also supports order placement — but execution stays on Kite by default unless you explicitly use Dhan for orders.

> ⛔ **KNOWN ISSUE (as of 17-Aug-2026) — Dhan Data API is not entitled.** Login succeeds and `positions`/`funds` work, but **every** market-data call (`ltp`, `expirylist`, `optionchain`) returns `API Error: Unauthorized`. Dhan sells Data APIs as a **separate paid subscription**; the OAuth consent only grants the trading scope. Re-running `login` will never fix it — the Data API plan must be activated in the Dhan account. See [`mcp-usage-log.md` §2.1](./mcp-usage-log.md#21-dhan-data-api-not-entitled--open).
>
> **Verify Dhan with `expirylist`, never with `funds`** — `funds` returns a well-formed all-zeros response even when unauthenticated, which falsely reads as "connected".
>
> ⚠️ **Never call `mcp__dhan__login` twice.** Each call invalidates the previous pending consent, causing `{"status":"error","message":"Target session is not pending login."}` on the callback. Issue **one** consent URL and wait for the user.

**If setup is broken (one-time fix):**
```bash
# Run in terminal outside Claude Code:
claude mcp remove dhan
claude mcp add --transport http --client-id <DHAN_CLIENT_ID> dhan https://mcp.dhan.co/mcp
# Then re-authenticate via /mcp → dhan → Authenticate
```

---

## Session Start Sequence (in order)

```
Step 1 → Connect Kite      → verify with: "Show my Zerodha margin"
Step 2 → Connect Kotak Neo → verify with: "Show my Kotak available margin"
Step 3 → Connect Dhan      → verify with: "Get NIFTY option chain from Dhan"
Step 4 → Record the outcome as a row in mcp-usage-log.md §4
Step 5 → All green? → proceed with market view / trade analysis
```

**Verify each MCP with a call that exercises the capability you actually need** — a successful login or funds call does not prove the data endpoints work.

**If any MCP is red:** do not proceed with trades. Flag which broker failed and re-attempt that login before continuing.

**Observed reality vs designed architecture:** see [`mcp-usage-log.md`](./mcp-usage-log.md) for the verified capability matrix, which endpoints are currently broken and why, where the trading capital actually sits, and the per-session log.

---

## Quick Reference

| Broker | Role | Login trigger phrase |
|--------|------|----------------------|
| Kite (Zerodha) | Order execution, live quotes, GTT | `"Login to Zerodha"` |
| Kotak Neo | Research reports, account data | `"Login to Kotak Neo"` (UCC = V6PZT) |
| Dhan | Option chain + Greeks, live data, orders | `"Login to Dhan"` |

---

## Safety Rules (always active)

- Never share credentials, MPIN, OTP, or passwords in the chat
- Kite can place real orders — Claude drafts, **you confirm** before any `place_order` call
- All sessions expire when Claude Code closes — re-login is not optional
