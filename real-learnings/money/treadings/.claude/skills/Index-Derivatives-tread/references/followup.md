# followup — Live Position Monitoring

Use whenever the user says "recheck", "how is my trade", "check positions", or at scheduled intervals (12:30, 1:30, 2:00, 2:30). Fast cycle — all data fetches in parallel.

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

From Dhan option chain (fastest for full context):
```
mcp__dhan__market_data_agent_tool action=optionchain
{"UnderlyingScrip": 13, "UnderlyingSeg": "IDX_I", "Expiry": "<expiry>"}
```

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

```
Stop threshold = entry_credit × k  (k=1.5 default)
Current spread = short_leg_LTP - long_leg_LTP
Buffer = stop_threshold - current_spread
Buffer % = buffer / stop_threshold × 100
```

Report: "Stop at X pts · Current Y pts · Buffer Z pts (W% of stop)"

Urgency levels:
- Buffer > 50%: 🟢 Safe — hold
- Buffer 25-50%: 🟡 Watch — tighten attention
- Buffer 10-25%: 🟠 Alert — prepare to exit
- Buffer < 10%: 🔴 Exit immediately

---

## Step 5: §8.13 Kill switch check (at each scheduled recheck)

From the latest candles:
1. **ORH/ORL**: Has price broken the opening range and held outside it for 2+ candles?
2. **VIX**: Is it rising sharply (+5% from session open)? If yes and price is moving against us?
3. **OI shift**: Compare OI at the short strike now vs morning print (from Dhan chain)
   - If short strike OI is falling fast → writers covering → wall weakening

Report: "Kill switch: X of 3 markers. [Detail each]"

---

## Step 6: OI wall check (§8.7.4)

Check the OI at the put wall (below current price) and call wall (above):
```
If put wall OI is FALLING while price approaches it → floor being removed → bearish signal
If call wall OI is RISING while price approaches it → resistance strengthening → good for bear call
```

Compare current OI vs the OI from the prior check (note "OI at 11:00 was X, now Y = ΔZ").

---

## Step 7: Report format

```
## <HH:MM> — Recheck

NIFTY: <price> (Δ from last check)  |  VIX: <level>

Position mark-to-market:
| Leg | Entry | Last check | Now | Δ |
|-----|-------|-----------|-----|---|
| SHORT <strike> CE | <fill> | <prev> | <now> | <chg> |
| LONG  <strike> CE | <fill> | <prev> | <now> | <chg> |
| Spread (cost to close) | <entry cr> | <prev> | <now> | working/against |

Gross P&L: +/-₹<X>  (~<Y>% of ₹<capital>)
Stop: <threshold> pts · Buffer: <Z> pts (<W>%) → [SAFE/WATCH/ALERT/EXIT]

OI watch:
| Strike | Session open | Now | Change |
| <short strike> | <X>L | <Y>L | <Δ> |

Kill switch: <N>/3  [<details>]

Verdict: HOLD / PREPARE EXIT / EXIT NOW
```

---

## Step 8: When to recommend exit before target time

Exit now if ANY of:
- Kill switch fires 2+ of 3 markers AND position is losing
- VIX spikes above 13.0 and expanding while our position is losing
- Short strike OI falls >15% in one 20-min window (wall collapsing — §8.7.4)
- Spread reaches 85% of stop threshold (not worth risking the last 15%)
- Price makes a sustained 15-min close THROUGH the short strike

**Do not recommend early exit just because the market is uncomfortable.** Only exit when the risk evidence warrants it.

---

## Step 9: Update tread.md

Append every recheck result to today's tread.md (chronological log). Use the format above. Never overwrite — always append.

---

## Exit execution (when the time comes)

Remind user of the sequence:
```
1. BUY back the short leg (24,200 CE) at market ask — place first
2. SELL the long leg (24,400 CE) at market bid — place immediately after
3. Note both actual fill prices
4. Report to Claude for final P&L calculation
```

After user confirms exit fills → immediately run `session-close`.
