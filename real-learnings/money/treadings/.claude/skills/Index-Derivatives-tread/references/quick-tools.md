# Quick Tools — size-it · check-expiry · basis-check · no-trade

Four fast utilities. Read the relevant section based on the sub-command.

---

## size-it — Lot Sizing Calculator

**Trigger:** "how many lots", "size it", "sizing for X structure", "lot count"

**Input (ask user if not provided):**
- Structure type (bear call spread / bull put spread / iron condor / etc.)
- Short strike and long strike
- Net credit in points
- Stop type: k=1.5 (combined premium reaches 1.5× credit) or k=2.0 (reaches 2× credit)
- Index (NIFTY/BANKNIFTY/SENSEX) → determines lot size

**Lot sizes:** NIFTY=65 · BANKNIFTY=30 (monthly only) · SENSEX=20

**Output table:**

```
Structure: <type> <short>/<long>  |  Credit: <X> pts  |  k=<1.5 or 2.0>
Loss at stop per lot = (k-1) × credit × lot_size

| Option | Lots | Loss at stop | Gross if full capture | Margin (est.) |
|---|---|---|---|---|
| Conservative | <N> | ₹8,000-10,000 | ₹<X> | ~₹<Y> |
| Standard | <N> | ₹15,000-20,000 | ₹<X> | ~₹<Y> |
| Aggressive | <N> | ₹25,000-35,000 | ₹<X> | ~₹<Y> |

Stop trigger: spread reaches <k × credit> pts
Price abort: <underlying> 15-min close through <short strike>
Max deployment check: <N> lots × margin per lot ≤ ₹4.9L (70% of ₹7.02L)
```

Also show: "At 1 DTE flat market (20% capture): ₹X net. At directional move of Y pts: ₹Z net."

---

## check-expiry — Expiry Dates & Calendar Feasibility

**Trigger:** "when does NIFTY expire", "check expiry", "expiry dates", "how many sessions left"

Fetch expiry lists for all 3 indexes in parallel:
```
NIFTY:    UnderlyingScrip=13, UnderlyingSeg=IDX_I
BANKNIFTY: UnderlyingScrip=25, UnderlyingSeg=IDX_I
SENSEX:   UnderlyingScrip=51, UnderlyingSeg=IDX_I
```

Calculate trading sessions to each nearest expiry (count Mon-Fri, skip known holidays).

Output:
```
| Index | Nearest expiry | Calendar days | Trading sessions | §8.11.6 verdict |
|---|---|---|---|---|
| NIFTY 50 | <date> | <N> | <M> | <verdict> |
| SENSEX | <date> | <N> | <M> | <verdict> |
| BANKNIFTY | <date> (monthly) | <N> | <M> | <verdict> |

§8.11.6 verdicts:
  0-DTE (expiry day): full theta today — 1% IS achievable intraday ✅
  1-DTE (expiry eve): delta-driven — 1% needs directional move ⚠️
  2-3 DTE: moderate theta — 0.5-0.75% realistic intraday ⚠️
  4+ DTE: low theta — near-breakeven intraday, better for positional ⛔
```

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
| §7 Go/No-Go | <N> Red |
| §8.11.6 Feasibility | <verdict> |
| §8.11.7 Noise floor | <pass/fail> |

**What would change this:** <specific condition — e.g., "VIX drops below 12", "tomorrow is expiry day", "use 24,300 strike instead">

**Deployed ₹0. Risked ₹0.**
```

Also score the no-trade neutrally (per §8.15.4):
- Price the declined structures at bid/ask at the decision time
- Record what they would have returned at the §8.3 mandated exit time
- Note as MAE/MFE if observable

Then proceed to `session-close` to write the learning.md.

---

## Common to all quick tools

After any quick tool completes, append a brief record to today's tread.md. Even a one-liner: "14:15 — size-it: 24200/24400 BCS, k=1.5 → Conservative 8L / Standard 15L / Aggressive 22L."

This keeps the session log complete without extra effort.
