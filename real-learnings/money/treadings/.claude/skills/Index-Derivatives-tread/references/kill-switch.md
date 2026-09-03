# kill-switch.md — Trend-day kill switch (Gate 3)

**Loaded by:** find-trade, followup

Canonical definitions used identically in both entry (find-trade) and recheck (followup). Scored 0–3, escalates on 2–3.

---

## The three markers — definitions

| # | Marker | FIRES when |
|---|---|---|
| **M1** | **Opening-range break** | **Two consecutive 15-min candles close outside the 9:15–9:45 OR high/low.** A wick outside is not a break. |
| **M2** | **VWAP one-sidedness** | Price on one side of VWAP for **≥ 45 minutes** with no close through it, **and** VWAP itself sloping the same way. |
| **M3** | **OI confirming direction** | Price and OI aligned per the §8.13 matrix — falling price + rising CE OI (short buildup above = bearish), or rising price + rising PE OI (short buildup below = bullish). Compare each strike's OI to its **`oi_day_high`**, not to the morning print. |

⛔ **VIX is NOT a fourth marker.** VIX is Go/No-Go row 1 and an exit trigger in followup Step 8. Counting it here silently made the switch a 4-of-3 instrument on multiple sessions.

⚠️ **M2 is permanently unmeasurable for cash indices.** Kite returns `volume: 0` for `BSE:SENSEX` and the other cash indices, so VWAP cannot be computed. **The switch is a 2-of-3 instrument there. Log M2 as a gap; never score it green.** (Found 03-Sep-2026.)

---

## Scoring and escalation

| Score | Verdict | Action |
|---|---|---|
| **0/3** | Not a trend day | Proceed to Gate 4. ⚠️ **0/3 means "not a trend day". It NEVER means "bullish", and it is NEVER a reason to hold a losing position.** |
| **1/3** | Elevated caution | Proceed, but the entry filters must all pass with margin — no borderline calls. |
| **2/3** | **Trend day** | ⛔ **No NEW position.** If already in one, the untested side is the only survivable side; exit if the position is on the wrong side of the trend. |
| **3/3** | **Abort** | ⛔ No new position, and **close any open structure immediately at market**, profitable or not. |

---

## Re-check discipline (for followup)

Every scheduled recheck re-pulls **all** of:
- Spot / VWAP (from 15-min candles)
- VIX (not a marker, but an exit trigger)
- ATM straddle
- **OI and `oi_day_high` at the short strikes and the OI walls**

**Compare OI to its day high, not to the morning print.** On 01-Sep-2026 the 24,000 PE wall went 57.76M → 32.8M (−43%) in 50 minutes. Measured check-to-check that reads as −17% per 30-min window and never crosses a −20% trigger. Against `oi_day_high` it crosses at the first check.

**Check times:** see [`TRADING_CONSTANTS.md` §7](../../../../TRADING_CONSTANTS.md). Currently: 9:45 / 10:30 / 11:30 / 1:30. If those ever differ from this file, TRADING_CONSTANTS.md wins.

---

## Data requirements

- **15-min OHLC candles** for the index (last 2 hours) — from Kite `get_historical_data`
- **OI per strike** — from Kite `get_quotes` (includes `oi_day_high`) or Dhan chain
- **VWAP** — compute from the 15-min candles: `Σ(typical_price × volume) / Σ(volume)`, where `typical_price = (high + low + close) / 3`

**For cash indices (SENSEX):** Kite returns `volume: 0` → VWAP is not computable. **M2 must be logged as a gap, never scored green or red.**

---

## The §8.13 Price vs OI matrix (for M3)

| Price | OI | Interpretation | Signal |
|---|---|---|---|
| ↑ | ↑ | Long buildup | Bullish |
| ↑ | ↓ | Short covering | Bullish (weaker) |
| ↓ | ↑ | Short buildup | Bearish |
| ↓ | ↓ | Long unwinding | Bearish (weaker) |

**For M3:** look for the **strong** signals (price and OI moving together) at the relevant strikes:
- Bearish trend → CE OI rising at strikes above spot (short calls being added as resistance)
- Bullish trend → PE OI rising at strikes below spot (short puts being added as support)

---

## Why this exists (01-Sep-2026, −₹15,564)

On 01-Sep-2026:
- NIFTY opened 24,185, fell to 23,980 by 13:30 (−205 pts, −0.85%)
- A Bull Put Spread 24,000/23,800 was entered on a 0/3 kill switch
- Pro desk was net short 1,09,003 calls = a hard ceiling (Gate 5 failure)
- **The structure fought both the intraday trend and the participant positioning**

The kill switch is a regime gate, not a structure veto. 0/3 means "not a trend day" → neutral structures are permitted. **It says nothing about which side to sell.** That is Gate 5's job.

---

## Reporting format

```
Kill switch: <N>/3
  M1 Opening-range break: [YES/NO] — <detail>
  M2 VWAP one-sidedness: [YES/NO/n/a — cash index] — <detail>
  M3 OI confirming direction: [YES/NO] — <which strikes, dOI vs day high>

Verdict: [proceed | elevated caution | no new position | abort]
```

Always name the specific observation supporting each marker. "OI confirming" without the strike and the `oi_day_high` comparison is not a recheck, it's a memory.

---

## Cross-reference

- Full definitions + the 4-rung escalation: `strategy_ref_book.md` §8.13
- Check times: [`TRADING_CONSTANTS.md` §7](../../../../TRADING_CONSTANTS.md)
- OI wall erosion thresholds (−20% → exit): `followup.md` Step 6
