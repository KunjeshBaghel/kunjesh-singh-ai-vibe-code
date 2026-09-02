# followup — Live Position Monitoring

Use whenever the user says "recheck", "how is my trade", "check positions", or on the schedule below. Fast cycle — all data fetches in parallel.

> ★ **Every number in this file is quoted from [`TRADING_CONSTANTS.md`](../../../../TRADING_CONSTANTS.md). If they ever disagree, that file wins and this one is a bug.**

---

## Step 0: The monitoring schedule — every 30 minutes from the fill

```
FIRST CHECK  = fill time + 30 min          ← not a fixed clock hour
THEN         = every 30 min, on the half hour
MIDDAY GATE  = 12:30 — if capture < 25% of credit, close. The day is not paying.
FINAL CHECK  = at the hard flat: 2:30 PM NIFTY/BANKNIFTY · 2:15 PM SENSEX
```

⚠️ **The old fixed list (12:30 / 1:30 / 2:00 / 2:30) left a 165-minute unwatched window after a 9:45 entry**, against a documented 30-minute re-check rule. The entry window is 9:30–11:15, so the first check is often before 12:30. Anchor to the fill, not the clock.

**A missed check is a violation.** If more than 45 minutes have passed since the last one, say so at the top of the report.

**The resting SL-LIMIT order is the protection — this cycle is not.** If any check finds no live stop order at the broker, that is a 🔴 and the instruction is: place it now, or close at market.

---

## Step 1: Pull live positions from Kotak Neo

```
mcp__kotak-neo__get_positions(sessionid=<session>)
```

Parse each open leg:
- Trading symbol → extract strike, option type (CE/PE), expiry
- Buy/Sell amount → calculate avg fill price
- IsPosition Open = true → still live

If no positions found: report "no open positions" and stop.

---

## Step 2: Pull live prices for each leg (parallel)

**Primary: Dhan REST** — the MCP's OAuth binding is unreliable and typically dead by mid-session, which is exactly when this cycle runs. Go straight to REST for rechecks:
```bash
source .broker_creds
curl -s -X POST "https://api.dhan.co/v2/optionchain" \
  -H "access-token: $DHAN_ACCESS_TOKEN" \
  -H "client-id: $DHAN_CLIENT_ID" \
  -H "Content-Type: application/json" \
  -d '{"UnderlyingScrip":<id>,"UnderlyingSeg":"IDX_I","Expiry":"<YYYY-MM-DD>"}'
# Scrip IDs: NIFTY=13 · BANKNIFTY=25 · SENSEX=51   (field is UnderlyingSeg, not UnderlyingSegment)
```

Fallback: Dhan MCP `market_data_agent_tool action=optionchain`. Second fallback: Kite `get_quotes` on the two legs directly — enough for P&L and the stop check even with no chain.

⛔ **Never skip a scheduled check because a data source is down.** Two `get_quotes` calls give the leg prices; that is sufficient to run Steps 3 and 4, which are the ones that matter.

Also pull from Kite:
```
mcp__kite__get_ltp: ["NSE:NIFTY 50", "NSE:INDIA VIX"]
mcp__kite__get_historical_data: last 2 15-min candles
```

---

## Step 3: Calculate current P&L

For a credit spread:
```
Entry credit = sell_price - buy_price (from Kotak position data)
Current cost to close = short_leg_LTP - long_leg_LTP
Current P&L = entry_credit - current_cost_to_close  (in pts)
Gross P&L = pts × lot_size × lots
Net P&L estimate = Gross P&L - exit charges estimate
```

---

## Step 4: Check stop proximity

⚠️ **Divide by the stop DISTANCE, not the stop THRESHOLD.** The old formula used the threshold, which made a freshly-opened position report 37.5% buffer — 🟡 Watch — and made 🟢 Safe mathematically unreachable until the position was already at its profit target. On expiry day it escalated on a ~2-point tick. Every alarm it raised was noise, which is the fastest way to train someone to ignore alarms.

```
k               = 1.6
stop_threshold  = entry_credit × k              ← the price the SL order triggers at
stop_distance   = entry_credit × (k − 1)        ← how far the spread can move before that
current_spread  = short_leg_LTP − long_leg_LTP

buffer_pts = stop_threshold − current_spread
BUFFER %   = buffer_pts / stop_distance × 100   ← denominator is the DISTANCE
```

**Sanity anchors — check these two before reporting:**
- At entry (`current_spread = credit`), BUFFER % = **100%**. A fresh position must read 100% / 🟢.
- At the stop (`current_spread = 1.6 × credit`), BUFFER % = **0%**. 🔴.
- Above 100% means the trade is in profit. Report the excess as capture, not as buffer.

| Buffer % | State | Action |
|---|---|---|
| > 60% | 🟢 Safe | Hold. Resting stop does the work. |
| 30–60% | 🟡 Watch | Hold. Note it. Confirm the SL order is still live. |
| 15–30% | 🟠 Alert | The stop is close. Do not adjust the structure — do not widen, roll or add. Prepare to close. |
| < 15% | 🔴 Exit | Close at market now. Do not wait the last few points for the SL to fill. |

Report: `Stop at X pts · now Y pts · buffer Z pts = W% of the 0.6×credit stop distance → [state]`

**Also report capture:** `capture = (entry_credit − current_spread) / entry_credit × 100%`. Target is **50%** — one exit, no scaling out, no trailing.

---

## Step 5: §8.13 Kill switch check (at each scheduled recheck)

Use the **canonical marker definitions from `find-trade.md` Gate 3** — identical tests, so the score means the same thing at 11:00 as it did at 9:40:

