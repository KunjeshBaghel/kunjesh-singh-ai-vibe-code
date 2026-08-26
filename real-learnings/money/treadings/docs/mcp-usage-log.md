# MCP Usage Log — which broker MCP we use for what, and what actually works

Companion to [`broker-session-startup.md`](./broker-session-startup.md) (how to connect) and the capability map in [`CLAUDE.md`](../CLAUDE.md) (what each broker *claims* to support).

**Purpose of this file:** `CLAUDE.md` records the *designed* architecture. This file records the **observed** reality — which endpoints actually respond, which are entitlement-blocked, and which MCP we ended up using for each data point in each session. Update it whenever a call behaves differently from the capability map.

---

## 1. Live capability matrix — verified, not assumed

Legend: ✅ verified working · ❌ verified failing · ⬜ not yet tested · ⚠️ works but caveated

*Last verified: **24-Aug-2026, 12:45 IST***

| Data point / action | Kite (Zerodha) | Kotak Neo | Dhan | We use |
|---|---|---|---|---|
| Session login | ✅ `login` → browser 2FA | ✅ `get_login` → QR → `validate_login` | ✅ `login` → consent URL | all three |
| Account / margin | ⚠️ `get_margins` — ₹500 only | ✅ `get_limits` — **₹7.02L** | ⚠️ `funds` — ₹0.00 | **Kotak** |
| Index spot (NIFTY / BANKNIFTY / SENSEX) | ✅ `get_ltp` | ⬜ | ⬜ `ltp` (subscription active, unverified post-upgrade) | **Kite** |
| India VIX | ✅ `get_ltp` `NSE:INDIA VIX` | ⬜ | ⬜ | **Kite** |
| Instrument / strike search | ✅ `search_instruments` (`filter_on: underlying`) | ⬜ `search_instrument` | ⬜ | **Kite** |
| Option LTP + OHLC | ✅ `get_quotes` | ⬜ `get_quote` | ⬜ | **Kite** |
| **Open Interest per strike** | ✅ `get_quotes` → `oi`, `oi_day_high`, `oi_day_low` | ⬜ | ⬜ | **Kite** |
| **Bid/ask depth (5 level)** | ✅ `get_quotes` → `depth` | ⬜ | ⬜ | **Kite** |
| **Implied Volatility** | ❌ not provided | ❌ not provided | ✅ `optionchain` → `CE IV` / `PE IV` per strike — **verified 24-Aug-2026** | **Dhan** |
| **Greeks (Δ Γ Θ V)** | ❌ not provided | ❌ not provided | ✅ `optionchain` returns strike-level IV; full Greeks (Δ Γ Θ V) included in response — **verified 24-Aug-2026** | **Dhan** |
| Full option chain object | ❌ (build from `get_quotes`) | ❌ | ✅ `optionchain` — all strikes, CE+PE LTP/OI/IV — **verified 24-Aug-2026** | **Dhan** |
| Expiry list | ⚠️ derive from `search_instruments` | ⬜ | ✅ `expirylist` — returns full expiry list per underlying — **verified 24-Aug-2026** | **Dhan** |
| Historical OHLC candles | ✅ `get_historical_data` | ❌ | ⬜ | **Kite** |
| Holdings / positions | ✅ | ✅ | ✅ `positions` | any |
| Basket / SPAN margin | ✅ `get_margins` (account-level only) | ✅ `get_margin` | ⬜ `margin_agent_tool` | **Kotak** |
| Research reports | ❌ | ✅ `get_research` | ❌ | **Kotak** |
| **Order placement** | ❌ no `NFO`/`BFO` on account | ❌ no order tools in MCP | ⚠️ has tools, ₹0 funded | ⛔ **manual in Kotak app** |

---

## 2. Known broken — root causes

### 2.1 Dhan: Data API subscription ✅ *resolved 20-Aug-2026*

**Full subscription (trading + market data) activated 20-Aug-2026.**

Access token (24h, Method 1 — direct from web.dhan.co → My Profile → Access DhanHQ APIs) stored in `.broker_creds` as `DHAN_ACCESS_TOKEN`.

```
positions    → ✅ working
funds        → ✅ returns (note: returns ₹0.00 even when unauthenticated — never use for verify)
ltp          → ⬜ unverified post-upgrade (was Unauthorized before)
expirylist   → ⬜ unverified post-upgrade (was Unauthorized before)
optionchain  → ⬜ unverified post-upgrade (was Unauthorized before)
```

**What the two subscription tiers cover:**
- **Trading API** — free for all Dhan account holders: login, positions, funds, orders, alerts, margin
- **Data API** — separate paid subscription: `ltp`, `ohlc`, `quote`, `optionchain`, `expirylist`, historical data

