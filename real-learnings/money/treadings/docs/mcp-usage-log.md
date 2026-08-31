# MCP Usage Log — which broker MCP we use for what, and what actually works

Companion to [`broker-session-startup.md`](./broker-session-startup.md) (how to connect) and the capability map in [`CLAUDE.md`](../CLAUDE.md) (what each broker *claims* to support).

**Purpose of this file:** `CLAUDE.md` records the *designed* architecture. This file records the **observed** reality — which endpoints actually respond, which are entitlement-blocked, and which MCP we ended up using for each data point in each session. Update it whenever a call behaves differently from the capability map.

---

## 1. Live capability matrix — verified, not assumed

Legend: ✅ verified working · ❌ verified failing · ⬜ not yet tested · ⚠️ works but caveated

*Last verified: **31-Aug-2026, 11:43 IST***

> ⚠️ **Two Dhan findings from 28-Aug-2026 still apply:**
> **(a)** ~~Dhan MCP tools are dead~~ → **resolved 31-Aug-2026** — see §2.6. `market_data_agent_tool` verified working.
> **(b)** Dhan's **Greeks and IV are computed off spot, not the forward** — they are *present, plausible, and wrong.* See §2.5. Every ✅ against Dhan below means "the field is populated", **not** "the value is usable".

| Data point / action | Kite (Zerodha) | Kotak Neo | Dhan | We use |
|---|---|---|---|---|
| Session login | ✅ `login` → browser 2FA | ✅ `get_login` → QR → `validate_login` | ✅ `authenticate` → browser → auto-upgrade; if `invalid_client` retry `authenticate` once (§2.6) | all three |
| Account / margin | ⚠️ `get_margins` — ₹500 only | ✅ `get_limits` — **₹7.02L** | ⚠️ `funds` — ₹0.00 | **Kotak** |
| Index spot (NIFTY / BANKNIFTY / SENSEX) | ✅ `get_ltp` | ⬜ | ⬜ `ltp` (subscription active, unverified post-upgrade) | **Kite** |
| India VIX | ✅ `get_ltp` `NSE:INDIA VIX` | ⬜ | ⬜ | **Kite** |
| Instrument / strike search | ✅ `search_instruments` (`filter_on: underlying`) | ⬜ `search_instrument` | ⬜ | **Kite** |
| Option LTP + OHLC | ✅ `get_quotes` | ⬜ `get_quote` | ⬜ | **Kite** |
| **Open Interest per strike** | ✅ `get_quotes` → `oi`, `oi_day_high`, `oi_day_low` | ⬜ | ⬜ | **Kite** |
| **Bid/ask depth (5 level)** | ✅ `get_quotes` → `depth` | ⬜ | ⬜ | **Kite** |
| **Implied Volatility** | ❌ not provided | ❌ not provided | ⚠️ **populated but UNRELIABLE** — CE IV ≠ PE IV at the same strike (§2.5) | ⛔ **none trustworthy** |
| **Greeks (Δ Γ Θ V)** | ❌ not provided | ❌ not provided | ⚠️ **populated but UNRELIABLE** — computed off spot, not forward; Δ=0.50 lands ~85 pts low on NIFTY (§2.5) | ⛔ **§8.7.3 straddle rule** |
| **Forward / basis** | ⚠️ via `get_quotes` on `NIFTY26SEPFUT` | ⬜ | ✅ derive from chain: `F = K + C − P` (parity, model-free) | **parity, cross-checked vs Kite futures** |
| Full option chain object | ❌ (build from `get_quotes`) | ❌ | ✅ **REST only** — all strikes, CE+PE LTP/OI/bid-ask/`previous_oi` — **re-verified 28-Aug-2026** | **Dhan (curl)** |
| Expiry list | ⚠️ derive from `search_instruments` | ⬜ | ✅ **REST only** — `/v2/optionchain/expirylist` (`/v2/expirylist` is a 404) | **Dhan (curl)** |
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

### 2.4 Dhan: the MCP tools are dead — use direct REST ⛔ *resolved 31-Aug-2026 — see §2.6*

~~The OAuth consent flow completes normally, and every `mcp__dhan__*` tool still fails.~~ **Resolved 31-Aug-2026** — see §2.6. The Dhan MCP server was updated to use agent-style tools and `mcp__dhan__market_data_agent_tool` action=`expirylist` now works.

**The REST path remains valid as a fallback.** Recreate each session; `/tmp` does not persist:

