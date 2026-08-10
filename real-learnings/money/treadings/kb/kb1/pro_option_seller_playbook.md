# Pro Option Seller Playbook — NSE/BSE Index Options
## Capital Base: ₹20,00,000 (₹20 Lakhs) — 100% Dedicated Trading Capital

> **Role:** This document is written from the perspective of a practicing pro option seller in Indian markets — not bookish theory. Every number is tied to ₹20L capital, realistic margins, and 2%/week target.
>
> **Capital assumption:** ₹20,00,000 is the full dedicated options trading account. Personal living expenses, emergency fund, and mutual fund SIPs come from a completely separate fund. This ₹20L is only for F&O — it never gets used for anything else.
>
> **Why this changes everything:** When your living needs don't depend on this capital, you can run a higher margin utilization (65% vs 50%), hold positions through intraday dips without panic, and take the full-size trades that produce meaningful weekly income.
>
> **Scope:** NIFTY 50 (NSE), SENSEX (BSE). Strategy logic applies to BANKNIFTY as a variation.
>
> **Target:** ₹40,000/week net profit = 2% on ₹20L deployed capital (across good weeks).

---

## Index

- [1. Honest Expectation Setting](#1-honest-expectation-setting)
- [2. Capital Allocation Framework](#2-capital-allocation-framework)
- [3. Contract Specs to Check Every Week](#3-contract-specs-to-check-every-week)
- [4. Strategy 1: Iron Butterfly — The Bread-and-Butter Trade](#4-strategy-1-iron-butterfly--the-bread-and-butter-trade)
- [5. Strategy 2: Iron Condor — The Conservative Variant](#5-strategy-2-iron-condor--the-conservative-variant)
- [6. Strategy 3: Credit Spreads — The Directional Seller](#6-strategy-3-credit-spreads--the-directional-seller)
- [7. Bonus: Expiry-Day Strangle Sell — The 2-Hour Trade](#7-bonus-expiry-day-strangle-sell--the-2-hour-trade)
- [8. Two-Trade Weekly Calendar (NIFTY + SENSEX)](#8-two-trade-weekly-calendar-nifty--sensex)
- [9. VIX Filter — The One Rule That Separates Pros from Amateurs](#9-vix-filter--the-one-rule-that-separates-pros-from-amateurs)
- [10. Pre-Trade Checklist (Run Before Every Entry)](#10-pre-trade-checklist-run-before-every-entry)
- [11. Exit Rules (Non-Negotiable)](#11-exit-rules-non-negotiable)
- [12. Annual Return Projections](#12-annual-return-projections)
- [13. Risk Management for ₹20L Dedicated Capital](#13-risk-management-for-20l-dedicated-capital)
- [14. Common Mistakes and How Pros Avoid Them](#14-common-mistakes-and-how-pros-avoid-them)

---

## 1. Honest Expectation Setting

Before the numbers: **2% weekly ≠ 2% every week.**

| Scenario | What it looks like |
|----------|-------------------|
| 2% weekly compounded = 104% annual | Impossible to achieve consistently. Nobody does this. |
| Realistic good year | 35–50% on capital. ~30 strong winning weeks, ~14 moderate, ~8 losing weeks. |
| Realistic average year | 20–30% on capital. |
| Realistic bad year | 5–12% on capital. Rare but happens during election years, global crisis months. |

**Why the gap?** India VIX overestimates actual realized volatility ~75–80% of the time. That structural overpricing is why option sellers win more weeks than they lose. But losing weeks do exist — and losing weeks are larger in rupee terms than winning weeks unless stop-losses are followed without exception.

**Your actual weekly target with ₹20L (dedicated):**

| Week Type | Frequency | Weekly P&L |
|-----------|-----------|-----------|
| Strong Win — all 3 trades fire | ~30% of weeks | ₹40,000–₹50,000 |
| Moderate Win — 2 trades fire | ~30% of weeks | ₹20,000–₹30,000 |
| Flat — 1 trade or mixed signals | ~20% of weeks | ₹0–₹12,000 |
| Loss — stop-loss triggered | ~20% of weeks | -₹40,000 to -₹80,000 |

**Annual net (realistic case): ₹7,00,000–₹9,00,000 = 35–45% on ₹20L**

---

## 2. Capital Allocation Framework

**Total Capital: ₹20,00,000 — Pure Trading Account**

```
₹20,00,000  (this is 100% trading capital — personal fund is separate)
│
├── ACTIVE MARGIN (max 65%)         → up to ₹13,00,000
│   Split across:
│   ├── NIFTY Iron Butterfly (primary)  → ₹8,64,000  (12 lots × ₹72,000/lot)
│   └── SENSEX Iron Butterfly (secondary) → ₹4,05,000  (9 lots × ₹45,000/lot)
│   Combined peak margin:             ₹12,69,000 = 63.5% of ₹20L ✓
│
└── TRADING BUFFER (min 35%)         → ₹7,00,000 – ₹7,31,000
    Purpose (purely trading-related):
    ├── Cover MTM losses mid-week without a margin call
    ├── Add a hedge leg if trade goes off-center
    ├── Roll a losing leg to next week's expiry if needed
    └── Fund a 3rd trade (expiry-day strangle) when NIFTY IB exits early
```

**Why 65% margin is safe here (vs 50% in mixed-fund accounts):**
- Your living expenses are funded separately — zero psychological pressure to close a position early just because you "need the money"
- ₹7L buffer covers 9–10 consecutive days of worst-case MTM on a 12-lot Iron Butterfly before a stop-loss would trigger
- If capital grows above ₹20L, scale up gradually (add 1 lot per additional ₹1.5L)

**The Golden Rule:** 65% is the hard ceiling for active margin. Never exceed ₹13L in combined open positions. The moment you breach this, you are trading with survival money — which distorts every exit decision.

---

## 3. Contract Specs to Check Every Week

> Lot sizes and margins change by SEBI/exchange circulars. Verify before every trade week at broker platform or NSE contract specs page.

| Index | Exchange | Expiry Day | Lot Size (verify) | Settlement |
|-------|----------|------------|-------------------|------------|
| NIFTY 50 | NSE | Tuesday (weekly) | 25 units | Cash settled |
| SENSEX | BSE | Thursday (weekly) | 10 units | Cash settled |
| BANKNIFTY | NSE | Wednesday (verify) | 15 units | Cash settled |

**Margin reference (approximate — verify live with broker):**

| Strategy | Per Lot Margin (NIFTY) | Per Lot Margin (SENSEX) |
|----------|----------------------|------------------------|
| Iron Butterfly (hedged) | ₹65,000–₹80,000 | ₹40,000–₹55,000 |
| Iron Condor (hedged) | ₹55,000–₹70,000 | ₹35,000–₹45,000 |
| Credit Spread (Bull Put / Bear Call) | ₹18,000–₹25,000 | ₹10,000–₹15,000 |
| Expiry-day Strangle (hedged) | ₹40,000–₹50,000 | — |
| Naked Short Strangle (unhedged) | ₹1,80,000–₹2,40,000 | — |

**Key insight:** Hedged structures (Iron Butterfly, Iron Condor) cost **3–4× less margin** than naked selling. That is how you run 12 lots on ₹20L instead of 2–3 lots with the same capital.

---

## 4. Strategy 1: Iron Butterfly — The Bread-and-Butter Trade

**What it is:** Sell ATM straddle (CE + PE at same strike) + buy wings for protection. Converts a naked unlimited-loss straddle into a defined-risk structure.

**Who uses it:** 70% of serious retail option sellers in India. Most consistent income strategy for index sellers.

**Why it works:** IV overpricing means the ATM straddle you sell is statistically overpriced ~75% of the time. Wings cost 15–18% of credit but cap max loss to a manageable number.

---

### Full Trade Example — NIFTY Iron Butterfly

**Setup:**
```
Date: Monday (entry for Tuesday expiry)
Entry time: 10:15–10:30 AM (after open volatility settles)
NIFTY Spot: 24,500
VIX: 14.5 (suitable range — see §9)
```

**Legs:**

| Leg | Action | Strike | Type | Premium | Purpose |
|-----|--------|--------|------|---------|---------|
| 1 | Sell | 24,500 | CE | ₹120 | Primary credit |
| 2 | Sell | 24,500 | PE | ₹110 | Primary credit |
| 3 | Buy | 25,000 | CE | ₹20 | Upside protection (500 pts away) |
| 4 | Buy | 24,000 | PE | ₹18 | Downside protection (500 pts away) |

```
Gross credit collected:  120 + 110 = 230 points
Wings cost paid:           20 +  18 =  38 points
─────────────────────────────────────────────────
Net credit (per unit):   230 - 38  = 192 points
Per lot (25 units):      192 × 25  = ₹4,800
```

**For ₹20L dedicated trading capital — 12 lots:**

```
Margin per lot:             ~₹72,000 (hedged Iron Butterfly)
Total margin blocked:    12 × ₹72,000 = ₹8,64,000 (43.2% of ₹20L)
Trading buffer remaining:  ₹20,00,000 - ₹8,64,000 = ₹11,36,000

Gross credit (12 lots):  ₹4,800 × 12 = ₹57,600
Target exit at 50%:      ₹57,600 × 50% = ₹28,800

Estimated charges (12 lots round trip):
  Brokerage (₹20/order × 8 orders):         ₹160
  STT on short legs at entry:              ~₹900
  Exchange charges + SEBI fees:           ~₹1,100
  GST (18% on brokerage + exchange):      ~₹240
  Stamp duty:                              ~₹120
  Total charges:                         ~₹2,520

Net profit (if 50% exit achieved):  ₹28,800 - ₹2,520 = ₹26,280 ≈ ₹26,000
As % of ₹20L capital:               ₹26,000 / ₹20,00,000 = 1.3%
```

**Payoff at expiry (12 lots):**

| NIFTY at Expiry | Trade Outcome | Net P&L (12 lots) |
|----------------|--------------|-------------------|
| 24,500 (at ATM) | Max profit zone | +₹57,600 |
| 25,000 (upper wing) | Breakeven at wing | ~₹0 |
| 24,000 (lower wing) | Breakeven at wing | ~₹0 |
| 25,200 (above upper wing) | Maximum loss capped | -(500-192) × 25 × 12 = **-₹92,400** |
| 23,800 (below lower wing) | Maximum loss capped | **-₹92,400** |
| **50% profit exit (any day)** | **Most common real exit** | **+₹26,000 net** |

> **Note:** You never wait for expiry. Exit at 50% profit or stop-loss. The expiry payoffs above are theoretical boundaries.

**Strike selection for wings (adjust by VIX):**

| VIX Level | Wing Distance | Why |
|-----------|--------------|-----|
| VIX 11–13 | 400 pts | Low premium; tighter wings still give acceptable credit |
| VIX 13–18 | 500 pts (standard) | Normal setup |
| VIX 18–22 | 600–700 pts | Market moving more; need more breathing room |
| VIX > 22 | Do not run Iron Butterfly | Switch to Iron Condor (OTM strikes) |

---

## 5. Strategy 2: Iron Condor — The Conservative Variant

**What it is:** Instead of selling ATM straddle, sell OTM PE spread + OTM CE spread. Less credit collected but higher probability of expiring in the profit zone.

**When to use over Iron Butterfly:**
- Market has been trending (not perfectly sideways)
- VIX is in the 18–22 range (Iron Butterfly too risky at ATM)
- You want a wider profit zone and can accept less credit

---

### Full Trade Example — NIFTY Iron Condor

**Setup:**
```
Date: Monday entry for Tuesday expiry
NIFTY Spot: 24,500
VIX: 17.5 (slightly elevated — Iron Condor preferred over IB)
Expected range: 23,900 – 25,100 (based on market view)
```

**Legs (1 Standard Deviation away on each side = ~±1.5–2% for weekly):**

| Leg | Action | Strike | Type | Premium | Purpose |
|-----|--------|--------|------|---------|---------|
| 1 | Sell | 24,900 CE | OTM CE | ₹45 | Upper body (credit) |
| 2 | Buy | 25,200 CE | Far OTM CE | ₹15 | Upper wing (protection) |
| 3 | Sell | 24,100 PE | OTM PE | ₹40 | Lower body (credit) |
| 4 | Buy | 23,800 PE | Far OTM PE | ₹13 | Lower wing (protection) |

```
CE spread credit:    45 - 15 = 30 points
PE spread credit:    40 - 13 = 27 points
──────────────────────────────────────────
Total net credit per unit:   57 points
Per lot (25 units):     57 × 25 = ₹1,425
```

**For ₹20L dedicated capital — 18 lots (standalone):**

```
Margin per lot (Iron Condor):     ~₹62,000
Total margin blocked:          18 × ₹62,000 = ₹11,16,000 (55.8% of ₹20L)
Buffer remaining:              ₹8,84,000

Gross credit (18 lots):        ₹1,425 × 18 = ₹25,650
Target exit at 50%:            ₹12,825
After charges (~₹3,000):       ₹9,825 ≈ ₹10,000

As % of ₹20L = 0.5% → not the primary income driver alone
```

**The Iron Condor reality:** Per-lot credit is much lower than Iron Butterfly. Its role is:
- **Primary trade** only on high-VIX weeks where Iron Butterfly is too risky
- **Supplementary** alongside Iron Butterfly on SENSEX Thursday

---

## 6. Strategy 3: Credit Spreads — The Directional Seller

**What it is:** Sell one OTM option + buy a further OTM option for protection. You take a clear directional view and collect premium for being right.

**When to use:** When you have a strong directional conviction — slightly bullish (Bull Put Spread) or slightly bearish (Bear Call Spread). Not a mechanical weekly trade; fired only when the market view is clear.

---

### 6A. Bull Put Spread (Slightly Bullish Market View)

**Trade logic:** NIFTY will stay above a key support level this week. Sell PE above that support, buy farther OTM PE for protection.

**Example:**
```
NIFTY Spot: 24,500
Key support: 24,000 (3-day OI buildup, PCR > 1.2)
Market view: Slightly Bullish — support will hold
```

| Leg | Action | Strike | Type | Premium |
|-----|--------|--------|------|---------|
| 1 | Sell | 24,200 PE | OTM PE | ₹55 |
| 2 | Buy | 23,900 PE | Far OTM PE | ₹20 |

```
Net credit per unit:    55 - 20 = 35 points
Max profit per unit:    35 points  (NIFTY stays above 24,200)
Max loss per unit:      300 - 35 = 265 points
Break-even:             24,200 - 35 = 24,165

Per lot (25 units):
  Net credit:   35 × 25 = ₹875
  Max profit:   ₹875
  Max loss:     265 × 25 = ₹6,625
```

**For ₹20L dedicated capital — 22 lots:**

```
Margin per lot (credit spread): ~₹22,000
Total margin blocked:        22 × ₹22,000 = ₹4,84,000 (24.2% of ₹20L)
Remaining buffer:            ₹15,16,000

Gross credit (22 lots):      ₹875 × 22 = ₹19,250
After charges (~₹2,000):     ₹17,250

Running alongside NIFTY IB (₹8.64L margin):
  Combined margin: ₹8.64L + ₹4.84L = ₹13.48L = 67.4% ← just over limit
  → Scale credit spread to 18 lots when running alongside IB:
  18 lots: ₹875 × 18 = ₹15,750 → after charges ₹13,500 (0.67% of ₹20L)
  Combined margin: ₹8.64L + ₹3.96L = ₹12.6L = 63% ✓
```

**Stop-loss:** If NIFTY closes below the support level (24,000 in this example) on any day, exit the spread immediately. Do not wait for the spread to reach max loss.

---

### 6B. Bear Call Spread (Slightly Bearish / Resistance Holding)

**Trade logic:** NIFTY has clear overhead resistance that will not break this week.

**Example:**
```
NIFTY Spot: 24,500
Resistance: 24,900 (heavy CE OI, FII short call buildup)
Market view: Slightly Bearish — 24,900 resistance holds
```

| Leg | Action | Strike | Type | Premium |
|-----|--------|--------|------|---------|
| 1 | Sell | 24,800 CE | OTM CE | ₹50 |
| 2 | Buy | 25,100 CE | Far OTM CE | ₹18 |

```
Net credit per unit:    50 - 18 = 32 points
Max profit per unit:    32 points
Max loss per unit:      300 - 32 = 268 points
Break-even:             24,800 + 32 = 24,832

Per lot (25 units):
  Net credit:   32 × 25 = ₹800
  Max loss:     268 × 25 = ₹6,700
```

**For ₹20L dedicated capital — 18 lots (alongside IB):**

```
Margin per lot: ~₹22,000
Total margin: 18 × ₹22,000 = ₹3,96,000
Combined with IB: ₹8.64L + ₹3.96L = ₹12.6L = 63% ✓

Gross credit (18 lots): ₹800 × 18 = ₹14,400
After charges:          ~₹12,000 (0.6% of ₹20L)
```

**Credit Spreads + Iron Butterfly combined — a strong week:**

```
Iron Butterfly (NIFTY, 12 lots, Tue):    +₹26,000
Bear Call Spread (NIFTY, 18 lots):       +₹12,000
────────────────────────────────────────────────
Week total:                              +₹38,000 = 1.9% on ₹20L
Combined margin:                          ₹12.6L = 63% ✓
```

Run both simultaneously only when:
- Market view has clear directional bias confirmed by PCR + FII OI
- Combined margin ≤ 65% of ₹20L = ₹13L
- VIX is 13–18 (not elevated)

---

## 7. Bonus: Expiry-Day Strangle Sell — The 2-Hour Trade

**What it is:** Sell OTM CE and PE on Tuesday morning (NIFTY expiry day), collect expiry-day theta in 2 hours, exit at 50% profit.

**When it fires:** Only when the NIFTY Iron Butterfly has already closed at 50% profit (Monday or Tuesday morning). The freed ₹8.64L margin is then redeployed into this short trade.

**Why expiry day is special:** Theta decay is exponential on expiry day. An OTM option at ₹30 on Monday 3 PM can fall to ₹8–10 by Tuesday 11 AM if NIFTY stays range-bound. You collect that in 2 hours.

**Entry rule:** Enter only after 9:45 AM. The 9:15–9:45 opening window has gap/whipsaw risk that will stop you out before you collect any theta.

---

### Full Trade Example — NIFTY Expiry Day Strangle

```
Date: Tuesday (NIFTY expiry day)
Entry time: 9:45–10:00 AM
Condition: NIFTY Iron Butterfly already closed at 50% profit
NIFTY Spot: 24,500 | VIX: 14
```

| Leg | Action | Strike | Type | Premium | Note |
|-----|--------|--------|------|---------|------|
| 1 | Sell | 24,700 CE | OTM CE | ₹28 | 200 pts away from spot |
| 2 | Sell | 24,300 PE | OTM PE | ₹25 | 200 pts away from spot |
| 3 | Buy | 24,900 CE | Far OTM CE | ₹8 | Wing — caps upside loss |
| 4 | Buy | 24,100 PE | Far OTM PE | ₹7 | Wing — caps downside loss |

```
Net credit per unit:     (28 + 25) - (8 + 7) = 38 points
Per lot (25 units):      38 × 25 = ₹950
```

**For ₹20L dedicated capital — 15 lots (using freed IB margin):**

```
Margin per lot (hedged expiry strangle): ~₹45,000
Total margin blocked:   15 × ₹45,000 = ₹6,75,000 (33.75% of ₹20L)
(IB is already closed — this replaces it in the capital stack)

Gross credit (15 lots):  ₹950 × 15 = ₹14,250
Target exit at 50%:      ₹7,125
After charges (~₹1,800): ₹5,325 ≈ ₹5,500
```

**Combined week (IB closed early + expiry strangle):**

| Trade | Entry Day | Lots | Net P&L |
|-------|-----------|------|---------|
| Iron Butterfly | Monday 10:15 AM | 12 | +₹26,000 |
| Expiry Strangle | Tuesday 9:45 AM | 15 | +₹5,500 |
| **NIFTY week total** | | | **+₹31,500** |

**Hard exit rules for expiry day:**
- 50% profit hit → exit all legs immediately, no exceptions
- NIFTY moves 150+ points against short strike by 11 AM → close full position
- Compulsory close: 2:45 PM regardless — do NOT hold through final 15 minutes

---

## 8. Two-Trade Weekly Calendar (NIFTY + SENSEX)

Running NIFTY (Tuesday expiry) + SENSEX (Thursday expiry) gives two independent income events every week. The capital recycles between the two.

```
MONDAY
  ├── 9:00 AM  : Review FII/DII data, check VIX, form market view
  ├── 9:30 AM  : NIFTY option chain — PCR, OI at key strikes, GIFT Nifty gap
  └── 10:15 AM : Enter NIFTY Iron Butterfly (12 lots, ₹8,64,000 margin)

TUESDAY (NIFTY Expiry)
  ├── Monitor Iron Butterfly — exit when 50% profit hit
  ├── 9:45 AM  : IF Iron Butterfly already closed → enter Expiry Strangle (15 lots)
  └── 2:45 PM  : Close ALL NIFTY positions. No exceptions.

WEDNESDAY
  ├── 9:00 AM  : Review SENSEX option chain, form view for Thursday expiry
  ├── 9:30 AM  : SENSEX PCR, OI, BSE futures data
  └── 10:15 AM : Enter SENSEX Iron Butterfly (9 lots, ₹4,05,000 margin)

THURSDAY (SENSEX Expiry)
  ├── Monitor SENSEX positions — exit when 50% profit hit
  └── 2:45 PM  : Close ALL SENSEX positions. No exceptions.

FRIDAY
  └── Log P&L, review what worked, plan next week capital and lot size
```

**Combined weekly P&L target (all trades firing):**

| Trade | Index | Lots | Margin Used | Gross Credit | 50% Target | Net After Charges |
|-------|-------|------|-------------|-------------|-----------|-------------------|
| Iron Butterfly | NIFTY | 12 | ₹8,64,000 | ₹57,600 | ₹28,800 | ₹26,000 |
| Expiry Strangle* | NIFTY | 15 | ₹6,75,000 | ₹14,250 | ₹7,125 | ₹5,500 |
| Iron Butterfly | SENSEX | 9 | ₹4,05,000 | ₹31,500 | ₹15,750 | ₹13,500 |
| **TOTAL** | | | **≤₹13L peak** | | | **₹45,000 = 2.25%** |

> *Expiry Strangle fires only when NIFTY IB exits before Tuesday morning. NIFTY IB and Expiry Strangle never run simultaneously.

> **Peak simultaneous margin:** NIFTY IB (₹8.64L) + SENSEX IB (₹4.05L) = ₹12.69L = **63.5% of ₹20L** ✓

**SENSEX Iron Butterfly assumptions (9 lots):**
```
SENSEX spot: ~81,000 | Lot size: 10 units
Sell ATM CE ~₹250 + Sell ATM PE ~₹210 = ₹460 gross credit
Buy CE wing (600 pts away) ~₹22 + Buy PE wing (600 pts away) ~₹18 = ₹40 cost
Net credit per unit: 460 - 40 = 420 points (conservative estimate: use ₹350/unit)
Per lot: ₹350 × 10 = ₹3,500
9 lots gross: ₹31,500 | 50% exit: ₹15,750 | After charges: ₹13,500
```

---

## 9. VIX Filter — The One Rule That Separates Pros from Amateurs

**India VIX** measures expected NIFTY volatility for the next 30 days. Higher VIX = more premium but more actual movement. The VIX level dictates which strategy to run and at what size.

```
VIX < 11
  → DO NOT sell. Premium is too thin for meaningful credit.
  → Risk/reward is unfavorable. This calm often precedes a spike.
  → Sit out. Preserve capital.

VIX 11 – 13
  → Proceed with caution. Reduce to 8 lots NIFTY IB (from 12).
  → Use Iron Condor (OTM) instead of Iron Butterfly (ATM).
  → Wing distance: 400 points.
  → SENSEX: 6 lots instead of 9.

VIX 13 – 16  ← SWEET SPOT
  → Standard setup. 12 lots NIFTY IB + 9 lots SENSEX IB.
  → This is where 80% of your trades will happen.
  → Wing distance: 500 points.

VIX 16 – 20  ← PREMIUM SELLER'S PARADISE
  → Full size: 12 lots NIFTY + 9 lots SENSEX.
  → Move wings farther: 600–700 points.
  → More credit collected but more real movement — buffer critical.
  → Do not add extra lots beyond 12 even though premium is tempting.

VIX 20 – 25
  → Switch to Iron Condor only. OTM strikes 1.5–2 SD away.
  → Reduce to 8 lots NIFTY. Skip SENSEX this week.
  → Expiry strangle: skip entirely (too much overnight gap risk).

VIX > 25  ← DANGER ZONE
  → Sit out entirely, OR only buy options (Long Straddle directional bet).
  → As a seller: wait for VIX to peak and then start falling before re-entering.
  → Historical context: VIX spikes above 25 during RBI emergencies,
    election result days, US Fed shock decisions, global circuit breakers.
```

**VIX timing rule:** Check VIX at 9:30 AM on entry day. If VIX is rising by more than +1 point from previous close — delay entry to 10:30 AM and re-evaluate.

---

## 10. Pre-Trade Checklist (Run Before Every Entry)

Complete all 6 checks. **3 or more red flags = sit out this week or reduce to 50% lot size.**

```
CHECKLIST — RUN MONDAY 9:00–9:30 AM

[ ] 1. VIX Level
    GREEN:  VIX 13–18 → full size (12 lots NIFTY IB)
    YELLOW: VIX 11–13 or 18–22 → reduce to 8 lots, Iron Condor
    RED:    VIX < 11 or > 22 → skip or credit spreads only

[ ] 2. Event Risk in Next 48 Hours
    Check: RBI MPC date, Union Budget, Q-results of Nifty heavyweights, US FOMC
    GREEN: No major event in next 48 hrs
    YELLOW: Q-results of a mid-weight stock → reduce size by 30%
    RED: RBI MPC / Budget / US Fed in next 24 hrs → skip or max 6 lots

[ ] 3. PCR (Put-Call Ratio) Slope
    Fetch from: NSE option chain, Sensibull, or Dhan MCP optionchain
    GREEN: PCR 0.9 – 1.3 (balanced, sideways likely)
    YELLOW: PCR < 0.7 (too bullish, PE side of IB more vulnerable)
    YELLOW: PCR > 1.5 (too bearish, CE side more vulnerable)

[ ] 4. FII Participant OI
    Check from: NSE/BSE FII data or x.com/FII_DII_Nifty
    GREEN: FII net OI change flat or mixed (no strong direction today)
    RED: FII adding heavily to one side (calls or puts) → that wing is at risk

[ ] 5. GIFT Nifty (Pre-Market Signal)
    GREEN: GIFT Nifty gap < ±0.5% from previous NSE close
    YELLOW: Gap ±0.5% to ±1.0% → delay entry to 10:30 AM, watch price
    RED: Gap > ±1.0% → do NOT enter at open. Wait 45 min minimum.

[ ] 6. Weekly Chart Structure
    GREEN: NIFTY inside weekly range, no imminent breakout / breakdown
    RED: NIFTY at multi-week high or low, potential breakout zone
    → If at breakout zone: run credit spread (directional) instead of Iron Butterfly
```

---

## 11. Exit Rules (Non-Negotiable)

These rules are what separate profitable sellers from those who give back months of gains in one week.

### Rule 1: 50% Profit Exit

When the position shows 50% of max credit as profit, close the entire position.

```
Example: Entered at ₹57,600 gross credit (12-lot Iron Butterfly)
50% = ₹28,800 profit
→ Close all 4 legs immediately at market or limit order
→ Do not wait for 60% or 70% "to squeeze more"

Why 50%: The last 50% of profit requires holding through exponential gamma risk.
The gamma risk of losing ₹25,000+ in the final hours is not worth capturing ₹8,000 more.
```

### Rule 2: Stop-Loss at 1.5× Credit Received

If the position shows a loss equal to 1.5× the credit received, close immediately.

```
Example: Gross credit received = ₹57,600 (12 lots)
Stop-loss trigger: ₹57,600 × 1.5 = ₹86,400 loss
→ Close all legs immediately. No discussion.

This means max loss per NIFTY trade = ₹86,400
As % of ₹20L = 4.3% drawdown per trade — painful but survivable.
3 consecutive stop-losses (worst realistic streak) = ₹2,59,200 = 13% drawdown.
Buffer (₹7L+) absorbs this fully without a margin call.
```

### Rule 3: Time Stop

Close any remaining position by **2:45 PM on expiry day**, no exceptions.

The last 15 minutes of expiry day (3:00–3:15 PM) have extreme gamma spikes. Options can move 5× in 10 minutes. No professional holds through this.

### Rule 4: Event Stop

If a major unexpected event occurs mid-week (market circuit breaker, emergency RBI announcement, global market crash):
- Exit immediately at market price
- Do not wait to see if it recovers
- Re-enter only after the event has fully priced in (next day at earliest)

### Rule 5: Never Remove Wings Mid-Trade

When the trade is going well, it can be tempting to close the bought wing legs to collect extra premium. This converts your hedged structure to a naked position with unlimited loss potential.

**Never remove wings.** The wings cost ₹38/unit but protect against ₹308/unit loss beyond them. That insurance stays on until you close the entire trade.

---

## 12. Annual Return Projections

**Based on 52 trading weeks, ₹20L dedicated capital**

### Realistic Case (Disciplined execution, mixed market)

```
Week types in a typical year:
├── Strong Win (all 3 trades):   15 weeks × ₹45,000 = ₹6,75,000
├── Moderate Win (2 trades):     15 weeks × ₹25,000 = ₹3,75,000
├── Partial Win (1 trade):       12 weeks × ₹12,000 = ₹1,44,000
├── Flat / Break-even:            5 weeks × ₹2,000  =    ₹10,000
└── Loss (stop-loss triggered):   5 weeks × -₹65,000 = -₹3,25,000
                                                      ─────────────
Annual net P&L:                                        ₹8,79,000
As % of ₹20L:                                          43.9%
Monthly average:                                       ₹73,250
```

### Conservative Case (Higher volatility, more event-driven weeks)

```
├── Strong Win:    10 weeks × ₹45,000  = ₹4,50,000
├── Moderate Win:  15 weeks × ₹22,000  = ₹3,30,000
├── Partial Win:   14 weeks × ₹10,000  = ₹1,40,000
├── Flat:           7 weeks × ₹2,000   =    ₹14,000
└── Loss:           6 weeks × -₹70,000 = -₹4,20,000
                                        ─────────────
Annual net P&L:                          ₹5,14,000
As % of ₹20L:                            25.7%
Monthly average:                         ₹42,833
```

### Optimistic Case (Low VIX year, clean trends, consistent execution)

```
├── Strong Win:    25 weeks × ₹45,000 = ₹11,25,000
├── Moderate Win:  16 weeks × ₹25,000 =  ₹4,00,000
├── Partial Win:    7 weeks × ₹12,000 =     ₹84,000
├── Flat:           2 weeks × ₹2,000  =      ₹4,000
└── Loss:           2 weeks × -₹60,000 = -₹1,20,000
                                        ─────────────
Annual net P&L:                          ₹14,93,000
As % of ₹20L:                            74.6%
```

**Honest planning range: 25–50% annually on ₹20L dedicated capital.**

> Tax note: F&O income is business income under Indian IT law. Consult a CA on advance tax, audit requirements (turnover > ₹10Cr threshold based on contract value), and applicable deductions. Tax significantly affects net-of-tax return — plan for it.

---

## 13. Risk Management for ₹20L Dedicated Capital

### Per-Trade Loss Limit

```
Single NIFTY Iron Butterfly trade:
  Max loss (1.5× credit):   ₹86,400
  As % of ₹20L:             4.3%

Single SENSEX Iron Butterfly trade (9 lots):
  Gross credit: ₹31,500 | Stop at 1.5×: ₹47,250 loss
  As % of ₹20L: 2.4%

Single week worst case (both stop out):
  ₹86,400 + ₹47,250 = ₹1,33,650 = 6.7% of ₹20L
```

### Weekly Loss Limit

```
Hard stop: ₹1,00,000 loss in a single week (5% of ₹20L)
If weekly loss exceeds ₹1,00,000:
  → Stop trading for the remainder of that week
  → Review market structure before next week's entry
  → Do not "revenge trade" to recover it
```

### Monthly Drawdown Limit

```
Hard stop: ₹2,00,000 loss in a calendar month (10% of ₹20L)
If monthly drawdown hits ₹2L:
  → Reduce all lot sizes to 50% for the next month (6 lots NIFTY, 4-5 lots SENSEX)
  → Full size resumes only when capital is back above ₹19L
```

### Capital Growth → Lot Scale-Up Rule

```
Add lots gradually as capital grows:
  ₹20L → 21.5L: Add 1 lot to NIFTY IB (→ 13 lots)
  ₹21.5L → 23L: Add 1 lot more (→ 14 lots)
  ₹23L → 25L:   Add 1 lot SENSEX IB (→ 10 lots)

Never add lots after a losing week. Only scale up from a position of strength.
```

### The "Never Do" List

| Never Do | Why |
|----------|-----|
| Sell naked (unhedged) straddle / strangle | One gap-up/down can wipe 3 months of profit in 1 day |
| Remove wings to collect extra premium | Converts defined-risk to unlimited-loss instantly |
| Average down on a losing Iron Butterfly | You're adding to a position that is already wrong |
| Trade RBI MPC / Budget day without reducing to 6 lots | VIX spikes fastest on these days |
| Hold past 2:45 PM on expiry day | Gamma explosion in final 15 min is unpredictable |
| Exceed 65% margin utilization (₹13L) | Beyond this, you're trading with margin call risk |
| Use this ₹20L for anything other than F&O | Blurs the boundary between trading capital and personal capital |

---

## 14. Common Mistakes and How Pros Avoid Them

| Mistake | Amateur Behavior | Pro Behavior |
|---------|-----------------|-------------|
| Entry timing | 9:15 AM sharp to "catch the move" | 9:45–10:15 AM after opening volatility settles |
| Strike selection | ATM always, regardless of VIX | Adjusts wing distance and body strikes by VIX level |
| Profit exit | Waits for maximum expiry profit | Exits at 50% of credit — always, without discussion |
| Loss handling | Holds, hopes for recovery | Closes at stop-loss, re-evaluates with fresh eyes |
| Event risk | Doesn't check weekly calendar | Checks RBI calendar, Q-results, US FOMC every Monday |
| Lot sizing | Uses maximum possible lots | Caps at 65% margin utilization (₹13L), scales slowly |
| Win-rate obsession | "I win 70% of weeks — I'm profitable" | Tracks rupee P&L. One bad week can erase 3 good weeks |
| PCR interpretation | "PCR > 1.2 means bullish, sell PE" | Checks PCR trend over 3+ days, cross-validates with FII OI |
| Capital separation | Mixes trading and personal funds | ₹20L trading account is fully ring-fenced — zero overlap |
| Scaling lot size on emotion | Adds lots after a big win to "ride momentum" | Scale-up only follows the capital growth rule in §13 |

---

## Quick-Reference Card

```
EVERY MONDAY MORNING — 15 MINUTE SETUP

Capital:   ₹20L dedicated trading account (personal funds are separate)
Max margin today: ₹13L (65% of ₹20L)

1. India VIX → target 13–18
2. Major events this week? → RBI, Q-results, US FOMC
3. GIFT Nifty gap → < ±0.5% for clean entry
4. NIFTY PCR → 0.9–1.3 is balanced
5. FII OI direction → no heavy one-sided buildup

IF ALL GREEN → STANDARD SETUP:
┌─────────────────────────────────────────────────────────┐
│ NIFTY Iron Butterfly — 12 lots                          │
│   Entry: 10:15 AM                                       │
│   Gross credit: ~₹57,600                                │
│   Exit trigger A: ₹28,800 profit (50%) → CLOSE ALL     │
│   Exit trigger B: ₹86,400 loss (1.5×) → CLOSE ALL      │
│   Time stop: 2:45 PM Tuesday                            │
│   Margin: ₹8,64,000                                     │
│   Net target: ₹26,000 (1.3% of ₹20L)                   │
└─────────────────────────────────────────────────────────┘

IF NIFTY IB CLOSES EARLY (Monday or Tuesday AM):
┌─────────────────────────────────────────────────────────┐
│ Expiry-Day Strangle — 15 lots                           │
│   Entry: 9:45 AM Tuesday only                           │
│   Gross credit: ~₹14,250                                │
│   Exit at 50%: ₹7,125                                   │
│   Hard close: 2:45 PM                                   │
│   Net target: +₹5,500                                   │
└─────────────────────────────────────────────────────────┘

WEDNESDAY SETUP → SENSEX:
┌─────────────────────────────────────────────────────────┐
│ SENSEX Iron Butterfly — 9 lots                          │
│   Entry: 10:15 AM Wednesday                             │
│   Gross credit: ~₹31,500                                │
│   Exit at 50%: ₹15,750                                  │
│   Hard close: 2:45 PM Thursday                          │
│   Margin: ₹4,05,000                                     │
│   Net target: ₹13,500 (0.67% of ₹20L)                  │
└─────────────────────────────────────────────────────────┘

WEEKLY TOTAL (all firing):
  NIFTY IB:           +₹26,000
  Expiry Strangle:    +₹5,500
  SENSEX IB:          +₹13,500
  ─────────────────────────────
  TARGET:             +₹45,000 = 2.25% on ₹20L
  Peak margin used:   ₹12,69,000 = 63.5% ✓
```

---

*Sources: Zerodha Varsity Module 6, NSE Academy Options Strategies, NISM-VIII, SEBI derivatives study, practical community backtests (Subhadip Nandy, Vivek Bajaj, Sensibull research). All numbers are illustrative — always verify live premiums, lot sizes, and margins with your broker before placing any trade.*
