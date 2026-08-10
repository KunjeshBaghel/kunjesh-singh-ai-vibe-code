# Indian Index Option Seller Greeks — Documentation Design

## Goal

Rewrite `kb/option_chain_n_greeks.md` §4 so Delta, Theta, Vega, and Gamma form a practical, accurate study and trading reference for an Indian index-option seller.

The guide will support decision-making and risk management; it will not present option selling as guaranteed income or encourage autonomous execution.

## Scope

- Instruments: NIFTY 50, BANKNIFTY, and SENSEX options only.
- Perspective: option seller/writer.
- Settlement: European-style, cash-settled index options.
- Excluded: individual-stock options, physical settlement, foreign markets, and broker order execution.
- Contract details such as lot size and expiry schedule will be dated and linked to official exchange sources because exchanges can revise them.

## Section Structure

### 1. Greeks foundation

- Define a Greek as a model-based sensitivity, not a guaranteed premium change.
- Explain that option-chain Greeks normally describe a long option.
- Show how a short position reverses the signs:
  - short CE/PE Delta is the opposite of long CE/PE Delta;
  - long-option Theta is normally negative, while seller position Theta is positive;
  - seller Vega and Gamma are normally negative.
- Introduce the approximate combined premium-change equation:

  `Option change ≈ Delta × spot change + ½ × Gamma × spot change² + Theta × time + Vega × IV change`

- State that Greeks change continuously and the equation is only a local estimate.

### 2. Delta — direction and strike risk

- Explain CE/PE Delta ranges and seller sign reversal.
- Treat absolute Delta only as a rough risk/probability proxy, never a promised win rate.
- Cover moneyness, changing Delta, net strategy Delta, and rebalancing.
- Replace “perfectly offset” language with “approximately direction-neutral at that moment.”
- Explain why Delta-only stops are insufficient and must be combined with underlying-level and rupee-risk exits.
- Retain one worked short-PE example using the current NIFTY lot size, with an “as of” date and live-verification warning.

### 3. Theta — the seller’s income engine, with conditions

- Define Theta as estimated premium change from time passing while spot and IV are assumed unchanged.
- Correct the existing claim that `Theta = -12` guarantees a ₹12 fall “by tomorrow.”
- Explain:
  - only extrinsic/time value decays;
  - intrinsic value does not decay;
  - decay is non-linear;
  - ATM options generally carry the greatest absolute Theta near expiry;
  - far-OTM premium can approach zero, while ITM premium retains intrinsic value;
  - calendar time, weekends, and holidays are already incorporated by pricing models and market repricing;
  - observed decay can be overwhelmed by spot movement or an IV increase.
- Show long-option Theta versus positive short-position Theta.
- Add point and rupee calculations for NIFTY, BANKNIFTY, and SENSEX.
- Explain portfolio/net Theta for credit spreads, strangles, straddles, and iron condors.
- Emphasize that high near-expiry Theta is compensation for high Gamma/tail risk.

### 4. Vega — volatility repricing

- Explain premium sensitivity to a one-percentage-point IV change and seller-negative Vega.
- Distinguish IV from India VIX and avoid treating them as interchangeable.
- Cover IV expansion, IV crush, events, skew, and why low-IV selling may offer poor reward.
- Show how Vega can defeat Theta even on a quiet underlying.

### 5. Gamma — acceleration and expiry risk

- Explain Gamma as Delta’s rate of change and why sellers are short Gamma.
- Cover ATM and near-expiry concentration, gap risk, and convex losses.
- Connect Gamma directly to the Theta–Gamma trade-off.
- Explain why hedged spreads and predefined exits are preferred to unmanaged naked positions.

### 6. Indian index contract context

Include a dated reference box:

- NIFTY: weekly and monthly options, Tuesday expiry; current lot size 65.
- BANKNIFTY: monthly options, Tuesday expiry; current lot size 30.
- SENSEX: weekly and monthly options, Thursday expiry; current lot size 20.
- Holiday expiry shifts to the previous trading day.
- Traders must verify the exchange contract master and broker terminal before every trade.

Official NSE/BSE contract pages and applicable circulars will be cited.

### 7. Worked seller examples

Use hypothetical, clearly labelled examples rather than live recommendations:

1. NIFTY short OTM PE: Delta, Theta, spot-up, spot-down, premium-to-zero, and rupee P&L.
2. BANKNIFTY defined-risk credit spread: net Delta/Theta/Vega/Gamma and maximum loss.
3. SENSEX iron condor or credit spread: net Theta and what happens when IV rises or spot approaches a short strike.

Examples will separate:

- premium points;
- rupee P&L (`premium-point change × current lot size`);
- gross versus net P&L;
- current M2M versus realized P&L;
- maximum profit versus maximum loss.

## Practical Seller Workflow

The rewritten section will end with a reusable sequence:

1. Classify the market as Strongly Bullish, Slightly Bullish, Sideways, Slightly Bearish, or Strongly Bearish.
2. Check India VIX direction, strike IV/IVP, PCR slope, and intraday OI change.
3. Select the strategy before selecting the strike; prefer defined-risk credit structures.
4. Select expiry/DTE and inspect liquidity and bid–ask spread.
5. Select strikes using Delta, market structure, and OI—not Delta alone.
6. Calculate net credit, maximum profit, maximum loss, breakeven, and Greek exposure.
7. Define per-trade max loss, daily max loss, mandatory stop, adjustment rule, profit target, and time exit.
8. Recheck spot, IV, OI, PCR, and portfolio Greeks during the trade.

## Accuracy and Safety Corrections

- Remove guaranteed “85–90% win rate” language.
- Remove claims that neutral legs stay perfectly offset.
- Do not call all large OI institutional or assume an OI wall cannot break.
- Do not imply Theta accrues as guaranteed cash each day.
- Do not recommend naked option selling as the default.
- State that maximum premium is earned only if the short option expires worthless or is repurchased at zero; any lower buyback premium can still produce a profit.
- Keep all examples educational and require live-data validation before a trade.

## Verification

- Check formulas, signs, and example arithmetic manually.
- Verify current expiry schedules and lot sizes against official NSE/BSE sources.
- Confirm headings and links remain compatible with the existing table of contents.
- Scan the edited Markdown for contradictory claims elsewhere in the document.
- Preserve sections outside §4 except where a directly contradictory cross-reference must be corrected.
