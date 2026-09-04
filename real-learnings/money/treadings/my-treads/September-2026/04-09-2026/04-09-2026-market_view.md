# 04-09-2026 Market View

**Data Points Summary**

* NIFTY: 23,955.8 (PDC: 23,873.45 | PDH: 24,025.4 | PDL: 23,873.45) → gap up +82 pts (+0.34%)
* BANKNIFTY: 57,394.5
* SENSEX: 76,714.98 (PDC: 76,152.86 | PDH: 76,924.48 | PDL: 76,152.86) → gap up +562 pts (+0.74%)
* VIX: 10.97 — **CHEAP** (< 12, TC §10). Falling (US VIX −5.79%). Bullish environment for sellers.
* Sectoral: IT 30,958.95 · BANK 57,394.5 · FMCG 45,847.65 · AUTO 27,782.3 · METAL 13,185.85
* Margin (Kotak Neo, live): **₹6,86,627.79** *(PENDING USER RULING — see TC §1)*
* PCR (NIFTY, Sep-8 expiry): **0.895** → Mildly bearish (TC §10a: 0.80–1.00)
* PCR (SENSEX, Sep-10 expiry): **1.208** → Mildly bullish (TC §10a: 1.00–1.30)
* FII/DII Cash (T-1 = 03-Sep, Trendlyne): FII −₹2,345.87 Cr (net sellers) · DII +₹4,977.46 Cr (net buyers)
* FII/DII F&O (T-1 = 03-Sep, NSE CSV):
  * FII: Fut −5,939 · CE −12,954 (sold calls) · PE +56,826 (bought puts) → **Strongly Bearish**
  * Pro: Fut −7 · CE −96,366 (sold calls — heavy ceiling) · PE +30,824 (bought puts) → **Bearish/Ceiling**
  * Client: Fut +5,926 · CE +109,470 (bought calls) · PE −89,681 (sold puts) → Strongly Bullish (contrarian → bearish signal)
  * DII: minor F&O activity — negligible
* FII 5-day F&O trend: T=−75,719 · T-1=−19,081 · T-2=−36,481 · T-3=+40,829 · T-4=+62,995
  → By Count: **2B/3Be (Bearish)** · By Sentiment: **Bearish** (net −27,457)
* Global (overnight): S&P 500 +1.06% · Dow +1.18% · Nasdaq +1.40% · US VIX 14.32 (−5.79%) · Nikkei +0.99% · Hang Seng +2.08% · KOSPI +1.30% · FTSE +0.70% · DAX +0.63% · WTI Crude $92.09 (+0.87%) · DXY 99.04 (+0.13%)
* Nearest expiries: NIFTY **08-Sep-2026** (**3 sessions**) · SENSEX **10-Sep-2026** (**5 sessions**) · BANKNIFTY 29-Sep-2026 (monthly)

**Missing Data — Genuine Gaps Only**

