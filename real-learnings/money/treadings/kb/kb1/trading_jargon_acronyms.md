# Trading Jargon & Acronyms — NSE/BSE Options

Central reference for abbreviations and terms used across the knowledge base (`strategy_ref_book.md`, `option_chain.md`, `open_interest.md`, `Market_View.md`).

---

## Table of Contents

1. [Acronyms — Quick Reference](#acronyms--quick-reference)
2. [Price Levels & Session References](#price-levels--session-references)
3. [Option Basics](#option-basics)
4. [Moneyness](#moneyness)
5. [Option Chain Columns](#option-chain-columns)
6. [Greeks](#greeks)
7. [Open Interest & Price–OI Matrix](#open-interest--priceoi-matrix)
8. [Market Participants](#market-participants)
9. [Volatility & Sentiment](#volatility--sentiment)
10. [Exchanges, Regulators & Market Structure](#exchanges-regulators--market-structure)
11. [Financial Terms — Full Definitions](#financial-terms--full-definitions)
12. [Sources](#sources)

---

## Acronyms — Quick Reference

| Acronym | Full Form |
|---------|-----------|
| **API** | Application Programming Interface |
| **ATM** | At-The-Money |
| **ATR** | Average True Range |
| **BSE** | Bombay Stock Exchange |
| **CE** | Call European |
| **CFD** | Contract for Difference |
| **DII** | Domestic Institutional Investor |
| **EMA** | Exponential Moving Average |
| **EOD** | End of Day |
| **F&O** | Futures & Options |
| **FII** | Foreign Institutional Investor |
| **FOMC** | Federal Open Market Committee (US Fed) |
| **GIFT Nifty** | Gift City Nifty (overnight/pre-market Nifty futures on NSE IFSC) |
| **GST** | Goods and Services Tax |
| **GTT** | Good Till Triggered (order type) |
| **HNI** | High Net-worth Individual |
| **ITM** | In-The-Money |
| **IV** | Implied Volatility |
| **IVP** | Implied Volatility Percentile |
| **LTP** | Last Traded Price |
| **NCFM** | NSE's Certification in Financial Markets |
| **NISM** | National Institute of Securities Markets |
| **NSE** | National Stock Exchange of India |
| **OI** | Open Interest |
| **OTP** | One-Time Password |
| **OTM** | Out-of-The-Money |
| **PDC** | Previous Day Close |
| **PDH** | Previous Day High |
| **PDL** | Previous Day Low |
| **PCR** | Put-Call Ratio |
| **PE** | Put European |
| **POP** | Probability of Profit |
| **RA** | Research Analyst (SEBI registration category) |
| **RBI** | Reserve Bank of India |
| **RSI** | Relative Strength Index |
| **SEBI** | Securities and Exchange Board of India |
| **SPAN** | Standard Portfolio Analysis of Risk (margin framework) |
| **STT** | Securities Transaction Tax |
| **VIX** | Volatility Index (India VIX on NSE) |
| **VWAP** | Volume Weighted Average Price |

---

## Price Levels & Session References

#### PDH

| | |
|---|---|
| **Full form** | **Previous Day High** |
| **Meaning** | The highest price NIFTY / BANKNIFTY (or any security) reached during the **previous trading session**. |
| **How traders use it** | Marked as a horizontal resistance level on the chart. Price reacting at or failing to break above PDH often signals selling pressure; a clean breakout with volume can signal bullish continuation. Treat as a **hard line**, not a broad zone. |

#### PDL

| | |
|---|---|
| **Full form** | **Previous Day Low** |
| **Meaning** | The lowest price reached during the **previous trading session**. |
| **How traders use it** | Marked as a horizontal support level. Price holding above PDL suggests buyers are defending; a break below PDL with conviction often signals weakness or a bearish continuation. Treat as a **hard line**, not a broad zone. |

#### PDC

| | |
|---|---|
| **Full form** | **Previous Day Close** |
| **Meaning** | The **final closing price** at the end of the previous trading session (after 3:30 PM IST on NSE). |
| **How traders use it** | Used as a reference for overnight gap analysis and intraday bias — trading above PDC suggests bullish sentiment; below PDC suggests bearish sentiment. Often plotted alongside PDH and PDL as one of the "core four" pre-market levels. |

---

## Option Basics

- **Call option (CE — buy):** Buy when you expect price to go up. Gives the buyer the **right** (not obligation) to buy the underlying at the strike price on or before expiry.
- **Put option (PE — buy):** Buy when you expect price to go down. Gives the buyer the **right** to sell the underlying at the strike price on or before expiry.
- **Option buyer:** Pays **premium**; loss limited to premium paid; profit can be large.
- **Option seller / writer:** Receives premium; has an **obligation** to honour the contract if the buyer exercises; profit limited to premium, loss can be very large.
- **Premium:** The price paid by the buyer to the seller for an options contract. Premium = Intrinsic Value + Time (Extrinsic) Value.
- **European style:** Exercise is at expiry only (all NSE/BSE index and stock options).
- **Cash-settled:** Index options (NIFTY, BANKNIFTY, FINNIFTY, SENSEX, etc.) — no physical delivery; settled in cash.
- **Physically settled:** Individual stock options — ITM positions at expiry can create share delivery obligation.
- **Directional shorthand:**
  - Expect **up:** `buy CE` or `sell PE`
  - Expect **down:** `buy PE` or `sell CE`
- Direction alone is not enough — **time** and **volatility** also matter a lot.

---

## Moneyness

| Term | Meaning |
|------|---------|
| **ATM (At-The-Money)** | Strike equal to or closest to current spot. Zero intrinsic value; highest time value. |
| **ITM (In-The-Money)** | Positive intrinsic value. Call ITM when Spot > Strike; Put ITM when Spot < Strike. |
| **OTM (Out-of-The-Money)** | Zero intrinsic value. Call OTM when Spot < Strike; Put OTM when Spot > Strike. |
| **Moneyness** | Classification of an option as ITM, ATM, or OTM based on strike vs spot. |

---

## Option Chain Columns

| Term | Definition |
|------|------------|
| **Strike** | Predetermined price at which the option holder can buy (call) or sell (put) the underlying. |
| **LTP / LTP Chg / LTP (chg%)** | Last Traded Price and its absolute/percentage change from previous close. |
| **Bid** | Highest price a buyer is willing to pay. |
| **Ask / Offer** | Lowest price a seller is willing to accept. Price you pay when buying. |
| **Spread (Bid-Ask)** | Gap between Bid and Ask. Narrow = liquid; wide = costly to enter/exit. |
| **Intrinsic Value** | Immediate exercise value if expired today. Calls: Spot − Strike (if positive); Puts: Strike − Spot (if positive). Zero for OTM; never negative. |
| **Time Value / Extrinsic Value** | `LTP − Intrinsic Value`. Reflects time to expiry and volatility expectations. |
| **Volume** | Contracts traded in the current session. High volume = better liquidity. |
| **OI (Open Interest)** | Total outstanding unsettled contracts at a strike. Rising OI = new positions; falling OI = positions closing. |
| **OI Chg / OI Chg%** | Daily change in Open Interest — shows fresh writing or unwinding. |
| **Breakeven (%)** | Underlying move required from current price for the trade to profit at expiry. |
| **POP (Probability of Profit)** | Estimated probability of ≥ ₹1 profit at expiry, derived from pricing models and Greeks. |

---

## Greeks

| Greek | Measures | Trading significance |
|-------|----------|---------------------|
| **Delta (Δ)** | Premium change for a 1-point move in underlying. Call: 0 to +1; Put: −1 to 0. | Also approximates probability of expiring ITM. Used as safety filter for premium selling (e.g. Delta ~0.15–0.20 ≈ 80–85% POP). |
| **Gamma (Γ)** | Rate of change of Delta for a 1-point move in underlying. | Highest for ATM options near expiry. Small spot moves can cause large premium swings. |
| **Theta (Θ)** | Daily time decay — premium erosion per day. | Enemy of option buyers; friend of option sellers. **Theta Trap:** range-bound session engineered by writers where both-side buyers lose to decay. |
| **Vega (ν)** | Premium sensitivity to a 1% change in implied volatility. | Critical around events. High Vega + falling IV = **IV Crush** — premium drops even if direction is right. |
| **Rho** | Sensitivity to interest rate changes. | Less relevant for short-dated Indian index options. |

**Why premium changes (plain English):**

- **Price move** → Delta (and Gamma)
- **Time passing** → Theta
- **Volatility change** → Vega
- **Speed of Delta change** → Gamma

---

## Open Interest & Price–OI Matrix

### Futures / index OI quadrants

| Term | Price | OI | Meaning |
|------|-------|-----|---------|
| **Long Buildup** | ↑ | ↑ | New longs entering — strong uptrend |
| **Short Covering** | ↑ | ↓ | Shorts exiting — bounce, often fades at PDH |
| **Short Buildup** | ↓ | ↑ | New shorts entering — strong downtrend |
| **Long Unwinding** | ↓ | ↓ | Longs booking profits — dip, often bounces at PDL |

### Option OI bar directions (OI Change chart)

| Signal | Bar direction | Meaning |
|--------|---------------|---------|
| **Put Writing** | Green bar up | New put sellers — support (bullish) |
| **Call Writing** | Red bar up | New call sellers — resistance (bearish) |
| **Put Unwinding / Put Panic** | Green bar down | Put sellers closing — support breaking (bearish) |
| **Call Unwinding / Short Covering** | Red bar down | Call sellers covering — resistance breaking (bullish) |

### Chart-specific terms

| Term | Meaning |
|------|---------|
| **Squash Effect** | Resistance tower shrinking live as call writers cover — potential breakout signal. |
| **Shifting Walls** | Tallest OI bars moving toward or away from spot during the session. |
| **Crossover Trade** | Put OI line crossing above call OI line on Multi Strike chart — bullish momentum signal. |
| **Fake Out** | Spot moves up but put OI flat/falling — no institutional backing. |
| **Bhavcopy** | NSE end-of-day official data file; finalizes daily OI after market close. |

---

## Market Participants

| Participant | Who | How to read their data |
|-------------|-----|------------------------|
| **FII** | Foreign funds, banks — "smart money" | Market trend often follows FII positioning |
| **DII** | Indian mutual funds, insurers | Derivative data less predictive short-term than FII |
| **Pro** | Broker proprietary desks | Skilled traders; often net option sellers; watch alignment with FII |
| **Client** | Retail / HNI | Often used as **contrarian** indicator |

**Participant-wise OI columns:**

| Column | Meaning |
|--------|---------|
| **Net Change** | Today's flow — new positions added or closed |
| **Net OI** | Cumulative outstanding position carried forward |
| **T-1 Net OI** | Yesterday's cumulative position — compare with Net OI for daily shift |

**Golden rule:** Use **Net Change** for immediate momentum; validate with **Net OI** over 3+ consecutive days before calling a regime.

---

## Volatility & Sentiment

| Term | Definition |
|------|------------|
| **IV (Implied Volatility)** | Market's forecast of future price fluctuation embedded in premium. High IV = expensive options; low IV = cheap. Does not indicate direction. |
| **IVP (Implied Volatility Percentile)** | Ranks current IV vs its own history (e.g. IVP 62 = higher than 62% of past readings). |
| **IV Crush** | Sharp IV drop after a major event (Budget, RBI, earnings) — premiums fall even if underlying moves favourably. |
| **India VIX** | NSE volatility index. Below 12 = calm; 12–16 = normal; 16–20 = moderate fear; 20–25 = high fear; above 25 = panic. **Direction** (rising vs falling) matters as much as level. |
| **PCR (Put-Call Ratio)** | Total Put OI ÷ Total Call OI. > 1 often read as bullish; < 1 as bearish. Extreme readings can be contrarian. |
| **Max Pain** | Strike where option writers would face minimum payout at expiry — relevant mainly in expiry week. |
| **Volatility Skew / Smile** | Differing IV across strikes; Indian index options often show higher OTM put IV (downside protection demand). |

**Support / resistance from OI:**

- **High Call OI** at a strike → informal **resistance** (call writers capping upside)
- **High Put OI** at a strike → informal **support** (put writers defending floor)

---

## Exchanges, Regulators & Market Structure

| Term | Meaning |
|------|---------|
| **NSE** | National Stock Exchange — primary F&O venue; NIFTY weekly expiry every **Tuesday**; monthly last **Tuesday**. |
| **BSE** | Bombay Stock Exchange — SENSEX weekly expiry every **Thursday**; monthly last **Thursday**. |
| **SEBI** | Securities regulator — investor protection, algo-trading rules, derivatives oversight. |
| **NISM** | SEBI-established institute; equity derivatives certification curriculum. |
| **SPAN + Exposure margin** | Margin framework for F&O; hedged structures (e.g. Iron Condor) require less margin than naked shorts. |
| **STT** | Securities Transaction Tax — applies to F&O trades; affects real P&L vs theoretical payoff. |
| **Net debit / Net credit** | Debit strategy = net premium paid; credit strategy = net premium received. |
| **Lot size** | Contract multiplier — multiply per-unit P&L by lot size for rupee impact. |
| **Slippage** | Difference between expected and actual fill price — worse with low liquidity or wide spreads. |
| **Mark-to-market (MTM)** | Daily P&L adjustment on open F&O positions. |
| **Auction penalty** | Risk when physically settled stock options expire ITM without delivery readiness. |

---

## Financial Terms — Full Definitions

| Term | Full Form / Expansion | Definition |
|------|----------------------|------------|
| **Ask / Offer** | — | Lowest price at which a seller is willing to sell an option. Price you pay when buying. |
| **ATM (At-The-Money)** | At-The-Money | Strike equal to or closest to current spot. Zero intrinsic value; highest time value. |
| **Bid** | — | Highest price a buyer is willing to pay. Price you receive when selling (if filled at bid). |
| **Breakeven** | — | Underlying price at which a trade neither makes nor loses money at expiry. |
| **Call Option (CE)** | Call European | Right to buy underlying at strike on or before expiry. NSE index options are European and cash-settled. |
| **Delta (Δ)** | — | Premium change for a 1-point move in underlying. Also approximates ITM probability. |
| **Expiry** | Expiration Date | Last date the contract is valid; settled cash (index) or physical (stock) per NSE rules. |
| **Extrinsic Value** | — | Same as Time Value — premium above intrinsic value. |
| **F&O** | Futures & Options | Derivatives segment for standardized index and stock contracts. |
| **Gamma (Γ)** | — | Rate of change of Delta. Highest ATM near expiry. |
| **Greeks** | — | Risk metrics (Delta, Gamma, Theta, Vega, Rho) quantifying option price sensitivity. |
| **Implied Volatility (IV)** | Implied Volatility | Market's expected future fluctuation embedded in premium. |
| **Intrinsic Value** | — | Immediate exercise value if expired today. |
| **ITM (In-The-Money)** | In-The-Money | Option with positive intrinsic value. |
| **IV Crush** | Implied Volatility Crush | Sharp IV drop post-event causing premium collapse. |
| **IVP (Implied Volatility Percentile)** | Implied Volatility Percentile | Current IV rank vs historical range. |
| **Last Traded Price (LTP)** | Last Traded Price | Most recent transaction price for the contract. |
| **Liquidity** | — | Ease of buying/selling without moving price. High volume + tight spread = good liquidity. |
| **LTP Chg / LTP (chg%)** | Last Traded Price Change | Absolute and percentage LTP change from previous close. |
| **Moneyness** | — | ITM / ATM / OTM classification. |
| **NIFTY / Nifty 50** | National + Fifty | NSE benchmark index of 50 large-cap stocks; most liquid F&O underlying in India. |
| **Open Interest (OI)** | Open Interest | Total outstanding unsettled contracts at a strike. |
| **Option Chain** | — | Tabular display of all strikes with OI, volume, IV, LTP, and Greeks. |
| **Option Premium** | — | Price paid for an option contract. |
| **Option Writer** | — | Seller who collects premium and assumes obligation if buyer exercises. |
| **OTM (Out-of-The-Money)** | Out-of-The-Money | Zero intrinsic value. |
| **PCR (Put-Call Ratio)** | Put-Call Ratio | Total Put OI ÷ Total Call OI — sentiment indicator. |
| **PE (Put European)** | Put European | Right to sell underlying at strike on or before expiry. |
| **POP (Probability of Profit)** | Probability of Profit | Estimated probability of ≥ ₹1 profit at expiry. |
| **Premium** | — | See Option Premium. |
| **Put Option** | — | See PE (Put European). |
| **Resistance** | — | Price level capping upside; high Call OI strikes often treated as resistance zones. |
| **Slippage** | — | Expected vs actual fill price difference. |
| **Spot Price** | — | Current cash-market price of the underlying. |
| **Spread (Bid-Ask)** | — | Bid–Ask gap; narrow = liquid. |
| **Strike Price** | — | Exercise price for the option contract. |
| **Support** | — | Price level preventing decline; high Put OI strikes often treated as support zones. |
| **Theta (Θ)** | — | Daily time decay. Negative for long options; benefits sellers. |
| **Time Decay** | — | Erosion of time value as expiry nears; measured by Theta. |
| **Time Value** | — | `LTP − Intrinsic Value`; goes to zero at expiry. |
| **Vega (ν)** | — | Premium sensitivity to 1% IV change. |
| **Volume** | — | Contracts traded in current session. |
| **Volatility Skew / Smile** | — | IV pattern across strikes; Indian indices often show higher OTM put IV. |

---

## Sources

- [NSE India — Option Chain](https://www.nseindia.com/option-chain)
- [Zerodha Varsity](https://zerodha.com/varsity/)
- [Zerodha Varsity — Open Interest](https://zerodha.com/varsity/chapter/open-interest/)
- [Zerodha Varsity — Moneyness](https://zerodha.com/varsity/chapter/moneyness-of-an-option-contract/)
- [Investopedia — Option Greeks](https://www.investopedia.com/terms/g/greeks.asp)
- [Investopedia — Using the Greeks](https://www.investopedia.com/trading/using-the-greeks-to-understand-options/)
- [Economic Times — Components of Option Premium](https://economictimes.indiatimes.com/markets/stocks/news/learn-with-etmarkets-do-you-know-these-components-of-option-premium/articleshow/99687334.cms)
- [Interactive Brokers — Introduction to Options: The Greeks](https://www.interactivebrokers.com/campus/trading-lessons/introduction-to-options-the-greeks/)
- [TradingView — PDC indicator](https://in.tradingview.com/scripts/pdc/)
- [Capital.com — PDH & PDL](https://capital.com/en-int/analysis/day-traders-toolbox-previous-days-high-and-low-pdh-pdl)
