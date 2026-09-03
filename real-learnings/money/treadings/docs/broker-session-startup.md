# Broker MCP — session startup checklist

Run this **before any trading activity** each Claude Code session.

> **Read [`mcp-usage-log.md`](./mcp-usage-log.md) §1 before trusting any capability.** A successful login
> proves nothing about the data endpoints, and **a populated field is not a verified field.**
>
> Current shape: **Kite = data only** (no NFO/BFO entitlement) · **Dhan = the full option chain**, prices
> / OI / `previous_oi` / bid-ask trustworthy, **its IV and Greeks broken** (computed off spot, not the
> forward — CE IV ≠ PE IV at the same strike) · **Kotak = read-only**, and all execution is manual in the
> Kotak Neo app.
>
> Where things live: [`repo-map.md`](./repo-map.md). Every number: `TRADING_CONSTANTS.md`.

---

## Session start sequence

```
Step 1 → Kite       → verify: mcp__kite__get_ltp → NIFTY + INDIA VIX
Step 2 → Kotak Neo  → verify: mcp__kotak-neo__get_limits
Step 3 → Dhan       → verify: mcp__dhan__market_data_agent_tool action=expirylist
Step 4 → FII/DII    → ! python3 tools/fii-dii/fii_dii.py     (T-1 NSE archive, no login)
Step 5 → Record the outcome as a row in mcp-usage-log.md §4
Step 6 → All green? → /Index-Derivatives-tread analyse-today
```

**Verify each MCP with a call that exercises the capability you actually need.**
**If any MCP is red:** flag which one, say what it blocks, and re-attempt before continuing.

---

## 1 · Kite (Zerodha)

```
1. Say "Login to Zerodha" → Claude returns an auth link
2. Open it → Zerodha credentials + TOTP (2FA) → browser redirects back
3. Verify: mcp__kite__get_ltp on NIFTY 50 and INDIA VIX
```

Valid for one trading day; re-login every new session.

**Troubleshoot `-32000` on session start** *(root cause found 20-Aug-2026)*: the JFrog npm auth config in
the global `~/.npmrc` blocks `npx` from starting `mcp-remote`. A project-root `.npmrc` pointing at the
public registry already overrides it for this directory. If Kite still fails after `/mcp`, run in a
terminal `npx -y mcp-remote https://mcp.kite.trade/mcp` — it connects ("Proxy established") then shuts
down, priming the process — and run `/mcp` again. If npm itself is broken globally, `npm config fix` first.

---

## 2 · Kotak Neo

```
1. Say "Login to Kotak Neo"  (UCC = V6PZT)  → Claude calls get_login → you get a login link
2. Kotak Neo mobile app → Profile → Web Login → scan the QR on that link
3. Type "DONE" → Claude calls validate_login
4. Verify: get_limits
```

Ephemeral — expires when the Claude Code session ends.

⚠️ **Kotak tools need an explicit `sessionid` argument.** A bare call returns a misleading
"Session Expired". ⛔ **Never re-run `get_login` to fix that — it kills the working session.**
⛔ The session id is sensitive; never display it.

---

## 3 · Dhan

Full detail, curl blocks and scrip IDs: **`.claude/skills/Index-Derivatives-tread/references/dhan-api.md`**.

```
1. Say "Login to Dhan" → Claude calls mcp__dhan__login → browser consent URL
2. Log in → the browser redirects to .../auth/callback?tokenId=...
3a. "token already consumed" → possibly bound. ⚠️ NOT proof — only a successful expirylist is.
3b. Not auto-bound → "complete_login with tokenId <value>"
4. Verify: mcp__dhan__market_data_agent_tool action=expirylist
   ⛔ NEVER verify with funds/fundlimit — they return a well-formed response unauthenticated.
```

> ★ **`API Error: Unauthorized` is NOT a consent problem** *(root cause found 03-Sep-2026, after it
> burned four sessions across 02–03 Sep)*. It means the request reached Dhan and was rejected there:
> the OAuth **client registration on this machine is stale**. ⛔ **Do not run a login tool for it.** Fix:
>
> ```bash
> claude mcp remove dhan
> claude mcp add --transport http --client-id <DHAN_CLIENT_ID> dhan https://mcp.dhan.co/mcp
> # then /mcp → dhan → Authenticate
> ```
>
> After the reset, data flows with **no consent step at all**, and the MCP and REST agree exactly.
> This **supersedes** the retired advice to "call `login` again for a fresh consentId".

⚠️ **Do not call `mcp__dhan__login` while the user is mid-login on a valid URL** — each call mints a new
`client_id` and invalidates the pending consent (`"Target session is not pending login."`). Issue **one**
URL and wait. The only safe retry is after the URL has **already failed** in the browser with
`{"error":"invalid_client"}`.

⛔ **There is no `mcp__dhan__authenticate` and no `mcp__dhan__complete_authentication`.** The MCP exposes
`login`, `complete_login` and the agent tools, nothing else.

**REST is the reliable fallback** and has stayed working throughout: `source .broker_creds`, then both
headers `access-token` **and** `client-id`. See `dhan-api.md`.

---

## Safety rules — always active

- ⛔ Never share or display credentials, MPIN, OTP, passwords, tokens or session ids in the chat.
  They live in `.broker_creds` (gitignored) — source it into shell variables, never read it into chat.
- **Kite and Dhan can place real orders.** Claude drafts; **you confirm** before any `place_order`,
  `modify_order` or `cancel_order`. All actual execution is manual in the Kotak Neo app.
- All sessions expire when Claude Code closes. Re-login is not optional.
