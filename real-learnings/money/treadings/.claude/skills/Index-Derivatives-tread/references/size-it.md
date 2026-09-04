**Sub-command:** size-it

Lot sizing calculator for credit spreads. Returns the smaller of two caps: structural (worst-case payoff) and planned stop.

---

## Trigger

"how many lots", "size it", "sizing for X structure", "lot count"

## Input (ask user if not provided)

- Structure: **bear call spread or bull put spread — those two only.** Anything else → say it is locked ([`TRADING_CONSTANTS.md` §5](../../../../TRADING_CONSTANTS.md)) and stop.
- Short strike and long strike → **width**
- Net credit in points
- Index (NIFTY/BANKNIFTY/SENSEX) → lot size

## The formula — two caps, take the minimum

**k is fixed at 1.6.** It is not an input and not a choice. `k = 2.0` is ⛔ permanently (see [`TRADING_CONSTANTS.md` §11](../../../../TRADING_CONSTANTS.md)).

**Lot sizes:** NIFTY = 65 · BANKNIFTY = 30 (monthly only) · SENSEX = 20 ([`TRADING_CONSTANTS.md` §13](../../../../TRADING_CONSTANTS.md))
**Strike intervals:** NIFTY = 50 · SENSEX = 100 · **BANKNIFTY = 100** *(not 200 — corrected 04-Sep-2026 against the live chain)*

```
Structure: <type> <short>/<long>  |  Credit: <X> pts  |  Width: <Y> pts  |  c/W = <X/Y>%  |  k = 1.6

  STRUCTURAL MAX LOSS/lot = (width − credit) × lot_size = ₹<..>    ← if the stop never executes
  PLANNED STOP/lot        = 0.6 × credit × lot_size     = ₹<..>    ← what you intend to lose

  lots_A = floor( STRUCTURAL_CAP ÷ structural_max_loss_per_lot )  = <A>
  lots_B = floor( PLANNED_STOP_CAP ÷ planned_stop_per_lot )       = <B>
  LOTS   = min(A, B)                                              = <N>
     ★ Read STRUCTURAL_CAP and PLANNED_STOP_CAP from TRADING_CONSTANTS.md §3 at the moment you
       compute. Do not carry them in your head — §1's capital figure is under a pending ruling
       and both caps re-base if it changes.

  ⛔ N < 2 → narrow the width and recompute. Still < 2 → NO TRADE.
     Do NOT widen the strikes to "afford" more lots — width is chosen AFTER the cap, never before.

  At <N> lots:  max profit ₹<X × lot × N>  ·  structural max loss ₹<..>  ·  planned stop ₹<..>
  Net at the 50% target ≈ ₹<..>  (charges ~₹150 round trip, 2 legs)
```

**Caps and lot sizes:** [`TRADING_CONSTANTS.md` §3–§4](../../../../TRADING_CONSTANTS.md)

**Presentation order, always:** **max profit → breakeven → structural max loss → planned stop → lots.** Never quote a lot count before the max loss.

## The LOTS ≥ 2 floor

The floor is load-bearing — it silently bans every structure too coarse for this account. **NIFTY 200-wide can never be traded here.**

**Worked example: 01-Sep-2026 check** (Bull Put 24,000/23,800, credit 6.99, lot 65):

```
STRUCTURAL MAX LOSS/lot = (200 − 6.99) × 65 = ₹12,546
lots_A = floor(10,500 ÷ 12,546) = 0

⛔ BANNED OUTRIGHT — not downsized, BANNED.
```

The structure was recommended at 8 lots. The `k = 1.6` cap bound the planned stop to ₹3,500, and the stop-loss formula looked compliant. But the structural max loss was **₹12,546 per lot** — a single lot alone breached the entire ₹10,500 daily circuit-breaker. The loss was −₹15,564.

**Width is chosen AFTER the cap, never before.**

## Pre-computed width table

From [`TRADING_CONSTANTS.md` §4](../../../../TRADING_CONSTANTS.md), at typical `c/W ≈ 20%`:

| Index | Width | LOTS | Note |
|---|---|---|---|
| NIFTY | 50 | 4 | ✅ |
| NIFTY | 100 | 2 | ✅ |
| NIFTY | 200 | **0** | ⛔ banned — one lot alone breaches the structural cap |
| SENSEX | 100 | 6 | ✅ best granularity in the book |
| SENSEX | 200 | 3 | ✅ |
| BANKNIFTY | **100** | 4+ | ✅ **the BANKNIFTY default**, and the only width available during break-in |
| BANKNIFTY | 200 | 2 | ✅ full cap only — at the break-in half-cap this sizes to **1 lot** → §4 blocks it |

⚠️ **BANKNIFTY break-in ([`TRADING_CONSTANTS.md` §11a](../../../../TRADING_CONSTANTS.md)):** the
**first 3** BANKNIFTY trades size against **half the structural cap — ₹5,250, not ₹10,500.** Substitute
that into Cap A only; Cap B is unchanged. In practice this restricts BANKNIFTY to **width 100** until
the fourth trade. *A 1-lot restriction was considered and rejected: it collides with §4's
`LOTS < 2 → no trade` and would have silently re-created the ban the unlock removed.*

## What is NOT a sizing input

⛔ **Never present Conservative / Standard / Aggressive.** That menu was the mechanism of the 01-Sep-2026 loss: "Standard ₹15,000–20,000" was offered as a peer option and sat above the entire ₹10,500 structural cap. **The formula returns one number.** Less is always allowed; more is not.

⛔ **Conviction is NEVER a sizing input.** The 31-Aug "conservative/standard/aggressive" bands are DELETED ([`TRADING_CONSTANTS.md` §2](../../../../TRADING_CONSTANTS.md)).

⛔ **Margin is not a sizing input** — it is only a feasibility check: `<N> lots × margin/lot ≤ the deploy ceiling` ([`TRADING_CONSTANTS.md` §1–§3](../../../../TRADING_CONSTANTS.md), computed off the live Kotak `get_limits` read). Under the structural cap, margin will never bind — a permitted spread blocks ~₹10–12K.

---

## Logging

After completing, append a brief record to today's tread.md. Even a one-liner:

```
14:15 — size-it: 24200/24400 BCS, credit 21 pts, c/W 21%, k=1.6 → lots_A 3, lots_B 4 → 3 lots.
        Structural max loss ₹7,703, planned stop ₹2,457.
```
