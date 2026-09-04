# session-close — Post-session wrap and documentation

**Loaded by:** `/Index-Derivatives-tread session-close`
**Also load:** [`trade-log.md`](trade-log.md), [`no-trade.md`](no-trade.md), [`TRADING_CONSTANTS.md` §2–§3, §7, §12–§15](../../../../TRADING_CONSTANTS.md)

Closes the loop on all documentation, learning, and logging. Runs after the final exit is confirmed, OR after a no-trade decision.

---

## Step 1 — Pull final fills from Kotak

```
mcp__kotak-neo__get_order_book(sessionid=<session>)
mcp__kotak-neo__get_positions(sessionid=<session>)
```

Parse all orders for today:
- Filter by date (today's date in `Order Timestamp`)
- Identify entry fills (the original buys/sells)
- Identify exit fills (the close orders)
- Note any rejected orders (flag them in the log, don't include in P&L)

**If this was a no-trade day:** skip to Step 5, using the **[`no-trade.md`](no-trade.md)** template.

---

## Step 2 — COMPLIANCE AUDIT (run before P&L is discussed)

⚠️ **Violations are reported ABOVE P&L, always.** Violations lead; P&L lags. A profitable trade that broke a rule is a worse outcome than a losing trade that followed every one.

```
| # | Check | Y/N |
|---|---|---|
| 1 | Was a resting SL-LIMIT order on the SHORT LEG placed within 90 seconds of the fill? Order ID? |  |
| 2 | Did the stop ever move? (DOWN is fine; AWAY from price is a violation) |  |
| 3 | Was a triggered stop executed within 5 minutes? |  |
| 4 | Was any order placed that INCREASED short exposure while at a loss? |  |
| 5 | Was the position flat by the hard flat time **of its declared final session**? (TC §7 — intraday trades: same day. Multi-session holds: the last session of the declared period.) |  |
| 6 | Was this the only structure of the day? |  |
| 7 | Was the size within lots = min(cap A, cap B)? |  |
| 8 | Were all five gates written in tread.md BEFORE any strike was quoted? |  |
```

Hard flat times: [`TRADING_CONSTANTS.md` §7](../../../../TRADING_CONSTANTS.md). Currently: **2:30 PM NIFTY/BANKNIFTY · 2:15 PM SENSEX** — applied on the **declared final session** (TC §1a).

**If a multi-session hold is still open, the session does not close the trade.** Write the session's `learning.md` as normal, record the mark-to-market and that the hold continues, and re-verify the declared exit date. ⛔ Do **not** re-declare it — extending an open hold is a §12 violation (g).

**Any of rows 1–6 failing = a behavioural violation → 5-session trading halt** ([`TRADING_CONSTANTS.md` §12](../../../../TRADING_CONSTANTS.md)), **even if the trade was profitable.** State the halt plainly and name its end date. Do not soften it because the day made money.

**Running count:** report `Violations this month: <n>` in every session summary.

---

## Step 3 — Calculate final P&L

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

Full friction table: [`TRADING_CONSTANTS.md` §13](../../../../TRADING_CONSTANTS.md).

Net P&L = Gross P&L − estimated charges
% of capital = Net P&L ÷ <capital> × 100
   ★ Read <capital> from [`TRADING_CONSTANTS.md` §1](../../../../TRADING_CONSTANTS.md) at the moment
     you compute — the documented figure is under a PENDING USER RULING and may not match the
     live Kotak `get_limits` read. Never hardcode it here.

---

## Step 4 — Update tread.md (exit section)

Append to today's tread.md:

```markdown
## <HH:MM> — EXIT

| Leg | Action | Avg Fill | Time |
|---|---|---|---|
| <short strike> CE | BUY (close short) | <price> | <time> |
| <long strike> CE | SELL (close long) | <price> | <time> |

<INDEX> at exit: ~<price>

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

Exit reason: TARGET | STOP | TIME | VIOLATION      ← closed vocabulary, pick exactly one
```

Exit code detail: [`trade-log.md`](trade-log.md).

---

## Step 5 — Write learning.md

**This is non-negotiable.** Every session produces a `learning.md` — wins AND no-trades. Even if the session was routine, write at least 3 bullet points.

Template:
```markdown
# <DD-MM-YYYY> — Learnings

## Trade: <structure> · <N> lots · Net +/-₹<X> (<Y>%)
OR
## No trade — <reason code: Too dangerous / Too small / Too thin / UNPAID>

### 1. <Lesson title — specific, not generic>
<What happened, why it matters, what to do differently>

### 2. <Next lesson>
...
```

**Mandatory reflection prompts** (answer at least one):
- Did the market behave as the pre-session view predicted? Where did it diverge?
- Did any OI wall behave unexpectedly (built or unwound vs its `oi_day_high`)?
- Was every gate honestly scored, or was a borderline reading nudged?
- What would you do differently entering this exact setup again?

⛔ **Do not ask "would more lots have been better?"** Hindsight always says yes on a winner. That question is how the 31-Aug "size by conviction" rewrite happened off a single observation in the winning direction. The sizing rule is the formula; it is reviewed on 20+ trades at month end, never on today's outcome.

⛔ **Never loosen a filter mid-month**, and never as a reaction to one session. Fewer than 4 trades in a month is the only signal that filters are too tight — review it at month end.

> **Half the `learning.md` files in this repo are 0 bytes.** The compounding mechanism is currently off for half of all sessions. A short file that always gets written beats a rich one that does not.

---

## Step 6 — Update mcp-usage-log.md §4

Open `docs/mcp-usage-log.md` and append a new row to the session log table (§4):

```
| <DD-Mon-YYYY> | 🟢/🟡/🔴 Kite | 🟢/🟡/🔴 Kotak | 🟢/🟡/🔴 Dhan | <what each was used for> | <Outcome + key finding> |
```

Outcome categories: `TRADE EXECUTED ✅ · NO TRADE (Too dangerous) · NO TRADE (Too small) · NO TRADE (Too thin) · NO TRADE (UNPAID)`

**No-trade days get the same row and the same discipline as traded days.** They are ~75% of sessions and are the bulk of the record.

---

## Step 7 — Append FII/DII data (if available)

If today's FII/DII F&O participant data was not already added in `analyse-today`:
- If user has it: append to `my-treads/fii_dii_data_2026.md` using the existing format
- If not: leave a placeholder `## <DD/MM/YYYY> - FII DII Data — PENDING` and remind the user

---

## Step 8 — Neutral scoring of no-trade candidates (mandatory)

**Score at the mandated hard flat time** ([`TRADING_CONSTANTS.md` §7](../../../../TRADING_CONSTANTS.md)), never at a mid-session snapshot. Report MAE / exit-mark / MFE **at max permitted size — including for candidates you rejected in analysis and never wrote up.**

Otherwise the record cannot tell a good veto from a timid one.

```markdown
## <HH:MM> — Neutral scoring of declined candidates

| Structure | Entry mark | Hard-flat mark | Deployed size | Gross P&L | MAE | MFE |
|---|---|---|---|---|---|---|
| NIFTY 24200/24250 BPS | 10.5 pts | 6.2 pts | 4 lots | +₹1,118 | −₹78 | +₹1,430 |
| SENSEX 80500/80600 BPS | 21.3 pts | 15.8 pts | 6 lots | +₹660 | −₹240 | +₹840 |

Note: these are the candidates REJECTED during analysis and never written up in the tread log.
```

**If the session is being wrapped early, say the score is pending and come back for it.**

---

## Step 9 — Session summary to chat

Present a clean session summary:

```
## <DD-MM-YYYY> — Session Summary

### Compliance
Violations today: <n>   ·   Violations this month: <n>   ·   Halt in force until: <date | none>

### Result
<Trade | No Trade>
<Structure if traded> · <Lots> · Exit reason <TARGET|STOP|TIME|VIOLATION> · Net <+/-₹X> (<Y>%)
Month to date: ₹<X> against the monthly target ([`TRADING_CONSTANTS.md` §2](../../../../TRADING_CONSTANTS.md)).

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

Monthly target: [`TRADING_CONSTANTS.md` §2](../../../../TRADING_CONSTANTS.md).

---

## Step 10 — If the session earned a KB amendment

**The change must land in:**
- The target section
- Its parent index block
- The `§4` session row in `docs/mcp-usage-log.md`
- The day's `learning.md`
- **If it changes the routing:** also `SKILL.md`'s table and `docs/repo-map.md`

⛔ **Numbers go to [`TRADING_CONSTANTS.md`](../../../../TRADING_CONSTANTS.md) and nowhere else — never mirror a fact into `CLAUDE.md`.**

---

## Step 11 — Prompt for tomorrow's prep (if after 3:30 PM)

```
> Tomorrow's market view should be written after 3:30 PM today using post-close data.
> Run /Index-Derivatives-tread analyse-today tomorrow morning before 9:15 AM to recheck and update.
```
