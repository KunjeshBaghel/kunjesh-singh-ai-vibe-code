# find-trade — Structure selection and sizing

**Loaded by:** `/Index-Derivatives-tread find-trade`

**Also load:** [`gates.md`](gates.md) · [`check-expiry.md`](check-expiry.md) · [`basis-check.md`](basis-check.md) · [`kill-switch.md`](kill-switch.md) · [`dhan-api.md`](dhan-api.md) · [`size-it.md`](size-it.md) · [`entry-exit-orders.md`](entry-exit-orders.md) · [`trade-log.md`](trade-log.md) · [`TRADING_CONSTANTS.md`](../../../../TRADING_CONSTANTS.md)

Runs after `analyse-today`. Requires completed `market_view.md`. Follows gates strictly — never jumps to structure before all clear.

---

## Pre-check: hard preconditions

Read `my-treads/<Month>/<DD-MM-YYYY>/<DD-MM-YYYY>-market_view.md` and verify **all** of:

```
□ Five-view classification with HH:MM timestamp < 60 min old
□ Literal `GATE 5 INPUTS` block with all six numbers (FII/Pro × CE/PE/FUT)
□ Nearest expiry + session count for all 3 indexes
□ Basis line per index
□ Key support/resistance levels
```

⛔ **ANY absent: STOP.** Say `market_view.md incomplete — <which item>. Run analyse-today first.` Do not derive inline. On 02-Sep inline re-derivation missed FII's 93,282 net short calls.

---

## The five gates

See [`gates.md`](gates.md) for full definitions. Run all five, in order. Each takes ~2 min.

**Gate 1 · Feasibility** — fetch expiries (see [`check-expiry.md`](check-expiry.md)), count sessions (TC §6 row 1). Sessions ≥3 → NO TRADE on that index. Quote capital at risk when out of reach, not the shortfall.

**Gate 2 · Basis** — see [`basis-check.md`](basis-check.md). `F = K+C−P` at 3–4 strikes, basis > 0.1% → delta band unreliable. **★ Then run realised-vs-implied BEFORE pricing any strike** (added 03-Sep-2026): realised > implied → VRP negative, no credit structure is paid, STOP.

**Gate 3 · Kill switch** — see [`kill-switch.md`](kill-switch.md). 0/3 = not a trend day (proceed). 1/3 = elevated caution. 2/3 = no new position. 3/3 = ABORT. ⛔ 0/3 NEVER means "bullish" and is never a reason to HOLD.

