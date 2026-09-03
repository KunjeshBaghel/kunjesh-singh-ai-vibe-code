When an order is placed in the stock market, it travels through an automated electronic pipeline from your device to the stock exchange's matching engine in milliseconds.

**Order Lifecycle: Step-by-Step Journey**

1. **Order Placement (Front-End Layer):**
* **Retail Investors:** Enter a buy/sell order through a broker app (e.g., Zerodha, Groww, Angel One).
* **Pro Traders / Algorithmic Desks:** Submit orders via Direct Market Access (DMA) or automated trading algorithms located in exchange colocation servers (racks inside the exchange building for microsecond latency).
* **DIIs & FIIs:** Institutional desks route orders via FIX protocol software through institutional brokers or custodians, often using automated execution algorithms (like TWAP/VWAP) to avoid disturbing market prices.


2. **Broker Validation & Risk Checks (RMS & OMS):** Before hitting the exchange, the order passes through the broker’s Order Management System (OMS) and Risk Management System (RMS). The RMS checks if you have sufficient funds/shares, valid leverage, and compliance limits.
3. **Exchange Gateway:** Once validated, the order arrives at the exchange gateway (such as NSE or BSE) via dedicated fiber network channels.
4. **Exchange Matching Engine (The Order Book):** The order enters the exchange's **Central Limit Order Book (CLOB)**. If it is a *Limit Order*, it sits in a queue based on **Price-Time Priority** (best price comes first; equal prices are ordered by arrival time). If it is a *Market Order*, it immediately matches against the best available opposite limit order.
5. **Execution & Confirmation:** The moment a buy price equals a sell price, a trade is generated. Execution confirmation is sent back to the broker and trader instantly.
6. **Clearing & Settlement:** After market hours, the clearing corporation (e.g., NSE Clearing Ltd) nets all trade obligations. Shares and cash are settled electronically (on a T+1 basis in India) between Demat and bank accounts.

---

**How and Where to See the Live Order Book**

The order book is the real-time list of all pending buy (bid) and sell (ask) limit orders waiting at the exchange.

| Data Level | What It Shows | Where to Find It |
| --- | --- | --- |
| **Level 1** | Best single Bid (buy price) and best single Ask (sell price). | Basic stock price quotes on any finance website or standard ticker. |
| **Level 2 (Market Depth)** | Top 5 pending buy orders and top 5 pending sell orders, with quantities. | Standard feature on almost all broker trading terminals ("Market Depth" / "Depth of Market" tab). |
| **Level 3 (Tick-by-Tick)** | Top 20 bid/ask levels or full order book feed (every single tick, modification, and cancellation). | Professional charting tools (TradingView Pro, broker desktop applications like Upstox/Kotak Neo, or institutional feeds like Bloomberg/Refinitiv). |

---

**Building Direction Using Bid-Ask Ratio (Market Depth Analysis)**

The **Bid-Ask Volume Ratio** compares total pending buy quantity against total pending sell quantity in the order book depth.

$$\text{Bid-Ask Ratio} = \frac{\text{Total Pending Buy Quantity (Bids)}}{\text{Total Pending Sell Quantity (Asks)}}$$

* **Bullish Signal (Ratio > 1):** More total buy orders than sell orders indicate demand pressure, suggesting prices may move up.
* **Bearish Signal (Ratio < 1):** More total sell orders than buy orders indicate supply overhead, suggesting prices may move down.

**Institutional Traps to Watch Out For:**

* **Spoofing (Fake Depth):** Large traders often place huge limit orders deep in the order book to manipulate the bid-ask ratio, making the market look bullish or bearish, and then cancel them right before execution.
* **Iceberg Orders:** Big institutions rarely put 100,000 shares in the visible order book at once. They slice them into small hidden packets (e.g., showing 1,000 shares at a time), rendering the visible order book ratio incomplete.

---

**The First Place to See Orders & Their Nature (True Order Flow)**

The order book only shows **pending** orders (intent), which can be canceled at any time. The absolute first place to see **executed** orders and their true aggressive nature (buy vs. sell) is through **Tick-by-Tick (TBT) Data Streams**:

* **Time & Sales (The Tape):** A real-time running log of executed transactions. It reveals the exact execution timestamp, price, volume, and whether the trade hit the **Bid** (seller was aggressive, hitting the buyer's price) or the **Ask** (buyer was aggressive, paying the seller's price).
* **Footprint / Order Flow Charts:** Advanced charting tools aggregate TBT data to display **Cumulative Volume Delta (CVD)**. This isolates aggressive market buyers from aggressive market sellers, allowing you to see true institutional buying or selling pressure before it clearly reflects in price candles.


Tick-by-Tick (TBT) data actually **includes** executed volume—it streams both completed trades and real-time order book updates. Already executed orders are formally referred to as **Trades**, **Fills**, **Prints**, or **Time & Sales**.

**Understanding TBT Data vs. Absorption**

* **Tick-by-Tick (TBT) Stream:** The raw, unaggregated feed sent by exchange servers that broadcasts every single market event in sequence. It consists of two main data streams:
* **Trade Ticks:** Real-time data for every executed transaction (price, quantity, timestamp, and order direction).
* **Order Ticks:** Real-time changes to resting limit orders on the Depth of Market (DOM), including additions, modifications, and cancellations.


* **Absorption:** An order-flow event rather than a data feed. Absorption occurs when TBT **Trade Ticks** show heavy executed market volume hitting a specific price level, while TBT **Order Ticks** show passive limit orders continually refreshing or holding ground so price cannot break through.

**Industry Terminology for Executed Orders**

* **Trades / Fills / Prints:** Universal terms for completed transactions where an aggressive order matches against a resting limit order. Wall Street historically called executions "prints" because they printed onto paper ticker tapes.
* **Time & Sales (T&S):** The official real-time ledger displaying every executed trade chronologically. T&S records show exact execution timestamp, traded price, volume (lot size), and whether the trade was buyer-initiated (hit the ask) or seller-initiated (slammed the bid).
* **Aggressive Volume:** The portion of executed orders driven by market orders or marketable limit orders crossing the bid-ask spread. This is the exact data stream used to calculate Cumulative Volume Delta (CVD).
* **Passive Execution:** The opposing side of an executed order—the resting limit order sitting on the book that gets filled when an aggressive order hits it.