```bash
#!/bin/bash   # /tmp/dhan.sh
cd /Users/kbaghel/Desktop/my_kb/Git/kunjesh-singh-ai-vibe-code/real-learnings/money/treadings
set -a; . ./.broker_creds; set +a
curl -s -X POST "https://api.dhan.co/v2/$1" \
  -H "access-token: $DHAN_ACCESS_TOKEN" -H "client-id: $DHAN_CLIENT_ID" \
  -H "Content-Type: application/json" -d "$2"
```

| Gotcha | Correct form |
|---|---|
| Both headers are mandatory | `access-token` **and** `client-id` — either alone returns Unauthorized |
| **Field name** | `UnderlyingSeg` (NOT `UnderlyingSegment`) — wrong name returns `813: Invalid SecurityId` |
| **Index scrip IDs** | NIFTY=13 · BANKNIFTY=25 · FINNIFTY=27 · SENSEX=51 |
| Expiry list endpoint | `/v2/optionchain/expirylist` ✅ · `/v2/expirylist` is a **404** |
| Rate limit | option chain **1 unique request / 3 sec** — allow ~4s between calls |
| Expiry dates | **Never guess.** `2026-09-02` returned *Invalid Expiry Date*. Fetch the list first. |

### 2.6 Dhan: MCP tools now working ✅ *resolved 31-Aug-2026*

**Dhan MCP tools are live.** The server was updated to agent-style tools. Verified 31-Aug-2026 at 11:43 IST:

```
mcp__dhan__market_data_agent_tool action=expirylist → NIFTY dates returned ✅
```

**New tool names (post-31-Aug-2026):**
- `mcp__dhan__market_data_agent_tool` — ltp, ohlc, quote, optionchain, expirylist
- `mcp__dhan__portfolio_agent_tool` — positions, funds
- `mcp__dhan__margin_agent_tool` — margin calc
- `mcp__dhan__search_agent_tool` — instrument search
- `mcp__dhan__orderbook_agent_tool`, `mcp__dhan__tradebook_agent_tool`, `mcp__dhan__trading_agent_tool`

**Login flow (new):**
1. Call `mcp__dhan__authenticate` → browser URL
2. User completes Dhan login
3. If `{"error":"invalid_client"}` in browser → **call `mcp__dhan__authenticate` again** — first call may have a stale server-side client_id; second call generates a fresh one. Safe to retry when the URL has already failed.
4. If redirect page shows connection error (not `invalid_client`) → paste callback URL → `mcp__dhan__complete_authentication`
5. Post-auth: pre-auth tools (`authenticate`, `complete_authentication`) disappear; full agent tools appear
6. Verify with `expirylist`, not `funds`

**Payload format for market_data_agent_tool:**
```json
{"UnderlyingScrip": 13, "UnderlyingSeg": "IDX_I"}       // expirylist
{"UnderlyingScrip": 13, "UnderlyingSeg": "IDX_I", "Expiry": "YYYY-MM-DD"}  // optionchain
```
Field is `UnderlyingSeg` — using `UnderlyingSegment` returns `813: Invalid SecurityId` (misleading error).

### 2.5 ⛔ Dhan's Greeks and IV are computed off SPOT, not the FORWARD *(discovered 28-Aug-2026)*

**The most dangerous failure logged in this file, because nothing looks broken.** The fields are populated with plausible numbers that are wrong in a consistent direction.

**Proof, requiring no model:** one strike + one expiry + one underlying = exactly **one** implied volatility. Dhan returns two.

```
NIFTY 01-Sep-2026, observed 11:05 IST
   Strike    CE IV     PE IV     Gap
   24,100    12.77      7.38    +5.40
   24,150    11.96      6.97    +4.99
   24,200    11.47      6.41    +5.06
   24,250    11.01      5.63    +5.38
SENSEX +3.55 to +5.34 (same signature) · BANKNIFTY −1.87 to −3.79 (inverted, 32 DTE)
Deep-ITM legs return IV = 0, delta = 0, theta = 0 — solver non-convergence, not "no risk".
```

**Cause.** Put-call parity gives the forward the market is actually using, consistent to <1 pt across the chain:

```
F = K + C − P
  24000 + 260.25 −  23.85 = 24,236.4
  24100 + 180.50 −  43.70 = 24,236.8
  24200 + 113.60 −  76.60 = 24,237.0
  24300 +  63.90 − 127.00 = 24,236.9
NIFTY 01-Sep forward ≈ 24,237 · spot 24,155 · BASIS +82 pts (+0.34%)
```

