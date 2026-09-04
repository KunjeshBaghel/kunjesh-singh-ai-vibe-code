# The FII and DII data 

## what table means? 

### Participant: 
- The category of the investor or trader (explained in detail below).

- **Fii (Foreign Institutional Investors):** Large foreign entities like international mutual funds, pension funds, or foreign banks investing in India. Their movements are heavily watched because they bring in massive amounts of money and often drive market trends.

- **Dii (Domestic Institutional Investors):** Large Indian financial institutions, such as Indian mutual funds, insurance companies (like LIC), and local banks. They often act as a counterweight to FIIs.

- **Pro (Proprietary Traders):** Professional trading firms or brokers who are trading with their own firm's money to make a profit, rather than trading on behalf of clients. They are highly active and sophisticated.

- **Client:** This represents retail investors (individual traders like you and me) as well as High Net Worth Individuals (HNIs).

### Segment: 
- The specific financial instrument they are trading (e.g., Futures or Options).

- **Index Futures:** These are futures contracts based on a broad market index, such as the Nifty 50 or Bank Nifty. A futures contract obligates the buyer to purchase (or the seller to sell) the index at a predetermined future date and price.
- **Index Options:** This row represents the aggregate activity in options contracts for market indices. Options give the buyer the right, but not the obligation, to buy or sell the index.
- **Call (Subset of Index Options):** 
  - Buying a Call is a bullish bet (expecting the market to go up).
  - Selling (writing) a Call is a bearish or neutral bet.
- **Put (Subset of Index Options):**
  - Buying a Put is a bearish bet (expecting the market to go down).
  - Selling (writing) a Put is a bullish or neutral bet.
- **Stock Futures:** These are futures contracts based on individual company stocks (e.g., Reliance Industries, HDFC Bank) rather than the entire market index.


### Net Change: 
- The day's specific trading activity. It shows the net difference between the new long (buy) positions and short (sell) positions created or closed on this specific day.

Note: The numbers are often denoted with an 'L', which stands for Lakhs (1 Lakh = 100,000).
  - **Positive Number:** They added net longs (Bullish).
  - **Negative Number:** They added net shorts (Bearish).

### Interpretation (Next to Net Change): 
- What that specific day's activity implies. Bullish means their daily trades suggest they expect the market to go up. Bearish means their trades suggest they expect it to fall.

### Net OI (Open Interest): 
- The total number of outstanding (open) contracts currently held by that participant at the end of the day.
  - **Positive Number:** Their overall standing position is net long (Bullish).
  - **Negative Number:** Their overall standing position is net short (Bearish). (betting against the market)

### Interpretation (Next to Net OI): 
- The overall, longer-term stance of the participant based on their total open positions, categorized as either Bullish or Bearish.

### T-1 Net OI: 
- The total outstanding Open Interest from the previous trading day (T-1 stands for Today minus 1). If you subtract T-1 Net OI from the current Net OI, you get the day's Net Change.

### how to get this data?
- open https://x.com/Fii_Dii_Data/status || https://x.com/FII_DII_Nifty/
- open on browser [fii_dii_data_2026.md] /Users/kbaghel/Desktop/my_kb/Git/kunjesh-singh-ai-vibe-code/real-learnings/money/treadings/my-treads/fii_dii_data_2026.md
- [Prompt] Convert the image data into the markdown file format, like we have in [fii_dii_data_2026.md] (for example) tab at ## Date 28-July-2026


## 31/08/2026 — FII Activity Last 5 Days (computed from NSE CSV, replaces X.com)

**Formula:** FII Activity = (Opt Idx Call Long − Opt Idx Call Short) − (Opt Idx Put Long − Opt Idx Put Short) + (Fut Idx Long − Fut Idx Short)
*Verified exact match against @Fii_Dii_Data X.com image for 31-Aug-2026.*

| Day | Date | FII Activity | Trend |
| :--- | :--- | ---: | :--- |
| T | 31-Aug-2026 | **+40,829** | Bullish |
| T-1 | 28-Aug-2026 | **+62,995** | Bullish |
| T-2 | 27-Aug-2026 | **−1,12,312** | Bearish |
| T-3 | 26-Aug-2026 | **−45,603** | Bearish |
| T-4 | 25-Aug-2026 | *68,928 (X.com)* | Bullish* |
| **Overall By Count** | | 3 Bullish / 2 Bearish | **Bullish** |
| **Overall By Sentiment** | | +14,837 net | **Bullish** |

*25-Aug distortion: expiry day turnover inflates raw vol ~8×; X.com value used as-is.*

---

## 31/08/2026 — NSE Official Participant-wise OI (T-1 for 01-Sep session)

*Source: https://archives.nseindia.com/content/nsccl/fao_participant_vol_31082026.csv (public, no auth)*

