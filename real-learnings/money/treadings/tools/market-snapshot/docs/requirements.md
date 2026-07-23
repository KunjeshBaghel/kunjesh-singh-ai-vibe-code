# Tool: market-snapshot

## Purpose

Fetch live Indian options market data from trusted official sources and save it as a timestamped snapshot inside the current day's trade journal folder. Each run creates a new file — no overwriting. This gives Claude a stateful, time-ordered view of how the market evolved during the session so it can suggest full option strategies (legs, strikes, premiums, max profit zones), identify smart money movement, and help the user exit bad trades and enter better ones.

---

## Hard Requirement — No Local Calculations

**All Greeks (Delta, Theta, Vega, Gamma), IV, PCR, Max Pain, and OI Change must come pre-calculated from the broker API. The script does zero mathematical computation on market data.**

Reason: locally computed values introduce model risk and bugs (wrong interest rate assumption, wrong time-to-expiry, wrong IV input). The broker's own risk system runs these calculations with exchange-grade inputs. Claude's only job is to interpret pre-calculated data and suggest strategies — not to verify math.

If a data field cannot be obtained pre-calculated from a trusted broker API, the field is stored as `null` in the snapshot. Claude is told to treat `null` fields as unavailable and not to estimate them.

---

## Broker API Verdict — Greeks Availability

Research conducted before writing this spec confirmed the following:

| Broker | Full Option Chain API | Greeks via API | Notes |
|--------|----------------------|---------------|-------|
| **Dhan (DhanHQ)** | ✅ Single POST call | ✅ Delta, Theta, Gamma, Vega per strike | Best fit. Also returns IV, OI, prev OI, volume, bid/ask in one response |
| **Zerodha (Kite Connect)** | ❌ No single endpoint | ❌ Greeks not in API as of 2025 | Greeks visible on Kite UI but not exposed via API. Ruled out for this tool |
| **Kotak Neo** | ❌ No option chain endpoint | ❌ No Greeks API | Order routing only. Ruled out for this tool |

**Primary data source for option chain + Greeks: Dhan API.**

The user does not currently have a Dhan account. Creating one is a prerequisite before this tool can be built. Dhan is being added **for data only** — actual trade execution continues on Zerodha (Kite) and Kotak Neo.

### Broker Role Separation

| Broker | Role in this project |
|--------|---------------------|
| **Dhan** | Data source only — option chain, Greeks, OI, IV. No orders placed here |
| **Zerodha (Kite)** | Order execution, live positions, account margin |
| **Kotak Neo** | Research reports, holdings, account data |

This separation is intentional. Dhan's API is used purely as a market data feed — similar to subscribing to a data terminal, not a trading platform.

---

## Data Sources (Trusted Only)

| Source | What it provides | Auth | Path |
|--------|-----------------|------|------|
| **Dhan MCP** (official, first-party) | Full option chain — all strikes, pre-calculated Greeks (Delta, Theta, Gamma, Vega), IV, OI, prev OI, volume, bid/ask. Called directly by Claude in conversation. | Dhan account + access-token in `.mcp.json` | **Preferred** |
| **Dhan REST API** `/v2/optionchain` | Same data as MCP, fetched by Python script when MCP is unavailable | Dhan account + access-token in `.broker_creds` | Fallback |
| **NSE official JSON endpoint** | India VIX, NIFTY spot, FII/DII participant OI, NIFTY futures OI | Session cookie only (no account) | Always used (NSE data not in Dhan) |

### Data flow — MCP path (preferred)

```
Claude → Dhan MCP → Dhan servers → option chain + Greeks returned inline
Claude → NSE endpoint → VIX, spot, FII/DII, futures OI returned inline
```

No snapshot files needed. Claude gets live data on demand within the conversation.

### Data flow — Script path (fallback, if Dhan MCP lacks option chain tool)

```
User runs: python tools/market-snapshot/fetch.py
  → Dhan REST API  → option chain + Greeks
  → NSE endpoint   → VIX, spot, FII/DII, futures OI
  → merged into snapshot-HH-MM.json in today's my-treads/ folder
Claude reads the file on request.
```

No third-party MCPs. No unverified packages. Only Dhan (official broker) and NSE (exchange) as sources.

---

## Storage Location

Snapshots live inside the existing day folder in `my-treads/`, alongside the trade journal files.

