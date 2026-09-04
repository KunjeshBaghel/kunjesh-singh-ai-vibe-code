# dhan-api.md — Dhan data access: MCP and REST

**Loaded by:** analyse-today, find-trade, followup, basis-check, check-expiry

---

## TL;DR — the 03-Sep-2026 root cause

**`API Error: Unauthorized` is NOT a consent problem.** It is a **stale OAuth client registration on this machine.**

**Fix (one-time per machine):**
```bash
claude mcp remove dhan -s local
claude mcp add --transport http --client-id "$DHAN_CLIENT_ID" dhan https://mcp.dhan.co/mcp
```

Then in Claude Code: `/mcp` → open dhan → **Authenticate** (browser login).

**After the reset, data flows with no consent step at all.** Never run a login tool for this error.

**Diagnose by error string:**
- `API Error: Unauthorized` = reached Dhan, rejected there → do the reset above
- `requires re-authorization (token expired)` = blocked locally by Claude Code OAuth → just `/mcp` → Authenticate

⛔ **`claude mcp list` showing ✔ Connected and `/mcp` showing `dhan · connected · 11 tools` are transport-level only** — they stayed green through four consecutive failures across 02–03 Sep. **Verify with `expirylist`, never `funds`.**

---

## When to use which path

| Path | When | Why |
|---|---|---|
| **REST (curl)** | **First choice for mid-session rechecks** | MCP OAuth binding has failed repeatedly mid-session (01-Sep, 02-Sep ×2). REST with `DHAN_ACCESS_TOKEN` stayed working all day. |
| **MCP** | Session start, if the reset has been done | After the client reset above, the MCP works. Try it once. If `Unauthorized` → switch to REST permanently. |

**The two paths return identical data** — cross-verified 03-Sep-2026 on the full SENSEX 03-Sep-2026 chain, every strike.

---

## MCP tool names (post-31-Aug-2026 agent-style update)

⛔ **There is NO `mcp__dhan__authenticate` and NO `mcp__dhan__complete_authentication`.** Earlier versions of SKILL.md named tools that do not exist. The server was updated 31-Aug-2026 and now exposes:

- `mcp__dhan__login` — issues a browser consent URL
- `mcp__dhan__complete_login` — binds a `tokenId` from the callback
- `mcp__dhan__market_data_agent_tool` — ltp, ohlc, quote, optionchain, expirylist
- `mcp__dhan__historical_data_agent_tool`
- `mcp__dhan__portfolio_agent_tool` — positions, funds
- `mcp__dhan__margin_agent_tool`
- `mcp__dhan__search_agent_tool`
- `mcp__dhan__orderbook_agent_tool`, `mcp__dhan__tradebook_agent_tool`, `mcp__dhan__trading_agent_tool`

**The old `authenticate` tool does not exist.** Never call it.

---

## MCP login flow (rarely needed after the client reset)

1. Call `mcp__dhan__login` → returns a browser URL: `https://auth.dhan.co/consent-login?consentId=...`
2. User opens it, logs in, is redirected to `https://mcp.dhan.co/auth/callback?tokenId=...`
3a. **If Claude says "token already consumed for this session"** → the MCP auto-bound. Proceed to verify.
3b. **If not auto-bound** → user pastes the full callback URL → call `mcp__dhan__complete_login` with the `tokenId`.
4. **Verify:** `mcp__dhan__market_data_agent_tool` action=`expirylist`, payload `{"UnderlyingScrip": 13, "UnderlyingSeg": "IDX_I"}`.

⛔ **Never verify with `funds` or `fundlimit`** — they return well-formed all-zeros responses even when unauthenticated.

⛔ **Do not call `login` while the user is mid-login on a valid URL.** Each call mints a fresh `client_id` and invalidates the previous pending consent. Issue ONE URL and wait.

**The one exception:** if the URL has **already failed** in the browser (`{"error":"invalid_client"}`), call `login` **once** more — the server's `client_id` can be stale. Safe to retry only after visible failure.

---

## REST API (the reliable path)

**Both headers are mandatory:**

```bash
source .broker_creds     # sets DHAN_ACCESS_TOKEN and DHAN_CLIENT_ID

curl -s -X POST "https://api.dhan.co/v2/optionchain/expirylist" \
  -H "access-token: $DHAN_ACCESS_TOKEN" \
  -H "client-id: $DHAN_CLIENT_ID" \
  -H "Content-Type: application/json" \
  -d '{"UnderlyingScrip": 13, "UnderlyingSeg": "IDX_I"}'
```

**Security:** never echo or print token values. Source `.broker_creds` into shell variables only.

### Expiry list

```bash
curl -s -X POST "https://api.dhan.co/v2/optionchain/expirylist" \
  -H "access-token: $DHAN_ACCESS_TOKEN" \
  -H "client-id: $DHAN_CLIENT_ID" \
  -H "Content-Type: application/json" \
  -d '{"UnderlyingScrip": <id>, "UnderlyingSeg": "IDX_I"}'
```

