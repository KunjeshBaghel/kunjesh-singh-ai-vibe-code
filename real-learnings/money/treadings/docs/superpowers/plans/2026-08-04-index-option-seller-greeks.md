# Indian Index Option Seller Greeks Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rewrite the Greeks section of `kb/option_chain_n_greeks.md` as an accurate, practical risk-management guide for sellers of NIFTY, BANKNIFTY, and SENSEX index options.

**Architecture:** Keep the existing single-file knowledge-base structure, but replace §4 with consistently structured Delta, Theta, Vega, and Gamma subsections. Each Greek will progress from definition and seller sign convention to practical use, worked arithmetic, failure modes, and a checklist; the section will close with Indian contract context and a unified seller workflow.

**Tech Stack:** Markdown, option-pricing sensitivities, official NSE/BSE contract specifications.

## Global Constraints

- Cover only NIFTY 50, BANKNIFTY, and SENSEX European-style, cash-settled index options.
- Write from the option seller/writer perspective while clearly identifying long-option Greeks shown by option-chain platforms.
- Treat Greeks as dynamic model estimates, not guarantees or standalone trading signals.
- Prefer defined-risk credit structures and require per-trade max loss, daily max loss, and mandatory stop-loss.
- Date all lot-size and expiry details and require verification against the current exchange contract master.
- Keep examples educational and hypothetical; do not present them as live trade recommendations.
- Do not commit changes unless the user explicitly requests a commit.

---

### Task 1: Rewrite the Greeks foundation and Delta subsection

**Files:**
- Modify: `kb/option_chain_n_greeks.md:125-187`

**Interfaces:**
- Consumes: existing §1 definitions of intrinsic/time value and the five-view market classification in `kb/Market_View.md`.
- Produces: terminology and sign conventions used by the Theta, Vega, Gamma, and worked-example subsections.

- [ ] **Step 1: Replace the §4 introduction with the seller sign convention**

State explicitly:

- option-chain Greeks generally describe a one-unit long option;
- a short position reverses each displayed Greek’s sign;
- short CE has negative Delta and short PE has positive Delta;
- option sellers generally have positive position Theta, negative Vega, and negative Gamma;
- Greek values vary with spot, strike, IV, time, rates, and model assumptions.

Add this approximation and define every unit:

```text
Long-option premium change ≈
  Delta × spot-point change
  + ½ × Gamma × (spot-point change)²
  + Theta × elapsed calendar days
  + Vega × IV change in percentage points

Short-position change ≈ the negative of the long-option change
```

Warn that this is a local estimate: for large moves, recalculate with current Greeks because Delta, Gamma, Theta, and Vega change during the move.

- [ ] **Step 2: Rewrite Delta with precise probability language**

Cover:

- long CE Delta: `0` to `+1`; long PE Delta: `-1` to `0`;
- short-position Delta reverses sign;
- absolute Delta is commonly used as a rough risk/probability proxy, not an exact probability or promised win rate;
- net Delta near zero means approximately direction-neutral only at that instant;
- Gamma, IV, skew, and time prevent two legs from remaining perfectly offset.

Remove or replace:

- “85–90% win rate”;
- “perfectly offset”;
- any universal claim that Delta reaching `0.40` is automatically the correct stop.

Use a three-part risk exit: underlying invalidation, strategy-value/rupee max loss, and a Delta threshold chosen before entry.

- [ ] **Step 3: Correct the NIFTY short-PE example**

Use a clearly hypothetical example with current contract context dated `4-Aug-2026`:

```text
NIFTY spot: 22,000
Position: sell one 21,700 PE
Entry premium: 50 points
Long-option Delta shown in chain: -0.20
Seller position Delta: +0.20
Current NIFTY lot size: 65 (verify live contract master)
```

Show:

- approximate 100-point fall: premium rises about 20 points before Gamma/Theta/Vega, loss `(70 - 50) × 65 = ₹1,300`;
- approximate 100-point rise: premium falls about 20 points, gain `(50 - 30) × 65 = ₹1,300`;
- premium repurchased at zero or expires worthless: maximum gross profit `50 × 65 = ₹3,250`;
- any repurchase below 50 can produce a gross profit;
- charges and slippage reduce net profit.

- [ ] **Step 4: Review the rewritten Delta material**

Confirm manually:

- CE/PE and long/short Delta signs are correct;
- all point-to-rupee arithmetic uses quantity 65;
- no sentence equates low Delta with a guaranteed win;
- no sentence claims a net-zero Delta remains neutral after market movement.

---

### Task 2: Build the complete Theta seller guide

**Files:**
- Modify: `kb/option_chain_n_greeks.md` immediately after the rewritten Delta subsection and before Vega.

**Interfaces:**
- Consumes: seller sign convention and combined Greek approximation from Task 1.
- Produces: Theta concepts referenced by Vega, Gamma, examples, and seller workflow.

