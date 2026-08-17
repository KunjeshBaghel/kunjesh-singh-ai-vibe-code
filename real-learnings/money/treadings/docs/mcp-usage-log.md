# MCP Usage Log — which broker MCP we use for what, and what actually works

Companion to [`broker-session-startup.md`](./broker-session-startup.md) (how to connect) and the capability map in [`CLAUDE.md`](../CLAUDE.md) (what each broker *claims* to support).

**Purpose of this file:** `CLAUDE.md` records the *designed* architecture. This file records the **observed** reality — which endpoints actually respond, which are entitlement-blocked, and which MCP we ended up using for each data point in each session. Update it whenever a call behaves differently from the capability map.

---

## 1. Live capability matrix — verified, not assumed

Legend: ✅ verified working · ❌ verified failing · ⬜ not yet tested · ⚠️ works but caveated

*Last verified: **17-Aug-2026, 10:45 IST***

| Data point / action | Kite (Zerodha) | Kotak Neo | Dhan | We use |
|---|---|---|---|---|
| Session login | ✅ `login` → browser 2FA | ✅ `get_login` → QR → `validate_login` | ✅ `login` → consent URL | all three |
| Account / margin | ⚠️ `get_margins` — ₹500 only | ✅ `get_limits` — **₹7.02L** | ⚠️ `funds` — ₹0.00 | **Kotak** |
| Index spot (NIFTY / BANKNIFTY / SENSEX) | ✅ `get_ltp` | ⬜ | ❌ `ltp` → Unauthorized | **Kite** |
| India VIX | ✅ `get_ltp` `NSE:INDIA VIX` | ⬜ | ❌ | **Kite** |
| Instrument / strike search | ✅ `search_instruments` (`filter_on: underlying`) | ⬜ `search_instrument` | ❌ | **Kite** |
| Option LTP + OHLC | ✅ `get_quotes` | ⬜ `get_quote` | ❌ | **Kite** |
| **Open Interest per strike** | ✅ `get_quotes` → `oi`, `oi_day_high`, `oi_day_low` | ⬜ | ❌ | **Kite** |
| **Bid/ask depth (5 level)** | ✅ `get_quotes` → `depth` | ⬜ | ❌ | **Kite** |
| **Implied Volatility** | ❌ not provided | ❌ not provided | ❌ **entitlement-blocked** | ⛔ **none** |
| **Greeks (Δ Γ Θ V)** | ❌ not provided | ❌ not provided | ❌ **entitlement-blocked** | ⛔ **none** |
| Full option chain object | ❌ (build from `get_quotes`) | ❌ | ❌ `optionchain` → Unauthorized | ⛔ **none** |
| Expiry list | ⚠️ derive from `search_instruments` | ⬜ | ❌ `expirylist` → Unauthorized | **Kite** |
| Historical OHLC candles | ✅ `get_historical_data` | ❌ | ❌ | **Kite** |
| Holdings / positions | ✅ | ✅ | ✅ `positions` | any |
| Basket / SPAN margin | ✅ `get_margins` (account-level only) | ✅ `get_margin` | ⬜ `margin_agent_tool` | **Kotak** |
| Research reports | ❌ | ✅ `get_research` | ❌ | **Kotak** |
| **Order placement** | ❌ no `NFO`/`BFO` on account | ❌ no order tools in MCP | ⚠️ has tools, ₹0 funded | ⛔ **manual in Kotak app** |

---

## 2. Known broken — root causes

### 2.1 Dhan: Data API not entitled ⛔ *open*

Dhan authenticates and serves **trading/portfolio** endpoints, but **every market-data endpoint returns `API Error: Unauthorized`.**

```
positions    → ✅ "No open positions."
funds        → ✅ returns (₹0.00)
ltp          → ❌ API Error: Unauthorized
expirylist   → ❌ API Error: Unauthorized
optionchain  → ❌ API Error: Unauthorized
```

**Cause:** Dhan sells **Data APIs as a separate paid subscription** from the trading API. OAuth consent grants the trading scope only. This is an *entitlement* error, not a session error — re-running `login` will never fix it.

**Impact:** Dhan is the only MCP with pre-calculated IV and Greeks. Until this is resolved we have **no IV and no Greeks from any source**, which blocks delta-band strike selection and the IV/IVP filter in [`option_chain_n_greeks.md` §5](../kb/option_chain_n_greeks.md).

**Fix:** activate the Data API plan in the Dhan account, then re-verify with `expirylist`.

> ⚠️ **Never verify Dhan with `funds`.** It returns a well-formed all-zeros response even when unauthenticated, which reads as "connected". **Always verify with `expirylist`.**

### 2.2 Zerodha: F&O segment not activated ⛔ *open*

`get_profile` returns `exchanges: ["BSE","MF","NSE"]` — `NFO` and `BFO` absent; `commodity.enabled: false`; available balance ₹500.

**Impact:** Kite cannot execute derivatives orders. **Market data is unaffected** — `get_quotes` on NFO symbols works fine, so Kite remains our data source.

### 2.3 Kotak Neo: MCP is read-only *by design*

No order-placement tools exist in the Kotak MCP. Since the capital is here, **all execution is manual in the Kotak Neo app.** Claude provides structure, strikes, sizing and levels; the user places the orders.