| Participant | Idx Fut Long | Idx Fut Short | Idx Fut Net | Idx Call Long | Idx Call Short | Idx Call Net | Idx Put Long | Idx Put Short | Idx Put Net | Reading |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | :--- |
| **FII** | 11,785 | 18,467 | **−6,682** | 44,26,946 | 44,22,388 | **+4,558** | 43,77,447 | 44,20,400 | **−42,953** | Short Futures, Put Writer (Mixed-Range) |
| **Client** | 34,766 | 33,506 | **+1,260** | 2,71,89,568 | 2,70,85,083 | **+1,04,485** | 2,98,73,540 | 2,98,34,520 | **+39,020** | Bullish (contrarian = bearish signal) |
| **Pro** | 21,752 | 16,405 | **+5,347** | 3,49,12,995 | 3,50,21,998 | **−1,09,003** | 3,53,21,489 | 3,53,14,851 | **+6,638** | Long Futures + Short Calls (Range/Covered) |
| **DII** | 333 | 258 | **+75** | 440 | 480 | **−40** | 435 | 3,140 | **−2,705** | Negligible |

**Regime reading (01-Sep pre-market):**
FII: Not cleanly bearish — short futures BUT writing 42,953 net puts (bullish/range). Pro: Long futures + short calls = range/capped upside. Retail bullish (contrarian → slight bearish signal).
→ **Pattern: Range-Bound / Institutional Consensus** (not Distribution/Trap). Aligns with 24,000 PE wall holding + 24,100-24,200 CE ceiling.

---

## 28/08/2026 - FII DII Data at a Glance**

| Participant | Segment | Net Change | Interpretation | Net OI | Interpretation | T-1 Net OI |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Fii** | Index Futures | -4,841 | Bearish | -2.03L | Bearish | -1.98L |
| | Index Options | 67,836 | Bullish | -8.24L | Bearish | -8.92L |
| | Call | 35,836 | Bullish | -2.3L | Bearish | -2.66L |
| | Put | -32,000 | Bullish | 5.94L | Bearish | 6.26L |
| | Stock Futures | 7,856 | Bullish | 5.49L | Bullish | 5.41L |
| **Dii** | Index Futures | 700 | Bullish | 20,213 | Bullish | 19,513 |
| | Index Options | -950 | Bearish | -30,139 | Bearish | -29,189 |
| | Call | 25 | Bullish | 4,350 | Bullish | 4,325 |
| | Put | 975 | Bearish | 34,489 | Bearish | 33,514 |
| | Stock Futures | -27,612 | Bearish | -41.64L | Bearish | -41.36L |
| **Pro** | Index Futures | 1,340 | Bullish | 5,461 | Bullish | 4,121 |
| | Index Options | 1.67L | Bullish | 38,256 | Bullish | -1.29L |
| | Call | 1.62L | Bullish | 1.34L | Bullish | -27,622 |
| | Put | -4,892 | Bullish | 96,217 | Bearish | 1.01L |
| | Stock Futures | 12,906 | Bullish | 4.54L | Bullish | 4.41L |
| **Client** | Index Futures | 2,801 | Bullish | 1.77L | Bullish | 1.74L |
| | Index Options | -2.34L | Bearish | 8.16L | Bullish | 10.5L |
| | Call | -1.98L | Bearish | 91,197 | Bullish | 2.89L |
| | Put | 35,917 | Bearish | -7.25L | Bullish | -7.61L |
| | Stock Futures | 6,850 | Bullish | 31.61L | Bullish | 31.54L |


## 27/08/2026 - FII Activity for last 5 days**

| Period | Value | Trend |
| :--- | :--- | :--- |
| Today (T) | -112312 | Bearish |
| T-1 Day | -45603 | Bearish |
| T-2 Day | 68928 | Bullish |
| T-3 Day | -105095 | Bearish |
| T-4 Day | 28907 | Bullish |
| **Overall Trend** | By Count | Bearish |
| **Overall Trend** | By Sentiment | Bearish |

*Get FREE Algo Tools at BluechipAlgos.com*

## 26/08/2026 - FII DII FNO ACTIVITY

| Participant | Instrument | Change | Activity | Trend |
| :--- | :--- | :--- | :--- | :--- |
| FII | Future | -1,833 | Sold Futures | Bearish |
| FII | CE | -37,455 | Sold Calls | Bearish |
| FII | PE | 6,315 | Bought Puts | Bearish |
| PRO | Future | -1,061 | Sold Futures | Bearish |
| PRO | CE | -58,893 | Sold Calls | Bearish |
| PRO | PE | 51,150 | Bought Puts | Bearish |
| DII | Future | 247 | Bought Futures | Bullish |
| DII | CE | -30 | Sold Calls | Bearish |
| DII | PE | 1,516 | Bought Puts | Bearish |
| RETAIL | Future | 2,647 | Bought Futures | Bullish |
| RETAIL | CE | 96,378 | Bought Calls | Bullish |
| RETAIL | PE | -58,982 | Sold Puts | Bullish |
| **OVERALL TREND:** | - | - | - | **BEARISH** |

