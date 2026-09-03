# The trade log — minimum fields

**Loaded by:** `find-trade` (fields 1–9 are written **before** entry), `session-close` (the rest).
**Purpose:** the closed field list that makes the record teach something.

It must be completable in under three minutes. **Half the `learning.md` files in this repo are 0 bytes** —
the compounding mechanism is currently off for half of all sessions. A short log that always gets written
beats a rich one that does not.

---

## Fields

```
 1  date · index · expiry · SESSIONS to expiry
 2  entry HH:MM · exit HH:MM
 3  short strike · long strike · width · lots
 4  entry credit/lot (pts) · total net credit (₹)
 5  ★ CREDIT ÷ WIDTH ratio            ← this is your delta. Sort losers by it after 30 trades.
 6  spot · forward F = K + C − P · India VIX · ATM straddle — all at entry
 7  planned stop: spread price · short-leg trigger · ₹ · % of capital
       ⛔ RECORDED BEFORE ENTRY. Written after the fact, it is a rationalisation, not a plan.
 8  structural max loss ₹ and % of capital
 9  ★ SL ORDER ID + the timestamp it read "Trigger Pending"
       ⛔ Blank = the trade was unauthorised, regardless of its P&L.
10  exit reason — EXACTLY ONE CODE, no free text:   TARGET / STOP / TIME / VIOLATION
       Free text is where rationalisation lives. A closed vocabulary means VIOLATION cannot be
       relabelled "discretionary exit based on price action."
11  P&L: gross · costs · net · % of capital · R-multiple (net ÷ planned stop)
12  ★ MAE and MFE — the worst and best spread price seen while in the trade
       MAE on winners tells you if the stop is too tight; MFE on losers tells you what you gave
       back. Without both, every parameter change is a guess.
13  filters: pass/fail, NAMING the failing filter
14  ★ LOG THE NO-TRADE DAYS TOO, with the failing filter code.
       ~16 of 21 sessions were no-trades. That is 75% of the decision record and it is currently
       invisible. If one filter vetoes 20 days running, either it is miscalibrated or the strategy
       has no market — and you cannot tell which without this row.
```

**Score at the mandated exit time (TC §7), never at a mid-session snapshot**, and report MAE /
exit-mark / MFE **at max permitted size — including for candidates you rejected in analysis and never
wrote up.** Otherwise the record cannot tell a good veto from a timid one.

---

## Reviewing the record

- **Report the violation count ABOVE P&L in every weekly review.** Violations lead; P&L lags.
- **Win rate is a vanity metric** (§8.15). R-multiple distribution and MAE/MFE are not.
- **Frequency governor:** fewer than 4 trades in a month → the filters are too tight. Review at month
  end. ⛔ **Never loosen a filter mid-month.**
- For the first three months the target is a **violation count of zero**, not a rupee number.

---

## The four session artefacts — non-negotiable

Every session produces all four. Learning is part of every session, not a separate request.

| # | Artefact | Content |
|---|---|---|
| 1 | `my-treads/<Month>-2026/<DD-MM-YYYY>/DD-MM-YYYY-tread.md` | append-only: all analysis, decisions, fills, monitoring checks |
| 2 | `…/DD-MM-YYYY-learning.md` | bullet lessons after the close — **wins AND no-trades** |
| 3 | `docs/mcp-usage-log.md` §4 | one new session row |
| 4 | `my-treads/fii_dii_data_2026.md` | today's FII/DII appended, if available |

No exceptions.
