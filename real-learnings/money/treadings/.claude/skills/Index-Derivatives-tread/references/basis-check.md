**Sub-command:** basis-check

Gate 2 — forward basis, chain-trust check, and realised-vs-implied volatility.

---

## Trigger

"what is the forward", "check basis", "basis check", "is the chain accurate"

## Method

Fetch the option chain for the specified index + expiry from Dhan (see `references/dhan-api.md`). Then compute:

### 1. Forward from put-call parity

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

### 2. Vendor sanity check

**One strike + one expiry = ONE IV. CE IV ≠ PE IV → the Greeks are broken.**

⛔ **Dhan's Greeks and IV are computed off SPOT, not the forward** — populated, plausible and wrong. Deep-ITM legs return IV/Δ/Θ = 0. We have **no trustworthy Greeks source**. See [`TRADING_CONSTANTS.md` §14](../../../../TRADING_CONSTANTS.md).

✅ **Permitted (arithmetic, not models):**
- Put-call parity `F = K + C − P`
- ATM-forward straddle relation `≈ 0.7979 × F × σ√T`
- HV from Kite candles
- §8.7.3 straddle-rule strikes

⛔ **Not permitted:** solving Black-Scholes for Δ/Γ/Θ/V, or presenting a derived figure as a vendor figure.

### 3. ★ The arithmetic delta substitute

**Use `credit ÷ width` wherever the book asks for a delta.** As width narrows, a vertical's price → Δ × W exactly. Model-free, vendor-free, unbreakable.

From [`TRADING_CONSTANTS.md` §14](../../../../TRADING_CONSTANTS.md):

| Book says | Use instead |
|---|---|
| Sell the 16Δ strike | §8.7.3 straddle rule on the parity forward `F` |
| Untested short "below 7Δ" | Untested short's mark ≤ **25%** of its entry premium |
| Short "reaches 30Δ" | Tested short's mark ≥ **2.5×** its entry premium |
| Net position delta > ±0.15/lot | Tested short's mark ≥ **3×** the untested short's mark |
| Deep-ITM rows showing Δ=0 / IV=0 | **Discard the row** — missing data, not zero risk |

## Notes on basis

**Near-term basis is large and tenor-dependent.** 28-Aug: NIFTY +82 (4d), SENSEX +283 (6d), BANKNIFTY +382 (32d).

- **The true ATM is the forward, not spot** — often more than one strike away.
- **Recheck every session; never reuse yesterday's basis.**
- ⛔ **GIFT Nifty is a futures price — never compare it to spot.**

## ★ Gate-2 rider — Realised-vs-Implied (added 03-Sep-2026)

**Run this BEFORE pricing any strike.** A low VIX is a low-IMPLIED signal, not a cheap-vol signal.

⛔ **Use the form that matches the DECLARED holding period** (TC §10b). An intraday pts/min ratio says
nothing about a 10-session hold, and an annualised ratio says nothing about this afternoon. **Log which
form was used.**

**Form A — intraday-declared trade:**
```
REALISED = (day_high − day_low) ÷ minutes_elapsed_since_open
IMPLIED  = (ATM-forward straddle × ~1.25) ÷ minutes_remaining_to_close
RATIO    = REALISED ÷ IMPLIED
```

**Form B — multi-session declared hold** (this is also where BANKNIFTY's `σ_ATM` comes from):
```
1. F      = K + CE − PE at the ATM strike                      (parity; permitted under SI-5)
2. σ_ATM  = ATM_straddle ÷ (0.7979 × F × sqrt(N / 252))        N = DECLARED sessions, not to expiry
3. σ_real = stdev(daily log returns) × sqrt(252), on THREE windows: 252 / 120 / 60 sessions
             → Kite get_historical_data, interval "day".  ⚠️ dates need "YYYY-MM-DD HH:MM:SS".
4. RATIO  = σ_real ÷ σ_ATM   — compute all three, TAKE THE WORST
```
**Check `σ_ATM` against the per-index vol band in TC §6 row 8 before anything else.** For BANKNIFTY
this is the *only* implied vol available — ⛔ **India VIX is NIFTY's measure and does not price it.**

**Report all three windows.** One window is a choice of regime, and choosing the flattering one is how
a negative VRP gets traded. *04-Sep-2026 BANKNIFTY: σ_ATM 11.41% against realised 16.61 / 20.75 /
13.45% → ratios 1.46 / 1.82 / 1.18. Negative on every window; the 60-session number alone would have
looked like the mildest possible fail rather than the flat block it was.*

**The three bands live in [`TRADING_CONSTANTS.md` §10b](../../../../TRADING_CONSTANTS.md).** Read them there; do not quote them from memory.

**At the top band, VRP is negative before friction and no credit structure is paid. Stop there; do not price strikes** — and log the stand-down as `UNPAID`, never as "Too thin". "Too thin" prescribes a different structure; nothing about the strike, width or size fixes negative VRP.

On 03-Sep SENSEX realised 232.98 pts in 98 min (2.38 pts/min) against an implied ~1.40 pts/min — **1.7×** — and all six candidates failed simultaneously. That is the signature of negative VRP, not of a bad strike choice.

⚠️ **A low VIX hides high realised vol.** VIX 11.10 read as "calm" while the tape delivered a 233-pt range. Low IV with high RV is the worst tape for a seller and looks identical to the best one on a VIX quote alone.

## ★ Score candidate strikes against the day's HIGH/LOW, never spot

A stop inside the day's realised range is a stop the tape has already hit once.

## Output format

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

Realised-vs-implied check:
  Day high/low: <H>/<L> = <range> pts over <M> min → <realised> pts/min
  ATM straddle × 1.25 = <X> pts over <N> min remaining → <implied> pts/min
  Ratio: <realised/implied>   → band per TC §10b
  → <verdict: ✅ PAID | ⚠️ THIN | ⛔ UNPAID → no trade, reason code UNPAID>
```

---

## Logging

After completing, append to today's tread.md:

```
09:22 — basis-check: NIFTY F=24,119, basis +52 (+0.22%) → delta band unreliable, use straddle rule.
        Realised 1.89 pts/min vs implied 1.52 → VRP positive ✅
```