## 26/08/2026 - FII Activity for last 5 days
| Period / Metric | Value | Trend |
| :--- | :--- | :--- |
| Today (T) | -45603 | Bearish |
| T-1 Day | 68928 | Bullish |
| T-2 Day | -105095 | Bearish |
| T-3 Day | 28907 | Bullish |
| T-4 Day | 170195 | Bullish |
| Overall Trend (By Count) | - | Bullish |
| Overall Trend (By Sentiment) | - | Bullish |

## 25/08/2026 - FII Activity for last 5 days

| Period / Metric | Value / Category | Signal |
| :--- | :---: | :---: |
| Today (T) | 68928 | Bullish |
| T-1 Day | -105095 | Bearish |
| T-2 Day | 28907 | Bullish |
| T-3 Day | 170195 | Bullish |
| T-4 Day | -58118 | Bearish |
| **Overall Trend** | **By Count** | Bullish |
| **Overall Trend** | **By Sentiment** | Bullish |

## 25/08/2026 - FII DII FNO ACTIVITY

| Category | Instrument | Change | Activity | Trend |
| :--- | :--- | :--- | :--- | :--- |
| FII | Future | 35,156 | Bought Futures | Bullish |
| | CE | 1,250 | Bought Calls | Bullish |
| | PE | -32,522 | Sold Puts | Bullish |
| PRO | Future | -3,958 | Sold Futures | Bearish |
| | CE | 1,35,000 | Bought Calls | Bullish |
| | PE | -1,74,000 | Sold Puts | Bullish |
| DII | Future | -7,678 | Sold Futures | Bearish |
| | CE | -4074 | Sold Calls | Bearish |
| | PE | -33,089 | Sold Puts | Bullish |
| RETAIL | Future | -23,520 | Sold Futures | Bearish |
| | CE | -1,32,000 | Sold Calls | Bearish |
| | PE | 2,40,000 | Bought Puts | Bearish |
| **OVERALL TREND:** | | | | **BULLISH** |

*Note: Trend calculated using our proprietary method*
*Get FREE Algo Tools at BluechipAlgos.com*

## 19/08/2026 - FII DII FNO ACTIVITY

| Participant | Instrument | Change | Activity | Trend |
| :--- | :--- | :--- | :--- | :--- |
| **FII** | Future | -15,649 | Sold Futures | Bearish |
| | CE | -81,925 | Sold Calls | Bearish |
| | PE | -39,456 | Sold Puts | Bullish |
| **PRO** | Future | 7,541 | Bought Futures | Bullish |
| | CE | 1,05,000 | Bought Calls | Bullish |
| | PE | 57,977 | Bought Puts | Bearish |
| **DII** | Future | -3,504 | Sold Futures | Bearish |
| | CE | 0 | Sold Calls | Bearish |
| | PE | -3,104 | Sold Puts | Bullish |
| **RETAIL** | Future | 11,612 | Bought Futures | Bullish |
| | CE | -22,677 | Sold Calls | Bearish |
| | PE | -15,419 | Sold Puts | Bullish |



## 19/08/2026 - FII Activity for last 5 days

| Day | Value | Sentiment |
| :--- | :--- | :--- |
| **Today (T)** | -58118 | Bearish |
| **T-1 Day** | -124707 | Bearish |
| **T-2 Day** | 37952 | Bullish |
| **T-3 Day** | -18860 | Bearish |
| **T-4 Day** | -35814 | Bearish |

---

## Overall Trend

| Metric | Status |
| :--- | :--- |
| **By Count** | Bearish |
| **By Sentiment** | Bearish |

## 14/08/2026 - FII DII FNO ACTIVITY

| Category | Instrument | Change | Activity | Trend |
| :--- | :--- | :--- | :--- | :--- |
| **FII** | Future | -7,996 | Sold Futures | Bearish |
| | CE | 12,196 | Bought Calls | Bullish |
| | PE | 23,060 | Bought Puts | Bearish |
| **PRO** | Future | 959 | Bought Futures | Bullish |
| | CE | 49,637 | Bought Calls | Bullish |
| | PE | 99,219 | Bought Puts | Bearish |
| **DII** | Future | 741 | Bought Futures | Bullish |
| | CE | -40 | Sold Calls | Bearish |
| | PE | -148 | Sold Puts | Bullish |
| **RETAIL** | Future | 6,296 | Bought Futures | Bullish |
| | CE | -61,793 | Sold Calls | Bearish |
| | PE | -1,22,000 | Sold Puts | Bullish |
| **OVERALL TREND** | — | — | — | **BULLISH** |

> **Note:** Trend calculated using our proprietary method.  
> **Get FREE Algo Tools at BluechipAlgos.com**

## 14/08/2026 - FII Activity for Last 5 Days

| Period | Net Value | Sentiment |
| :--- | :--- | :--- |
| **Today (T)** | -18860 | Bearish |
| **T-1 Day** | -35814 | Bearish |
| **T-2 Day** | -56991 | Bearish |
| **T-3 Day** | -56963 | Bearish |
| **T-4 Day** | -4390 | Bearish |
| **Overall Trend: By Count** | — | **Bearish** |
| **Overall Trend: By Sentiment** | — | **Bearish** |