* GIFT Nifty — use opening 15-min candle
* IV/Greeks — unusable (Dhan spot-based); parity forward F used instead (TC §14)
* IVP — use VIX direction (10.97, falling = sellers' tailwind)
* Intraday VRP — to be measured at 9:45 kill-switch check if applicable

**Basis Check**

| Index | F (parity) | Spot | Basis | 0.1% threshold | Verdict |
|---|---|---|---|---|---|
| NIFTY (Sep-8) | 23,995.65 | 23,955.8 | +39.85 | 23.96 | ⚠️ > threshold — **vendor delta DISCARDED**, use §8.7.3 on F |
| SENSEX (Sep-10) | 76,852 | 76,714.98 | +137 | 76.71 | ⚠️ > threshold — **vendor delta DISCARDED**, use §8.7.3 on F |

NIFTY F verified across 5 strikes: 23,995–23,996 (consistent within 1 pt ✅)
SENSEX F verified across 5 strikes: 76,851–76,853 (consistent ✅)

**OI Wall Map — NIFTY (Sep-8 expiry)**

| Type | Strike | OI | Note |
|---|---|---|---|
| Call wall | **24,000** | 21.5M | **Strongest ceiling** — only 44 pts above spot |
| Call wall | 24,200 | 14.3M | Secondary ceiling |
| Call wall | 24,100 | 14.1M | Secondary |
| Put wall | **23,900** | 22.1M | **Strongest floor** — 56 pts below spot |
| Put wall | 23,800 | 14.2M | Secondary floor |

NIFTY Pinning zone: **23,900–24,000** (100-point channel, market sitting mid-channel at 23,956)

**OI Wall Map — SENSEX (Sep-10 expiry)**

| Type | Strike | OI | Note |
|---|---|---|---|
| Call wall | **77,000** | 1.0M | Ceiling 285 pts above spot |
| Put wall | **76,500** | 1.1M | Floor 215 pts below spot |
| Put wall | 76,600 | 811K | Inner floor |

SENSEX Pinning zone: **76,500–77,000**

---

**Classification: Sideways · Conviction: Low · as of 09:52 IST**

**Participant-by-participant (T-1 = 03-Sep-2026, NSE CSV):**

| Participant | Index Fut | CE | PE | Reading | Implication |
|---|---|---|---|---|---|
| FII | −5,939 (sold) | −12,954 (sold) | +56,826 (bought) | **Strongly Bearish** | Directional short bias; selling calls, buying puts aggressively |
| Pro | −7 (neutral) | −96,366 (sold, heavy) | +30,824 (bought) | **Ceiling writer** | Writing calls — ceiling defined at 24,000–24,200 NIFTY; 77,000 SENSEX |
| Client | +5,926 (bought) | +109,470 (bought) | −89,681 (sold) | Strongly Bullish (contrarian → **slight bearish signal**) | Retail buying calls and selling puts = usually fades the move |
| DII | +20 (tiny) | −150 | +2,031 | Negligible F&O | Buying cash heavily (+₹4,977 Cr), not directional in F&O |

```
GATE 5 INPUTS   (T-1 = 03-Sep-2026 vs T-2 = 02-Sep-2026)   source: fao_participant_oi_*.csv
  net_CE_short = |Opt Idx Call Short| − |Opt Idx Call Long|      ΔCE = net(T-1) − net(T-2)

           level T-1     level T-2       ΔCE          ΔPE       limit (TC §9)   verdict
  FII        312,207       299,253      +12,954      −56,826        65,000        silent
  Pro         74,441       −21,925      +96,366      −30,824       100,000        silent

  ★ Read limits from TC §9. Trigger is the CHANGE column, never the level.
  → Structures FORBIDDEN: NONE — Gate 5 is SILENT. Not permission for either side.
```

**Synthesis:**

Today's market presents a clear tug-of-war between global bullishness and domestic institutional caution. Global cues are strongly positive — US indices rose 1–1.4%, US VIX fell 5.8%, and Asian markets followed with Hang Seng +2.08%. This explains the significant gap-up (NIFTY +82 pts, SENSEX +562 pts).

Against this, FII F&O positioning is firmly bearish: they sold futures, sold calls and bought puts aggressively on 03-Sep. This is a 3-day bearish streak by FII in F&O, though directionally they've been wrong in the near-term as global cues override. Pro has written heavy calls at 24,000 (NIFTY) and 77,000 (SENSEX), effectively defining the ceiling. DII is absorbing FII cash selling (bought ₹4,977 Cr vs FII sold ₹2,346 Cr) keeping the cash market supported.

Net read: **Sideways to slightly bullish** intraday, but the ceiling is heavy and nearby at 24,000. Market is likely to oscillate in 23,900–24,050 range. The gap up absorbed, any sustained move above 24,000 requires Pro to cover calls — unlikely on a Friday.

PCR at 0.895 (NIFTY) is mildly bearish, consistent with the call-heavy OI structure. SENSEX PCR 1.208 is mildly bullish but that expiry is 5 sessions out (less informative today).

**What invalidates intraday:** NIFTY sustained close above 24,050 (Pro call covering, momentum buy) or VIX spike above 12 (regime shift).

**Key Levels, Bias & Conviction**

* Bias: **Sideways** · Range: 23,900–24,050 NIFTY
* Conviction: **Low** — global (bullish) vs FII F&O (bearish) conflict; PCR and OI both suggest range-bound
* NIFTY: Support **23,900** (22M put OI wall, strongest) · Resistance **24,000** (21.5M call OI, Pro ceiling) · Pin zone **23,900–24,000**
* SENSEX: F=76,852 · Support **76,500** (put wall) · Resistance **77,000** (call wall)
* BANKNIFTY: Not analysed — monthly expiry, Gate 1 blocked, locked (TC §11)

---

## ⛔ Gate 1 — NO TRADE TODAY

| Index | Sessions to expiry | Gate 1 | Reason |
|---|---|---|---|
| NIFTY | **3** (Sep 4, Sep 7, Sep 8) | ⛔ BLOCKED | sessions_to_expiry ≥ 3 |
| SENSEX | **5** (Sep 4→10) | ⛔ BLOCKED | sessions_to_expiry ≥ 3 |
| BANKNIFTY | many | ⛔ BLOCKED | sessions_to_expiry ≥ 3 + locked |

**No structure will be evaluated today. Gate 1 is a hard stop with no override.**

Next opportunity:
* **NIFTY**: Monday Sep-7 (sessions=2, expiry eve) or Tuesday Sep-8 (sessions=1, 0-DTE)
* **SENSEX**: Tuesday Sep-9 (sessions=2) or Wednesday Sep-10 (sessions=1, expiry day Thursday)

**What to Watch Before Taking a Trade (for Monday planning)**

1. Opening Monday: NIFTY above/below 24,000 (key battleground)
2. 23,900 PE OI on Monday at 9:45: dropping fast = floor removal
3. Kill switch at 9:45 per gates.md
4. VIX post-open: if it spikes from 10.97 base, reassess
5. Monday gap: large gap down = FII bearish thesis asserting; large gap up = global tape wins again
