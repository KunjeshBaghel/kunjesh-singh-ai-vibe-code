# find-trade — Structure Selection & Sizing

Runs after `analyse-today`. Requires a completed market_view.md. Follows the gates strictly — never jumps to structure before all gates clear.

> ★ **Every number in this file is quoted from [`TRADING_CONSTANTS.md`](../../../../TRADING_CONSTANTS.md). If they ever disagree, that file wins and this one is a bug.**

---

## Pre-check: hard preconditions — ABORT if any is missing

Read `my-treads/<Month>/<DD-MM-YYYY>/<DD-MM-YYYY>-market_view.md` and verify **all** of:

```
□ A five-view classification with an HH:MM timestamp less than 60 minutes old
□ A literal `GATE 5 INPUTS` block with all six numbers (FII/Pro × net CE short / net PE short / FUT)
□ Nearest expiry + session count for all 3 indexes
□ A basis line per index
□ Key support/resistance levels
```

⛔ **If ANY is absent: STOP.** Say `market_view.md is incomplete — <which item>. Run analyse-today first.`
**Do not derive the missing item inline.** On 02-Sep-2026 inline re-derivation is precisely what
inspected only Pro and missed FII's 93,282 net short calls. The written block is the gate's only
enforcement mechanism; deriving it on the fly defeats it.

---

## Gate 1: §8.11.6 Feasibility — run this first

**Counting convention (canonical):** `sessions_to_expiry` = trading sessions remaining **including today**, up to and including expiry. **Expiry day = 1** ("0-DTE"). **Expiry eve = 2** ("1-DTE"). If a day's holiday status is uncertain, count it as a trading day.

```
For each index:
  sessions_to_expiry = <count>
  intraday_only = YES (the user never holds overnight, ever)

  ⛔ If sessions_to_expiry ≥ 3  →  NO TRADE on this index. Hard stop.
     Intraday theta is a rounding error at 2+ DTE. Do NOT quote a smaller % and trade it
     anyway — that is the size-creep failure mode.

  MAX CREDIT = planned-stop cap ÷ (k − 1) = ₹3,500 ÷ 0.6 = ₹5,833      k = 1.6
  REQUIRED CAPTURE = (k − 1) × 100% = 60% of the credit
```

> ⚠️ **The numerator is the PER-STRUCTURE planned stop (₹3,500), never the daily budget (₹10,500).**
> Using the daily figure inflates permitted credit by 200% and lets the same pool be spent again
> later in the day. The daily figure is a circuit breaker, never a sizing input.

**State the verdict clearly, per index:**
- `sessions = 1 (expiry day)` — full theta today. ✅ Tradeable.
- `sessions = 2 (expiry eve)` — **delta-driven, not theta-driven.** Tradeable ONLY with a Gate-5-clean directional view. Say what move, in points, is required. ⚠️
- `sessions ≥ 3` — ⛔ no trade, per §8.11.6.

If no index has a viable calendar → say so and stop. **Do not force a trade.** ~75% of sessions are correctly no-trades.

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

**The 3 markers — canonical definitions. Use these exact tests, here and in `followup`:**

| # | Marker | FIRES when |
|---|---|---|
| 1 | **Opening-range break** | Two consecutive 15-min candles **close** outside the 9:15–9:45 OR high/low. A wick outside is not a break. |
| 2 | **VWAP one-sidedness** | Price on one side of VWAP for **≥ 45 min** with no close through it, AND VWAP itself sloping the same way. |
| 3 | **OI confirming direction** | Price and OI aligned per the §8.13 matrix — falling price + rising CE OI (short buildup above), or rising price + rising PE OI. Compare each strike to its **`oi_day_high`**, not to the morning print. |

Scoring — **and what each score licenses:**

| Score | Verdict | Action |
|---|---|---|
| 0/3 | Not a trend day | Proceed to Gate 4. ⚠️ **0/3 means "not a trend day". It NEVER means "bullish", and it is NEVER a reason to hold a losing position.** |
| 1/3 | Elevated caution | Proceed, but the entry filters must all pass with margin — no borderline calls. |
| 2/3 | **Trend day** | ⛔ **No NEW position.** If already in one, the untested side is the only survivable side; exit if the position is on the wrong side of the trend. |
| 3/3 | **Abort** | ⛔ No new position, and **close any open structure immediately at market**, profitable or not. |

