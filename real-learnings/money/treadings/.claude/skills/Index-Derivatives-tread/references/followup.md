# followup — Monitoring a live position

**Loaded by:** `/Index-Derivatives-tread followup`
**Also load:** [`kill-switch.md`](kill-switch.md), [`entry-exit-orders.md`](entry-exit-orders.md), [`adjustments-are-closed.md`](adjustments-are-closed.md), [`dhan-api.md`](dhan-api.md), [`TRADING_CONSTANTS.md` §7–§8](../../../../TRADING_CONSTANTS.md)

---

## Step 1 — Pull live positions

```
mcp__kotak-neo__get_positions(sessionid=<session>)
```

Parse each open leg:
- Trading symbol → extract strike, option type (CE/PE), expiry
- Buy/Sell amount → calculate avg fill price
- IsPosition Open = true → still live

If no positions found: report "no open positions" and stop.

---

## Step 2 — Pull live market data (parallel)

**Primary: Dhan REST.** MCP OAuth binding fails mid-session; go straight to REST for rechecks. Full curl blocks: **[`dhan-api.md`](dhan-api.md) §REST API**.

**Also pull from Kite:**
```
mcp__kite__get_ltp: ["NSE:NIFTY 50", "NSE:INDIA VIX"]
mcp__kite__get_historical_data: last 2 hours of 15-min candles (for VWAP + kill switch M1)
```

⛔ **Never skip a check because a data source is down.** Two `get_quotes` calls give the leg prices; that is sufficient to run Steps 3 and 4, which are the ones that matter.

---

## Step 3 — Calculate current P&L

For a credit spread:
```
Entry credit = sell_price - buy_price (from Kotak position data)
Current cost to close = short_leg_LTP - long_leg_LTP
Current P&L = entry_credit - current_cost_to_close  (in pts)
Gross P&L = pts × lot_size × lots
Net P&L estimate = Gross P&L - exit charges estimate
```

---

## Step 4 — Check stop proximity

⚠️ **Divide by the stop DISTANCE, not the stop THRESHOLD.** The old formula made a fresh position read 37.5% buffer (🟡 Watch) and 🟢 Safe mathematically unreachable until profit target — every alarm was noise.

```
k               = 1.6                               [TRADING_CONSTANTS.md §8]
stop_threshold  = entry_credit × k                  ← the price the SL order triggers at
stop_distance   = entry_credit × (k − 1)            ← how far the spread can move before that
current_spread  = short_leg_LTP − long_leg_LTP

buffer_pts = stop_threshold − current_spread
BUFFER %   = buffer_pts / stop_distance × 100       ← denominator is the DISTANCE
```

**Sanity anchors — check these two before reporting:**
- At entry (`current_spread = credit`), BUFFER % = **100%**. A fresh position must read 🟢.
- At the stop (`current_spread = 1.6 × credit`), BUFFER % = **0%**. 🔴.
- Above 100% means the trade is in profit. Report the excess as capture, not as buffer.

**Look the resulting % up in the escalation table at [`TRADING_CONSTANTS.md` §8a](../../../../TRADING_CONSTANTS.md)** — Safe / Watch / Alert / Exit and the action for each. The bands are not restated here on purpose; a second copy is how the looser one wins on a losing day. If Alert or Exit fires, ⛔ **do not adjust** — see [`adjustments-are-closed.md`](adjustments-are-closed.md).

**Also report capture:** `capture = (entry_credit − current_spread) / entry_credit × 100%`. Target is **50%** ([`TRADING_CONSTANTS.md` §8](../../../../TRADING_CONSTANTS.md)) — one exit, no scaling, no trailing.

---

## Step 5 — Kill switch check

Run the **canonical three markers from [`kill-switch.md`](kill-switch.md)** at each scheduled recheck — M1 opening-range break, M2 VWAP one-sidedness, M3 OI confirming direction. Identical tests to `find-trade`, so the score means the same thing at 11:00 as it did at 9:40.