- [ ] **Step 1: Define Theta accurately**

Explain:

- displayed long-option Theta estimates premium change from one calendar day passing, assuming spot, IV, rates, and other inputs stay unchanged;
- seller position Theta is the opposite sign;
- `Theta = -12` means an estimated 12-point long-option loss under unchanged assumptions, not a guaranteed ₹12 fall by the next market session;
- points convert to rupees only after multiplying by current lot quantity.

- [ ] **Step 2: Explain what decays and how decay changes**

Include:

- `premium = intrinsic value + extrinsic value`;
- only extrinsic/time value decays toward expiry;
- ITM options retain intrinsic value if they remain ITM;
- ATM options generally have the largest absolute Theta near expiry;
- OTM premium can approach zero as the probability of expiring ITM collapses;
- decay is non-linear and generally accelerates near expiry, especially around ATM;
- weekends and holidays are calendar time already reflected through pricing and market repricing, so “weekend Theta” is not guaranteed free profit.

- [ ] **Step 3: Explain when Theta loses**

Use explicit counterexamples:

- favorable Theta `+12` but adverse Delta/Gamma effect `-35` gives about `-23` premium points for the seller before Vega;
- favorable Theta `+12` but IV expansion causes seller Vega loss `-20`, leaving only about `-8` points before directional effects;
- a gap through a short strike can overwhelm several days of collected decay.

State: positive Theta is compensation for short-Gamma and short-Vega exposure, not an independent edge.

- [ ] **Step 4: Add DTE and moneyness guidance**

Describe behavior without promising an optimum:

- farther expiry: slower daily decay, more Vega exposure, more time for the thesis to fail;
- near expiry: faster ATM decay, much higher Gamma sensitivity, less adjustment time;
- far OTM: lower premium and often smaller absolute Theta, but severe gap/tail risk still exists;
- ITM: premium cannot decay below remaining intrinsic value.

Explain why DTE must be selected from the expected duration of the market view and risk budget, not simply by choosing the highest Theta.

- [ ] **Step 5: Add net-Theta strategy guidance**

Cover:

- naked short option: positive Theta with undefined or very large directional loss;
- credit spread: positive net Theta with capped maximum loss;
- iron condor: positive net Theta while spot remains inside the planned range, with capped loss;
- short straddle/strangle: high positive Theta but high short-Gamma/tail risk and therefore not the default beginner structure.

For every structure, direct the reader to evaluate net strategy Greeks, not the short leg in isolation.

- [ ] **Step 6: Add the Theta entry and management checklist**

Before entry:

1. classify the five-view market bias;
2. check India VIX direction and strike IV/IVP;
3. inspect PCR slope and intraday OI change;
4. choose strategy and DTE;
5. confirm both legs’ liquidity and bid–ask spread;
6. calculate net credit, maximum loss, breakeven, and net Greeks;
7. define stop, profit capture, adjustment, time exit, per-trade max loss, and daily max loss.

During the trade:

1. recheck spot relative to short strikes;
2. monitor net Delta and Gamma acceleration;
3. monitor IV/Vega loss;
4. exit when the predefined invalidation or risk limit is reached rather than waiting for Theta to rescue the position.

---

### Task 3: Expand Vega and Gamma and add Indian-index examples

**Files:**
- Modify: `kb/option_chain_n_greeks.md` from the existing Vega paragraph through the end of §4.

**Interfaces:**
- Consumes: foundation, Delta, and Theta concepts from Tasks 1–2.
- Produces: the complete four-Greek seller reference.

- [ ] **Step 1: Rewrite Vega**

Explain:

- long-option Vega estimates premium-point change for a one-percentage-point IV change;
- option sellers normally have negative position Vega;
- strike IV is not the same measurement as India VIX;
- IV expansion can raise premiums despite elapsed time;
- IV crush helps sellers only if adverse spot/Delta/Gamma effects do not dominate;
- compare IV with its own historical context, liquidity, skew, event risk, and expected move.

- [ ] **Step 2: Rewrite Gamma**

Explain:

- Gamma is the change in Delta for a one-point underlying move;
- long CE and PE normally have positive Gamma; short options have negative position Gamma;
- Gamma is greatest around ATM and increases sharply near expiry;
- short-Gamma losses accelerate as spot moves against the seller;
- high expiry-day Theta and high Gamma arrive together.

Add this rule:

```text
Do not select a short option merely because Theta is high.
Check distance to the short strike, net Gamma, maximum loss, liquidity,
event/gap risk, and available adjustment time.
```

- [ ] **Step 3: Add dated Indian contract context**

Document as of `4-Aug-2026`:

| Index | Exchange | Available expiries relevant here | Standard expiry day | Lot size |
|---|---|---|---|---:|
| NIFTY 50 | NSE | Weekly and monthly | Tuesday | 65 |
| BANKNIFTY | NSE | Monthly | Tuesday | 30 |
| SENSEX | BSE | Weekly and monthly | Thursday | 20 |