**Index security IDs:** NIFTY=13 · BANKNIFTY=25 · FINNIFTY=27 · SENSEX=51

⚠️ **Dhan returns `bid_price` / `ask_price` = `0.00` across the ENTIRE BANKNIFTY monthly chain**
(observed 04-Sep-2026, 29-Sep expiry, 357 strikes). `last_price` and `oi` are populated; depth is not.
**A populated `last_price` next to a zero bid/ask is a missing field, not a zero spread** (SI-5).
→ **TC §6 rows 6 and 7 cannot be scored from Dhan for BANKNIFTY.** Pull depth from Kite
`get_quotes`, or score both rows YELLOW under §6 row 11. ⛔ Never infer a spread from LTP.

### Option chain

```bash
curl -s -X POST "https://api.dhan.co/v2/optionchain" \
  -H "access-token: $DHAN_ACCESS_TOKEN" \
  -H "client-id: $DHAN_CLIENT_ID" \
  -H "Content-Type: application/json" \
  -d '{"UnderlyingScrip": <id>, "UnderlyingSeg": "IDX_I", "Expiry": "YYYY-MM-DD"}'
```

Returns all strikes, each keyed as a float (e.g. `"24000.000000"`), with `.ce` and `.pe` sub-dicts containing:
- LTP, bid_price, ask_price, bid_qty, ask_qty
- OI, previous_oi (day's opening OI)
- IV (⚠️ unreliable — see below)
- delta, gamma, theta, vega (⚠️ unreliable — see below)

**Rate limit:** one unique option-chain request per 3 seconds. Allow ~4s between calls.

---

## Field names & common errors

| Gotcha | Correct |
|---|---|
| **Field name** | `UnderlyingSeg` (NOT `UnderlyingSegment`) — wrong name returns `813: Invalid SecurityId` |
| **Expiry endpoint** | `/v2/optionchain/expirylist` ✅ · `/v2/expirylist` is a **404** |
| **Both headers mandatory** | `access-token` **and** `client-id` — either alone returns Unauthorized |
| **Never guess a date** | `2026-09-02` returned *Invalid Expiry Date*. Always fetch the list first. |

---

## What Dhan's data is good for

✅ **Trustworthy:** prices (LTP, bid, ask), OI, `previous_oi`, depth.

⛔ **Unusable:** IV and Greeks (delta, gamma, theta, vega).

**Why IV/Greeks are broken (discovered 28-Aug-2026):** they are computed off **spot, not the forward**. Proof requiring no model: one strike + one expiry = exactly **one** implied volatility. Dhan returns two — CE IV ≠ PE IV at the same strike.

**Observed 01-Sep-2026, 11:05 IST:**
```
Strike    CE IV    PE IV    Gap
24,100    12.77     7.38    +5.40
24,150    11.96     6.97    +4.99
24,200    11.47     6.41    +5.06
24,250    11.01     5.63    +5.38
```

Put-call parity gave F ≈ 24,237 (NIFTY spot 24,155 → basis +82 pts). Dhan's Δ=0.50 landed ~85 points below the true ATM-forward.

**Impact:** every strike selected off Dhan's delta band is systematically wrong. Deep-ITM legs return IV=0, delta=0, theta=0 — solver non-convergence, not "no risk."

**Sanctioned substitutes:** see [`TRADING_CONSTANTS.md` §14](../../../../TRADING_CONSTANTS.md).
- ✅ Permitted: `F = K + C − P` (arithmetic, model-free)
- ✅ Permitted: §8.7.3 straddle rule centred on F
- ⛔ Not permitted: local Black-Scholes solve for Δ/Γ/Θ/V, or presenting a derived number as if it came from Dhan

**Never substitute silently.** If Greeks are needed and Dhan's are unusable, say so and ask.

---

## Verification checklist

Before any analysis that depends on Dhan:

```
□ Is the client registration current? (Last reset date: _______)
□ If Unauthorized → did you do the reset, not a login tool?
□ Verified with expirylist (not funds)?
□ If using IV/Greeks → did you run §8.7.1a basis check first?
□ If basis > 0.1% of spot → are you using §8.7.3, not the delta band?
```

---

## Session history — what failed when

| Date | MCP | REST | What happened |
|---|---|---|---|
| 01-Sep-2026 | ❌ Unauthorized after 3 re-auth | ✅ all session | OAuth breaks mid-session |
| 02-Sep-2026 | ❌ Unauthorized ×2 (07:17, 09:27) | ✅ all session | Regressed after 31-Aug fix |
| 03-Sep-2026 | ✅ after client reset | ✅ | **Root cause found** — stale client registration |
| 31-Aug-2026 | ✅ (working after update) | ✅ | Temporarily fixed, broke again by 02-Sep |

**Conclusion:** try the MCP once per session. If `Unauthorized` → switch to REST, do not retry.