**Gate 4 · Go/No-Go** — point-scored per TC §6 row 11. SCORE = (2 × RED) + (1 × YELLOW). SCORE ≥4 → SIT OUT. Disjoint inputs. Blank row = YELLOW. Automatic blockers (don't count toward score): no five-view · undefined max loss · no live SL order · Gate 5 not written.

**Gate 5 · Structure↔View↔Participants** — see [`gates.md`](gates.md) §5. Restate five-view WITH TIMESTAMP. ⛔ Bull Put FORBIDDEN under bearish views. ⛔ Bear Call FORBIDDEN under bullish. Then the participant test: **the T-1 vs T-2 CHANGE in net OI**, FII first, Pro veto-only, limits from TC §9. ΔCE over limit ⛔ Bull Put · ΔPE over limit ⛔ Bear Call · both ⛔ NO TRADE · below = SILENCE. **Gate 5 forbids, never authorises.** Write 5A sentence and 5B table into `tread.md` BEFORE quoting a strike.

---

## ★ Always screen all 3 indexes

**NIFTY 50 (NSE, Tue) + BANKNIFTY (NSE, monthly only) + SENSEX (BSE, Thu).** Never analyse only one when looking for trade positions. Compare all three before picking best opportunity.

BANKNIFTY fails Gate 1 by construction on all but final ~2 sessions. State `BANKNIFTY: N sessions → Gate 1 ⛔, excluded` in one line; do not price. ⛔ Never the fallback when NIFTY+SENSEX blocked — that is a **no-trade day**.

---

## Fetch full option chain

See [`dhan-api.md`](dhan-api.md) for REST curl blocks (primary path) and MCP fallback.

Extract:
- OI at 5 strikes above (call walls), 5 below (put walls)
- ATM straddle at parity forward F
- Bid/ask spreads at candidate short strikes

---

## Entry filters — all of them, on every candidate

See TC §6 for the full list and thresholds. Summary:

```
□ sessions_to_expiry ≤ 2
□ c/W ≥ 15% (20%+ preferred) — TC §6 row 2
□ net credit at chosen size ≥ the floor — TC §6 row 3
□ k × credit < width   (k from TC §4)
□ noise floor (see below)
□ bid-ask ≤ 15% of credit
□ depth ≥ 5× lots
□ VIX < 20 and change ≤ +8%
□ basis within 0.1% or §8.7.3 used
□ ★ stop's spot level OUTSIDE today's traded range
```

---

## ★ §8.11.7 Noise floor — spread-based, run it

```
credit        = short_premium − long_premium
stop_distance = (k − 1) × credit    (k from TC §4)

spread_swing  = max over last 3 completed 30-min bars of:
                  (short_high − long_high) − (short_low − long_low)    ← intra-bar, both legs

⛔ stop_distance < 1.5 × spread_swing  →  NO TRADE at any size
```

**Pull 30-min bars for BOTH LEGS via Kite `get_historical_data` and price the SPREAD at each bar's index extremes.** Do not proxy with index range. Opening gap bar excluded. ≥1.5× passes; <1.5× fails — no threshold band.

**03-Sep evidence:** real legs gave 16.30-pt swing → 0.92× (FAIL). Index proxy gave ~11 pts → 1.35× (would have passed). The proxy would have passed the trade.

---

## ★ Score candidate strikes against day's HIGH/LOW, never spot

A stop inside the day's realised range is a stop the tape already hit once. 03-Sep: from spot those stops looked like 160–170 pt cushions.

---

## ★ When the squeeze IS the answer

**When credit floor (TC §6 row 3) and c/W floor (TC §6 row 2) squeeze from opposite directions with no strike between them, stop pricing — that squeeze IS the answer.** Faster read than testing six structures.

---

## Derive stop's SPOT level from chain — HARD GATE

Premium stop is the trigger, but user needs to know *where index goes* for it to fire. Estimating from two intraday observations gives wrong answers (02-Sep: quoted 76,870; true ~76,650 — 220-pt error).

**Permitted arithmetic (vertical-spread relation on chain prices, not Black-Scholes):**
```
Δ(K) ≈ −[ C(K+100) − C(K−100) ] / 200        # from adjacent strikes
spread_delta = Δ(short) − Δ(long)
spot_move_to_stop = stop_distance / spread_delta
stop_spot_level   = spot ± spot_move          # add for call spread, subtract for put
```

⛔ **If `stop_spot_level` INSIDE today's high–low: NO TRADE.** Market demonstrated it can reach that level without doing anything unusual. Stronger than noise floor (uses realised range, not estimate).

Gamma puts true level slightly further, so quote as band and use **near** edge for gate.

---

## ⚠️ On expiry day (0-DTE) adjustments are CLOSED

See [`adjustments-are-closed.md`](adjustments-are-closed.md). **Only two permitted actions once in trade: HOLD or EXIT.** §8.9 adjustment playbook applies **only** to 2+ DTE (which Gate 1 rarely permits). In practice §8.9 is almost never the answer.

---

## Present ONE structure with ONE lot count

For single best candidate clearing all gates, all filters, noise floor.

⛔ **Do not present sizing "options".** Conservative/Standard/Aggressive menu was the 01-Sep loss mechanism. The formula returns one number (see [`size-it.md`](size-it.md)). Quote that number. Less is always allowed; more is not.

**Present in this order, always:** **max profit → breakeven → structural max loss → planned stop → lots.** Never quote lot count before max loss.

```
Structure: <type> <short>/<long>  Expiry: <date>  (sessions: <n>)
Net credit: <X> pts  |  Width: <Y> pts  |  c/W = <X/Y>%  |  Short <Z> pts OTM from F

  MAX PROFIT       = credit         = <X> pts      = ₹<X×lot>/lot
  BREAKEVEN        = short ± credit = <level>
  STRUCTURAL MAX LOSS = width − credit = <Y−X> pts = ₹<(Y−X)×lot>/lot
        ← what you lose if stop never executes. Cap: TC §3
  PLANNED STOP (k from TC §4) = (k−1) × credit = <pts> = ₹<..>/lot
        ← what you intend to lose. Cap: TC §3
  Stop's SPOT level ≈ <level>   (today's range: <low>–<high>. Outside? YES/NO)

Sizing — see [`size-it.md`](size-it.md):
  lots_A = floor( [TC §3 structural cap] ÷ structural_max_loss/lot )   = <A>
  lots_B = floor( [TC §3 planned cap] ÷ planned_stop/lot )             = <B>
  LOTS   = min(A, B)                                                    = <N>
  ⛔ N < 2 → narrow width, recompute. Still < 2 → NO TRADE.

  At <N> lots:  max profit ₹<..>  ·  structural max loss ₹<..>  ·  planned stop ₹<..>
  Charges ≈ ₹150 round trip. Net at target (TC §8) ≈ ₹<..>

Stop ORDER — see [`entry-exit-orders.md`](entry-exit-orders.md):
  SL-LIMIT BUY-TO-CLOSE on SHORT LEG ONLY
  Trigger = <short_entry> + k × <net credit/lot pts>         (verify against chain)
  Limit   = trigger + max(12%, <2 pts NIFTY/BN | 5 pts SENSEX>)
  ⛔ Never SL-M on option. Never stop the long leg.
Price abort: <e.g. "15-min close beyond <short>">
Hard flat: <from TC §7> — never into CAS
```

Always show all 3 indexes if multiple viable — user picks best.

---

## Execution guidance

Manual in Kotak Neo app. See [`entry-exit-orders.md`](entry-exit-orders.md) for full sequence.

```
1. Confirm structure + lot count with user before they execute
2. BUY long leg first → confirm fill
3. SELL short leg → confirm fill
4. Note actual fill prices
5. After fills: report actual credit, recalculate stop, set entry time
```

### ⚠️ MANDATORY within 90 seconds — stop is ORDER not alert

See [`entry-exit-orders.md`](entry-exit-orders.md) for the exact order parameters.

```
ACTION REQUIRED — place RESTING order in Kotak app NOW:

  Type:    SL-LIMIT, BUY TO CLOSE, SHORT LEG ONLY
  Symbol:  [short leg]
  Qty:     [lots]
  Trigger: [short_entry + k × net credit/lot pts]   (k from TC §4)
  Limit:   [trigger + max(12%, 2 pts NIFTY/BN | 5 pts SENSEX)]

  ⛔ NEVER SL-M on option. Never stop long leg.

Then report ORDER ID and "Trigger Pending".
No order ID = no position. Cannot place → close at market.
```

Two price alerts on INDEX (not instead): at stop's spot level, at price-abort level. Notification only; resting order is protection.

**Why order not alert:** 01-Sep trigger was stated (₹11.00), market reached it (₹11.45), **move was observed**, but nothing resting at broker. Exiting required decision under loss pressure; decision not made. −₹1,800 became −₹15,564. An alert delegates the hard part back to the person who freezes there.

---

## ⛔ HARD RULE — no order may increase short exposure in losing structure

On any day, any hour, if structure at loss:
- **ALLOWED:** Hold (with resting stop) or Exit
- ⛔ **FORBIDDEN:** sell more short leg, roll short closer, add lot, average credit, leg into ratio

**§8.9 adjustment playbook CLOSED on expiry day (0-DTE).** Only HOLD or EXIT. Elsewhere §8.9 offers shifts/rolls; on 0-DTE gamma makes every one a martingale.

01-Sep: 9th lot added at ₹11.45 — *above* exit trigger — instead of closing. Breaking this = **behavioural violation**, triggers 5-session halt (TC §12) **even if trade ends profitable**. Rule is about decision, not outcome.

---

## Update tread.md

**Before any strike quoted**, append gate record:
- Gate results, ALL FIVE (feasibility · basis · kill switch · Go/No-Go · Gate 5 with 5A sentence and 5B table verbatim)
- Entry-filter checklist, every line ticked or failed

**After presenting structure:**
- Single structure with reasoning, full payoff block, one lot count
- "Awaiting user execution confirmation"

**After user confirms fills:**
- Actual fill prices per leg, actual net credit, recomputed stop trigger pts+₹
- **Stop ORDER ID and "Trigger Pending" confirmation** — position not live without it
- Entry time

**If verdict is no-trade:** log anyway, with which reason (see [`no-trade.md`](no-trade.md)) — **too dangerous** (regime), **too small** (calendar), or **too thin** (structure). They generalise differently. No-trade days ~75% of sessions, logged with same discipline as trades.