State that a holiday normally shifts expiry to the previous trading day and that exchange circulars can change schedules and lot sizes. Link:

- NSE contract specifications: `https://www.nseindia.com/static/products-services/equity-derivatives-contract-specifications`
- NSE lot-size circular FAOP70616: `https://nsearchives.nseindia.com/content/circulars/FAOP70616.pdf`
- BSE contract specifications: `https://beta.bseindia.com/static/markets/Derivatives/DeriReports/contractindex.aspx`
- BSE expiry notice 20250623-59: `https://www.bseindia.com/markets/MarketInfo/DispNewNoticesCirculars.aspx?page=20250623-59`

- [ ] **Step 4: Add three hypothetical worked examples**

Example A — NIFTY short PE:

- reuse Task 1’s 65-quantity example;
- add Theta `-6` shown for the long PE, therefore seller position Theta `+6`;
- unchanged-input one-day estimate: `6 × 65 = ₹390` gross favorable decay;
- explicitly state actual P&L will differ when spot, IV, or Greeks change.

Example B — BANKNIFTY bull put spread:

```text
Sell PE at 120; buy lower-strike PE at 70; quantity 30
Net credit = 50 points
Strike width = 200 points
Maximum gross profit = 50 × 30 = ₹1,500
Maximum gross loss = (200 - 50) × 30 = ₹4,500
Short-leg Theta = -10; hedge Theta = -6
Seller net position Theta = +10 - 6 = +4 points/day
Approximate unchanged-input daily decay benefit = 4 × 30 = ₹120
```

Example C — SENSEX iron condor:

Use hypothetical same-expiry credit spreads with:

```text
Total net credit = 100 points; wing width = 500 points; quantity 20
Maximum gross profit = 100 × 20 = ₹2,000
Maximum gross loss = (500 - 100) × 20 = ₹8,000
Net position Theta = +8 points/day
Approximate unchanged-input daily benefit = 8 × 20 = ₹160
```

Explain that spot approaching either short strike increases directional and Gamma risk, while IV expansion can increase the condor’s mark-to-market loss.

- [ ] **Step 5: Add a one-page practical seller workflow**

End §4 with:

`Market view → event/IV check → strategy → expiry/DTE → strikes/Delta/OI → liquidity → net Greeks → max-loss and exit plan → monitoring`

Include a no-go box:

- no five-view classification;
- rising VIX/IV without compensation or a planned event trade;
- conflicting PCR/OI signals;
- illiquid hedge leg or wide spread;
- undefined max loss;
- three or more warning signals from the existing §7 checklist.

---

### Task 4: Correct contradictions and verify the final document

**Files:**
- Modify if needed: `kb/option_chain_n_greeks.md:1-366`
- Reference: `docs/superpowers/specs/2026-08-04-index-option-seller-greeks-design.md`

**Interfaces:**
- Consumes: completed rewritten §4.
- Produces: a coherent, internally consistent Markdown reference.

- [ ] **Step 1: Search for contradictory claims**

Search the document for:

```text
win rate
perfectly offset
₹1,000 per lot
50 qty
Theta
institutional
solid wall
```

Correct only direct contradictions, including outdated NIFTY quantity/arithmetic and claims that all large OI must be institutional.

- [ ] **Step 2: Verify arithmetic manually**

Check:

- NIFTY: `20 × 65 = ₹1,300`; `50 × 65 = ₹3,250`; `6 × 65 = ₹390`;
- BANKNIFTY: `50 × 30 = ₹1,500`; `150 × 30 = ₹4,500`; `4 × 30 = ₹120`;
- SENSEX: `100 × 20 = ₹2,000`; `400 × 20 = ₹8,000`; `8 × 20 = ₹160`.

- [ ] **Step 3: Verify domain accuracy**

Confirm:

- seller Greek signs;
- only extrinsic value decays;
- Theta uses an unchanged-input assumption;
- IV and India VIX are distinguished;
- high Theta is paired with Gamma risk;
- all three indices are described as European-style and cash-settled;
- BANKNIFTY is not described as having weekly options;
- every hard-coded lot size has an as-of date and live-verification warning.

- [ ] **Step 4: Verify Markdown structure**

Confirm:

- `### 4. Option Greeks` remains intact for existing table-of-contents anchors;
- Delta, Theta, Vega, Gamma, examples, and checklist use nested headings;
- source URLs render as Markdown links;
- no placeholder language (`TBD`, `TODO`, or incomplete examples) remains.

- [ ] **Step 5: Review edited-file diagnostics**

Run the available Markdown/IDE diagnostics for `kb/option_chain_n_greeks.md`. Fix only errors introduced by this rewrite and report any pre-existing warnings separately.
