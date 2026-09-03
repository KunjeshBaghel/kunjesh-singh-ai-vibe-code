**Sub-command:** no-trade

Journalling a stand-down. This is a real deliverable, not a shrug.

---

## Trigger

"no trade today", "decided not to trade", "standing down", "sitting out"

## The four reason codes

Exactly one code per stand-down. **The code is chosen by what would have to change, not by how the
day felt** — that is the whole point of a closed vocabulary.

| Reason | Code | What to say | What changes it |
|---|---|---|---|
| Kill switch fired / Go/No-Go score ≥ 4 / compression squeeze / gap risk | **Too dangerous** | "Sitting out — regime not suitable. Will re-enter when: <condition>" | Wait for the **regime** to change (17-Aug, 27-Aug-2026) |
| Clean setup but no permitted size reaches a worthwhile payoff | **Too small** | "Sitting out — calendar constraint. Will re-enter when: <next expiry>" | Wait for the **calendar** to change (24-Aug, 28-Aug-2026) |
| Credit so small the stop sits inside one candle ([`TRADING_CONSTANTS.md` §6](../../../../TRADING_CONSTANTS.md) row 5: noise floor) | **Too thin** | "Sitting out — structure doesn't pass noise floor. Try: <alternative>" | Pick a **different structure**: closer strikes or wider width. More size makes it worse, not better. |
| **Realised vol ≥ implied — negative VRP** ([`TRADING_CONSTANTS.md` §10b](../../../../TRADING_CONSTANTS.md)) | **UNPAID** | "Sitting out — the tape is realising more than it is paying. Ratio <X>. Nothing on the board is paid today." | Wait for **vol to reprice** — IV up or RV down. ⛔ No strike, width or size fixes it. |

**★ `UNPAID` is checked BEFORE any strike is priced.** It is the only code that can be determined
without pricing a single candidate, and skipping that order of operations is what cost 03-Sep
ninety minutes.

> **Adopted 03-Sep-2026** (previously a proposal). 03-Sep was logged `Too thin`, but `Too thin`
> prescribes "closer strikes or wider width" — a fix that had already been tested and did not exist.
> The real cause was negative VRP: realised **1.7×** implied. Mis-coding it sent the session hunting
> a structure that could not exist. A code whose prescribed fix is unreachable is worse than no code.

## Why conflating them buries the fixable cause

On 28-Aug-2026 the kill switch was 0/3, Go/No-Go 0 red, VRP positive and VIX falling — a **clean** day on which the then-target still needed 20–33 lots (**14.9–24.7% of capital**). The cause was calendar (sessions_to_expiry = 3), not regime.

**When something is out of reach, quote the capital at risk, not the shortfall.** A ratio ends the discussion; an adjective invites size creep.

## There is no obligation to trade

~75% of sessions are correctly no-trades. From [`TRADING_CONSTANTS.md` §2](../../../../TRADING_CONSTANTS.md), honest per-session expectancy is **₹1,274 (0.20%)**.

## ★ Log the no-trade days

**~16 of 21 sessions were no-trades — that is 75% of the decision record and it is currently invisible.**

If one filter vetoes 20 days running, either it is miscalibrated or the strategy has no market, and you cannot tell which without this row. See [`TRADING_CONSTANTS.md` §15](../../../../TRADING_CONSTANTS.md).

## What to write and where

Today's `my-treads/<Month>/<DD-MM-YYYY>/` — append to `*-tread.md`, then the `*-learning.md`.

### In tread.md

```markdown
## <HH:MM> — DECISION: NO TRADE

**Reason: <Too dangerous / Too small / Too thin / UNPAID>**

| Gate/Check | Result |
|---|---|
| §8.13 Kill switch | <N>/3 |
| §7 Go/No-Go | score <N> = (2×<red>) + (1×<yellow>); sit-out at ≥4 |
| Gate 1 Feasibility | <sessions> sessions → <verdict> |
| §8.11.7 Noise floor | <pass/fail> — (k−1)×credit vs 1.5× spread swing |
| TC §10b VRP | realised <X> ÷ implied <Y> = <ratio> → <PAID / THIN / UNPAID> |
| Gate 5 | <5A sentence> · FII/Pro ΔCE and ΔPE vs TC §9 limits |

**What would change this:** <specific condition — e.g., "VIX drops below 12", "tomorrow is expiry day", "use 24,300 strike instead">

**Deployed ₹0. Risked ₹0.**
```

### Score the no-trade neutrally (per §8.15.4)

**This scoring happens at the hard flat, not at the moment of the decision.** A no-trade called at 9:45 is scored at 2:15/2:30 the same day; do not close the session at 9:45 and then claim a mark you never took.

If the session is being wrapped early, say the score is pending and come back for it.

- Price the declined structures at bid/ask at the decision time — **including candidates rejected during analysis and never written up.** Those are the ones the memory flatters.
- Record what they would have returned **at the mandated hard flat** (2:30 PM NIFTY/BANKNIFTY · 2:15 PM SENSEX from [`TRADING_CONSTANTS.md` §7](../../../../TRADING_CONSTANTS.md)) at max permitted size — never at a mid-session snapshot.
- Record MAE and MFE over the same window.

```markdown
## <HH:MM> — Neutral scoring of declined candidates

| Structure | Entry mark | Hard-flat mark | Deployed size | Gross P&L | MAE | MFE |
|---|---|---|---|---|---|---|
| NIFTY 24200/24250 BPS | 10.5 pts | 6.2 pts | 4 lots | +₹1,118 | −₹78 | +₹1,430 |
| SENSEX 80500/80600 BPS | 21.3 pts | 15.8 pts | 6 lots | +₹660 | −₹240 | +₹840 |

Note: these are the candidates REJECTED during analysis and never written up in the tread log.
```

### In learning.md

```markdown
- **No trade today — <reason code>.** <one-line summary of the failing filter and the fix>
```

Then proceed to `session-close` to complete the learning.md.

---

## Logging

After completing, append to today's tread.md:

```
09:45 — no-trade: reason "Too small" — sessions_to_expiry = 3 for all indexes → Gate 1 ⛔.
        Will re-enter tomorrow (expiry eve).
```
