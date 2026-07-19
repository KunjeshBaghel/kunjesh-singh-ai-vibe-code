Based on the [Sensibull Option Chain](https://web.sensibull.com/option-chain?tradingsymbol=NIFTY&expiry=2026-07-21&view=all) you are viewing, here is a detailed breakdown of all the columns, what they mean, and how you can use them in real-world trading.

To make it easier to digest, I have grouped the columns into four main categories: **Price & Value**, **Liquidity & Market Sentiment**, **Probability & Risk**, and **Option Greeks**.

---

## Table of Contents

| # | Section | Topics Covered |
|---|---------|----------------|
| 1 | [Price & Value Columns](#1-price--value-columns) | Strike, LTP, Bid/Offer, Intrinsic Value, Time Value |
| 2 | [Liquidity & Market Sentiment](#2-liquidity--market-sentiment) | Volume, Open Interest, OI Change, PCR, IV |
| 3 | [Probability & Risk](#3-probability--risk) | Breakeven, POP |
| 4 | [Option Greeks](#4-option-greeks) | Delta, Theta, Vega, Gamma |
| 5 | [Top 3 Columns for Quality Safe Trades](#5-top-3-columns-for-quality-safe-trades) | Delta/POP, OI & OI Chg, IV/IVP — the practical filter for safe premium selling |
| 6 | [Glossary & Acronyms](#glossary--acronyms) | Full forms and definitions of all financial jargon used in this guide |

### Quick Index — Column by Column

| Column / Term | Category | Jump To |
|---------------|----------|---------|
| Strike | Price & Value | [§1](#1-price--value-columns) |
| LTP, LTP Chg, LTP (chg%) | Price & Value | [§1](#1-price--value-columns) |
| Bid & Offer (Ask) | Price & Value | [§1](#1-price--value-columns) |
| Int Val S (Spot) & Int Val F (Future) | Price & Value | [§1](#1-price--value-columns) |
| Time Value | Price & Value | [§1](#1-price--value-columns) |
| Volume | Liquidity & Sentiment | [§2](#2-liquidity--market-sentiment) |
| OI-lakh (Open Interest) | Liquidity & Sentiment | [§2](#2-liquidity--market-sentiment) |
| OI Chg & OI Chg% | Liquidity & Sentiment | [§2](#2-liquidity--market-sentiment) |
| PCR (Put-Call Ratio) | Liquidity & Sentiment | [§2](#2-liquidity--market-sentiment) |
| IV (Implied Volatility) | Liquidity & Sentiment | [§2](#2-liquidity--market-sentiment) |
| Breakeven (%) | Probability & Risk | [§3](#3-probability--risk) |
| POP (Probability of Profit) | Probability & Risk | [§3](#3-probability--risk) |
| Delta | Option Greeks | [§4](#4-option-greeks) |
| Theta | Option Greeks | [§4](#4-option-greeks) |
| Vega | Option Greeks | [§4](#4-option-greeks) |
| Gamma | Option Greeks | [§4](#4-option-greeks) |
| **Delta / POP** ⭐ | **Top 3 for Safe Trades** | [§5](#5-top-3-columns-for-quality-safe-trades) |
| **OI & OI Chg** ⭐ | **Top 3 for Safe Trades** | [§5](#5-top-3-columns-for-quality-safe-trades) |
| **IV / IVP** ⭐ | **Top 3 for Safe Trades** | [§5](#5-top-3-columns-for-quality-safe-trades) |

---

### 1. Price & Value Columns

These columns tell you exactly what you are paying for an option and what its true "value" is right now.

* **Strike:** The specific price of the underlying asset (NIFTY) at which the option contract can be exercised.
* *Trading Significance:* This is your target. You choose the strike based on where you think the market is headed and how much risk you want to take.


* **LTP, LTP Chg, & LTP(chg%):** "Last Traded Price" is the current premium of the option. The "Chg" shows the absolute point change, and "(chg%)" shows the percentage change from the previous day's close.
* *Trading Significance:* It tells you the exact cost to buy or the premium you receive to sell an option. The change percentage helps you gauge immediate momentum.


* **Bid & Offer:** The **Bid** is the highest price a buyer is willing to pay. The **Offer** (or Ask) is the lowest price a seller is willing to accept.
* *Trading Significance:* The difference between the two is the "spread." A tight spread (e.g., Bid at 100, Offer at 100.5) means high liquidity, and you won't lose much money just entering and exiting the trade.


* **Int Val S (Spot) & Int Val F (Future):** Intrinsic Value. This is the real, built-in value of the option if it were to expire right this second. It is calculated based on either the Spot price (current cash price of NIFTY) or the Futures price.
* *Trading Significance:* Out-of-the-Money (OTM) options have zero intrinsic value. In-The-Money (ITM) options have intrinsic value. It helps you separate the real worth of the option from the "hope" (time value) priced into it.


* **Time Value:** The portion of the option's premium (LTP) that is purely based on the time left until expiry (Calculated as `LTP - Intrinsic Value`).
* *Trading Significance:* Option buyers *pay* time value and lose it as expiry approaches. Option sellers *collect* time value and want it to decay to zero.



### 2. Liquidity & Market Sentiment

These columns show where the "big money" is positioned and how active the contract is.

* **Volume:** The total number of contracts traded during the current day.
* *Trading Significance:* High volume confirms strong interest. You should only trade strikes with high volume to ensure you can enter and exit trades easily without price slippage.


* **OI-lakh (Open Interest):** The total number of active, open contracts that have not yet been settled or closed, displayed in lakhs. The **Call OI** and **Put OI** visual bars represent this graphically.
* *Trading Significance:* OI acts as market support and resistance.
* **High Call OI:** Writers (sellers) are betting the market won't go above this level (Resistance).
* **High Put OI:** Writers are betting the market won't go below this level (Support).




* **OI Chg & OI Chg%:** The absolute and percentage change in Open Interest for the day.
* *Trading Significance:* Tells you the current trend. For example, if Call OI is increasing rapidly, it means sellers are aggressively building fresh resistance. If Put OI is decreasing (negative change), it means sellers are unwinding their support positions out of fear.


* **PCR (Put-Call Ratio):** (Listed at the top of the chain for the whole expiry) Total Put OI divided by Total Call OI.
* *Trading Significance:* It’s a sentiment indicator. A PCR > 1 indicates a bullish sentiment (more put writing). A PCR < 1 indicates a bearish sentiment. Extremely high or low numbers can signal an overbought or oversold market.


* **IV (Implied Volatility):** The market's expectation of how much the underlying asset will move in the future.
* *Trading Significance:* High IV makes options expensive; low IV makes them cheap. Generally, traders look to *buy* options when IV is low (expecting a breakout) and *sell* options when IV is high (expecting things to calm down).



### 3. Probability & Risk

These columns are crucial for calculating your statistical edge before taking a trade.

* **Breakeven(%):** The percentage the underlying NIFTY needs to move from its current price for your option trade to start making a profit at expiry.
* *Trading Significance:* Gives you a realistic reality check. If the breakeven requires a 3% move in NIFTY in 2 days, the trade is highly risky and unlikely to succeed.


* **POP (Probability of Profit):** The statistical chance (derived from the option Greeks and IV) that your trade will make at least ₹1 of profit at expiry.
* *Trading Significance:* Option sellers heavily rely on this. Selling far OTM options usually offers a POP of 80%+, meaning you have a high win rate (though the profit per trade is small). Option buying generally has a POP of less than 35-40%.



### 4. Option Greeks

Greeks measure how your option premium will react to changes in the market, time, and volatility.

* **Delta:** Measures how much the option price will change for a 1-point move in the underlying NIFTY. (Ranges from 0 to 1 for Calls, and -1 to 0 for Puts).
* *Trading Significance:* If your Call option has a Delta of 0.50, and NIFTY goes up by 100 points, your option premium will increase by approximately 50 points. *Pro-tip: Delta is also roughly the percentage chance that the option will expire In-The-Money.*


* **Theta:** Measures how much value the option loses every single day just because time passes.
* *Trading Significance:* This is the enemy of the option buyer and the best friend of the option seller. A Theta of -12 means the option will lose ₹12 by tomorrow simply due to time decay, even if NIFTY doesn't move a single point.


* **Vega:** Measures how much the option price will change for a 1% change in Implied Volatility.
* *Trading Significance:* Crucial during big events (like elections, earnings, or budget day). If Vega is high, a sudden drop in market fear (a drop in IV) can cause your option to lose massive value, even if the market moves in your desired direction (this is known as an "IV Crush").


* **Gamma:** The rate of change of Delta. It measures how fast your Delta will increase or decrease when the underlying moves.
* *Trading Significance:* Gamma represents explosive risk/reward. It gets extremely high for At-The-Money (ATM) options on Expiry Day. High Gamma means a small move in NIFTY can turn a worthless option into a highly profitable one (or vice versa).

---

### 5. Top 3 Columns for Quality Safe Trades

> **Question:** What are the most important columns — the top 3 — that help take a quality, safe trade that can give good premium?

To take a **high-quality, safe trade that also offers good premium**, you need to balance probability with risk. In options trading, "safety + good premium" usually means finding strikes with a high mathematical probability of winning, backed by institutional positioning, while ensuring the premium is not underpriced.

Based on the [Sensibull Option Chain](https://web.sensibull.com/option-chain?tradingsymbol=NIFTY&expiry=2026-07-21&view=all), the **top 3 most important columns** for this are:

#### 1. Delta (or POP — Probability of Profit)

If your primary goal is safety, **Delta** is your steering wheel.

* **Why it's crucial for safety:** While Delta technically measures how much an option price moves relative to NIFTY, professionals use it as a shortcut for **the probability of the option expiring In-The-Money** (worthless for the buyer, full profit for the seller).
* **How to use it for a safe trade:**
  * If you are looking to **sell options** (collect premium safely), look for a **Delta between 0.15 and 0.20** (or a **POP of 80% to 85%**).
  * This means the market is giving you an 80%+ statistical chance that NIFTY will *not* hit your strike price, allowing you to pocket the premium safely.

#### 2. OI (Open Interest) & OI Chg

Delta gives you the math; **Open Interest** gives you the market's muscle. It shows exactly where big institutions and heavy-pocketed writers have positioned their money.

* **Why it's crucial for safety:** Large institutions rarely move without research. If a specific strike has a massive block of Open Interest (the long blue/yellow bars on Sensibull), it acts as a **solid wall** — support or resistance.
* **How to use it for a safe trade:** Combine this with your Delta filter. Find a strike that has both a low Delta (high safety) *and* sits behind a massive OI wall. For example, to sell a Put safely, look for the highest Put OI strike below the current market price — NIFTY will struggle to break below that level.

#### 3. IV (Implied Volatility) & IVP (Implied Volatility Percentile)

While Delta and OI find your safe strike, **IV** tells you whether the premium you are collecting is actually *good* or underpriced.

* **Why it's crucial for good premium:** IV measures fear and uncertainty. When IV is high, option premiums swell; when IV is low, premiums shrink.
* **How to use it for a safe trade:** To collect a *good* premium safely, trade when **IV is relatively high** — or check **IVP** at the top of the Sensibull screen (e.g. IVP at 62 means current IV is higher than 62% of readings over the lookback period). Selling when IV/IVP is elevated means you get paid a larger premium for the same structural risk. When the market calms down, IV collapses and the premium drops rapidly in your favour ([IV Crush](#glossary--acronyms)).

#### Summary Checklist for a Quality Trade

| Step | Column | What to Look For |
|------|--------|------------------|
| 1 | **IV / IVP** | High enough that premiums are worth collecting |
| 2 | **Delta / POP** | OTM strike with Delta ~0.15 (POP ~80–85%) for statistical margin of safety |
| 3 | **OI & OI Chg** | Strike sits behind a massive institutional OI wall (support for puts, resistance for calls) |

---

## Glossary & Acronyms

Definitions below are aligned with official NSE terminology and widely cited educational sources: [NSE India Option Chain](https://www.nseindia.com/option-chain), [Zerodha Varsity](https://zerodha.com/varsity/), [Investopedia](https://www.investopedia.com/), and [Economic Times Markets](https://economictimes.indiatimes.com/markets).

### Acronyms — Quick Reference

| Acronym | Full Form |
|---------|-----------|
| **ATM** | At-The-Money |
| **CE** | Call European |
| **F&O** | Futures & Options |
| **ITM** | In-The-Money |
| **IV** | Implied Volatility |
| **IVP** | Implied Volatility Percentile |
| **LTP** | Last Traded Price |
| **NSE** | National Stock Exchange of India |
| **OI** | Open Interest |
| **OTM** | Out-of-The-Money |
| **PCR** | Put-Call Ratio |
| **PE** | Put European |
| **POP** | Probability of Profit |

### Financial Terms — Full Form & Definition

| Term | Full Form / Expansion | Definition |
|------|----------------------|------------|
| **Ask / Offer** | — | The lowest price at which a seller is willing to sell an option. Also called the *Offer* price. The price you pay when buying. |
| **ATM (At-The-Money)** | At-The-Money | An option whose strike price is equal to or closest to the current spot price of the underlying. ATM options have zero intrinsic value and the highest time value. |
| **Bid** | — | The highest price a buyer is willing to pay for an option. The price you receive when selling (if filled at bid). |
| **Breakeven** | — | The underlying price at which an option trade neither makes nor loses money at expiry. *Breakeven (%)* expresses this as the percentage move required from the current price. |
| **Call Option (CE)** | Call European | A derivative contract that gives the buyer the right (not obligation) to buy the underlying asset at the strike price on or before expiry. Index options on NSE are European-style and cash-settled. |
| **Delta (Δ)** | — | A Greek that measures how much an option's premium changes for a ₹1 (or 1-point) move in the underlying. Call delta ranges 0 to +1; put delta ranges −1 to 0. Also approximates the probability of expiring ITM. |
| **Expiry** | Expiration Date | The last date on which an options contract is valid. After expiry, the contract ceases to exist and is settled (cash-settled for index options on NSE). |
| **Extrinsic Value** | — | Same as *Time Value* — the portion of premium above intrinsic value, driven by time remaining and volatility. |
| **F&O** | Futures & Options | The derivatives segment of the stock market where standardized contracts on indices and stocks are traded. |
| **Gamma (Γ)** | — | A Greek measuring the rate of change of Delta for a 1-point move in the underlying. Highest for ATM options, especially near expiry. |
| **Greeks** | — | A set of risk metrics (Delta, Gamma, Theta, Vega, Rho) that quantify how an option's price responds to changes in underlying price, time, and volatility. |
| **Implied Volatility (IV)** | Implied Volatility | The market's forecast of how much the underlying asset's price is expected to fluctuate, embedded in the option premium. High IV = expensive options; low IV = cheaper options. IV does not indicate direction. |
| **Intrinsic Value** | — | The immediate exercise value of an option if expired today. For calls: Spot − Strike (if positive); for puts: Strike − Spot (if positive). Zero for OTM options; never negative. |
| **ITM (In-The-Money)** | In-The-Money | An option with positive intrinsic value. Call ITM when Spot > Strike; Put ITM when Spot < Strike. |
| **IV Crush** | Implied Volatility Crush | A sharp drop in IV after a major event (budget, RBI policy, earnings), causing option premiums to fall even if the underlying moves favourably. |
| **IVP (Implied Volatility Percentile)** | Implied Volatility Percentile | Ranks current IV against its own historical range (e.g. IVP 62 = current IV is higher than 62% of past readings). Helps decide if premiums are relatively expensive or cheap before selling or buying options. |
| **Last Traded Price (LTP)** | Last Traded Price | The price at which the most recent transaction in that option contract occurred. Represents the current market premium. |
| **Liquidity** | — | How easily an option can be bought or sold without significantly moving its price. High volume and tight bid-ask spread indicate good liquidity. |
| **LTP Chg / LTP (chg%)** | Last Traded Price Change | Absolute and percentage change in LTP from the previous trading session's closing price. |
| **Moneyness** | — | Classification of an option as ITM, ATM, or OTM based on the relationship between strike price and current spot price. |
| **NIFTY / Nifty 50** | National + Fifty | India's benchmark stock market index comprising 50 large-cap companies listed on NSE. The most actively traded index for F&O in India. |
| **Open Interest (OI)** | Open Interest | Total number of outstanding (unsettled) option contracts at a given strike. Unlike volume, OI counts live positions, not daily turnover. Rising OI = new positions; falling OI = positions being closed. |
| **Option Chain** | — | A tabular display of all available strike prices for calls and puts of an underlying, showing OI, volume, IV, LTP, and Greeks side by side. Published by NSE at [nseindia.com/option-chain](https://www.nseindia.com/option-chain). |
| **Option Premium** | — | The price paid by the buyer to the seller for an options contract. Premium = Intrinsic Value + Time (Extrinsic) Value. |
| **Option Writer** | — | The seller of an option who collects premium and assumes the obligation to fulfil the contract if the buyer exercises. Also called the *option seller*. |
| **OTM (Out-of-The-Money)** | Out-of-The-Money | An option with zero intrinsic value. Call OTM when Spot < Strike; Put OTM when Spot > Strike. |
| **PCR (Put-Call Ratio)** | Put-Call Ratio | Sentiment indicator: Total Put OI ÷ Total Call OI. PCR > 1 often read as bullish (more put writing/hedging); PCR < 1 as bearish. Extreme readings can be contrarian signals. |
| **PE (Put European)** | Put European | A derivative contract giving the buyer the right to sell the underlying at the strike price on or before expiry. |
| **POP (Probability of Profit)** | Probability of Profit | Estimated statistical probability that a trade will be profitable (typically ≥ ₹1) at expiry, derived from option pricing models and Greeks. |
| **Premium** | — | See *Option Premium*. |
| **Put Option** | — | See *PE (Put European)*. |
| **Resistance** | — | A price level where selling pressure is expected to cap upward movement. In option chain analysis, strikes with high Call OI are often treated as informal resistance zones. |
| **Slippage** | — | The difference between the expected trade price and the actual fill price, often caused by low liquidity or wide bid-ask spreads. |
| **Spot Price** | — | The current cash-market price of the underlying asset (e.g., NIFTY index level in the cash segment). |
| **Spread (Bid-Ask)** | — | The gap between the Bid and Ask prices. A narrow spread indicates high liquidity; a wide spread increases transaction cost. |
| **Strike Price** | — | The predetermined price at which the option holder can buy (call) or sell (put) the underlying asset. Each row in the option chain represents a different strike. |
| **Support** | — | A price level where buying interest is expected to prevent further decline. In option chain analysis, strikes with high Put OI are often treated as informal support zones. |
| **Theta (Θ)** | — | A Greek measuring daily time decay — how much an option's premium erodes per day as expiry approaches, all else equal. Negative for long options; benefits option sellers. |
| **Time Decay** | — | The erosion of an option's time value as expiry nears. Accelerates sharply in the final days/weeks. Measured by Theta. |
| **Time Value** | — | The portion of premium remaining after subtracting intrinsic value (`LTP − Intrinsic Value`). Reflects time to expiry and volatility expectations. Goes to zero at expiry. |
| **Vega (ν)** | — | A Greek measuring sensitivity of option premium to a 1% change in implied volatility. Highest for ATM options with more time to expiry. |
| **Volume** | — | Total number of contracts traded in a given option during the current session. High volume confirms active participation and better liquidity. |
| **Volatility Skew / Smile** | — | The pattern of differing IV levels across strikes. Indian index options typically show higher IV on OTM puts (negative skew), reflecting demand for downside protection. |

### Sources

- [NSE India — Option Chain (Equity Derivatives)](https://www.nseindia.com/option-chain)
- [Zerodha Varsity — Moneyness of an Option Contract](https://zerodha.com/varsity/chapter/moneyness-of-an-option-contract/)
- [Investopedia — Option Greeks](https://www.investopedia.com/terms/g/greeks.asp)
- [Investopedia — Using the Greeks to Understand Options](https://www.investopedia.com/trading/using-the-greeks-to-understand-options/)
- [Economic Times — Components of Option Premium](https://economictimes.indiatimes.com/markets/stocks/news/learn-with-etmarkets-do-you-know-these-components-of-option-premium/articleshow/99687334.cms)
- [Interactive Brokers — Introduction to Options: The Greeks](https://www.interactivebrokers.com/campus/trading-lessons/introduction-to-options-the-greeks/)