---

## 3. Effective architecture (as of 17-Aug-2026)

```text
        DATA                    ANALYSIS                 EXECUTION
  ┌──────────────┐         ┌──────────────┐        ┌──────────────┐
  │  KITE MCP    │────────▶│              │        │  KOTAK NEO   │
  │  spot, VIX   │         │ Claude Code  │───────▶│  MOBILE APP  │
  │  OI, depth   │         │  structure   │ advice │  (manual)    │
  │  historicals │         │  + sizing    │        │   ₹7.02L     │
  └──────────────┘         │  + levels    │        └──────────────┘
  ┌──────────────┐         │              │
  │  KOTAK MCP   │────────▶│              │        Human approval step
  │  margin      │         └──────────────┘        is structural, not optional
  │  research    │                ▲
  └──────────────┘                │
  ┌──────────────┐                │
  │  DHAN MCP    │╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┘
  │  IV, GREEKS  │   ⛔ BLOCKED — Data API not entitled
  └──────────────┘
```

This differs from the designed architecture in `CLAUDE.md`, which assumes Dhan for chain/Greeks and Kite for execution. **Both of those are currently inverted or unavailable.**

---

## 4. Session log

| Date | Kite | Kotak | Dhan | What we used each for | Notes |
|---|---|---|---|---|---|
| 17-Aug-2026 | 🟢 data only | 🟢 ₹7.02L | 🔴 data blocked | Kite: NIFTY/BANKNIFTY/VIX spot, 18-Aug option chain prices + OI + depth, `NIFTY26AUGFUT`. Kotak: available margin. Dhan: nothing usable. | 3 consent URLs burned on Dhan before diagnosing entitlement issue — see §5. No Greeks available all session. **Outcome: NO TRADE** (8 red/warning signals vs a 3-signal sit-out threshold; IVP ≈ 2%). Full reasoning: [`17-08-2026-tread.md`](../my-treads/August-2026/17-08-2026/17-08-2026-tread.md). Workaround for the missing Greeks: the straddle rule, [`strategy_ref_book.md` §8.7.3](../kb/kb1/strategy_ref_book.md#873-method-3--the-straddle-rule-the-fastest-works-with-no-greeks-at-all). Session closed 11:55, no position. |

---

## 5. Session-startup gotchas learned the hard way

1. **Verify each MCP with a call that exercises the capability you need**, not just a login check. `funds` succeeding does not mean the chain will load.
2. **Never call `mcp__dhan__login` twice.** Each call invalidates the previous pending consent. The user then hits `{"status":"error","message":"Target session is not pending login."}` and the `tokenId` is rejected with *"already consumed for this session"* — which looks like an auth bug but is self-inflicted. Issue **one** URL and wait.
3. **`Token rejected: token_id already consumed` does not mean success.** Always follow it with a real API call.
4. **Match the `consentId`.** When the user pastes a callback URL, check its `consentId` equals the one most recently issued before using its `tokenId`.
5. **A missing `NFO` in Kite's profile `exchanges` array only blocks orders, not data.** Don't abandon Kite as a data source over it.
6. **Do not compute Greeks locally as a silent fallback.** The user has explicitly asked for Dhan's pre-calculated Greeks. If Dhan is down, say so and ask.

---

## 6. Open items

- [ ] Activate **Dhan Data API** subscription → restores IV + Greeks (highest priority; blocks normal workflow)
- [ ] Confirm whether **F&O is enabled on the Kotak Neo account** — `get_limits` does not expose segment entitlements
- [ ] Decide the long-term execution venue: activate F&O + fund Zerodha, or fund Dhan, or accept permanent manual execution on Kotak
- [ ] Update `CLAUDE.md` capability map + `docs/dhan_mcp.md` once Dhan Data API is live
      *(as of 17-Aug-2026 `CLAUDE.md` carries a "Current State / Known Blockers" section and an
      "Actually usable today" column mirroring §1 — both must be reverted to ✅ when Dhan is fixed)*

---

## 7. Working without Greeks — the sanctioned substitutes

Until §2.1 is resolved, these are the approved replacements. **Do not compute Greeks locally** — the user rejected that explicitly.

| Normally you'd use | Instead use |
|---|---|
| Delta band (8–12Δ / 12–20Δ) for strike selection | [`strategy_ref_book.md` §8.7.3](../kb/kb1/strategy_ref_book.md#873-method-3--the-straddle-rule-the-fastest-works-with-no-greeks-at-all) — the straddle rule: `call = spot + 0.85 × straddle`, `put = spot − 1.05 × straddle` |
| Delta-matching the two sides of a condor/strangle | §8.6.8 premium-matching proxy (equal credit, not equal distance) — put skew makes equidistant strikes silently long delta |
| IV / IVP per strike | India VIX from Kite + ATM straddle ÷ spot as an IV proxy; HV20 from Kite daily candles; **VRP = IV − HV20** |
| Expected move from IV | `EM ≈ ATM straddle × 0.85` |
| Position delta | OI walls (§8.7.4) + directional structure only. If the trade genuinely needs a delta number, **stop and tell the user.** |