⛔ **VIX is NOT a kill-switch marker.** It is Go/No-Go row 1 and an exit trigger in Step 6.

⚠️ **M2 is permanently unmeasurable for cash indices** (Kite returns `volume: 0` for `BSE:SENSEX`). Log M2 as a gap; never score it green.

Report: `Kill switch: X of 3. [detail each, naming the observation]`

- **2/3 while the position is losing → EXIT.**
- **3/3 → EXIT at market regardless of P&L.**
- **0/3 means "not a trend day". It is NOT a reason to hold a loser** and says nothing about direction.

---

## Step 6 — OI wall check

**Baseline:** each strike's OI is compared to **its own `oi_day_high`**, never to the morning print or the prior check.

```
erosion = (oi_day_high − oi_now) / oi_day_high × 100%
```

⚠️ **Check-to-check differencing hides collapses.** On 01-Sep-2026 the 24,000 PE wall went 57.76M → 32.8M, **−43% in 50 minutes**. Measured between adjacent 30-min checks that reads as −17% per window and never crosses the trigger. Against `oi_day_high` it crosses at the first check.

The erosion threshold is [`TRADING_CONSTANTS.md` §8a](../../../../TRADING_CONSTANTS.md). Apply it as:

- Breached at the **SHORT strike** → 🔴 **EXIT.** Writers are covering.
- Breached at the *protective* wall (the one between spot and your short) → 🟠 Alert.
- Wall OI *rising* on the side you sold → confirming. Hold.

Report the day high alongside the current value so the erosion is visible.

---

## Step 7 — Recheck cadence

```
FIRST CHECK  = fill time + 30 min          ← not a fixed clock hour
THEN         = every 30 min, on the half hour
MIDDAY GATE  = 12:30 — if capture < 25% of credit, close. The day is not paying.
FINAL CHECK  = at the hard flat: 2:30 PM NIFTY/BANKNIFTY · 2:15 PM SENSEX
```
Times: [`TRADING_CONSTANTS.md` §7](../../../../TRADING_CONSTANTS.md).

⚠️ **The old fixed list (12:30 / 1:30 / 2:00 / 2:30) left a 165-minute unwatched window after a 9:45 entry.** Anchor to the fill, not the clock.

**A missed check is a violation.** If more than 45 minutes have passed since the last one, say so at the top of the report.

**The resting SL-LIMIT order is the protection — this cycle is not.** If any check finds no live stop order at the broker, that is a 🔴 and the instruction is: place it now, or close at market.

---

## Step 8 — Exit triggers

Exit now if **ANY** of:

| Trigger | Where the number lives | Detail |
|---|---|---|
| Buffer in the 🔴 band (Step 4) | TC §8a | Close at market; do not wait for the SL to fill |
| **Kill switch 2/3 and losing**, or **3/3 at any P&L** | [`kill-switch.md`](kill-switch.md) | — |
| Short-strike OI erosion past the trigger (Step 6) | TC §8a | The wall you sold against is going |
| VIX level or day-change past its limit, **while losing** | TC §6 rows 8–9 | Vol is repricing against a short-vol structure |
| Midday gate: capture below the floor at the midday time stop | TC §7 | The day is not paying; theta from here does not fund gamma risk |
| Sustained 15-min **close** through the short strike | TC §8a | Not a wick — consecutive closes |
| **No live SL order** and it cannot be placed | TC §8 | Close at market |

**Do not exit merely because the market is uncomfortable** — the list above is the evidence. But equally: **do not hold past one of these because the day "still looks fine".**

### ⚠️ BANNED as evidence that the thesis is broken

These are **not** exit triggers:

- Morning/intraday spread P&L — **a widened credit spread is a BETTER entry, not a broken thesis**
- The last three candles
- Kill switch 0/3 — it means "not a trend day", never "bullish" or "bearish"
- Any rule that did not fire

---