---

## Gate 4: §7 Go/No-Go — POINT-SCORED (5 checks)

| # | Check | GREEN (0) | YELLOW (1) | RED (2) |
|---|---|---|---|---|
| 1 | VIX level & direction | < 16 and falling/stable | 16–20, or +3–8% rise | **≥ 20, or +8%+ spike** |
| 2 | Open vs prior close | Within the expected move | Gap 0.3–0.6% | Gap > 0.6% |
| 3 | Theta-trap bundle | VIX falling **and** PCR stable/rising | Mixed | VIX rising **and** PCR dropping |
| 4 | FII regime | 3 consecutive consistent days + Net OI confirms | 1–2 days only | Today contradicts the cumulative Net OI |
| 5 | PCR intraday slope | Flat or rising | Declining slowly | Sharp PCR drop + call OI building |

```
SCORE = (2 × RED count) + (1 × YELLOW count)
⛔ SCORE ≥ 4  →  SIT OUT.
```

Three rules that keep this honest:

1. **Disjoint inputs.** VIX appears in rows 1 and 3; PCR in rows 3 and 5. If two rows fire on the *same* underlying observation, count the higher one and mark the other GREEN with a note. Double-counting one fact into a 4 is not a real 4 — and neither is dismissing both because they overlap.
2. **A blank row is YELLOW, never GREEN.** Unmeasured is not benign. If FII data has not been pulled, row 4 = 1 point.
3. ⚠️ **GIFT Nifty is a futures price.** Never compare it to spot to score row 2 — compare spot open to prior spot close, and compare GIFT only to the *futures* forward.

**Automatic blockers** — immediate sit-out regardless of score, and they do **not** count toward the 4:
- No five-view classification, or one older than 60 minutes
- Undefined stop level, or a stop that cannot be expressed as a rupee number before entry
- Undefined max loss
- Gate 5 not written out in `tread.md`

---

## Gate 5: Structure–View–Participant reconciliation ⚠️ MANDATORY

**Run this BEFORE pricing anything.** Gates 1–4 decide *whether* to trade. Gate 5 decides *which side*. It has three parts and all three must be written out in `tread.md` before a single strike is quoted. Skipping any part has cost real money twice (01-Sep-2026: −₹15,564; 02-Sep-2026: caught only because the user challenged it).

---

### 5A — Structure ↔ View compatibility (HARD FORBID — no override exists)

Restate the five-view classification, then read this table. **⛔ means forbidden, full stop.** Not "prefer not to". There is no vol-state, skew, PE-first, or participant argument that unlocks a ⛔ cell.

| Structure | Strongly Bearish | Slightly Bearish | Sideways | Slightly Bullish | Strongly Bullish |
|---|---|---|---|---|---|
| **Bear Call Spread** | ✅ | ✅ | ✅ | ⛔ | ⛔ |
| **Bull Put Spread** | ⛔ | ⛔ | ✅ | ✅ | ✅ |
| Iron Condor / Strangle | ⛔ | ⚠️ skew strikes down | ✅ | ⚠️ skew strikes up | ⛔ |
| Iron Fly | ⛔ | ⛔ | ✅ | ⛔ | ⛔ |
| Long Put / put debit | ✅ | ✅ | ⛔ | ⛔ | ⛔ |
| Long Call / call debit | ⛔ | ⛔ | ⛔ | ✅ | ✅ |
| Ratio / ladder | repair only — never an entry (§8.6.13) | | | | |

> **§8.5.4 "PE-first" is a tie-breaker for a SIDEWAYS view only.** It never promotes a Bull Put Spread into a bearish cell. CLAUDE.md's own wording — *"override to CE selling for explicitly bearish views with call OI wall visible"* — means the bearish view already decides it; the OI wall only picks the strike.
>
> **The §8.5 vol-state grid does not relax this table, it narrows it further.** CHEAP × Slightly Bearish and NORMAL × Slightly Bearish are *different cells*. Read the row for today's VIX, not the one you remember.

**Write this sentence verbatim before pricing:**
`View = <one of five>. Permitted structures = <list from the row>. Chosen = <X>, which is ✅ in that row.`

---

### 5B — Participant reconciliation (FII **and** Pro — not Pro alone)

From today's `market_view.md` participant table (NSE T-1 CSV), extract **all six** numbers:

```
FII_net_CE_short = |FII CE Short| − |FII CE Long|     Pro_net_CE_short = |Pro CE Short| − |Pro CE Long|
FII_net_PE_short = |FII PE Short| − |FII PE Long|     Pro_net_PE_short = |Pro PE Short| − |Pro PE Long|
FII_net_FUT                                            Pro_net_FUT
```

Apply the thresholds to **FII first** — CLAUDE.md: *"FII = primary trend setter; Client (retail) = contrarian."* Then to Pro. **If either fires, it fires.**

| Net CE short (FII **or** Pro) | Signal | Mandate |
|---|---|---|
| **> 80,000** | **HARD CEILING** | **Bear Call Spread at the ceiling strike. Bull Put Spread is FORBIDDEN regardless of view or vol state.** |
| 50,000–80,000 | Strong ceiling | Prefer Bear Call Spread. Bull Put only if the view is bullish AND spot is 150+ pts above the ceiling strike. |
| < 50,000 | No ceiling | Fall through to 5A + the §8.5 grid. **This is silence, not permission to sell puts.** |

| Net PE short (FII **or** Pro) | Signal | Mandate |
|---|---|---|
| **> 80,000** | **HARD FLOOR** | **Bull Put Spread at the floor strike. Bear Call Spread forbidden.** |
| 50,000–80,000 | Strong floor | Prefer Bull Put Spread if the view permits it (5A). |
| < 50,000 | No floor | Fall through. |

**If a ceiling AND a floor both fire** (institution is short a strangle → they want a range):
- The **larger** magnitude wins the directional tie-break.
- It must still be ✅ in the 5A row. **If it is ⛔, take no directional trade** — the range structure only, or no trade.

**⚠️ Long-straddle / long-gamma counterparty check.** If FII or Pro is net **LONG** both CE and PE in size (>100,000 either leg), they have paid for movement and are long gamma. You would be selling premium to the most sophisticated buyer in the market.
- **Halve the size, or stand down.**
- Do **not** argue that an early move has "already delivered" what they paid for and inverted the signal. That reasoning was used on 02-Sep-2026 to justify selling into Pro's 300K long straddle. It is a rationalisation: a long-gamma book re-hedges and stays long gamma; it does not become a premium seller because one leg paid.

**Write this table verbatim before pricing:**

| | Fut | net CE short | net PE short | Fires? | Structure implied |
|---|---|---|---|---|---|
| FII | | | | | |
| Pro | | | | | |
| **Reconciliation** | *Chosen structure aligns with / fights: FII ___ , Pro ___ . Justification if it fights either:* | | | | |

---

### 5C — Banned inputs (these are not evidence of direction)

Every one of these has produced a wrong call. If a directional argument rests on one, it is void:

| ⛔ Banned input | Why it's wrong | What to use instead |
|---|---|---|
| **"Spread X decayed this morning, spread Y widened → trade X's side"** | Momentum-chasing. For a **credit seller a widened spread is a BETTER entry, not a broken structure** — you are paid more for the same bet. Most morning "decay" after a gap is **delta**, not theta. | The 5A row + 5B participants |
| **Intraday price making a new high/low in the last 30–60 min** | A bounce inside a down day is not a view change. The daily view changes on PDH/PDL, gap fill, and OI walls — not on the last 3 candles. | Is spot above/below PDL? Is the gap filled? |
| **Kill switch = 0/3 reads as "bullish"** | 0/3 means *not a trend day* → range structures are permitted. It says **nothing** about direction. | Direction comes from 5A + 5B only |
| **A rule that did NOT fire read as endorsement of its opposite** | `< 50,000` = silence. It hands the decision to the grid; it does not vote. | Fall through to 5A |
| **Reusing a classification from >60 min ago without restating it** | The grid input goes stale. | Re-state the five-view classification with a timestamp at the top of Gate 5 |

---

### §8.5 Regime grid — SIZE only. It can never change the SIDE.

⚠️ **This grid was the direct cause of the 01-Sep-2026 loss and the 02-Sep-2026 near-miss.** Its old NORMAL row named *Bull Put Spread* under Slightly Bearish — handing back the exact structure 5A forbids — and VIX has sat 11–13 all week, so NORMAL was the default row every session. It has been rebuilt so that **it cannot name a structure at all.** The side is already decided by 5A + 5B. All the grid does now is set the vol gate and the size multiplier.

