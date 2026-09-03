# Options Trading — how is the market today?

## Table of Contents

1. [Different Expiries](#different-expiries)
   - [Weekly Options Expiries](#weekly-options-expiries)
   - [Monthly Options Expiries](#monthly-options-expiries)
2. [Market View](#market-view)
   - [Different Data Points to Form the Market View](#different-data-points-to-form-the-market-view)
   - [1. Price Action / Market Structure](#1-price-action--market-structure)
   - [2. Price vs OI Matrix](#2-price-vs-oi-matrix)
   - [3. FII / DII — Cash Market](#3-fii--dii--cash-market)
   - [4. FII / DII — F&O Participant-wise OI](#4-fii--dii--fo-participant-wise-oi)
     - [@Fii_Dii_Data on X](#fiidii-data-on-x)
     - [How to Read Participant-wise OI Data](#how-to-read-participant-wise-oi-data)
     - [Market View Scenarios](#market-view-scenarios)
     - [Golden Rule](#golden-rule)
   - [5. Five Market Views — Quick Reference](#5-five-market-views--quick-reference)
   - [6. India VIX](#6-india-vix)
   - [7. Option Chain — PCR, Max Pain, OI](#7-option-chain--pcr-max-pain-oi)
   - [8. Global Cues](#8-global-cues)
   - [9. News & Macros](#9-news--macros)
   - [10. Expiry Week — Special Rules](#10-expiry-week--special-rules)

> **Terms & acronyms:** See [trading_jargon_acronyms.md](./kb1/trading_jargon_acronyms.md) for PDH, PDL, PDC, FII, DII, PCR, and other definitions.

---

## Different Expiries

### Weekly Options Expiries

| Index | Exchange | Expiry Day |
|---|---|---|
| NIFTY 50 | NSE | Every Tuesday |
| SENSEX | BSE | Every Thursday |

### Monthly Options Expiries

1. **NSE (National Stock Exchange)**
   - All NSE monthly contracts expire on the **last Tuesday** of the expiry month.
2. **BSE (Bombay Stock Exchange)**
   - All BSE monthly contracts expire on the **last Thursday** of the expiry month.

---

## Market View

### Different Data Points to Form the Market View

> **Market view** = Global cues + Domestic data + Derivatives data. Read after **3:30 PM IST** (post-close) and recheck before **9:15 AM IST** (pre-open). **Intraday:** re-check change in OI every **30 minutes** — EOD views often shift in the first 45 minutes of the session.

---

#### 1. Price Action / Market Structure

**What to look:** NIFTY / BANKNIFTY close vs previous close; position vs key levels ([PDH](./kb1/trading_jargon_acronyms.md#pdh), [PDL](./kb1/trading_jargon_acronyms.md#pdl), [PDC](./kb1/trading_jargon_acronyms.md#pdc), weekly/monthly high-low, round numbers); candle type (bullish / bearish / doji). **Breadth:** if NIFTY looks bullish but BANKNIFTY or top heavyweights (Reliance, HDFC Bank, ICICI, Infosys, TCS) are weak, treat the move as low conviction. **Opening Range (ORH / ORL):** high and low of the first 15-min candle after 9:15 AM — intraday directional confirmation level; trade only after price sustains above ORH or below ORL. **VWAP:** price above VWAP = intraday institutional buying bias; below = selling bias.

**Where (open internet):**

| Source | Link |
|---|---|
| NSE India | [nseindia.com](https://www.nseindia.com) |
| Investing.com — NIFTY chart | [investing.com/indices/s-p-cnx-nifty-advanced-chart](https://www.investing.com/indices/s-p-cnx-nifty-advanced-chart) |
| TradingView | [tradingview.com — NIFTY](https://www.tradingview.com/chart/?symbol=NSE%3ANIFTY) |

---

#### 2. Price vs OI Matrix

Absolute OI marks support/resistance walls; **price change + OI change** marks trend **strength and conviction** — the key to separating *slightly* vs *strongly* bullish/bearish.

| Quadrant | Price | OI | Meaning |
|---|---|---|---|
| **Long Buildup** | ↑ | ↑ | New longs entering — strong uptrend |
| **Short Covering** | ↑ | ↓ | Shorts exiting — bounce, often fades at [PDH](./kb1/trading_jargon_acronyms.md#pdh) |
| **Short Buildup** | ↓ | ↑ | New shorts entering — strong downtrend |
| **Long Unwinding** | ↓ | ↓ | Longs booking profits — dip, often bounces at [PDL](./kb1/trading_jargon_acronyms.md#pdl) |

Apply to **Index Futures OI** (NSE participant data or Sensibull Fut OI vs Time). See [open_interest.md](./open_interest.md) for chart reading.

> **Ref:** [Zerodha Varsity — Open Interest](https://zerodha.com/varsity/chapter/open-interest/) · [OI Analysis for Traders (YouTube)](https://www.youtube.com/watch?v=5pt-dwdjh_w)

---

#### 3. FII / DII — Cash Market

**What to look:** FII net buy/sell and DII net buy/sell (₹ crore). Read the combination (both buying, FII buy + DII sell, FII sell + DII buy, both selling). Track over **5–20 days** — not a single day. Also check **delivery %** on index heavyweights — breakouts on low delivery/volume are often traps.

**Where (open internet):**

| Source | Link |
|---|---|
| NSE — FII/DII reports | [nseindia.com/reports/fii-dii](https://www.nseindia.com/reports/fii-dii) |
| Moneycontrol — FII/DII data | [moneycontrol.com/markets/fii-dii-data](https://www.moneycontrol.com/markets/fii-dii-data/) |

---

#### 4. FII / DII — F&O Participant-wise OI

**What to look:** FII, DII, Pro, Client positions across Index Futures, Index Options (Call / Put separately), Stock Futures — **Net Change** (today) and **Net OI** (cumulative).

**Where (open internet):**

| Source | Link |
|---|---|
| NSE — Derivatives reports | [nseindia.com/all-reports-derivatives](https://www.nseindia.com/all-reports-derivatives) |
| NiftyTrader — Participant-wise OI | [niftytrader.in/participant-wise-oi](https://www.niftytrader.in/participant-wise-oi) |
| Moneycontrol — OI participants | [moneycontrol.com/markets/fii-dii-data/oi-participants](https://www.moneycontrol.com/markets/fii-dii-data/oi-participants/) |
| Sensibull — FII/DII F&O | [web.sensibull.com/fii-dii-data](https://web.sensibull.com/fii-dii-data) |
| X — @Fii_Dii_Data (visual summary) | See detailed guide below |

##### @Fii_Dii_Data on X

- **Handler:** FIIDII Data — [@Fii_Dii_Data](https://x.com/Fii_Dii_Data) || [@FII_DII_Nifty](https://x.com/FII_DII_Nifty)
- **Note:** Open the info on tab manually so that the AI is able to read the data for better interpretation.

**Don't read it off a screenshot — fetch it.** `python3 tools/fii-dii/fii_dii.py <YYYY-MM-DD>` pulls
the same table straight from the NSE archive and prints the Gate 5 verdict with it.
*(A sample screenshot used to be linked here; the file was never committed.)*

##### How to Read Participant-wise OI Data

This table is a classic **Participant-wise Open Interest (OI) Data** sheet for the Indian stock market's derivatives segment (Futures & Options). Traders use this to gauge the sentiment of different market players—especially the "smart money" (FIIs)—to predict market direction.

**1. Understand the "Participants"**

The first column divides the market into four main categories of traders. Knowing who they are is crucial because their behavior tends to follow specific patterns:

| Participant | Who they are | How to use their data |
|---|---|---|
| **FII** (Foreign Institutional Investors) | Large foreign entities (funds, banks). They bring in big money and are usually considered the "smart money." | **The market trend often follows FII data.** |
| **DII** (Domestic Institutional Investors) | Indian mutual funds, insurance companies, etc. They mostly deal in cash markets but use derivatives to hedge. | Their derivative data is generally less predictive of short-term trends than FII data. |
| **Pro** (Proprietary Desk) | Trading desks of brokerages trading with their own capital. Highly skilled, high-frequency traders; often net option sellers. | Watch for alignment or divergence with FII positioning. |
| **Client** (Retail Investors / HNIs) | Regular individual traders. | Often used as a **contrarian indicator** — if Clients are highly bullish, the market might actually be heading down, and vice versa. |

**2. Understand the "Segments"**

This tells you *what* instruments these participants are trading:

| Segment | What it means |
|---|---|
| **Index Futures** (e.g., Nifty or BankNifty futures) | A straightforward bet on the market direction. |
| **Index Options** (overall) | Combined view of options; better to look at Calls and Puts individually. |
| **Call** | Right to buy. Buying calls = bullish; selling (writing) calls = bearish. |
| **Put** | Right to sell. Buying puts = bearish; selling (writing) puts = bullish. |
| **Stock Futures** | Bets on individual stock directions rather than the broader index. |

**3. Read the Core Metrics (the Columns)**

| Column | Meaning |
|---|---|
| **Net Change** | What happened *today*. New positions added or closed. **Negative (−)** = sold more than bought (net short). **Positive (+)** = bought more than sold (net long). |
| **Net OI** (Open Interest) | Cumulative total outstanding position currently held, carrying forward into tomorrow. Gives the macro view. |
| **T-1 Net OI** | Total outstanding positions as of *yesterday*. Compare with Net OI to see how much shifted today. |
| **Interpretation** | Color-coded stance: **Bullish** (green, expecting market to rise) or **Bearish** (red, expecting market to fall). |

**4. How to Connect the Dots (Practical Interpretation)**

Look for consensus or extreme divergence among participants, paying special attention to **FII** vs. **Client**.

**Analyze the FII stance (the trend setters)**

From the reference image above (14 Jul 2026), under **Net Change**:

- Index Futures: **−10,352** (bearish)
- Calls: **−2,960** (bearish)
- Puts: **+44,165** (bearish — buying puts)
- Stock Futures: **−81,587** (bearish)

*Conclusion:* FIIs created heavy short positions today. Their overall **Net OI** is also deeply bearish. They expect the market to go down.

**Analyze the Client stance (the contrarian view)**

From the same image, under **Net Change**:

- Index Futures: **+12,201** (bullish)
- Calls: **+1.07L** (bullish)
- Puts: **−22,601** (bullish — shorting/selling puts)

*Conclusion:* Retail clients were heavily buying into the market today, taking the opposite side of the FII trades. They are deeply bullish.

##### Market View Scenarios

Use the participant combinations below to classify the day's setup. The July 14, 2026 reference image maps to **Scenario 2**.

###### Scenario 1: The Classic Bullish Rally (Strong Bullish)

This is the most reliable bullish setup in the derivatives market.

| Participant | Stance |
|---|---|
| **FII** | Highly bullish — buying Index Futures, buying Calls, selling Puts |
| **Client** | Highly bearish — shorting Futures, selling Calls, buying Puts |
| **Pro** | Neutral to bullish |

**Market view:** **Strongly bullish.** Smart money is aggressively building long positions while retail is stuck on the short side. The market almost always rallies in this setup as retail is forced to cover their shorts.

###### Scenario 2: The Distribution / Trap Phase (Strong Bearish)

This is the exact setup seen in the data sheet from **14 Jul 2026** (reference image above).

| Participant | Stance |
|---|---|
| **FII** | Highly bearish — shorting Futures, selling Calls, buying Puts |
| **Client** | Highly bullish — buying Futures, buying Calls, selling Puts |
| **Pro** | Neutral to bearish |

**Market view:** **Strongly bearish.** FIIs are using retail enthusiasm to distribute their longs and build heavy short positions. When retail is overly optimistic and FIIs are shorting, a sharp market correction or crash is typically just around the corner.

**Scenario 3: Institutional Consensus (Ultra Bullish / Ultra Bearish)**

When the two smartest players in the game align, the market moves with high velocity.

| Combination | Market view |
|---|---|
| **FII + Pro** aligned (both building longs or both building shorts), **Client** on the opposite side | High-conviction trend |
| FII + Pro **bullish** vs. Client **bearish** | Massive breakout ahead |
| FII + Pro **bearish** vs. Client **bullish** | Severe breakdown ahead |

*Note:* Pros and FIIs rarely align perfectly, but when they do, it creates the highest-probability trades of the month.

**Scenario 4: The Option Writer's Trap (Potential Short Squeeze)**

Found by looking closely at Call/Put option data between FIIs and Pros.

| Participant | Stance |
|---|---|
| **Pro** | Heavily negative Net Change in Calls (selling/writing Calls — expecting the market won't rise) |
| **FII** | Heavily positive Net Change in Calls (buying Calls — expecting a breakout) |

**Market view:** **Potential short squeeze.** Pros are professional option writers and usually win, but FIIs have deeper pockets. If the market breaks above a key psychological resistance level, Pros will be forced to panic-buy and cover their short calls, triggering a violent upward spike.

###### Scenario 5: The Range-Bound / Sideways Market

| Participant | Stance |
|---|---|
| **FII** | Mixed or quiet (very low Net Change values across segments) |
| **Pro** | Negative Net Change in both Calls and Puts (shorting both sides — Straddles/Strangles) |
| **Client** | Actively buying options on both sides |

**Market view:** **Sideways / consolidation.** Pros are harvesting premium (theta decay) because they anticipate the market will get stuck in a tight range. Avoid buying options in this scenario — premium decay will bleed your capital.

###### Scenario 6: The Wild Volatility / Reversal Trap

| Participant | Stance |
|---|---|
| **FII** | Strongly directional (for example, heavily shorting Futures and buying Puts) |
| **Pro** | **Positive Net Change in both Calls and Puts** — consistent with buying Long Straddles/Strangles |
| **Client** | Usually trapped on the opposite side of the FII direction |

**Market view:** **Volatile directional — not a hold-and-sleep day.** This is a volatility overlay, not a sixth classification; retain one of the five market-view classifications below based on the full evidence.

*Interpretation:* Price may initially follow the heavy FII direction (for example, downward). But Pro buying on both sides signals an expectation of extreme volatility and a potentially violent reversal at key support or resistance. Do not carry unhedged directional positions all day; take intraday profits promptly and protect them with a trailing stop-loss.

##### Golden Rule

Always look at **Net Change** (today's action) to see immediate momentum, but validate it against **Net OI** (cumulative position) to see the bigger picture. A single day of FII shorting might just be profit-booking, but **3 consecutive days** of FII shorting combined with Client longing is a confirmed bearish regime.

---

#### 5. Five Market Views — Quick Reference

Combine [Price vs OI Matrix](#2-price-vs-oi-matrix), FII scenarios, PCR, and reality checks to classify the day:

| View | Price + OI | FII / Participants | PCR & Option Chain | Reality Check |
|---|---|---|---|---|
| **Strongly Bullish** | Long Buildup | [Scenario 1](#scenario-1-the-classic-bullish-rally-strong-bullish) — FII long, Client short | PCR > 1.30 · heavy Put writing at ATM | Heavyweights breaking resistance |
| **Slightly Bullish** | Short Covering | FII closing shorts (↓ short OI) | PCR 1.00–1.30 | Rally likely stalls at [PDH](./kb1/trading_jargon_acronyms.md#pdh) |
| **Strongly Bearish** | Short Buildup | [Scenario 2](#scenario-2-the-distribution--trap-phase-strong-bearish) — FII short, Client long | PCR < 0.80 · heavy Call writing ATM/OTM | VIX spiking |
| **Slightly Bearish** | Long Unwinding | FII closing longs, not building new shorts | PCR 0.80–1.00 | Dip often holds at [PDL](./kb1/trading_jargon_acronyms.md#pdl) |
| **Sideways** | Flat price · OI ↑ both sides | [Scenario 5](#scenario-5-the-range-bound--sideways-market) — Pros writing straddles | Max Pain ≈ ATM · PCR ~ 1.0 | VIX falling/crushing |

---

#### 6. India VIX

**What to look:** Current VIX level and direction (rising / falling / stable). Below 12 = calm; 12–16 = normal; 16–20 = moderate fear; 20–25 = high fear; above 25 = panic.

**Where (open internet):**

| Source | Link |
|---|---|
| NSE — India VIX | [nseindia.com/products-services/indices-vix](https://www.nseindia.com/products-services/indices-vix) |

---

#### 7. Option Chain — PCR, Max Pain, OI

**What to look:**

- **PCR** (Put OI ÷ Call OI): ⭐ **bands are defined once, in [`TRADING_CONSTANTS.md` §10a](../TRADING_CONSTANTS.md)** — `>1.30 bullish · 1.00–1.30 mildly bullish · 0.80–1.00 mildly bearish · <0.80 bearish`, no gaps. The `0.9–1.3 neutral / <0.7 bearish` scheme formerly quoted here left 0.70–0.90 unclassified and is retired.
- **Max Pain** strike — relevant mainly in expiry week
- **Highest Call OI** strike = resistance · **Highest Put OI** strike = support
- **Change in OI** — classify using [Price vs OI Matrix](#2-price-vs-oi-matrix) (not OI alone)
- **IVP (IV Percentile):** above 60 = elevated premiums, favourable for sellers; below 30 = cheap premiums, buyers' edge.
- **ATM Straddle Premium** (ATM CE LTP + ATM PE LTP) — market's priced-in expected move for the day; if intraday range stays within it, premium sellers win.
- **Volatility Skew:** OTM Put IV > OTM Call IV = bearish fear premium present even when PCR looks neutral.

**Where (open internet):**

| Source | Link |
|---|---|
| NSE — Option chain | [nseindia.com/option-chain](https://www.nseindia.com/option-chain) |
| Opstra — PCR, Max Pain, OI charts | [opstra.definedge.com](https://opstra.definedge.com) |
| NiftyTrader — OI & PCR | [niftytrader.in](https://www.niftytrader.in) |

---

#### 8. Global Cues

*(Check morning 7:00–8:30 AM IST)*

**What to look:**

- **GIFT Nifty** — expected gap-up / gap-down vs previous close
- **US markets** — Dow, S&P 500, Nasdaq (previous session)
- **Asian markets** — Nikkei, Hang Seng, Shanghai
- **Crude oil** — sharp moves affect INR and inflation
- **USD/INR** — weakening INR = FII outflow risk
- **Dollar Index (DXY)** — rising DXY = FII outflow pressure on India; cross-check against FII cash data.
- **US 10Y Treasury Yield** — rising yield (above 4.5%) = headwind for FII equity inflows into India.
- **Gold price** — sharp gold rally = risk-off globally; signals institutional demand for downside protection.

**Where (open internet):**

| Source | Link |
|---|---|
| Moneycontrol — Pre-market | [moneycontrol.com/markets/premarket](https://www.moneycontrol.com/markets/premarket/) |
| NSE India — GIFT Nifty | [nseindia.com](https://www.nseindia.com) |
| Trading Economics — Crude oil | [tradingeconomics.com/commodity/crude-oil](https://tradingeconomics.com/commodity/crude-oil) |
| RBI — USD/INR reference | [rbi.org.in](https://rbi.org.in) |
| Investing.com — Dollar Index | [investing.com/currencies/us-dollar-index](https://www.investing.com/currencies/us-dollar-index) |
| Investing.com — US 10Y Yield | [investing.com/rates-bonds/u.s.-10-year-bond-yield](https://www.investing.com/rates-bonds/u.s.-10-year-bond-yield) |
| Trading Economics — Gold | [tradingeconomics.com/commodity/gold](https://tradingeconomics.com/commodity/gold) |

---

#### 9. News & Macros

**What to look:** RBI / SEBI policy, Union Budget, Nifty earnings calendar, elections, Fed / FOMC, US CPI & jobs data, China data, geopolitics (Middle East, global risk-off events).

**Where (open internet):**

| Source | Link |
|---|---|
| Livemint | [livemint.com](https://www.livemint.com) |
| Economic Times — Markets | [economictimes.indiatimes.com/markets](https://economictimes.indiatimes.com/markets) |
| Moneycontrol — Earnings calendar | [moneycontrol.com](https://www.moneycontrol.com) |
| RBI | [rbi.org.in](https://rbi.org.in) |
| SEBI | [sebi.gov.in](https://www.sebi.gov.in) |
| Reuters — Markets | [reuters.com/markets](https://www.reuters.com/markets) |

**Avoid:** Telegram tips, WhatsApp groups, anonymous X accounts, paid tip services.

---

#### 10. Expiry Week — Special Rules

*(Only applies within 3 trading days of Tuesday NIFTY expiry or Thursday SENSEX expiry)*

- **Max Pain gravity stronger** — spot tends to close near Max Pain if gap to spot is < 100 points.
- **Theta decays faster** — avoid buying ATM options in the last 3 days; decay is ~20–30% higher per day.
- **Gamma spikes** — ATM options can double or halve in the final 60 minutes; highest risk/reward window.
- **PCR signal weakens in expiry week** — OI concentrates into the expiring series and PCR compresses toward 1.0. Treat **0.90–1.10 as uninformative** rather than as "mildly" anything; outside that, the [`TRADING_CONSTANTS.md` §10a](../TRADING_CONSTANTS.md) bands still apply.
- **Monthly vs weekly strikes** — do not use monthly strike OI to judge weekly expiry sentiment if they differ.

**Mark session type before forming market view:**
**Pre-Expiry** (> 5 days) · **Near-Expiry** (2–4 days) · **Expiry Day**
