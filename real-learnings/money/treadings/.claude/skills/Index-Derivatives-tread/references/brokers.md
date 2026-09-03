# brokers.md — Broker verification, one page

**Loaded by:** analyse-today, find-trade, followup

---

## The rule

**Verify each MCP with a call that exercises the capability you actually need.** A successful login proves nothing about the data endpoints. **A populated field is not a verified field.**

**If a broker fails:** flag it clearly. State exactly what is missing and what it blocks. Do not run analysis that depends on it.

---

## The three-broker table

Run all three in parallel at session start. Record the outcome in `tread.md` before proceeding.

| Broker | Login | Verify with | What it provides | Notes |
|---|---|---|---|---|
| **Kite (Zerodha)** | `mcp__kite__login` → browser → 2FA | `mcp__kite__get_ltp` on `["NSE:NIFTY 50", "NSE:INDIA VIX"]` | **Data only** — NIFTY/BANKNIFTY/SENSEX/VIX spot, option chain (via `get_quotes`), OI + `oi_day_high` / `oi_day_low`, 5-level bid/ask depth, historical OHLC (index + option legs), futures. ⛔ Cannot execute — no `NFO`/`BFO` on account (₹500 balance). | The missing segments block orders only, not data. Full chain, OI and depth work. |
| **Kotak Neo** | `mcp__kotak-neo__get_login` (UCC=V6PZT) → user scans QR in Kotak Neo app (Profile → Web Login) → user types DONE → `validate_login` | `mcp__kotak-neo__get_limits` → ₹7.02L (or current balance) | Account margin, research reports. ⛔ **MCP is read-only by design** — no order tools. All execution is manual in the Kotak Neo app. | ⚠️ **Kotak tools need an explicit `sessionid` argument.** A bare call returns a misleading "Session Expired". **Never re-run `get_login` to fix that** — it kills the working session. Pass the sessionid from the first `validate_login`. ⛔ The sessionid is sensitive — never display it. |
| **Dhan** | See `dhan-api.md` for the full flow. **Try once, then go straight to REST.** | `mcp__dhan__market_data_agent_tool` action=`expirylist`, payload `{"UnderlyingScrip": 13, "UnderlyingSeg": "IDX_I"}`. ⛔ **Never verify with `funds`** — returns all-zeros even unauthenticated. | Full option chain (all strikes, CE+PE LTP/OI/bid-ask/`previous_oi`), expiry list. ⚠️ **IV and Greeks are unusable** (computed off spot, not forward — see `dhan-api.md`). | **If `Unauthorized`:** not a consent problem — it's a stale client registration. See `dhan-api.md` for the reset. **Never run a login tool for this error.** |

---

## Kite (Zerodha) — data source

**Login:**
```
1. Say: "Login to Zerodha"
2. Click the auth link Claude returns
3. Complete Zerodha 2FA in browser
4. Session valid for the trading day
```

**Verify:**
```
mcp__kite__get_ltp(instrument_tokens=["NSE:NIFTY 50", "NSE:INDIA VIX"])
```

**What it provides:**
- Index spot: NIFTY 50, BANKNIFTY, SENSEX, INDIA VIX, sectoral indices
- Option quotes (LTP, OHLC, OI, `oi_day_high`, `oi_day_low`, 5-level depth): `get_quotes` on NFO symbols
- Historical candles: `get_historical_data` — daily, 15-min, 30-min, 1-min (index + option legs)
- Futures: `get_quotes` on `NIFTY26SEPFUT` etc.

**What it cannot do:**
- Execute orders — `NFO` and `BFO` absent from `get_profile().exchanges`
- Assemble a full option chain object in one call — must `get_quotes` per strike

**Gotcha solved 20-Aug-2026:** recurring `-32000` error on session start was JFrog npm auth in global `~/.npmrc` blocking `npx mcp-remote`. Fixed by a project `.npmrc` pointing to public registry. If it recurs: run `npx -y mcp-remote https://mcp.kite.trade/mcp` in terminal once, then `/mcp`.

---

## Kotak Neo — margin and execution venue

**Login:**
```
1. Say: "Login to Kotak Neo" (UCC = V6PZT)
2. Claude calls get_login → you get a link with QR
3. Open Kotak Neo mobile app → Profile → Web Login → scan QR
4. Type "DONE" in chat
5. Claude calls validate_login → session active
```

**Verify:**
```
mcp__kotak-neo__get_limits(sessionid=<from validate_login>)
```

**What it provides:**
- Available margin / limits — ⚠️ the documented capital figure is under a **PENDING USER RULING**
  (`TRADING_CONSTANTS.md` §1); read the live `get_limits` value, never a figure quoted in a doc
- Positions, holdings, trade book
- Research reports (`get_research`)

**What it cannot do:**
- Place orders — the MCP has no order tools, by design

**Execution is manual in the Kotak Neo app.** Claude provides structure, strikes, sizing, levels; the user places the orders.

⚠️ **NRML spreads must be legged in a specific order or Kotak rejects them** — the full entry sequence,
the SL-Limit construction and the stop-out ordering all live in
**[`entry-exit-orders.md`](entry-exit-orders.md)**. Do not place a spread from this file.

**Gotcha:** tools need an explicit `sessionid` argument. A bare `get_limits()` call returns "Session Expired" even when the session is live. Never re-run `get_login` to fix it — that kills the working session. Use the sessionid from `validate_login`.

---

## Dhan — option chain

See [`dhan-api.md`](./dhan-api.md) for the full reference. Summary:

**Login (rarely needed after the client reset):**
```
1. mcp__dhan__login → browser URL
2. User logs in → callback with tokenId
3. If "token already consumed" → auto-bound ✅
4. Else: mcp__dhan__complete_login with tokenId
5. Verify: market_data_agent_tool action=expirylist
```

**If `API Error: Unauthorized`:** not a consent problem. Do the client reset in `dhan-api.md`. Never run a login tool.

**What it provides:**
- Full option chain (all strikes, CE+PE LTP/OI/bid-ask/`previous_oi`)
- Expiry list
- ⚠️ IV and Greeks are **unusable** (computed off spot, not forward)

**Path priority:** try MCP once. If `Unauthorized` → switch to REST (`curl`) permanently. Both return identical data.

---

## Trading capital and execution reality

| | |
|---|---|
| **Capital location** | Kotak Neo. The figure itself lives in `TRADING_CONSTANTS.md` §1 and is currently under a PENDING USER RULING — quote the live `get_limits` read, not a doc |
| **Execution venue** | **Manual in Kotak Neo app** — all three MCPs either cannot execute or are unfunded |
| **Data architecture** | Kite: spot/VIX/OI/depth/historicals · Dhan: full chain (REST) · Kotak: margin |

**Claude's role:** structure selection, strike pricing, sizing, stop levels. **Human executes.** No order may be placed without explicit user approval.