| Vol State | Definition (VIX) | Gate | Size |
|---|---|---|---|
| **CHEAP** | < 12 | ✅ Trade | Full (per the two-cap formula) |
| **NORMAL** | 12–16 | ✅ Trade | Full |
| **RICH** | 16–20 | ⚠️ Trade only if the credit clears the noise floor with margin | **Half** |
| **HOSTILE** | ≥ 20, **or VIX up > 8% today** | ⛔ **NO TRADE** | — |

⛔ **VALIDATION RULE.** This grid contains no structure names, by design. If any future edit reintroduces one, that cell is a bug: **a cell may never name a structure that is ⛔ in its column's 5A row, and 5A always wins.** If a grid and 5A ever disagree, refuse the trade and report the grid as defective.

⛔ **Naked short options are banned outright** at this capital and are not a vol-state option. The permitted universe is the two-leg defined-risk credit vertical and nothing else — see [`TRADING_CONSTANTS.md` §5](../../../../TRADING_CONSTANTS.md). Four-leg structures (condor, fly) are locked until 30 clean verticals: they carry two unmeasurable gamma exposures and two manual stops, in an app where execution is by hand.

**Compression squeeze (§8.12.6a):** If active → veto NEUTRAL premium only. A one-sided credit vertical leaning the way the market leans is *paid* by the break — it is not vetoed.

### Fetch full option chain for selected index + expiry

**Primary: Dhan REST API** (reliable mid-session; MCP OAuth breaks after ~30 min):
```bash
source .broker_creds
curl -s -X POST "https://api.dhan.co/v2/optionchain" \
  -H "access-token: $DHAN_ACCESS_TOKEN" \
  -H "client-id: $DHAN_CLIENT_ID" \
  -H "Content-Type: application/json" \
  -d '{"UnderlyingScrip":<id>,"UnderlyingSeg":"IDX_I","Expiry":"<YYYY-MM-DD>"}'
# Scrip IDs: NIFTY=13 · BANKNIFTY=25 · SENSEX=51
# Strikes keyed as floats: "24000.000000" → .ce / .pe sub-dicts
```

**Fallback: Dhan MCP** (try once at session start; if Unauthorized, switch to REST permanently):
```
mcp__dhan__market_data_agent_tool action=optionchain
{"UnderlyingScrip": <id>, "UnderlyingSeg": "IDX_I", "Expiry": "<date>"}
```

**Fallback: Kite quotes** for individual strikes (format `NFO:NIFTY{YY}{M}{DD}{STRIKE}{TYPE}` e.g. `NFO:NIFTY2690124000PE`).

Extract:
- OI at 5 key strikes above (call walls) and 5 below (put walls)
- ATM straddle at the parity forward F
- Bid/ask spreads at the candidate short strikes

### Entry filters — run ALL of them, on every candidate, before quoting a lot count

Any single ❌ kills the candidate. Full list and rationale: [`TRADING_CONSTANTS.md` §6](../../../../TRADING_CONSTANTS.md).

```
□ sessions_to_expiry ≤ 2                     (Gate 1)
□ c/W ≥ 15%          20%+ preferred          ← the credit-to-width ratio IS the short delta
□ net credit ≥ ₹2,500 at the chosen size
□ k × credit < width       k = 1.6           ← else the premium stop sits BEYOND max loss
                                                and can never trigger. Above c/W = 1/1.6 = 62.5%
                                                the stop is unreachable by construction.
□ noise floor: (k−1) × credit ≥ 1.5 × the SPREAD's 30-min intra-bar swing
□ bid-ask (both legs summed) ≤ 15% of credit
□ depth at the short strike ≥ 5 × intended lots
□ VIX < 20 and today's change ≤ +8%
□ basis within 0.1% of spot, or §8.7.3 used instead of any delta band
□ stop's spot level sits OUTSIDE today's traded range
```

### §8.11.7 Noise floor test — spread-based, needs no Greeks

```
credit        = short_premium − long_premium         (points)
stop_distance = (k − 1) × credit = 0.6 × credit      (k = 1.6)

spread_swing  = max over the last 3 completed 30-min bars of:
                  (short_high − long_high) − (short_low − long_low)      ← intra-bar, both legs

IF stop_distance < 1.5 × spread_swing:
  ⛔ the stop sits inside one candle → NO TRADE at any size.
     More size makes it worse. The fix is a different structure: closer strikes or a wider width.
```