1. **Opening-range break** — two consecutive 15-min *closes* outside the 9:15–9:45 OR high/low. A wick is not a break.
2. **VWAP one-sidedness** — price one side of VWAP ≥ 45 min with no close through it, VWAP sloping the same way.
3. **OI confirming direction** — price and OI aligned per the §8.13 matrix, measured against `oi_day_high` (Step 6).

> **VIX is NOT a kill-switch marker.** It is Go/No-Go row 1 and an exit trigger in Step 8. Counting it here silently made this a 4-marker test scored out of 3.

Report: `Kill switch: X of 3. [detail each, naming the observation]`

- **2/3 while the position is losing → EXIT.**
- **3/3 → EXIT at market regardless of P&L.**
- **0/3 means "not a trend day". It is NOT a reason to hold a loser** and says nothing about direction.

---

## Step 6: OI wall check (§8.7.4) — baseline is `oi_day_high`, always

**One baseline, used everywhere:** each strike's OI is compared to **its own `oi_day_high`**, never to the morning print, the prior check, or yesterday's close.

```
erosion = (oi_day_high − oi_now) / oi_day_high × 100%
```

⚠️ **Check-to-check differencing hides collapses.** On 01-Sep-2026 the 24,000 PE wall went 57.76M → 32.8M, **−43% in 50 minutes**. Measured between adjacent 30-min checks that reads as roughly −17% per window and never crosses a −20% trigger — the signal was present the whole time and the framing hid it. Against `oi_day_high` it crosses at the first check.

- **Erosion > 20% at the SHORT strike → 🔴 EXIT.** Writers are covering; the wall you sold against is going.
- Erosion > 20% at the *protective* wall (the one between spot and your short) → 🟠 Alert.
- Wall OI *rising* on the side you sold → confirming. Hold.

Report the day high alongside the current value so the erosion is visible, not just the delta since the last look.

---

## Step 7: Report format

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

**Track MAE and MFE from the first check onward** — they are mandatory fields in the trade log and cannot be reconstructed after the close.

---

## Step 8: When to recommend exit before target time

Exit now if ANY of:
- **Buffer < 15%** (Step 4) — close at market; do not wait the last points for the SL to fill
- **Kill switch 2/3 and the position is losing**, or **3/3 at any P&L**
- **Short-strike OI erosion > 20% from its own `oi_day_high`** — the wall you sold against is going (§8.7.4)
- **VIX ≥ 20, or up > 8% on the session**, while the position is losing
- **12:30 midday gate: capture < 25% of credit → close.** The day is not paying and theta from here does not fund the gamma risk
- Sustained 15-min **close** through the short strike
- **No live SL order at the broker** and it cannot be placed → close at market

**Do not exit merely because the market is uncomfortable** — the list above is the evidence. But equally: **do not hold past one of these because the day "still looks fine".** Each line is a trigger, not a topic.

### ⚠️ FIRST LINE of every recheck — is the stop ORDER live?

```
SL ORDER CHECK: order <id> on <short leg>, trigger ₹<X> — status?
  LIVE / "Trigger Pending"  → good, continue
  Not found / cancelled / rejected → 🔴 place it NOW, or close the structure at market.
                                      An unprotected short is not a position we hold.
```

A price **alert** is not a substitute and never satisfies this check. On 01-Sep-2026 the ₹11.00 trigger on the 24,000 PE was stated at 13:05 and the market reached ₹11.45 at 13:11 — **the move was seen.** Nothing was resting at the broker, so acting still required a decision under loss pressure; a 9th lot was added instead and the loss tripled. The order is the protection; the human is the fallback, not the mechanism.

### ⚠️ HARD RULE — no order may increase short exposure in a losing structure

At any hour, on any day, while the structure is at a loss:
- **ALLOWED:** hold with the stop live, or exit
- ⛔ **FORBIDDEN:** add lots, sell more of the short, roll the short closer, average the credit, leg into a ratio

**§8.9's adjustment playbook is CLOSED on expiry day** — only HOLD and EXIT exist. Rolling a short ITM on expiry costs more than the original stop, and gamma is at its maximum.

Breaking this is a **behavioural violation** → 5-session halt per [`TRADING_CONSTANTS.md` §12](../../../../TRADING_CONSTANTS.md), **even if the trade closes profitable.** So is: not executing a triggered stop within 5 minutes, moving a stop away from price, holding past the hard flat, or running without a live SL order.

When buffer is under 30% on expiry day, state it flatly — "buffer is X pts, W% of the stop distance" — then give **one** action. Not a menu.

---

## Step 9: Update tread.md

Append every recheck result to today's tread.md (chronological log). Use the format above. Never overwrite — always append.

---

## Exit execution (when the time comes)

Remind the user of the sequence:
```
0. CANCEL the resting SL order first — otherwise it can fire after you have closed
   manually and leave you naked long the wrong leg.
1. BUY BACK THE SHORT LEG at market ask — always first. This is the leg with the risk.
2. SELL the long leg at market bid — immediately after.
3. Note both actual fill prices.
4. Report to Claude for final P&L.
```

⚠️ **Sequence is not optional.** Closing the long first leaves a naked short — briefly, in a market that is moving, which is why you are exiting. Budget **2.0 pts/leg slippage on a stop exit** (01-Sep-2026 observed 23.85 pts on a panicked manual close), against 0.5 pts/leg on a planned one.

Hard flat: **2:30 PM NIFTY/BANKNIFTY · 2:15 PM SENSEX.** Never into the 3:15 PM CAS. There is no second, later "hard" time — the two-tier target/hard scheme has been deleted.

After the user confirms exit fills → immediately run `session-close`.