Cross-checked and confirmed live: Kite's own 11:00 prints on the same strike gave F ≈ 24,241, and Kite futures showed `NIFTY26SEPFUT` 24,348.80 (+194 over spot). Price with S when F is 82 points higher and calls look dear / puts cheap — **exactly the observed pattern.**

| Index (28-Aug) | Spot | Forward | Basis |
|---|---|---|---|
| NIFTY 01-Sep | 24,155 | 24,237 | **+82** |
| SENSEX 03-Sep | 77,240 | 77,523 | **+283** |
| BANKNIFTY 29-Sep | 57,534 | 57,916 | **+382** |

**Impact:** Dhan puts NIFTY's Δ=0.50 near 24,190 when the true ATM-forward is 24,237 — **every strike selected off Dhan's delta band is ~85 points bearish, silently.**

**Standing rule until this is resolved:**

1. **Run the §8.7.1a basis check before trusting any Dhan delta.** If `basis > 0.1% of spot`, **discard the delta band.**
2. Fall back to `strategy_ref_book.md` **§8.7.3** (the straddle rule), centred on **F**, not spot.
3. Extracting F via `F = K + C − P` **is permitted** — arithmetic, not a model. Recomputing Δ/Θ/IV locally is **not** (§5.6).
4. **Tell the user the Greeks are unusable.** Never substitute silently.

> Dhan's **prices, OI, `previous_oi` and bid/ask are unaffected and remain trustworthy.** It is only the derived analytics that are broken.

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
  │  DHAN — REST │────────────────┘
  │  curl /v2/   │   ⛔ MCP tools dead (§2.4) — use /tmp/dhan.sh
  │  optionchain │   ✅ prices · OI · previous_oi · bid/ask
  │              │   ⛔ IV / GREEKS unreliable (§2.5) — off spot, not forward
  └──────────────┘
