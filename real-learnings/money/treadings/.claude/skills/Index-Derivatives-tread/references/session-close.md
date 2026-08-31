# session-close — Post-Session Wrap

Triggered when the user says "I closed the trade", "session is done", "wrap up", or after the final exit is confirmed. Closes the loop on all documentation, learning, and logging.

---

## Step 1: Pull final fills from Kotak

```
mcp__kotak-neo__get_order_book(sessionid=<session>)
mcp__kotak-neo__get_positions(sessionid=<session>)
```

Parse all orders for today:
- Filter by date (today's date in `Order Timestamp`)
- Identify entry fills (the original buys/sells)
- Identify exit fills (the close orders)
- Note any rejected orders (flag them in the log, don't include in P&L)

---

## Step 2: Calculate final P&L

For a credit spread:
```
Entry:
  sell_fill = average price of the sold leg (from Kotak order data)
  buy_fill  = average price of the bought leg
  credit_received = sell_fill - buy_fill

Exit:
  buy_back_fill = average price of the buyback (closing short)
  sell_out_fill = average price of the sell (closing long)
  cost_to_close = buy_back_fill - sell_out_fill

Gross P&L = (credit_received - cost_to_close) × lot_size × lots
```

**Charges estimate** (rough — user's actual brokerage statement is authoritative):
- STT: 0.10% on option sell-side (entry + exit sell legs only)
- Exchange: ~0.035% of turnover
- Brokerage: ₹20/order × number of filled orders
- GST 18% on brokerage
- Slippage: already captured in the fill vs chain mid difference

Net P&L = Gross P&L − estimated charges
% of capital = Net P&L ÷ ₹7,02,275 × 100

---

## Step 3: Update tread.md (exit section)

Append to today's tread.md:

```markdown
## <HH:MM> — EXIT

| Leg | Action | Avg Fill | Time |
|---|---|---|---|
| <short strike> CE | BUY (close short) | <price> | <time> |
| <long strike> CE | SELL (close long) | <price> | <time> |

NIFTY at exit: ~<price>

## FINAL P&L

| | Pts | ₹ |
|---|---|---|
| Entry credit | <X> | +₹<Y> |
| Exit cost | <X> | -₹<Y> |
| **Gross profit** | **<X>** | **+/-₹<Y>** |
| Est. charges | — | ~-₹<Z> |
| **Net P&L** | **<X>** | **+/-₹<Y>** |
| **% of ₹7.02L** | | **<X>%** |

MAE (worst mark): ₹<X> at <time> (spread <Y> pts)
MFE (best mark): ₹<X> at <time> (spread <Y> pts)
```

---

## Step 4: Write learning.md

This is non-negotiable. Even if the session was routine, write at least 3 bullet points. If it was a no-trade, still write what you observed.

Template:
```markdown
# <DD-MM-YYYY> — Learnings

## Trade: <structure> · <N> lots · Net +/-₹<X> (<Y>%)

### 1. <Lesson title — specific, not generic>
<What happened, why it matters, what to do differently>

### 2. <Next lesson>
...

### <If no trade>
### 1. <Why no trade — which gate blocked it>
<Reason code: Too dangerous / Too small / Too thin>
What condition would have changed the decision.
```

**Mandatory reflection prompts** (answer at least one):
- Did the market behave as the pre-session view predicted? Where did it diverge?
- Did any OI wall behave unexpectedly (built or unwound)?
- Was the sizing right? Would more or fewer lots have been better?
- Did the exit timing work? Should target or hard exit times be adjusted?
- What would you do differently entering this exact setup again?

---

## Step 5: Update mcp-usage-log.md §4

Open `docs/mcp-usage-log.md` and append a new row to the session log table (§4):

```
| <DD-Mon-YYYY> | 🟢/🟡/🔴 Kite | 🟢/🟡/🔴 Kotak | 🟢/🟡/🔴 Dhan | <what each was used for> | <Outcome + key finding> |
```

Outcome categories: `TRADE EXECUTED ✅ · NO TRADE (Too dangerous) · NO TRADE (Too small) · NO TRADE (Too thin)`

---

## Step 6: Append FII/DII data (if available)

If today's FII/DII F&O participant data was not already added in `analyse-today`:
- If user has it: append to `my-treads/fii_dii_data_2026.md` using the existing format
- If not: leave a placeholder `## <DD/MM/YYYY> - FII DII Data — PENDING` and remind the user

---

## Step 7: Session summary to chat

Present a clean session summary:

```
## <DD-MM-YYYY> — Session Summary

### Result
<Trade | No Trade>
<Structure if traded> · <Lots> · Net <+/-₹X> (<Y>%)

### Key decisions
1. <Gate or threshold that was decisive>
2. <Sizing or timing call>

### What was learned
<2-3 bullet points from learning.md>

### Files updated
- tread.md ✅
- learning.md ✅
- mcp-usage-log.md §4 ✅
- fii_dii_data_2026.md ✅ / ⏳ PENDING
```

---

## Step 8: Prompt for tomorrow's prep (if after 3:30 PM)

```
> Tomorrow's market view should be written after 3:30 PM today using post-close data.
> Run /Index-Derivatives-tread analyse-today tomorrow morning before 9:15 AM to recheck and update.
```
