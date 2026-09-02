# Quick Tools — size-it · check-expiry · basis-check · no-trade

Four fast utilities. Read the relevant section based on the sub-command.

> ★ **Every number here is quoted from [`TRADING_CONSTANTS.md`](../../../../TRADING_CONSTANTS.md). If they disagree, that file wins and this one is a bug.**

---

## size-it — Lot Sizing Calculator

**Trigger:** "how many lots", "size it", "sizing for X structure", "lot count"

**Input (ask user if not provided):**
- Structure: **bear call spread or bull put spread — those two only.** Anything else → say it is locked (`TRADING_CONSTANTS.md` §5) and stop.
- Short strike and long strike → **width**
- Net credit in points
- Index (NIFTY/BANKNIFTY/SENSEX) → lot size

**k is fixed at 1.6.** It is not an input and not a choice. `k = 2.0` is ⛔ permanently.
**Lot sizes:** NIFTY=65 · BANKNIFTY=30 (monthly only) · SENSEX=20

**The formula — two caps, take the minimum:**

```
Structure: <type> <short>/<long>  |  Credit: <X> pts  |  Width: <Y> pts  |  c/W = <X/Y>%  |  k = 1.6

  STRUCTURAL MAX LOSS/lot = (width − credit) × lot_size = ₹<..>    ← if the stop never executes
  PLANNED STOP/lot        = 0.6 × credit × lot_size     = ₹<..>    ← what you intend to lose

  lots_A = floor( 10,500 ÷ structural_max_loss_per_lot )  = <A>
  lots_B = floor(  3,500 ÷ planned_stop_per_lot )         = <B>
  LOTS   = min(A, B)                                      = <N>

  ⛔ N < 2 → narrow the width and recompute. Still < 2 → NO TRADE.
     Do NOT widen the strikes to "afford" more lots — width is chosen AFTER the cap, never before.

  At <N> lots:  max profit ₹<X × lot × N>  ·  structural max loss ₹<..>  ·  planned stop ₹<..>
  Net at the 50% target ≈ ₹<..>  (charges ~₹150 round trip, 2 legs)
```

**Pre-computed width table** (from `TRADING_CONSTANTS.md` §4, at typical c/W ≈ 20%):

| Index | Width | LOTS | Note |
|---|---|---|---|
| NIFTY | 50 | 4 | ✅ |
| NIFTY | 100 | 2 | ✅ |
| NIFTY | 200 | **0** | ⛔ banned — one lot alone breaches the ₹10,500 cap |
| SENSEX | 100 | 6 | ✅ |
| SENSEX | 200 | 3 | ✅ |
| BANKNIFTY | 200 | 2 | ⚠️ locked until 30 net-positive NIFTY/SENSEX trades |

⛔ **Never present Conservative / Standard / Aggressive.** That menu was the mechanism of the 01-Sep-2026 loss: "Standard ₹15,000–20,000" was offered as a peer option and sat above the entire ₹10,500 structural cap. **The formula returns one number.** Less is always allowed; more is not.

Margin is **not** a sizing input — it is only a feasibility check: `<N> lots × margin/lot ≤ ₹2.8L (40% of ₹7.02L)`.

---

## check-expiry — Expiry Dates & Calendar Feasibility

**Trigger:** "when does NIFTY expire", "check expiry", "expiry dates", "how many sessions left"

Fetch expiry lists for all 3 indexes in parallel:
```
NIFTY:    UnderlyingScrip=13, UnderlyingSeg=IDX_I
BANKNIFTY: UnderlyingScrip=25, UnderlyingSeg=IDX_I
SENSEX:   UnderlyingScrip=51, UnderlyingSeg=IDX_I
```

Count trading **sessions**, not calendar days. **Convention: expiry day = 1 ("0-DTE"). Expiry eve = 2 ("1-DTE").** Count Mon–Fri and skip known holidays; if a day's holiday status is uncertain, count it as a trading day.

Output:
```
| Index | Nearest expiry | Calendar days | Sessions | Gate 1 verdict |
|---|---|---|---|---|
| NIFTY 50 | <date> | <N> | <M> | <verdict> |
| SENSEX | <date> | <N> | <M> | <verdict> |
| BANKNIFTY | <date> (monthly) | <N> | <M> | <verdict> |

Gate 1 (§8.11.6) verdicts — a BINARY gate:
  sessions = 1  (expiry day)  → ✅ TRADEABLE. Full theta today.
  sessions = 2  (expiry eve)  → ⚠️ TRADEABLE ONLY with a Gate-5-clean directional view.
                                 Delta-driven, not theta-driven. State the required move in POINTS.
  sessions >= 3               → ⛔ NO TRADE on this index. Hard stop.
```

