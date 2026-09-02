# Broker MCP — Session Startup Checklist

Run this **before any trading activity** each Claude Code session. All three MCPs must be green before you ask for market data or trade suggestions.

> **Where everything else lives:** [`CLAUDE.md`](../CLAUDE.md) is the repo index — it has a **⚡ Fast Load** table (which docs to read for which kind of ask), the **§8 map** of the live operating manual, and the current **Known Blockers**. There is no README.
>
> **Read [`mcp-usage-log.md`](./mcp-usage-log.md) §1 before trusting any capability.** As of 02-Sep-2026: Dhan's Data API **is** entitled and its prices/OI/bid-ask are trustworthy, but its **MCP OAuth binding is unreliable — try it once, then go straight to REST**; its **IV and Greeks are broken** (computed off spot, not the forward — CE IV ≠ PE IV at the same strike), so there is **no trustworthy Greeks source from any broker** (§7 there lists the sanctioned substitutes). Kite is data-only. All execution is manual in the Kotak Neo app.

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

**Troubleshoot `-32000` error (recurring on session start):**
- Root cause (discovered 20-Aug-2026): the JFrog npm auth config in global `~/.npmrc` blocks `npx` from starting `mcp-remote`
- **Fix (one-time):** a `.npmrc` file pointing to public registry is already in this project root — it overrides JFrog for this directory
- If Kite still fails after `/mcp`, run in terminal: `npx -y mcp-remote https://mcp.kite.trade/mcp` — it will connect (output "Proxy established") then shut down. This primes the mcp-remote process. Now run `/mcp` again.
- If npm itself is broken globally, run `npm config fix` first, then retry

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
6. Verify: ask for NIFTY `expirylist` from Dhan (never use `funds` — returns zeros even unauthenticated)
```

> **Architecture note:** Dhan is primarily used for **option chain + Greeks** (the only MCP with pre-calculated Delta/Theta/Gamma/Vega + OI per strike). It also supports order placement — but execution stays on Kite by default unless you explicitly use Dhan for orders.

> ⚠️ **KNOWN ISSUE (reopened 02-Sep-2026) — Dhan MCP OAuth binding is unreliable.** The Data API subscription **is** active (since 20-Aug-2026), so this is no longer an entitlement problem. What fails is the *binding*: `login` issues a fresh consentId, the user completes consent, `complete_login` replies `token_id already consumed for this session`, and every agent tool still returns `API Error: Unauthorized`. It failed **twice in one morning** on 02-Sep. **`"token already consumed"` is NOT proof of binding — only a successful `expirylist` is.**
>
> **Try the MCP once. Then go straight to REST.** Do not spend market hours on consent URLs. Dhan REST (`access-token` + `client-id` headers) pulled all three full chains reliably all session. See [`mcp-usage-log.md` §2.4](./mcp-usage-log.md).
>
> **Verify Dhan with `expirylist`, never with `funds`** — `funds` returns a well-formed all-zeros response even when unauthenticated, which falsely reads as "connected".
>
> ⚠️ **Do not call `mcp__dhan__login` while the user is mid-login on a valid URL.** Each call issues a new consentId and invalidates the previous pending consent, causing `{"status":"error","message":"Target session is not pending login."}` on the callback. Issue **one** consent URL and wait.
>
> **The one exception:** if the URL has **already failed** (`{"error":"invalid_client"}`), call `login` again — the server generates a new OAuth client_id per call and the first can be stale. A second call is safe *only* once the first has visibly failed. There is **no `mcp__dhan__authenticate` tool**; the MCP exposes `login` and `complete_login` only.

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
Step 1 → Connect Kite      → verify with: mcp__kite__get_ltp → NIFTY + VIX
Step 2 → Connect Kotak Neo → verify with: mcp__kotak-neo__get_limits → ₹7L available
Step 3 → Connect Dhan      → verify with: mcp__dhan__market_data_agent_tool expirylist NIFTY
Step 4 → FII/DII data      → run: ! python3 tools/fii-dii/fii_dii.py  (T-1 NSE archive, no login)
Step 5 → Record the outcome as a row in mcp-usage-log.md §4
Step 6 → All green? → proceed with /Index-Derivatives-tread analyse-today
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