**How to verify the subscription is active:** the Dhan profile API response includes `dataPlan` and `dataValidity` fields. The practical test is `expirylist` returning dates instead of Unauthorized.

> ⚠️ **Never verify Dhan with `funds`.** It returns a well-formed all-zeros response even when unauthenticated, which reads as "connected". **Always verify with `expirylist`.**

**MCP OAuth vs direct token:** The Dhan MCP uses the OAuth consent flow (`mcp__dhan__login`). The `DHAN_ACCESS_TOKEN` in `.broker_creds` is a direct REST token (Method 1, 24h validity). Both should now carry Data API entitlement. Re-login via MCP each session and verify with `expirylist`.

### 2.2 Zerodha: F&O segment not activated ⛔ *open*

`get_profile` returns `exchanges: ["BSE","MF","NSE"]` — `NFO` and `BFO` absent; `commodity.enabled: false`; available balance ₹500.

**Impact:** Kite cannot execute derivatives orders. **Market data is unaffected** — `get_quotes` on NFO symbols works fine, so Kite remains our data source.

### 2.3 Kotak Neo: MCP is read-only *by design*

No order-placement tools exist in the Kotak MCP. Since the capital is here, **all execution is manual in the Kotak Neo app.** Claude provides structure, strikes, sizing and levels; the user places the orders.

---

## 3. Effective architecture (as of 20-Aug-2026)

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
  │  DHAN MCP    │────────────────┘
  │  IV, GREEKS  │   ✅ Data API subscription active (20-Aug-2026)
  │  optionchain │   ⬜ verify with expirylist on first use
  └──────────────┘
```

Kite remains the data layer for spot/VIX/OI (faster, always working). Dhan adds option chain Greeks + IV which Kite cannot provide. Execution stays manual on Kotak app.

---

## 4. Session log

| Date | Kite | Kotak | Dhan | What we used each for | Notes |
|---|---|---|---|---|---|
| 17-Aug-2026 | 🟢 data only | 🟢 ₹7.02L | 🔴 data blocked | Kite: NIFTY/BANKNIFTY/VIX spot, 18-Aug option chain prices + OI + depth, `NIFTY26AUGFUT`. Kotak: available margin. Dhan: nothing usable. | 3 consent URLs burned on Dhan before diagnosing entitlement issue — see §5. No Greeks available all session. **Outcome: NO TRADE** (8 red/warning signals vs a 3-signal sit-out threshold; IVP ≈ 2%). Full reasoning: [`17-08-2026-tread.md`](../my-treads/August-2026/17-08-2026/17-08-2026-tread.md). Workaround for the missing Greeks: the straddle rule, [`strategy_ref_book.md` §8.7.3](../kb/kb1/strategy_ref_book.md#873-method-3--the-straddle-rule-the-fastest-works-with-no-greeks-at-all). Session closed 11:55, no position. |
| 20-Aug-2026 | 🟢 data only | 🟢 ₹7.02L | 🟡 login OK, data unverified | Setup session — no trading. Fixed recurring MCP connection issue (JFrog npm auth blocking mcp-remote). Added project `.npmrc` → public registry. Dhan Data API subscription purchased; access token stored in `.broker_creds`. Greeks/IV pending first live verify with `expirylist`. |
| 24-Aug-2026 | 🟢 data only | 🟢 ₹7.02L | 🟢 **fully verified** (expirylist + optionchain) | Kite: NIFTY/BANKNIFTY/SENSEX/VIX spot. Dhan: `expirylist` ✅, `optionchain` ✅ — IV and full chain confirmed working. Dhan access token renewed and saved to `.broker_creds`. **Outcome: NO TRADE** — CHEAP IV (VIX 11.47), NIFTY + BANKNIFTY both 1 DTE (Gamma unmanageable manually), SENSEX sizing at 1 lot does not reach 1% target without breaching daily loss cap. 3 Go/No-Go warnings fired. Full reasoning: [`24-08-2026-tread.md`](../my-treads/August-2026/24-08-2026/24-08-2026-tread.md). |

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

- [x] ~~Activate **Dhan Data API** subscription~~ — done 20-Aug-2026; full subscription (trading + data).
- [x] ~~First live verify of Dhan data endpoints post-upgrade~~ — **verified 24-Aug-2026**: `expirylist` ✅, `optionchain` (IV + full chain) ✅. Delta-band strike selection and IVP filter are now fully unblocked.
- [ ] Confirm whether **F&O is enabled on the Kotak Neo account** — `get_limits` does not expose segment entitlements
- [ ] Decide the long-term execution venue: activate F&O + fund Zerodha, or fund Dhan, or accept permanent manual execution on Kotak

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
