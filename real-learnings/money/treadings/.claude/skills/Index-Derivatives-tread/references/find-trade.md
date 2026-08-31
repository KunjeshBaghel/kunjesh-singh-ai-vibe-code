# find-trade — Structure Selection & Sizing

Runs after `analyse-today`. Requires a completed market_view.md. Follows the gates strictly — never jumps to structure before all gates clear.

---

## Pre-check: Read today's market view

Read `my-treads/<Month>/<DD-MM-YYYY>/<DD-MM-YYYY>-market_view.md`.

Extract:
- Five-view classification
- Nearest expiry + trading sessions for all 3 indexes
- Key support/resistance levels
- Any data gaps that were flagged

---

## Gate 1: §8.11.6 Feasibility — run this first

```
For each index:
  sessions_to_expiry = <count>
  intraday_only = YES (user never holds overnight)

  If intraday_only AND sessions_to_expiry ≥ 2:
    → Structure is DELTA-DRIVEN (not theta-driven) today
    → Theta materialises at expiry, not intraday
    → For 1% net: need directional move OR expiry-day theta
    → Honest intraday capture on a flat market: 20-35% of credit

  MAX_CREDIT_POOL = daily_risk_budget ÷ (k - 1)
    (k=1.5 → budget ÷ 0.5; k=2.0 → budget ÷ 1.0)

  REQUIRED_CAPTURE = (k-1) × 100%
    (k=1.5 → 50%; k=2.0 → 100% — only at expiry)
```

**State the verdict clearly:**
- "1-DTE (expiry eve): delta-driven. 1% reachable if market moves ~X pts in our favour."
- "3-DTE: theta is real but ~35 pts/session. At flat market, net ~0.5% intraday."
- "Multiple sessions away: intraday theta is rounding error. No trade unless strongly directional."

If no index has a viable calendar for the target → say so and stop. Do not force a trade.

---

## Gate 2: §8.7.1a Basis check (all 3 indexes)

For each index chain (from Dhan optionchain):
```
F = K + CE - PE  at 3-4 near-ATM strikes
Must agree ±1 pt across strikes.
basis = F - spot
If basis > 0.1% of spot → Dhan's delta band unreliable → use §8.7.3
```

Report: "NIFTY forward F ≈ 24,119 · spot 24,067 · basis +52 pts (+0.22%) → delta band unreliable"

---

## Gate 3: §8.13 Kill Switch check

Fetch intraday candles (Kite 15-min) for the last 2 hours:
```
instrument_token=256265 (NIFTY), interval=15minute
```

Check the 3 markers:
1. **Opening range break**: ORH/ORL from first 30 minutes. Has price broken and SUSTAINED outside it?
2. **VWAP one-sidedness**: Price consistently above or below estimated VWAP for 45+ min?
3. **OI confirming direction**: From Dhan chain — are call OI or put OI building while price moves in same direction?

Scoring:
- 0/3: Normal day → all structures permitted
- 1/3: Elevated caution → lean structures only, tighter sizing
- 2+/3: Trend day → one-sided structures only (bear call spread on downtrend, bull put on uptrend); no condors
- 3/3: Abort → no new structures

---

## Gate 4: §7 Go/No-Go (5 checks)

| # | Check | Green | Yellow | Red |
|---|---|---|---|---|
| 1 | VIX direction | Falling or stable | +3-5% rise | +8%+ spike |
| 2 | Open vs GIFT | Within expected range | Minor surprise | Gap mismatch (GIFT was futures, not spot) |
| 3 | Theta-trap bundle | VIX falling + PCR stable | Mixed | VIX rising + PCR dropping |
| 4 | FII regime (3-day) | 3 consecutive consistent + Net OI confirms | 1-2 days only | Contradicting cumulative |
| 5 | PCR intraday slope | PCR flat or rising | Declining slowly | Sharp PCR drop + call OI building |

**3+ RED → sit out.** Automatic blockers (no market view, undefined stop, no max loss) = immediate sit-out regardless of count.

---

## If all gates clear: Structure selection

### §8.5 Regime grid

| Vol State | Strongly Bearish | Slightly Bearish | Sideways | Slightly Bullish | Strongly Bullish |
|---|---|---|---|---|---|
| **CHEAP** (VIX<12, VRP+) | Bear Call Spread | Bear Call Spread | Iron Fly (half size) | Bull Put Spread | Bull Put Spread |
| **NORMAL** (VIX 12-16) | Bear Call Spread | Bull Put Spread | Iron Condor | Bull Put Spread | Bull Put Spread |
| **RICH** (VIX 16-20) | Naked/Wide Spread | Bull Put or Strangle | Iron Condor (wide) | Bull Put or Strangle | Naked/Wide Spread |
| **HOSTILE** (VIX 20+) | No new structures | No new structures | No new structures | No new structures | No new structures |

**Compression squeeze (§8.12.6):** If active → veto NEUTRAL premium. Permit one-sided vertical leaning with the break direction.

### Fetch full option chain for selected index + expiry

```
mcp__dhan__market_data_agent_tool action=optionchain
{"UnderlyingScrip": <id>, "UnderlyingSeg": "IDX_I", "Expiry": "<date>"}
```

Extract:
- OI at 5 key strikes above (call walls) and 5 below (put walls)
- ATM straddle at the parity forward F
- Bid/ask spreads at the candidate short strikes

### §8.11.7 Noise floor test

For each candidate structure:
```
credit = short_premium - long_premium
stop_distance = (k-1) × credit       (k=1.5 → 0.5 × credit)
short_leg_30min_range = delta × NIFTY_30min_range + vega_change_estimate
IF stop_distance < 1.5 × short_leg_30min_range:
  → stop is inside one candle → no trade at any size → try different structure
```

---

## Present 3 sizing options

For each structure that clears all gates and noise floor:

```
Structure: <name> <short strike>/<long strike>  Expiry: <date>
Net credit: <X> pts  |  Width: <Y> pts  |  Short strike <Z> pts OTM

Sizing options:
  Conservative  — Stop ₹8,000-10,000 → <N> lots
    Gross P&L if flat: ₹<X>  |  Gross P&L if market moves <direction>: ₹<Y>
    Rupee loss at stop: ₹8,000-10,000

  Standard      — Stop ₹15,000-20,000 → <N> lots
    Gross P&L if flat: ₹<X>  |  Gross P&L if market moves <direction>: ₹<Y>
    Rupee loss at stop: ₹15,000-20,000

  Aggressive    — Stop ₹25,000-35,000 → <N> lots
    Gross P&L if flat: ₹<X>  |  Gross P&L if market moves <direction>: ₹<Y>
    Rupee loss at stop: ₹25,000-35,000

Stop trigger: <description — e.g. "spread cost reaches 1.5× credit" or "NIFTY closes above 24,200">
Price abort: <e.g. "NIFTY 15-min close above <strike>">
Target exit: <time per §8.3>
```

Always show all 3 indexes if multiple are viable — user picks the best opportunity.

---

## Execution guidance (user places orders manually in Kotak app)

```
1. Confirm the structure and lot count with the user before they execute.
2. Execution sequence for credit spreads (NRML):
   a. BUY long leg first → confirm fill
   b. SELL short leg → confirm fill
   c. Note actual fill prices — they will differ from chain mid
3. After fills confirmed: report actual credit, recalculate stop in pts, set entry time in tread.md
```

---

## Update tread.md

After presenting analysis (before trades are executed), append:
- Gate results (all 4)
- Selected structure(s) with reasoning
- Sizing table shown to user
- "Awaiting user execution confirmation"

After user confirms fills: append actual entry prices and live trade parameters.