```

Kite remains the data layer for spot/VIX/OI (faster, always working). Dhan adds the full chain object with `previous_oi` and bid/ask, which Kite cannot assemble cheaply. Execution stays manual on Kotak app.

> **Revised as of 28-Aug-2026:** Dhan is no longer the Greeks/IV layer. **We currently have no trustworthy Greeks source.** Strike selection runs on §8.7.3 (straddle rule) + parity forward + OI walls; volatility state runs on Kite HV + India VIX + the ATM-forward straddle. This is the same posture as the pre-20-Aug period — see §7.

---

## 4. Session log

| Date | Kite | Kotak | Dhan | What we used each for | Notes |
|---|---|---|---|---|---|
| 17-Aug-2026 | 🟢 data only | 🟢 ₹7.02L | 🔴 data blocked | Kite: NIFTY/BANKNIFTY/VIX spot, 18-Aug option chain prices + OI + depth, `NIFTY26AUGFUT`. Kotak: available margin. Dhan: nothing usable. | 3 consent URLs burned on Dhan before diagnosing entitlement issue — see §5. No Greeks available all session. **Outcome: NO TRADE** (8 red/warning signals vs a 3-signal sit-out threshold; IVP ≈ 2%). Full reasoning: [`17-08-2026-tread.md`](../my-treads/August-2026/17-08-2026/17-08-2026-tread.md). Workaround for the missing Greeks: the straddle rule, [`strategy_ref_book.md` §8.7.3](../kb/kb1/strategy_ref_book.md#873-method-3--the-straddle-rule-the-fastest-works-with-no-greeks-at-all). Session closed 11:55, no position. |
| 20-Aug-2026 | 🟢 data only | 🟢 ₹7.02L | 🟡 login OK, data unverified | Setup session — no trading. Fixed recurring MCP connection issue (JFrog npm auth blocking mcp-remote). Added project `.npmrc` → public registry. Dhan Data API subscription purchased; access token stored in `.broker_creds`. Greeks/IV pending first live verify with `expirylist`. |
| 24-Aug-2026 | 🟢 data only | 🟢 ₹7.02L | 🟢 **fully verified** (expirylist + optionchain) | Kite: NIFTY/BANKNIFTY/SENSEX/VIX spot. Dhan: `expirylist` ✅, `optionchain` ✅ — IV and full chain confirmed working. Dhan access token renewed and saved to `.broker_creds`. **Outcome: NO TRADE** — CHEAP IV (VIX 11.47), NIFTY + BANKNIFTY both 1 DTE (Gamma unmanageable manually), SENSEX sizing at 1 lot does not reach 1% target without breaching daily loss cap. 3 Go/No-Go warnings fired. Full reasoning: [`24-08-2026-tread.md`](../my-treads/August-2026/24-08-2026/24-08-2026-tread.md). |
| 27-Aug-2026 | 🟢 data only | 🟢 connected | 🟡 **MCP tool blocked / REST ✅** | Kite: spot + VIX + daily & 15-min historicals (HV20 computation). Dhan **direct REST curl**: `optionchain` for all 3 indexes — **full Greeks + IV + previous_oi**. Kotak: login verified. **Outcome: NO TRADE** — §8.12.6 Range-Compression Squeeze fires on every criterion (IVP **2.5%**, VIX 10.57 = 6-month closing low and **+5.58%** today, 6 sessions of overlapping ranges, HV30→HV20→HV10 monotonic decline). SENSEX 0-DTE fly failed 2 of 4 §8.6.10 filters (not an inside day; VIX >5%). Intraday-only constraint kills the 5-DTE NIFTY bear call spread (0.23%). Full reasoning: [`27-08-2026-tread.md`](../my-treads/August-2026/27-08-2026/27-08-2026-tread.md). **SETTLEMENT: compression broke DOWNWARD** — SENSEX closed 76,933.59 (−0.70%) at the day's low, 192 pts below the 6-session floor. The declined SENSEX 77500/77700 bear call spread **expired worthless (a winner)**; ~₹1,750 (0.29%) forgone at the 2:15 PM time stop. **Two KB amendments earned:** [§8.12.6a](../kb/kb1/strategy_ref_book.md#8126a-the-neutralone-sided-distinction--amendment-27-aug-2026) (compression veto applies to *neutral* premium only) and [§8.10.5](../kb/kb1/strategy_ref_book.md#8105-abort-conditions-must-match-the-structures-greeks--added-27-aug-2026) (aborts must match the structure's dominant Greek). | **Dhan MCP `market_data_agent_tool` returns `Unauthorized` even after successful OAuth — but direct REST with `access-token` + `client-id` works.** Use curl, not the MCP tool. Correct endpoint is `/v2/optionchain/expirylist`; `/v2/expirylist` is a 404. |

| 31-Aug-2026 | 🟢 data only | 🟢 ₹7.02L | 🟢 **MCP now working** (§2.6) | Kite: NIFTY/VIX/BANKNIFTY/SENSEX spot + 15-min intraday candles. Dhan MCP: `market_data_agent_tool` expirylist + optionchain (both verified). Kotak: margin. **Outcome: TRADE EXECUTED ✅** — NIFTY 01-Sep Bear Call Spread 24,200/24,400, 5 lots, NRML. Entry 12:24 (sell 45.35, buy 9.45 = 35.90 cr). Exit 14:37 (buy 32.40, sell 6.75 = 25.65). **Gross P&L: +₹3,331 · Net ~₹3,131 · 0.52% of ₹6L.** Kill switch 0/3 · Go/No-Go 0 Red · §8.12.6 compression resolved downside (break below 24,025 range floor). Sizing lesson: 5 lots earned 0.52%; 20 lots would have earned 2.08% at same risk distance. New policy: conviction-based sizing, not rigid risk-cap formula. Full session: [`31-08-2026-tread.md`](../my-treads/August-2026/31-08-2026/31-08-2026-tread.md). **Dhan MCP fixed:** `authenticate` → if `invalid_client`, call again (fresh client_id). Field is `UnderlyingSeg` not `UnderlyingSegment`. **Kotak order sequence:** BUY long leg first in NRML spread, then SELL — hedge must be in place before SELL or RMS rejects as naked. |
| 28-Aug-2026 | 🟢 data only | 🟢 ₹7.02L, ₹0 used | 🔴 **MCP dead (DH-901) / REST ✅ but Greeks broken** | Kite: spot + VIX + daily/15-min historicals (HV5/10/20/30), NIFTY & SENSEX futures, option minute-bars for the decay measurement. Dhan **REST**: chains for all 3 indexes + expiry lists. Kotak: `get_limits`. **Outcome: NO TRADE** — and for a *new* reason: not risk, **insufficient reward at permitted size.** §8.13 kill switch **0 of 3**, §7 Go/No-Go **0 Red**, VRP **+1.2** vs HV20, VIX falling — the day was clean. The binding constraint was the **expiry calendar**: nearest expiries NIFTY 01-Sep (2 sessions), SENSEX 03-Sep (4), BANKNIFTY 29-Sep (22, monthly only) — **no 0-DTE or 1-DTE instrument existed**, so an intraday-only mandate had almost no theta to harvest. Priced 4 candidates at bid/ask with full charges: NIFTY iron fly **−₹204 to −₹87**, NIFTY 24000/23900 bull put **+₹263 to +₹823**, SENSEX fly ~₹105/lot, BANKNIFTY ~₹86/lot. Reaching ₹6,000 needed **20–33 lots = 14.9–24.7% of capital** vs a 1.0% cap. Full reasoning: [`28-08-2026-tread.md`](../my-treads/August-2026/28-08-2026/28-08-2026-tread.md). **Six KB amendments earned:** [§8.11.6](../kb/kb1/strategy_ref_book.md#8116-the-feasibility-gate--can-todays-target-be-reached-at-all-added-28-aug-2026) (the feasibility gate + credit-ceiling theorem — run at 9:15, **before** chain analysis, plus the dominant-Greek caveat), [§8.11.7](../kb/kb1/strategy_ref_book.md#8117-the-noise-floor-test--is-your-stop-inside-one-candle-added-28-aug-2026) (**the noise-floor test**), [§8.15.4](../kb/kb1/strategy_ref_book.md#8154-scoring-the-day--mark-at-the-mandated-exit-and-always-report-mae-and-mfe-added-28-aug-2026) (**scoring protocol — mandated exit time + MAE/MFE**), [§8.7.1a](../kb/kb1/strategy_ref_book.md#871a-the-forward-basis-check--run-this-before-you-trust-any-delta-added-28-aug-2026) (forward-basis check), `option_chain_n_greeks.md` §7 Filter 1 (GIFT Nifty is a *futures* price), and **§8.13.3 (what to re-pull at every scheduled check — OI is not optional)**. ⚠️ **The 13:09 validation was SUPERSEDED at 16:54** — it was marked inside the worst 90-min window of the day and two of three conclusions reversed. Close: NIFTY **24,175.65 (+84.80)**, SENSEX **+330.92**, VIX at its **day low** 10.68. Re-scored at the §8.3 mandated exit (2:30 PM): iron fly **−1.45 pts (scratch, not −₹675)**, bull put **−5.00**, bear call **+19.80** (decays to +4.60 by close = a loss after costs). **The decisive fact only MAE surfaces:** the bull put hit **−9.60 = 95% of its stop, 30 min after entry**, then finished +1.25 — stop distance 10.10 pts vs a ±12 pt 30-min range in the short leg → **§8.11.7**. Best structure of the day at max permitted size = **0.35%**, so §8.11.6's ceiling holds. Also self-caught: BANKNIFTY's day was estimated **from theta on a vega-dominant 32-DTE structure** (₹86 modelled vs ₹915 actual, ~7×, sign-symmetric). **The miss:** neither the 11:27 nor the 13:09 recheck pulled OI — the 24,200 PE wall was at its day high (193.1L) when cited at 11:00 and closed at **82.13L (−57%)** while support held at 24,000, exactly §8.7.4's "wall being unwound"; the read was right and abandoned. **Close config for Monday:** both call walls (24,300 · 24,400) closed at **intraday OI lows** → mildly bullish into 01-Sep. | **§2.5 — Dhan's Greeks/IV are computed off spot, not the forward.** Discovered by the CE IV ≠ PE IV test. NIFTY basis **+82**, SENSEX **+283**, BANKNIFTY **+382**. Dhan's Δ=0.50 sits ~85 pts below the true ATM-forward. Prices/OI/bid-ask remain fine. **§2.4 — Dhan MCP now 2-for-2 dead; go straight to REST, do not re-run `login`.** |

---

## 5. Session-startup gotchas learned the hard way

1. **Verify each MCP with a call that exercises the capability you need**, not just a login check. `funds` succeeding does not mean the chain will load.
2. **Never call `mcp__dhan__login` twice.** Each call invalidates the previous pending consent. The user then hits `{"status":"error","message":"Target session is not pending login."}` and the `tokenId` is rejected with *"already consumed for this session"* — which looks like an auth bug but is self-inflicted. Issue **one** URL and wait.
3. **`Token rejected: token_id already consumed` does not mean success.** Always follow it with a real API call.
4. **Match the `consentId`.** When the user pastes a callback URL, check its `consentId` equals the one most recently issued before using its `tokenId`.
5. **A missing `NFO` in Kite's profile `exchanges` array only blocks orders, not data.** Don't abandon Kite as a data source over it.
6. **Do not compute Greeks locally as a silent fallback.** The user has explicitly asked for Dhan's pre-calculated Greeks. If Dhan is down, say so and ask.
7. **Skip the Dhan MCP entirely — go straight to REST** (§2.4). Two sessions confirmed dead. Rebuild `/tmp/dhan.sh` at session start; `/tmp` does not survive.
8. **A populated field is not a verified field.** Dhan's Greeks returned plausible numbers for four sessions before anyone checked them (§2.5). **Verify each data point with a call that exercises the capability *and* a sanity check on the value.** The CE IV ≠ PE IV test takes ten seconds.
9. **Fetch the expiry list before anything else** (§8.11.6 step 1). On 28-Aug the whole session's verdict was determined by "nearest expiry is 2 sessions away" — knowable at 9:15, actually established at 11:00.

---

## 6. Open items

- [x] ~~Activate **Dhan Data API** subscription~~ — done 20-Aug-2026; full subscription (trading + data).
- [x] ~~First live verify of Dhan data endpoints post-upgrade~~ — **verified 24-Aug-2026**: `expirylist` ✅, `optionchain` (IV + full chain) ✅.
- [ ] 🔴 **NEW (28-Aug-2026) — raise the spot-vs-forward Greeks defect with Dhan support** (§2.5). Until fixed, **we have no trustworthy Greeks source** and delta-band strike selection is re-blocked. Reproduction is one line: CE IV ≠ PE IV at the same strike/expiry.
- [ ] 🔴 **NEW (28-Aug-2026) — fix or abandon the Dhan MCP OAuth binding** (§2.4). Dead 2 sessions running while REST works. Consider dropping the MCP from `.mcp.json` and documenting REST as the only Dhan path.
- [ ] Confirm whether **F&O is enabled on the Kotak Neo account** — `get_limits` does not expose segment entitlements
- [ ] Decide the long-term execution venue: activate F&O + fund Zerodha, or fund Dhan, or accept permanent manual execution on Kotak

---

## 7. Working without Greeks — the sanctioned substitutes

> ⚠️ **Re-activated 28-Aug-2026.** §2.1 was resolved, but **§2.5 re-broke Greeks in a worse way** — they are now present *and wrong*, which is more dangerous than absent. This table is live again and is the default posture until §2.5 clears.

**Run first, every session:** the [§8.7.1a](../kb/kb1/strategy_ref_book.md#871a-the-forward-basis-check--run-this-before-you-trust-any-delta-added-28-aug-2026) forward-basis check. It tells you in 30 seconds whether the vendor's Greeks can be trusted at all.

| Permitted | Not permitted |
|---|---|
| `F = K + C − P` (put-call parity) — **arithmetic, assumes nothing** | Recomputing Δ / Γ / Θ / V locally |
| ATM-forward straddle ≈ `0.7979 × F × σ√T` to back out a forward-consistent σ | Any local Black-Scholes solve for a *Greek* |
| HV from Kite daily candles; India VIX | Presenting a derived number as a vendor number |

These are the approved replacements. **Do not compute Greeks locally** — the user rejected that explicitly.

| Normally you'd use | Instead use |
|---|---|
| **The ATM strike itself** | **The parity forward `F`, not spot.** On 28-Aug the true NIFTY ATM was 24,237 while spot was 24,155 — more than one strike apart. |
| Delta band (8–12Δ / 12–20Δ) for strike selection | [`strategy_ref_book.md` §8.7.3](../kb/kb1/strategy_ref_book.md#873-method-3--the-straddle-rule-the-fastest-works-with-no-greeks-at-all) — the straddle rule, **centred on F**: `call = F + 0.85 × straddle`, `put = F − 1.05 × straddle` |
| Delta-matching the two sides of a condor/strangle | §8.6.8 premium-matching proxy (equal credit, not equal distance) — put skew makes equidistant strikes silently long delta |
| IV / IVP per strike | India VIX from Kite + ATM straddle ÷ spot as an IV proxy; HV20 from Kite daily candles; **VRP = IV − HV20** |
| Expected move from IV | `EM ≈ ATM straddle × 0.85` |
| Position delta | OI walls (§8.7.4) + directional structure only. If the trade genuinely needs a delta number, **stop and tell the user.** |