## 07/08/2026 - FII Activity for last 5 days

| Period / Category | Value / Metric | Sentiment / Trend |
| :--- | :--- | :--- |
| Today (T) | -81711 | Bearish |
| T-1 Day | 152876 | Bullish |
| T-2 Day | -44168 | Bearish |
| T-3 Day | -91757 | Bearish |
| T-4 Day | 98667 | Bullish |
| **Overall Trend** | By Count | Bullish |
| | By Sentiment | Bearish |

*Get FREE Algo Tools at BluechipAlgos.com*

### 07/08/2026 - FII DII FNO ACTIVITY

| Category | Instrument | Change | Activity | Trend |
| :--- | :--- | :--- | :--- | :--- |
| FII | Future | -4,940 | Sold Futures | Bearish |
| FII | CE | -49,986 | Sold Calls | Bearish |
| FII | PE | 26,785 | Bought Puts | Bearish |
| PRO | Future | -1,436 | Sold Futures | Bearish |
| PRO | CE | 49,749 | Bought Calls | Bullish |
| PRO | PE | 1,40,000 | Bought Puts | Bearish |
| DII | Future | -143 | Sold Futures | Bearish |
| DII | CE | 1163 | Bought Calls | Bullish |
| DII | PE | 1,470 | Bought Puts | Bearish |
| RETAIL | Future | 6,519 | Bought Futures | Bullish |
| RETAIL | CE | -927 | Sold Calls | Bearish |
| RETAIL | PE | -1,68,000 | Sold Puts | Bullish |

**OVERALL TREND: BEARISH**

*Note: Trend calculated using our proprietary method*  
*Get FREE Algo Tools at BluechipAlgos.com*


## 07/08/2026 - FII DII FNO ACTIVITY

| Entity | Instrument | Change | Activity | Trend |
| :--- | :--- | :--- | :--- | :--- |
| FII | Future | -4,940 | Sold Futures | Bearish |
| FII | CE | -49,986 | Sold Calls | Bearish |
| FII | PE | 26,785 | Bought Puts | Bearish |
| PRO | Future | -1,436 | Sold Futures | Bearish |
| PRO | CE | 49,749 | Bought Calls | Bullish |
| PRO | PE | 1,40,000 | Bought Puts | Bearish |
| DII | Future | -143 | Sold Futures | Bearish |
| DII | CE | 1163 | Bought Calls | Bullish |
| DII | PE | 1,470 | Bought Puts | Bearish |
| RETAIL | Future | 6,519 | Bought Futures | Bullish |
| RETAIL | CE | -927 | Sold Calls | Bearish |
| RETAIL | PE | -1,68,000 | Sold Puts | Bullish |
| **OVERALL TREND:** | | | | **BEARISH** |

**Note:** Trend calculated using our proprietary method  
Get FREE Algo Tools at BluechipAlgos.com


## 07/08/2026 - FII Activity for last 5 days

| Period | Value | Sentiment |
| :--- | :--- | :--- |
| Today (T) | -81711 | Bearish |
| T-1 Day | 152876 | Bullish |
| T-2 Day | -44168 | Bearish |
| T-3 Day | -91757 | Bearish |
| T-4 Day | 98667 | Bullish |
| **Overall Trend** | **By Count** | **Bullish** |
| **Overall Trend** | **By Sentiment** | **Bearish** |

**Note:** Get FREE Algo Tools at BluechipAlgos.com


## 05/08/2026 - FII DII FNO ACTIVITY

| Entity | Instrument | Change | Activity | Trend |
| --- | --- | --- | --- | --- |
| FII | Future | -5,130 | Sold Futures | Bearish |
| FII | CE | -63,594 | Sold Calls | Bearish |
| FII | PE | -24,556 | Sold Puts | Bullish |
| PRO | Future | 6,123 | Bought Futures | Bullish |
| PRO | CE | 1,65,000 | Bought Calls | Bullish |
| PRO | PE | 80,921 | Bought Puts | Bearish |
| DII | Future | -2,847 | Sold Futures | Bearish |
| DII | CE | -10 | Sold Calls | Bearish |
| DII | PE | 1,254 | Bought Puts | Bearish |
| RETAIL | Future | 1,854 | Bought Futures | Bullish |
| RETAIL | CE | -1,02,000 | Sold Calls | Bearish |
| RETAIL | PE | -57,618 | Sold Puts | Bullish |
| **OVERALL TREND:** |  |  |  | **BEARISH** |

**Note:** Trend calculated using our proprietary method


## 05/08/2026 - FII Activity for last 5 days

| Period | Value | Sentiment |
| --- | --- | --- |
| Today (T) | -44168 | Bearish |
| T-1 Day | -91757 | Bearish |
| T-2 Day | 98667 | Bullish |
| T-3 Day | -7786 | Bearish |
| T-4 Day | 26585 | Bullish |
| **Overall Trend** | **By Count** | **Bearish** |
| **Overall Trend** | **By Sentiment** | **Bearish** |

