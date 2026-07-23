Based on the [Sensibull Option Chain](https://web.sensibull.com/option-chain?tradingsymbol=NIFTY&expiry=2026-07-21&view=all) you are viewing, here is a detailed breakdown of all the columns, what they mean, and how you can use them in real-world trading.

For acronyms and term definitions, see [trading_jargon_acronyms.md](./trading_jargon_acronyms.md).

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
| 6 | [Live Market Monitoring — Smart Money Footprints](#6-live-market-monitoring--smart-money-footprints) | Intraday OI change, heavy writing, real-time squeeze/unwind signals |
| 7 | [Pre-Trade Go/No-Go Checklist — Session Learnings](#7-pre-trade-gono-go-checklist--session-learnings) | Theta trap pattern, GIFT Nifty caveats, VIX direction, when to sit out |

> **Terms & acronyms:** See [trading_jargon_acronyms.md](./trading_jargon_acronyms.md) for full definitions.

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
| Intraday OI Change | Live Monitoring | [§6](#6-live-market-monitoring--smart-money-footprints) |
| OI vs Strike Chart | Live Monitoring | [§6](#6-live-market-monitoring--smart-money-footprints) |
| Multi-Strike OI Chart | Live Monitoring | [§6](#6-live-market-monitoring--smart-money-footprints) |
| Intraday PCR Slope | Live Monitoring | [§6](#6-live-market-monitoring--smart-money-footprints) |
| GIFT Nifty Caveat | Pre-Trade Filter | [§7](#7-pre-trade-gono-go-checklist--session-learnings) |
| Theta Trap Pattern | Pre-Trade Filter | [§7](#7-pre-trade-gono-go-checklist--session-learnings) |
| VIX Direction Filter | Pre-Trade Filter | [§7](#7-pre-trade-gono-go-checklist--session-learnings) |
| FII Futures Divergence | Pre-Trade Filter | [§7](#7-pre-trade-gono-go-checklist--session-learnings) |
| Pre-Trade Go/No-Go Checklist | Pre-Trade Filter | [§7](#7-pre-trade-gono-go-checklist--session-learnings) |

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
* **How to use it for a safe trade:** To collect a *good* premium safely, trade when **IV is relatively high** — or check **IVP** at the top of the Sensibull screen (e.g. IVP at 62 means current IV is higher than 62% of readings over the lookback period). Selling when IV/IVP is elevated means you get paid a larger premium for the same structural risk. When the market calms down, IV collapses and the premium drops rapidly in your favour ([IV Crush](./trading_jargon_acronyms.md#volatility--sentiment)).

#### Summary Checklist for a Quality Trade

| Step | Column | What to Look For |
|------|--------|------------------|
| 1 | **IV / IVP** | High enough that premiums are worth collecting |
| 2 | **Delta / POP** | OTM strike with Delta ~0.15 (POP ~80–85%) for statistical margin of safety |
| 3 | **OI & OI Chg** | Strike sits behind a massive institutional OI wall (support for puts, resistance for calls) |

---

### 6. Live Market Monitoring — Smart Money Footprints

> **Core idea:** Move away from static, lagging indicators (moving averages, RSI) and track **real-time institutional footprints** through live derivatives data. Option writing requires heavy margin (₹1 Lakh+ per lot on NSE/BSE), so aggressive writing is almost always **institutional** — FIIs and Pro Desks placing multi-crore bets you can see in the chain.

During market hours, keep the [Sensibull Live Option Chain](https://web.sensibull.com/option-chain?view=greeks) open. Focus on **OI-lakh** and **OI Chg** on both CE and PE sides as spot moves.

#### 1. Intraday OI Change (Not EOD OI)

Total OI shows where historical walls sit. **Intraday OI Change** (refreshed every ~5 minutes) shows what big players are doing *right now*.

* **What to watch:** Strikes where OI is expanding or shedding rapidly within a 15-minute window.
* **Example — Short Buildup:** Market falling + Call OI expanding fast at ATM → institutions are writing calls to cap upside (high-conviction bearish positioning).
* **Tool:** [Sensibull Multi-Strike OI Chart](https://web.sensibull.com/open-interest/multistrike-oi?tradingsymbol=NIFTY) — plot 3 CE and 3 PE strikes around spot on a time-series line.

#### 2. Heavy Writing at Specific Strikes

Option buyers need little capital; **writers need massive margin**. Tall OI bars = institutional conviction, not retail noise.

| Signal | What It Means | Read As |
|--------|---------------|---------|
| **Heavy Call Writing (CE)** | Big players selling calls at a strike | Aggressive **resistance** — market unlikely to cross that level |
| **Heavy Put Writing (PE)** | Big players selling puts at a strike | Hard **support floor** — market unlikely to break below |

* **Tools:** [OI vs Strike Chart](https://web.sensibull.com/open-interest/oi-vs-strike?tradingsymbol=NIFTY) for tallest bars; live option chain for strike-by-strike detail.

#### 3. Real-Time "Sure Shot" Setups

High-probability intraday moves show up when institutions get trapped or double down:

| Setup | What to Watch | What It Signals |
|-------|---------------|-----------------|
| **Short Squeeze / Unwinding** | Spot breaks a heavily written strike; Put OI drops fast in real time | Support collapsing — writers panicking, sharp flush likely |
| **Multi-Strike OI Crossover** | A CE OI line shoots up and crosses a PE OI line near current price | Bears took control of that price zone |
| **Intraday PCR Slope** | PCR line on a 5-min chart sloping steeply **down** | Aggressive call writing across strikes — structural weakness |

> **Practical workflow:** (1) Identify the heaviest CE/PE writing strikes from OI vs Strike. (2) Track intraday OI change on those strikes every 5 minutes. (3) Watch for unwind (OI drop) or fresh buildup (OI spike) when spot approaches or breaks a level. (4) Confirm with PCR slope, not a single static PCR number.

---

### 7. Pre-Trade Go/No-Go Checklist — Session Learnings

> These filters come from live trading sessions where pre-market analysis looked solid but the market behaved differently. They catch the edge cases that theoretical frameworks miss.

---

#### Filter 1: Never Over-Weight GIFT Nifty Alone

**The trap:** GIFT Nifty showed a 100–115 pt gap-down. Actual open was only 22 pts down. A large pre-market signal does not guarantee a large actual gap.

**Rule:** Treat GIFT Nifty as a *direction* indicator, not a *magnitude* indicator. Before deciding how aggressively to trade the gap, wait for the actual open and the first 5-minute candle to confirm the scale of the move. Cross-check with SGX/Dow futures and dollar-index trend — if global cues are mixed, discount the GIFT Nifty reading by 50%.

---

#### Filter 2: PDL and PDH Are Near-Exact Levels, Not Zones

**The observation:** On 21 July 2026, the PDL was 24,135.85. The intraday low was 24,135.65 — a difference of just 0.20 points. Dip buyers stepped in almost to the tick.

**Rule:** Treat PDH and PDL as **hard lines**, not broad zones. When placing a stop-loss or targeting a breakdown entry, do not buffer these levels by 20–30 points. Watch price action at the exact level first — if it holds twice, it is a structural support/resistance worth respecting.

---

#### Filter 3: VIX Direction Matters as Much as VIX Level

**The trap:** VIX was at 13 (calm zone). Expectation was that it would spike on a gap-down and validate bearish momentum. Instead VIX fell further to 12.6.

**Rule:** Before any directional option buy, check whether VIX is rising or falling:

| VIX Behaviour | Environment | What to Do |
|---------------|-------------|------------|
| **Rising (even if below 15)** | Fear entering the market | Directional option buys can work; risk is expanding |
| **Flat/Falling (even on a falling market)** | Option writers in control | Avoid naked directional buys; theta decay is brutal |
| **Sudden spike past 16–17** | Panic / institutional unwinding | Only then consider buying OTM puts/calls for momentum |

---

#### Filter 4: Recognise the "Theta Trap" Session Before Entering

A **Theta Trap** is a session deliberately engineered by institutional option writers to make the day range-bound, killing all premium buyers from both sides.

**Signature — watch for all three together:**
1. VIX is low (≤ 14) **and falling** intraday
2. Call OI is rapidly building (heavy CE writing at ATM or just OTM)
3. Put OI is unwinding (put writers covering) rather than building

**What it means:** Institutions are capping both upside (fresh call writing) and already holding enough put writing below to create a floor. The market chops sideways eating up theta. Option buyers on CE and PE both lose even if the underlying moves a little in their favour.

**Rule:** If all three signals are present by 10:00 AM, *do not take any directional option buy*. The correct trade is either:
- A short Iron Condor / short strangle (if your capital allows the margin), or
- **Sit out entirely** — sitting out is a valid, profitable decision when the session is a theta trap.

> *From 21-Jul-2026: PCR fell from 1.2 (bullish) to 0.81 (bearish) while VIX dropped. Total Call OI (15.45 Cr) crushed Put OI (12.56 Cr) by end-of-day. The session was a textbook theta trap; not trading was the best outcome.*

---

#### Filter 5: FII Futures Divergence = No Clean Directional Edge

**The trap:** FIIs bought +3,690 Nifty futures (bullish signal) but shorted -6,914 BankNifty futures (bearish signal) on the same day. Acting on either signal alone would have led to a wrong-sided trade.

**Rule:** When FII Index Futures and FII Sector Futures (BankNifty/FinNifty) are pointing in *opposite directions*, treat it as a **mixed / no-signal** day. Do not use FII data to justify a directional trade. Wait for 2–3 consecutive days of alignment before calling an FII-driven regime.

---

#### Filter 6: PCR Shift Intraday Is More Powerful Than Opening PCR

**The observation:** Opening PCR was 1.2 (apparently bullish). By end of day it was 0.81 — a massive shift driven entirely by aggressive Call writing. The direction of PCR *during the session* was more informative than the static opening number.

**Rule:** Check PCR at three points — pre-market, 11:30 AM, and 2:30 PM. If PCR is falling steadily despite a flat or rising market, institutions are writing calls to cap the upside; treat the day as range-bound or mildly bearish regardless of the opening PCR.

---

#### Summary: Pre-Trade Go/No-Go Quick Check

Run this checklist **after the first 15 minutes of trading**:

| # | Check | Green (Trade OK) | Red (Sit Out or Adjust) |
|---|-------|-----------------|------------------------|
| 1 | **VIX direction** | Rising or flat | Falling intraday |
| 2 | **Actual open vs GIFT Nifty** | Gap confirmed within 50% of signal | Gap mostly filled at open |
| 3 | **Theta trap signs** | Either VIX rising, OI building on both sides, or PCR stable | VIX falling + Call OI surging + Put OI unwinding |
| 4 | **FII F&O alignment** | Index and sector futures in same direction for 2+ days | Divergent or contradictory (buy index, sell sector) |
| 5 | **PCR trend (intraday)** | Stable or rising from open | Falling steadily despite flat/sideways price |

**Decision rule:** 3 or more Red signals = sit out or sell premium only (never buy naked options).