⛔ **Do not attach a quoted return to any verdict.** The old table said "2–3 DTE: 0.5–0.75% realistic" — which turned a hard STOP into a tradeable ⚠️ with a number attached to reach for. At 3+ sessions intraday theta is a rounding error; there is no smaller percentage that makes it a trade.

⛔ **BANKNIFTY is never the fallback when NIFTY and SENSEX are both blocked.** It is monthly-only, so it is almost always 3+ sessions out, and it is locked until 30 net-positive NIFTY/SENSEX trades. Both majors blocked = **no trade today**, which is the correct and common answer (~75% of sessions).

---

## basis-check — Forward Basis (§8.7.1a)

**Trigger:** "what is the forward", "check basis", "basis check", "is the chain accurate"

Fetch the option chain for the specified index + expiry from Dhan. Then compute:

```
For 4-5 near-ATM strikes:
  F = K + CE_LTP - PE_LTP

All F values must agree within ±1 pt.
If they don't: chain is stale — report and stop.

basis = F - spot_price
basis_pct = basis / spot × 100

If basis_pct > 0.1%:
  → Dhan's delta band UNRELIABLE (Dhan uses spot not forward)
  → True ATM = the strike closest to F (not spot)
  → Use §8.7.3 straddle rule centred on F for strike selection
```

Output:
```
NIFTY parity forward computation:
  K=24,050 → 24,050 + 116.75 - 47.65 = 24,119.10
  K=24,100 → 24,100 +  86.35 - 67.25 = 24,119.10
  K=24,150 → 24,150 +  62.20 - 93.00 = 24,119.20
  Forward F ≈ 24,119 ✅ (consistent to <0.3 pts)

Spot: 24,067 | Basis: +52 pts (+0.22%)
→ Basis > 0.1% — delta band unreliable. True ATM = 24,119.
→ Strike selection: use §8.7.3 straddle rule on F.

ATM straddle at F: CE + PE ≈ <X> pts
Expected move to expiry: X ÷ 0.7979 ≈ <Y> pts
```

---

## no-trade — Document a No-Trade Decision

**Trigger:** "no trade today", "decided not to trade", "standing down", "sitting out"

Ask the user (if not already clear): which of the 3 stand-down reasons applies?

| Reason | Code | What to say |
|---|---|---|
| Kill switch fired / 3+ Go/No-Go reds / dangerous setup | **Too dangerous** | "Sitting out — regime not suitable. Will re-enter when: <condition>" |
| Clean setup but theta/size can't reach target | **Too small** | "Sitting out — calendar constraint. Will re-enter when: <next expiry>" |
| Credit too thin for stop to sit outside noise | **Too thin** | "Sitting out — structure doesn't pass noise floor. Try: <alternative>" |

Write to today's tread.md:
```markdown
## <HH:MM> — DECISION: NO TRADE

**Reason: <Too dangerous / Too small / Too thin>**

| Gate/Check | Result |
|---|---|
| §8.13 Kill switch | <N>/3 |
| §7 Go/No-Go | score <N> = (2×<red>) + (1×<yellow>); sit-out at ≥4 |
| Gate 1 Feasibility | <sessions> sessions → <verdict> |
| §8.11.7 Noise floor | <pass/fail> — (k−1)×credit vs 1.5× spread swing |
| Gate 5 | <5A sentence> · FII/Pro six numbers |

**What would change this:** <specific condition — e.g., "VIX drops below 12", "tomorrow is expiry day", "use 24,300 strike instead">

**Deployed ₹0. Risked ₹0.**
```

Also score the no-trade neutrally (per §8.15.4):
- Price the declined structures at bid/ask at the decision time — **including candidates rejected during analysis and never written up.** Those are the ones the memory flatters.
- Record what they would have returned **at the mandated hard flat** (2:30 PM NIFTY/BANKNIFTY · 2:15 PM SENSEX) at max permitted size — never at a mid-session snapshot.
- Record MAE and MFE over the same window.

⚠️ **This scoring happens at the hard flat, not at the moment of the decision.** A no-trade called at 9:45 is scored at 2:15/2:30 the same day; do not close the session at 9:45 and then claim a mark you never took. If the session is being wrapped early, say the score is pending and come back for it.

Then proceed to `session-close` to write the learning.md.

---

## Common to all quick tools

After any quick tool completes, append a brief record to today's tread.md. Even a one-liner: `14:15 — size-it: 24200/24400 BCS, credit 21 pts, c/W 21%, k=1.6 → lots_A 3, lots_B 4 → 3 lots. Structural max loss ₹7,703, planned stop ₹2,457.`

This keeps the session log complete without extra effort.