```
my-treads/
  22-July-2026/
    22-July-2026-market_view.md
    22-July-2026-tread.md
    22-July-2026-learning.md
    snapshot-09-15.json       ← first run (pre-open)
    snapshot-10-00.json       ← after market opens
    snapshot-10-30.json       ← 30-min check
    snapshot-14-20.json       ← before entering a trade
    snapshot-15-20.json       ← exit check / EOD
```

### File naming

`snapshot-HH-MM.json` — 24-hour IST time at the moment of fetch.

If the same minute is triggered twice (rare), append `-2` (e.g., `snapshot-10-30-2.json`).

### No overwrite rule — core invariant

Every run creates a new file. No existing snapshot is ever modified or deleted. This enables Claude to track how OI, PCR, VIX, and Greeks changed across the session (OI vs Time, Fut OI vs Time) by comparing files in time order.

---

## What Each Snapshot Contains

**Zero processing rule:** the script calls the API, gets the response, and writes it directly to the JSON file. No field renaming, no restructuring, no type conversion, no derived values. What the API returns is what the file contains. Claude reads the raw API response.

The snapshot file has two top-level keys — one per source — plus a thin `meta` block written by the script (timestamp and source labels only, no market data).

---

### Snapshot file structure

```json
{
  "meta": {
    "fetched_at_ist": "2026-07-22T14:20:00+05:30"
  },
  "dhan_option_chain": { ... raw Dhan API response, stored verbatim ... },
  "nse":              { ... raw NSE API responses, stored verbatim ... }
}
```

---

### `dhan_option_chain` — raw response from `POST /v2/optionchain`

Stored exactly as Dhan returns it. Not touched.

```json
"dhan_option_chain": {
  "data": {
    "last_price": 25642.8,
    "oc": {
      "25650.000000": {
        "ce": {
          "average_price": 146.99,
          "greeks": {
            "delta": 0.53871,
            "theta": -15.1539,
            "gamma": 0.00132,
            "vega": 12.18593
          },
          "implied_volatility": 9.789193798280868,
          "last_price": 134,
          "oi": 3786445,
          "previous_close_price": 244.85,
          "previous_oi": 402220,
          "security_id": 42528,
          "top_ask_price": 134,
          "top_ask_quantity": 1365,
          "top_bid_price": 133.55,
          "top_bid_quantity": 1625,
          "volume": 117567970
        },
        "pe": {
          "average_price": 134.62,
          "greeks": {
            "delta": -0.46732,
            "theta": -10.61131,
            "gamma": 0.00109,
            "vega": 12.2025
          },
          "implied_volatility": 11.939337251984934,
          "last_price": 132.8,
          "oi": 3096145,
          "previous_close_price": 178.30,
          "previous_oi": 287440,
          "security_id": 42529,
          "top_ask_price": 132.75,
          "top_ask_quantity": 980,
          "top_bid_price": 132.45,
          "top_bid_quantity": 1120,
          "volume": 157009970
        }
      },
      "25700.000000": { ... next strike ... },
      "25600.000000": { ... next strike ... }
    }
  }
}
```

Every strike Dhan returns is stored. No filtering, no trimming.

---

### `nse` — raw responses from NSE endpoints

Stored exactly as NSE returns them. Not touched.

```json
"nse": {
  "option_chain": { ... raw response from nseindia.com/api/option-chain-indices?symbol=NIFTY ... },
  "participant_oi": { ... raw response from NSE participant OI endpoint ... },
  "vix": { ... raw response from NSE VIX endpoint ... }
}
```

NSE `option_chain` response contains `records.underlyingValue` (NIFTY spot), `records.timestamp`, `records.data[]` (per-strike CE/PE with `openInterest`, `changeinOpenInterest`, `impliedVolatility`, `lastPrice`), and `filtered.CE.totOI` / `filtered.PE.totOI`.

NSE `participant_oi` contains FII, DII, Pro, Client positions across Index Futures, Calls, Puts — `netChange` and `netOI` per participant per segment.

NSE `vix` contains the India VIX level and change.

---

### OI vs Time and Fut OI vs Time — derived by Claude, not by the script

Claude compares all `snapshot-*.json` files for the current day in time order. The script writes nothing extra for this. Claude reads raw `oi` and `previous_oi` values from the Dhan response across snapshots to track how OI moved over time per strike.

---

## How Claude Uses the Snapshots

When the user says **"refresh data"** or **"check current market"**:

```
User runs:  python tools/market-snapshot/fetch.py
            → new snapshot-HH-MM.json appears in today's my-treads/ folder

Claude:
  1. Reads the latest snapshot → full market analysis
  2. If 2+ snapshots exist → reports what changed across time (trend layer)
  3. Classifies market as one of five views (kb/Market_View.md §5)
  4. Runs Pre-Trade Go/No-Go checklist (kb/option_chain.md §7) on real numbers
  5. Suggests full strategy: legs, strikes, premiums, max profit zone, stop-loss
  6. Evaluates existing positions: exit / hold / roll — based on live chain data
```

---

## Strategy Suggestion Scope

With the full chain (all strikes, Greeks, OI) from Dhan, Claude can suggest:

- **Which expiry** to trade based on IV and theta already in the data
- **Which strikes** — target delta range, OI walls, bid/ask spread quality
- **All legs** of a multi-leg strategy with actual premiums from the snapshot
- **Max profit, max loss, breakeven prices** — computed from the premiums, not from models
- **Probability of Profit** — read from delta (e.g., Delta 0.15 → ~85% POP for the short side)
- **Where smart money walls are** — highest CE OI = resistance, highest PE OI = support
- **Exit signals** — strike's OI unwinding, delta moving toward ITM, VIX spike
- **Roll suggestions** — when to move to a different expiry or adjust strikes

---

## Suggested Run Times

| Time (IST) | Why |
|-----------|-----|
| 08:45 – 09:10 | Pre-open: prev session FII/DII data, GIFT Nifty level |
| 09:15 – 09:30 | First 15 min after open — opening direction before any trade |
| Every 30 min during session | Intraday OI shift tracking (`kb/Market_View.md` guideline) |
| Before entering a trade | Go/No-Go checklist + strategy suggestion |
| 15:15 – 15:20 | EOD: closing PCR, final OI, FII/DII for next-day view |

---

## What Is Out of Scope

- Any local financial model computation (Black-Scholes, IV calculation, Greeks — must come from Dhan)
- Placing or modifying orders — this tool only reads, never writes to the broker
- Storing snapshots outside the current day's `my-treads/` folder
- Any third-party MCP or data vendor not listed in the Data Sources table
- Automated / scheduled runs — always triggered manually by the user
- BANKNIFTY, FINNIFTY, or stock options — NIFTY 50 only for now

---

## Prerequisites Before Building

### Step 1 — Create a Dhan account

Go to [dhan.co](https://dhan.co), open a trading account, then go to the API dashboard to generate an `access-token` and `client-id`. These are required before any code can be written or tested.

### Step 2 — Check if Dhan MCP covers option chain + Greeks

Dhan has an **official first-party MCP server** (launched June 2026, docs at [docs.dhanhq.co/mcp](https://docs.dhanhq.co/mcp/)). It works with Claude Code exactly like the Kite and Kotak Neo MCPs already in `.mcp.json`.

After account creation, check the MCP tool list at `docs.dhanhq.co/mcp/tools/` for a tool that fetches option chain with Greeks (delta, theta, vega, gamma, IV, OI).

**This check determines the entire implementation path:**

| Outcome | Implementation |
|---------|---------------|
| **Dhan MCP exposes option chain + Greeks** | Add Dhan MCP to `.mcp.json`. Claude calls it directly in conversation — real-time, no script, no snapshot files needed. The `market-snapshot` Python script is not built. |
| **Dhan MCP does not expose option chain** | Build the Python script in this folder using Dhan's REST API (`/v2/optionchain`). Snapshot files are saved to `my-treads/DD-Month-YYYY/` as designed in this doc. |

**Preferred outcome:** Dhan MCP path. It is simpler, fully real-time, and consistent with the existing MCP-first approach in this project.

### Step 3 — Confirm API pricing

Verify whether the option chain + Greeks endpoint (`/v2/optionchain`) is on the free API tier or requires a paid plan.

## Open Questions Before Building

1. **Dhan access-token storage:** Token will be stored in `.broker_creds` (already gitignored). Confirm this is acceptable.
2. **Futures OI endpoint:** NSE has a separate endpoint for NIFTY futures data. Confirm exact URL before building.
3. **Max Pain:** Dhan does not return Max Pain pre-calculated. NSE does not either. Options: (a) skip it and mark `null`, (b) compute it from raw OI (simple min-loss lookup, not a financial model). Decision needed before building.
4. **Strike range:** Dhan returns all strikes in one call. Store all or trim to ±20 around ATM to keep snapshot files small?