⚠️ **No Greeks anywhere in that formula, deliberately.** The old version read `delta × index_30min_range + vega_change_estimate`, which requires two numbers this repo does not have a trustworthy source for. Pull both legs' 30-min candles from Kite and difference the highs and the lows.

**Use intra-bar swing, never bar closes.** Closes hide the excursion: in the 10:15 bar on 02-Sep-2026 the closes moved a spread 0.05 pts while it swung ~14 pts intra-bar.

**≥ 1.5× is a PASS; anything below is a fail — there is no "on the threshold" band.** 1.51× passes. Say "passes, thinly" and move on. Do not convert a numeric test into a judgement call — that is how a marginal candidate gets talked into a trade.

**Exclude the opening 30-min bar from the estimate, but report it.** Gap candles are not representative. If the stop sits inside the opening bar's swing, state that as the live risk.

### Derive the stop's SPOT level from the chain — HARD GATE, not a preference

The premium stop is the trigger, but the user needs to know *where the index has to go* for it to fire. Estimating from two intraday observations gives wrong answers (02-Sep-2026: quoted SENSEX 76,870; the true level was ~76,650 — a 220-point error in the number the whole trade is watched against).

**Permitted arithmetic — the vertical-spread relation on the chain's own prices** (a price difference across strikes, not a Black-Scholes solve):
```
Δ(K) ≈ −[ C(K+100) − C(K−100) ] / 200        # from adjacent strike prices in the chain
spread_delta = Δ(short) − Δ(long)
spot_move_to_stop = stop_distance / spread_delta
stop_spot_level   = spot ± spot_move_to_stop        # add for a call spread, subtract for a put spread
```

⛔ **If `stop_spot_level` falls INSIDE today's already-traded high–low range: NO TRADE.** The market has demonstrated it can reach that level today without doing anything unusual — the stop will fire on ordinary chop. This is a hard block, not a "prefer otherwise": it is a *stronger* piece of evidence than the noise floor, since it uses the index's realised range rather than an estimate, and it must not be the weaker rule.

Gamma puts the true level slightly further away than this linear estimate, so quote it as a band and use the **near** edge for the gate.

---

## Present ONE structure with ONE lot count

For the single best candidate that clears all gates, all entry filters, and the noise floor.

⚠️ **Do not present sizing "options".** The Conservative / Standard / Aggressive menu that used to live here was the mechanism of the 01-Sep-2026 loss: "Standard ₹15,000–20,000" was offered as a peer choice, the operator picked it, and it sat above the entire ₹10,500 structural cap. **The formula returns one number. Quote that number.** If the user wants less, less is always allowed; more is not.

**State the full payoff before the lot count — max profit → breakeven → structural max loss → planned stop → lots.** Fixed order, every time.