## Step 9 — First line of every recheck: is the stop ORDER live?

```
SL ORDER CHECK: order <id> on <short leg>, trigger ₹<X> — status?
  LIVE / "Trigger Pending"  → good, continue
  Not found / cancelled / rejected → 🔴 place it NOW, or close at market.
```

A price **alert** is not a substitute. On 01-Sep-2026 the ₹11.00 trigger was stated at 13:05 and the market reached ₹11.45 at 13:11 — **the move was seen.** Nothing was resting at the broker, so acting still required a decision under loss pressure; a 9th lot was added instead and the loss tripled.

---

## Step 10 — HARD RULE: no order may increase short exposure in a losing structure

**Full detail: [`adjustments-are-closed.md`](adjustments-are-closed.md).**

At any hour, on any day, while the structure is at a loss:
- **ALLOWED:** hold with the stop live, or exit
- ⛔ **FORBIDDEN:** add lots, sell more of the short, roll the short closer, average the credit, leg into a ratio

**On expiry day (0-DTE), only HOLD and EXIT exist.** §8.9's adjustment playbook is closed. Rolling a short ITM on expiry costs more than the original stop.

Breaking this is a **behavioural violation** → 5-session halt ([`TRADING_CONSTANTS.md` §12](../../../../TRADING_CONSTANTS.md)), **even if the trade closes profitable.**

When buffer is under 30% on expiry day, state it flatly — "buffer is X pts, W% of the stop distance" — then give **one** action. Not a menu.

---

## Step 11 — Report format

```
## <HH:MM> — Recheck   (last check <HH:MM>, <n> min ago)

SL ORDER: <order id> — LIVE / ⛔ NOT FOUND      ← first line, every time
<index>: <price> (Δ from last check)  |  VIX: <level> (<±%> from open)

Position mark-to-market:
| Leg | Entry | Last check | Now | Δ |
|-----|-------|-----------|-----|---|
| SHORT <strike> CE | <fill> | <prev> | <now> | <chg> |
| LONG  <strike> CE | <fill> | <prev> | <now> | <chg> |
| Spread (cost to close) | <entry cr> | <prev> | <now> | working/against |

Gross P&L: +/−₹<X>   Capture: <C>% of credit   (target 50%)
Stop: <threshold> pts · now <spread> pts · buffer <Z> pts = <W>% of stop distance → [🟢/🟡/🟠/🔴]
MAE so far: <worst spread seen> pts   MFE so far: <best> pts

OI watch (vs each strike's own day high):
| Strike | oi_day_high | Now | Erosion |
| <short strike> | <X>L | <Y>L | <−Z%> |

Kill switch: <N>/3  [<details>]

Verdict: HOLD / PREPARE EXIT / EXIT NOW
```

**Track MAE and MFE from the first check onward** — they are mandatory log fields ([`trade-log.md`](trade-log.md)) and cannot be reconstructed after the close.

---

## Step 12 — Update tread.md

Append every recheck result to today's tread.md (chronological log). Use the format above. Never overwrite — always append.

---

## Step 13 — Exit execution (when the time comes)

**Full order sequence: [`entry-exit-orders.md`](entry-exit-orders.md) §Stopping out.**

Summary for the user:
```
0. CANCEL the resting SL order first — otherwise it can fire after you close manually.
1. BUY BACK THE SHORT LEG at market ask — always first.
2. SELL the long leg at market bid — immediately after.
3. Note both actual fill prices.
4. Report to Claude for final P&L.
```

⚠️ **Sequence is not optional.** Closing the long first leaves a naked short. Budget **2.0 pts/leg slippage on a stop exit** ([`TRADING_CONSTANTS.md` §13](../../../../TRADING_CONSTANTS.md)), against 0.5 pts/leg on a planned one. (01-Sep-2026 observed 23.85 pts on a panicked manual close.)

After the user confirms exit fills → immediately run `/Index-Derivatives-tread session-close`.