**Note:** Get FREE Algo Tools at BluechipAlgos.com *(Text from the bottom of the image)*



## 03/08/2026 - FII DII FNO ACTIVITY

| Participant | Instrument | Change | Activity | Trend |
| :--- | :--- | :--- | :--- | :--- |
| **FII** | Future | 22,297 | Bought Futures | Bullish |
| | CE | 55,995 | Bought Calls | Bullish |
| | PE | -20,375 | Sold Puts | Bullish |
| **PRO** | Future | -11,103 | Sold Futures | Bearish |
| | CE | 26,049 | Bought Calls | Bullish |
| | PE | -1,05,000 | Sold Puts | Bullish |
| **DII** | Future | 448 | Bought Futures | Bullish |
| | CE | -255 | Sold Calls | Bearish |
| | PE | -795 | Sold Puts | Bullish |
| **RETAIL** | Future | -11,642 | Sold Futures | Bearish |
| | CE | -81,790 | Sold Calls | Bearish |
| | PE | 1,27,000 | Bought Puts | Bearish |

**OVERALL TREND:** **BULLISH**

*Note: Trend calculated using our proprietary method*
*Get FREE Algo Tools at BluechipAlgos.com*

### 03/08/2026 - FII Activity for last 5 days

| Day / Metric | Value | Trend |
| :--- | :--- | :--- |
| Today (T) | 98667 | Bullish |
| T-1 Day | -7786 | Bearish |
| T-2 Day | 26585 | Bullish |
| T-3 Day | 144841 | Bullish |
| T-4 Day | -536 | Bearish |
| **Overall Trend** | **By Count** | **Bullish** |
| | **By Sentiment**| **Bullish** |

*Get FREE Algo Tools at BluechipAlgos.com*


## Date 31-July-2026

| Participant | Segment | Net Change | Interpretation | Net OI | Interpretation | T-1 Net OI |
| --- | --- | --- | --- | --- | --- | --- |
| **Fii** | Index Futures | 13,499 | Bullish | -1.73L | Bearish | -1.87L |
|  | Index Options | -21,285 | Bearish | -6.38L | Bearish | -6.17L |
|  | Call | -8,240 | Bearish | -1.85L | Bearish | -1.76L |
|  | Put | 13,045 | Bearish | 4.54L | Bearish | 4.41L |
|  | Stock Futures | 22,174 | Bullish | 6.44L | Bullish | 6.22L |
| **Dii** | Index Futures | -4,351 | Bearish | 45,207 | Bullish | 49,558 |
|  | Index Options | -145 | Bearish | -48,205 | Bearish | -48,060 |
|  | Call | 150 | Bullish | 4,495 | Bullish | 4,345 |
|  | Put | 295 | Bearish | 52,700 | Bearish | 52,405 |
|  | Stock Futures | -8,270 | Bearish | -39.4L | Bearish | -39.31L |
| **Pro** | Index Futures | -3,584 | Bearish | -18 | Bearish | 3,566 |
|  | Index Options | -1.8L | Bearish | -25,236 | Bearish | 1.55L |
|  | Call | 23,847 | Bullish | 1.56L | Bullish | 1.32L |
|  | Put | 2.04L | Bearish | 1.81L | Bearish | -22,921 |
|  | Stock Futures | -5,831 | Bearish | 4.48L | Bullish | 4.54L |
| **Client** | Index Futures | -5,564 | Bearish | 1.28L | Bullish | 1.33L |
|  | Index Options | 2.02L | Bullish | 7.12L | Bullish | 5.1L |
|  | Call | -15,758 | Bearish | 24,116 | Bullish | 39,874 |
|  | Put | -2.17L | Bullish | -6.88L | Bullish | -4.7L |
|  | Stock Futures | -8,073 | Bearish | 28.48L | Bullish | 28.56L |


## Date 28-July-2026

| Participant | Segment | Net Change | Interpretation | Net OI | Interpretation | T-1 Net OI |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Fii** | Index Futures | 61,324 | Bullish | -2.06L | Bearish | -2.67L |
| | Index Options | -61,860 | Bearish | -7.69L | Bearish | -7.08L |
| | Call | -22,009 | Bearish | -2.48L | Bearish | -2.26L |
| | Put | 39,851 | Bearish | 5.22L | Bearish | 4.82L |
| | Stock Futures | -86,982 | Bearish | 5.64L | Bullish | 6.51L |
| **Dii** | Index Futures | -10,614 | Bearish | 54,471 | Bullish | 65,085 |
| | Index Options | 8,189 | Bullish | -34,797 | Bearish | -42,986 |
| | Call | -4,255 | Bearish | 3,280 | Bullish | 7,535 |
| | Put | -12,444 | Bullish | 38,077 | Bearish | 50,521 |
| | Stock Futures | -10,741 | Bearish | -39.41L | Bearish | -39.3L |
| **Pro** | Index Futures | -34,770 | Bearish | -2,123 | Bearish | 32,647 |
| | Index Options | -37,720 | Bearish | -8,129 | Bearish | 29,591 |
| | Call | -96,158 | Bearish | 55,221 | Bullish | 1.51L |
| | Put | -58,438 | Bullish | 63,350 | Bearish | 1.22L |
| | Stock Futures | 1.18L | Bullish | 4.98L | Bullish | 3.81L |
| **Client** | Index Futures | -15,940 | Bearish | 1.53L | Bullish | 1.69L |
| | Index Options | 91,392 | Bullish | 8.12L | Bullish | 7.21L |
| | Call | 1.22L | Bullish | 1.89L | Bullish | 66,623 |
| | Put | 31,031 | Bearish | -6.23L | Bullish | -6.54L |
| | Stock Futures | -20,076 | Bearish | 28.78L | Bullish | 28.98L |