```
Structure: <name> <short strike>/<long strike>  Expiry: <date>   (sessions to expiry: <n>)
Net credit: <X> pts  |  Width: <Y> pts  |  c/W = <X/Y>%  |  Short strike <Z> pts OTM from F

  MAX PROFIT       = credit         = <X> pts      = ₹<X×lot>/lot   (spot beyond nothing; short expires OTM)
  BREAKEVEN        = short ± credit = <level>
  STRUCTURAL MAX LOSS = width − credit = <Y−X> pts = ₹<(Y−X)×lot>/lot
        ← what you lose if the stop is never executed. Cap: ₹10,500 TOTAL.
  PLANNED STOP (k=1.6) = 0.6 × credit = <0.6X> pts = ₹<..>/lot
        ← what you intend to lose. Cap: ₹3,500 TOTAL.
  Stop's SPOT level ≈ <level>   (today's range: <low>–<high>. Outside? YES/NO)

Sizing — both caps, then the minimum:
  lots_A = floor( 10,500 ÷ ((Y−X) × <lot_size>) )   = <A>     structural
  lots_B = floor(  3,500 ÷ (0.6 × X × <lot_size>) ) = <B>     planned stop
  LOTS   = min(A, B)                                = <N>
  ⛔ If N < 2 → narrow the width and recompute. Still < 2 → NO TRADE.

  At <N> lots:  max profit ₹<..>  ·  structural max loss ₹<..>  ·  planned stop ₹<..>
  Charges ≈ ₹150 round trip. Net at target (50% of credit) ≈ ₹<..>

Stop ORDER (place within 90 seconds of the fill — see followup):
  SL-LIMIT BUY-TO-CLOSE on the SHORT LEG ONLY
  Trigger = <short_leg_entry_price> + 1.6 × <net credit per lot in pts> = <..>
  Limit   = trigger + max(12%, <2 pts NIFTY/BN | 5 pts SENSEX>)         = <..>
  ⛔ Never SL-M on an option.
Price abort: <e.g. "15-min close beyond <short strike>">
Hard flat: <2:30 PM NIFTY/BANKNIFTY · 2:15 PM SENSEX> — never into the 3:15 CAS
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

### ⚠️ MANDATORY within 90 seconds of the fill — the stop is an ORDER, not an alert

```
ACTION REQUIRED — place this RESTING order in the Kotak app NOW, before anything else:

  Type:    SL-LIMIT, BUY TO CLOSE, on the SHORT LEG ONLY
  Symbol:  [short leg]
  Qty:     [same lots as the short]
  Trigger: [short_leg_entry_price + 1.6 × net credit per lot in pts]
  Limit:   [trigger + max(12% of trigger, 2 pts NIFTY/BANKNIFTY | 5 pts SENSEX)]

  ⛔ NEVER SL-M on an option — a market stop on an illiquid strike fills anywhere.
  ⛔ Never put a stop on the long leg. That un-hedges you at the worst moment.

Then report back the ORDER ID and the words "Trigger Pending".
No order ID = no position. If it cannot be placed, close the structure at market.
```

**Two price alerts are set in addition, on the INDEX, not instead of the order** — at the stop's spot level and at the price-abort level. They are a notification; the resting order is the protection.

**Why the order and not the alert.** On 01-Sep-2026 the trigger was stated (₹11.00 on the 24,000 PE), the market reached it (₹11.45), **and the move was observed** — notification was never the failure. The failure was that nothing was resting at the broker, so acting required a human decision under loss pressure, and that decision did not get made. An alert delegates the hard part back to the person who has already demonstrated they freeze there. −₹1,800 became −₹15,564. Kotak and Kite are also marked ❌ for conditional alerts in the capability map, so an alert-only plan may not even exist to be missed.

### ⚠️ HARD RULE — no order may ever increase short exposure in a losing structure

**On any day, at any hour**, if the structure is at a loss:
- **ALLOWED:** Hold (with the resting stop live) or Exit
- ⛔ **FORBIDDEN:** sell more of the short leg, roll the short closer, add a lot, average the credit, leg into a ratio — any order that increases short exposure

The **§8.9 adjustment playbook is CLOSED on expiry day.** Only HOLD or EXIT exist. Elsewhere in the book §8.9 offers shifts and rolls; on 0-DTE, gamma makes every one of them a martingale in disguise.

On 01-Sep-2026 a 9th lot was added at ₹11.45 — *above* the stated exit trigger — instead of closing. Breaking this rule is a **behavioural violation** and triggers the 5-session halt in [`TRADING_CONSTANTS.md` §12](../../../../TRADING_CONSTANTS.md), **even if the trade ends profitable.** The rule is about the decision, not the outcome.

---

## Update tread.md

**Before any strike is quoted**, append the gate record — this written block is Gate 5's only enforcement mechanism:
- **Gate results, all FIVE** (feasibility · basis · kill switch · Go/No-Go score · Gate 5 with the 5A sentence and the 5B six-number table written out verbatim)
- Entry-filter checklist, every line ticked or failed

**After presenting the structure:**
- The single structure with its reasoning, the full payoff block, and the one lot count
- "Awaiting user execution confirmation"

**After the user confirms fills:**
- Actual fill prices per leg, actual net credit, recomputed stop trigger in points and rupees
- **The stop ORDER ID and its "Trigger Pending" confirmation** — the position is not considered live without it
- Entry time

**If the verdict is no-trade:** log it anyway, with which of the three reasons applies — **too dangerous** (regime), **too small** (calendar), or **too thin** (structure). They generalise differently and conflating them buries the fixable cause. No-trade days are ~75% of sessions and are logged with the same discipline as trades.
