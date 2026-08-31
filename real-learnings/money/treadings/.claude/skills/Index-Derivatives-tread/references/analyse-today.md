# analyse-today — Morning Setup & Market View

Full morning workflow. Takes ~15 minutes. Do every step; do not skip data points.

---

## Step 1: Create today's folder and files

```
Date format: DD-MM-YYYY  e.g. 31-08-2026
Month folder: August-2026  (derive from date)

Create:
  my-treads/<Month-YYYY>/<DD-MM-YYYY>/
    <DD-MM-YYYY>-market_view.md   ← write market view here
    <DD-MM-YYYY>-tread.md         ← append session log here (start empty)
    <DD-MM-YYYY>-learning.md      ← post-session lessons (start empty)
```

Copy the structure from `my-treads/DD-MM-YYYY/` (blank template) if it exists, otherwise create from scratch.

Write the header to `tread.md` immediately:
```markdown
# <DD-MM-YYYY> — Tread Log
## <HH:MM> — Session start: broker connection check
| Broker | Result | Verified with |
```

---

## Step 2: Verify all 3 brokers (see SKILL.md Universal Rules §1)

Run in parallel:
- `mcp__kite__get_ltp` → NIFTY + VIX
- `mcp__kotak-neo__get_limits` (sessionid required)
- `mcp__dhan__market_data_agent_tool` action=`expirylist` NIFTY

Record results in `tread.md`. If any broker fails, flag it and stop.

---

## Step 3: Fetch expiry list — all 3 indexes

Run in parallel:
```
NIFTY:    UnderlyingScrip=13, UnderlyingSeg=IDX_I
BANKNIFTY: UnderlyingScrip=25, UnderlyingSeg=IDX_I
SENSEX:   UnderlyingScrip=51, UnderlyingSeg=IDX_I
```

For each index: extract nearest expiry date and count **trading sessions** (not calendar days).

---

## Step 4: Fetch live market data (all in parallel)

From **Kite**:
```
mcp__kite__get_ltp: ["NSE:NIFTY 50", "NSE:NIFTY BANK", "BSE:SENSEX", "NSE:INDIA VIX"]
```

From **Kite historical** (for HV computation if needed):
```
instrument_token=256265 (NIFTY), interval=day, last 45 sessions
```

From **Kotak**:
```
mcp__kotak-neo__get_limits → available margin
```

Collect:
- NIFTY spot, BANKNIFTY spot, SENSEX spot, India VIX
- Previous day's close (PDC), PDH, PDL
- Opening gap vs previous close

---

## Step 5: Fetch FII/DII data

**Preferred:** Ask the user to share today's FII/DII screenshot from [@Fii_Dii_Data](https://x.com/Fii_Dii_Data) on X. Prompt:
> "Please share today's FII/DII F&O participant-wise OI screenshot from @Fii_Dii_Data on X so I can include it in the market view."

**If user provides image/data:** Extract and append to `my-treads/fii_dii_data_2026.md` using the existing format (see 28/08/2026 entry as template).

**If not available:** Note as missing, proceed with prior day's data (flag as T-1), and flag the gap clearly in the market view.

Read the last 3 entries in `fii_dii_data_2026.md` to assess the 3-day trend (needed for FII regime validation).

---

## Step 6: Fetch option chain basics (for preliminary view)

For the nearest expiry on each index, fetch the chain from Dhan and pull:
- ATM straddle premium (CE + PE at nearest ATM strike)
- PCR: total PE OI ÷ total CE OI in near-money range
- Max pain: strike with lowest aggregate buyer loss
- Top 3 CE OI strikes (call walls = resistance)
- Top 3 PE OI strikes (put walls = support)

**Forward basis check (§8.7.1a):** Run F = K + CE - PE at 3 strikes. If basis > 0.1% of spot → note the true ATM-forward.

---

## Step 7: Classify the market (five-view)

Use all data points from `kb/Market_View.md` §5:

| Dimension | Check |
|---|---|
| Price vs OI matrix | Long Buildup / Short Covering / Short Buildup / Long Unwinding |
| FII regime | Match to 6 scenarios (Distribution Trap, Classic Rally, etc.) |
| PCR level | >1.3 bullish · 0.9-1.3 neutral · <0.7 bearish |
| VIX direction | Rising = vega headwind; falling = seller tailwind |
| Global cues | US markets, GIFT Nifty, crude, DXY |
| Pro desk check | Both CE+PE sold (range) vs both bought (volatile) |

**Classify to exactly one of:** Strongly Bullish · Slightly Bullish · Sideways · Slightly Bearish · Strongly Bearish

**Conviction:** High / Medium / Low — based on how many dimensions agree

---

## Step 8: Write market_view.md

```markdown
# <DD-MM-YYYY> Market View

**Data Points Summary**
* NIFTY: <price> (<change>%)
* BANKNIFTY: <price>
* SENSEX: <price>
* VIX: <level> (<direction>)
* PCR: <value>
* FII/DII (T or T-1): <key stance>
* Global cues: <1 line>
* Nearest expiries: NIFTY <date> (<N> sessions), SENSEX <date>, BANKNIFTY <date>

**Missing Data**
* <list any data points not available>

**Classification: <One of Five Views>**
<2-3 sentence summary of the thesis>

**Key Levels, Bias & Conviction**
* Bias: <Bullish/Bearish/Sideways>
* Conviction: <High/Medium/Low>
* NIFTY key levels: Support <level>, Resistance <level>
* BANKNIFTY: ...
* SENSEX: ...

**What to Watch Before Taking a Trade**
* <3-5 specific triggers to confirm or invalidate the thesis>
```

---

## Step 9: Flag missing data points

If any of these are missing, **stop and ask the user before calling direction:**
- India VIX (no substitute)
- FII/DII F&O participant OI (can proceed with T-1 but flag)
- Live spot prices (retry MCP)
- Expiry dates (never guess)

Do NOT guess or assume any numeric data point.

---

## Step 10: Update tread.md session header

Append the broker connection table and preliminary snapshot to `tread.md`.

**Next:** If the user wants to find a trade, they type `find-trade` or `/Index-Derivatives-tread find-trade`.