## Date 27-July-2026

| Participant | Segment | Net Change | Interpretation | Net OI | Interpretation | T-1 Net OI |
| --- | --- | --- | --- | --- | --- | --- |
| **Fii** | Index Futures | 3,922 | Bullish | -2.67L | Bearish | -2.71L |
|  | Index Options | 86,401 | Bullish | -7.08L | Bearish | -7.94L |
|  | Call | 33,272 | Bullish | -2.26L | Bearish | -2.59L |
|  | Put | -53,129 | Bullish | 4.82L | Bearish | 5.35L |
|  | Stock Futures | 76,479 | Bullish | 6.51L | Bullish | 5.75L |
| **Dii** | Index Futures | -43 | Bearish | 65,085 | Bullish | 65,128 |
|  | Index Options | -9,477 | Bearish | -42,986 | Bearish | -33,509 |
|  | Call | -5 | Bearish | 7,535 | Bullish | 7,540 |
|  | Put | 9,472 | Bearish | 50,521 | Bearish | 41,049 |
|  | Stock Futures | -25,294 | Bearish | -39.3L | Bearish | -39.05L |
| **Pro** | Index Futures | 3,426 | Bullish | 32,647 | Bullish | 29,221 |
|  | Index Options | -50,247 | Bearish | 29,591 | Bullish | 79,838 |
|  | Call | -55,124 | Bearish | 1.51L | Bullish | 2.07L |
|  | Put | -4,877 | Bullish | 1.22L | Bearish | 1.27L |
|  | Stock Futures | -35,586 | Bearish | 3.81L | Bullish | 4.16L |
| **Client** | Index Futures | -7,305 | Bearish | 1.69L | Bullish | 1.76L |
|  | Index Options | -26,676 | Bearish | 7.21L | Bullish | 7.48L |
|  | Call | 21,857 | Bullish | 66,623 | Bullish | 44,766 |
|  | Put | 48,533 | Bearish | -6.54L | Bullish | -7.03L |
|  | Stock Futures | -15,599 | Bearish | 28.98L | Bullish | 29.14L |


## Date 24-July-2026
| Participant | Segment | Net Change | Interpretation | Net OI | Interpretation | T-1 Net OI |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Fii** | Index Futures | -7,765 | Bearish | -2.71L | Bearish | -2.63L |
| | Index Options | 67,027 | Bullish | -7.94L | Bearish | -8.61L |
| | Call | 55,677 | Bullish | -2.59L | Bearish | -3.14L |
| | Put | -11,350 | Bullish | 5.35L | Bearish | 5.47L |
| | Stock Futures | 27,563 | Bullish | 5.75L | Bullish | 5.47L |
| **Dii** | Index Futures | -2,178 | Bearish | 65,128 | Bullish | 67,306 |
| | Index Options | -5,930 | Bearish | -33,509 | Bearish | -27,579 |
| | Call | -50 | Bearish | 7,540 | Bullish | 7,590 |
| | Put | 5,880 | Bearish | 41,049 | Bearish | 35,169 |
| | Stock Futures | -80,818 | Bearish | -39.05L | Bearish | -38.24L |
| **Pro** | Index Futures | 932 | Bullish | 29,221 | Bullish | 28,289 |
| | Index Options | 1.28L | Bullish | 79,838 | Bullish | -47,807 |
| | Call | 66,658 | Bullish | 2.07L | Bullish | 1.4L |
| | Put | -60,987 | Bullish | 1.27L | Bearish | 1.88L |
| | Stock Futures | 18,501 | Bullish | 4.16L | Bullish | 3.98L |
| **Client** | Index Futures | 9,011 | Bullish | 1.76L | Bullish | 1.67L |
| | Index Options | -1.89L | Bearish | 7.48L | Bullish | 9.36L |
| | Call | -1.22L | Bearish | 44,766 | Bullish | 1.67L |
| | Put | 66,456 | Bearish | -7.03L | Bullish | -7.69L |
| | Stock Futures | 34,754 | Bullish | 29.14L | Bullish | 28.79L |
## 31/08/2026 - FII DII FNO ACTIVITY

| Participant | Instrument | Change | Activity | Trend |
| :--- | :--- | :--- | :--- | :--- |
| **FII** | Future | -6,682 | Sold Futures | Bearish |
| | CE | +4,558 | Bought Calls | Bullish |
| | PE | -42,953 | Sold Puts | Bullish |
| **Client** | Future | +1,260 | Bought Futures | Bullish |
| | CE | +104,485 | Bought Calls | Bullish |
| | PE | +39,020 | Bought Puts | Bearish |
| **Pro** | Future | +5,347 | Bought Futures | Bullish |
| | CE | -109,003 | Sold Calls | Bearish |
| | PE | +6,638 | Bought Puts | Bearish |
| **DII** | Future | +75 | Bought Futures | Bullish |
| | CE | -40 | Sold Calls | Bearish |
| | PE | -2,705 | Sold Puts | Bullish |

## 31/08/2026 - FII Activity for last 5 days

| Period | Value | Trend |
| :--- | :--- | :--- |
| Today (T) | +40,829 | Bullish |
| T-1 Day | +62,995 | Bullish |
| T-2 Day | -112,312 | Bearish |
| T-3 Day | -45,603 | Bearish |
| T-4 Day | +291,103 | Bullish |
| **Overall Trend** | By Count | Bullish (3B/2Be) |
| **Overall Trend** | By Sentiment | Bullish (net +237,012) |

---

## 01/09/2026 - FII DII FNO ACTIVITY

| Participant | Instrument | Change | Activity | Trend |
| :--- | :--- | :--- | :--- | :--- |
| **FII** | Future | -12,717 | Sold Futures | Bearish |
| | CE | -93,282 | Sold Calls | Bearish |
| | PE | -69,518 | Sold Puts | Bullish |
| **Client** | Future | +8,911 | Bought Futures | Bullish |
| | CE | -75,332 | Sold Calls | Bearish |
| | PE | -62,619 | Sold Puts | Bullish |
| **Pro** | Future | +3,617 | Bought Futures | Bullish |
| | CE | +168,089 | Bought Calls | Bullish |
| | PE | +131,998 | Bought Puts | Bearish |
| **DII** | Future | +189 | Bought Futures | Bullish |
| | CE | +525 | Bought Calls | Bullish |
| | PE | +139 | Bought Puts | Bearish |

## 01/09/2026 - FII Activity for last 5 days

| Period | Value | Trend |
| :--- | :--- | :--- |
| Today (T) | -36,481 | Bearish |
| T-1 Day | +40,829 | Bullish |
| T-2 Day | +62,995 | Bullish |
| T-3 Day | -112,312 | Bearish |
| T-4 Day | -45,603 | Bearish |
| **Overall Trend** | By Count | Bearish (2B/3Be) |
| **Overall Trend** | By Sentiment | Bearish (net -90,572) |


---

## 02/09/2026 - FII DII FNO ACTIVITY

| Participant | Instrument | Change | Activity | Trend |
| :--- | :--- | :--- | :--- | :--- |
| **FII** | Future | -7,131 | Sold Futures | Bearish |
| | CE | -51,192 | Sold Calls | Bearish |
| | PE | -39,242 | Sold Puts | Bullish |
| **Client** | Future | +12,940 | Bought Futures | Bullish |
| | CE | +11,084 | Bought Calls | Bullish |
| | PE | +44,808 | Bought Puts | Bearish |
| **Pro** | Future | +1,401 | Bought Futures | Bullish |
| | CE | +40,683 | Bought Calls | Bullish |
| | PE | -3,651 | Sold Puts | Bullish |
| **DII** | Future | -7,210 | Sold Futures | Bearish |
| | CE | -575 | Sold Calls | Bearish |
| | PE | -1,915 | Sold Puts | Bullish |

**OVERALL TREND: BEARISH** (FII activity score: -19,081)

## 02/09/2026 - FII Activity for last 5 days

| Period | Value | Trend |
| :--- | :--- | :--- |
| Today (T) | -19,081 | Bearish |
| T-1 Day | -36,481 | Bearish |
| T-2 Day | +40,829 | Bullish |
| T-3 Day | +62,995 | Bullish |
| T-4 Day | -112,312 | Bearish |
| **Overall Trend** | By Count | Bearish (2B/3Be) |
| **Overall Trend** | By Sentiment | Bearish (net -64,050) |

## 02/09/2026 - CUMULATIVE NET OI (new — `fao_participant_oi_DDMMYYYY.csv`)

> ⚠️ **New block, added 03-Sep-2026.** Every prior entry in this file records only the *daily change*
> from `fao_participant_vol_*.csv`. CLAUDE.md requires change to be **validated against cumulative
> Net OI**, and that validation was impossible because the cumulative numbers were never recorded.
> Source: `https://archives.nseindia.com/content/nsccl/fao_participant_oi_DDMMYYYY.csv` (index F&O only).
> Sign convention: **positive = net SHORT**, negative = net LONG.

| Participant | Net Index Fut | Net CE (short+) | Net PE (short+) | Reading |
| :--- | ---: | ---: | ---: | :--- |
| **FII** | **net SHORT 229,163** | **+299,253** | -593,223 | Short futures + short calls + long puts = **Distribution/Trap** |
| **Pro** | +15,826 net long fut | -21,925 | -88,909 | Mildly long both wings; defines neither ceiling nor floor |
| **Client** | +200,070 net long fut | -273,067 | **+712,140** | Long fut + long calls + heavy put writing = very bullish → contrarian bearish |
| **DII** | +13,267 net long fut | -4,260 | -30,008 | Negligible |

*Raw: FII fut L 28,537 / S 257,700 · CE L 461,823 / S 761,076 · PE L 971,327 / S 378,104.
Pro fut L 46,234 / S 30,408 · CE L 853,160 / S 831,235 · PE L 784,778 / S 695,869.*

**✅ RESOLVED 03-Sep-2026 — and the answer was neither of the two candidates.**
The ambiguity above ("daily change vs cumulative net OI") assumed the source file was right. It
wasn't. Gate 5 had been reading `fao_participant_`**`vol`**`_*.csv` — *Participant wise **Trading
Volume***, i.e. contracts **traded**, not positions held. That file is **retired as a Gate 5 input.**

**The ruling, in force from 03-Sep-2026** — full evidence in
[`TRADING_CONSTANTS.md` §9](../TRADING_CONSTANTS.md):

- **Source:** `fao_participant_`**`oi`**`_DDMMYYYY.csv` (positions).
- **Basis:** the **T-1 vs T-2 change** in net OI. `ΔCE = net_CE_short(T-1) − net_CE_short(T-2)`.
- **The LEVEL never triggers.** Across 86 sessions the FII level cleared 80,000 on 97.7% of days
  (calls) and 100% (puts) — a gate that fires every day carries no information. Keep it as context.
- **Limits:** FII **65,000** (primary, read first) · Pro **100,000** (veto only) · DII/Client context.
- **Forbid-only:** over the limit on CE ⛔ forbids Bull Put; on PE ⛔ forbids Bear Call; both ⛔ no
  trade; under the limit is **silence, not permission for the other side.** Gate 5 never mandates.
- **Run it, don't hand-compute it:** `python3 tools/fii-dii/fii_dii.py <T-1 YYYY-MM-DD>`.

**Re-read of 03-Sep on the correct basis:** FII ΔCE +51,192 · ΔPE +39,242 · Pro ΔCE −40,683 ·
ΔPE +3,650 → **all under limit → Gate 5 SILENT.** The "hard ceiling / sell calls" reading recorded
above came from the retired volume file and from the level, and it did not survive. The 31-Aug
precedent does survive: Pro ΔCE **+109,002**, over 100,000 → Bull Put forbidden on 01-Sep.

---

## 03/09/2026 - FII DII FNO ACTIVITY

| Participant | Instrument | Change | Activity | Trend |
| :--- | :--- | :--- | :--- | :--- |
| **FII** | Future | −5,939 | Sold Futures | Bearish |
| | CE | −12,954 | Sold Calls | Bearish |
| | PE | +56,826 | Bought Puts | Bearish |
| **Pro** | Future | −7 | Sold Futures | Bearish |
| | CE | −96,366 | Sold Calls | Bearish |
| | PE | +30,824 | Bought Puts | Bearish |
| **Client** | Future | +5,926 | Bought Futures | Bullish |
| | CE | +109,470 | Bought Calls | Bullish |
| | PE | −89,681 | Sold Puts | Bullish |
| **DII** | Future | +20 | Bought Futures | Bullish |
| | CE | −150 | Sold Calls | Bearish |
| | PE | +2,031 | Bought Puts | Bearish |

**OVERALL TREND: BEARISH** (FII activity score: −75,719)

## 03/09/2026 - FII Activity for last 5 days

| Period | Value | Trend |
| :--- | :--- | :--- |
| Today (T) | −75,719 | Bearish |
| T-1 Day | −19,081 | Bearish |
| T-2 Day | −36,481 | Bearish |
| T-3 Day | +40,829 | Bullish |
| T-4 Day | +62,995 | Bullish |
| **Overall Trend** | By Count | Bearish (2B/3Be) |
| **Overall Trend** | By Sentiment | Bearish (net −27,457) |

## 03/09/2026 - Gate 5 inputs (T-1=03-Sep vs T-2=02-Sep, `fao_participant_oi_*.csv`)

| Participant | Leg | level T-1 | level T-2 | CHANGE | limit | verdict |
| :--- | :--- | ---: | ---: | ---: | ---: | :--- |
| FII | CE | 312,207 | 299,253 | +12,954 | 65,000 | silent |
| FII | PE | −650,049 | −593,223 | −56,826 | 65,000 | silent |
| Pro | CE | 74,441 | −21,925 | +96,366 | 100,000 | silent |
| Pro | PE | −119,733 | −88,909 | −30,824 | 100,000 | silent |

**Gate 5: SILENT — no structure forbidden. NOT permission for either side.**
