# 07-09-2026 Market View

**Data Points Summary**
* NIFTY: 23,784.85 (PDC: 23,897.70 | PDH: 24,005.75 | PDL: 23,895.85) → down 112 pts (−0.47%)
* BANKNIFTY: 57,103 (PDC: not fetched — data gap)
* SENSEX: 76,126.14 (PDC: 76,515.43 | PDH: 76,883.14 | PDL: 76,515.43) → down 389 pts (−0.51%)
* VIX: 11.24 (direction: check intraday — US VIX rose +1.47% to 14.53 overnight)
* Sectoral: IT 29,965 · AUTO 27,712 · FMCG 45,600 · METAL 13,188 · PHARMA 26,627 · REALTY 895
* PCR (08-Sep NIFTY): **0.558** → < 0.80 → **Bearish** (TC §10a) ⚠️ Expiry week — 2 sessions; extreme levels still informative
* PCR (10-Sep SENSEX): **0.697** → < 0.80 → **Bearish** (TC §10a)
* FII/DII F&O (T-1 = 04-Sep-2026, NSE CSV):
  * FII: Fut −736 · CE +8,753 (bought calls) · PE −69,138 (sold puts) → **Bullish (F&O)**
  * Pro: Fut −1,192 · CE +148,130 (bought calls massively) · PE −16,493 (sold puts) → **Long gamma / bullish**
  * Client: Fut +3,846 · CE −156,668 (sold calls) · PE +85,563 (bought puts) → **Bearish** (contrarian → slight bullish signal)
  * DII: Fut −1,918 · CE −215 · PE +68 → Negligible
* FII 5-day (T=04-Sep activity scores): T=+77,155 · T-1=−75,719 · T-2=−19,081 · T-3=−36,481 · T-4=+40,829 → **By Count: Bearish (2B/3Be) · By Sentiment: Bearish (net −13,297)**
* FII Cash (04-Sep): Net sellers −₹3,112 Cr · DII: Net buyers +₹8,930 Cr
* Global (as of ~12:10 IST — US closed): US S&P −0.38% · Dow −0.51% · Nasdaq −0.29% · US VIX 14.53 (+1.47%) · Nikkei +1.97% · Hang Seng −0.88% · Shanghai +0.03% · FTSE −0.00% · DAX +0.17%
* Crude WTI: $91.48 (+0.20%) · DXY: 99.10 (−0.08%)
* Nearest expiries: NIFTY **08-Sep-2026** (2 sessions) · SENSEX **10-Sep-2026** (4 sessions) · BANKNIFTY **29-Sep-2026** (~17 sessions — slot limit binds at 10)

**Missing Data — Genuine Gaps Only**
* BANKNIFTY PDC/PDH/PDL — not fetched this session
* GIFT Nifty — use opening 15-min candle (not applicable mid-session)
* IV/Greeks — Dhan broken (spot-based); TC §14 substitutes used throughout
* IVP — VIX direction used as proxy

---

**Basis Check**

| Index | F (parity) | Spot | Basis | 0.1% threshold | Verdict |
|---|---|---|---|---|---|
| NIFTY (08-Sep) | 23,832 | 23,785 | +47 pts | 23.8 pts | **EXCEEDS — use §8.7.3 on F** |
| SENSEX (10-Sep) | 76,312 | 76,126 | +186 pts | 76.1 pts | **EXCEEDS — use §8.7.3 on F** |
| BANKNIFTY (29-Sep) | 57,438 | 57,103 | +335 pts | 57.1 pts | **EXCEEDS — use §8.7.3 on F** |

Vendor delta bands unusable on all three — basis exceeds 0.1% threshold. CE IV ≠ PE IV confirms Greeks broken (TC §14).

---

**OI Wall Map — NIFTY (08-Sep expiry, 2 DTE)**

| Type | Strike | OI | Note |
|---|---|---|---|
| CE (resistance) | 23,800 | 32,744,270 | Massive call wall — largest in chain |
| CE (resistance) | 24,000 | 30,573,140 | |
| CE (resistance) | 23,900 | 30,365,335 | |
| CE (resistance) | 23,850 | 26,074,035 | |
| PE (support) | 23,800 | 20,615,855 | Same strike as top call → **pin zone** |
| PE (support) | 23,750 | 13,417,820 | |
| PE (support) | 23,700 | 13,376,805 | |
| PE (support) | 23,500 | 12,570,415 | |

Pinning zone: **23,750 – 23,800** (expiry tomorrow, OI concentration here)

---

**OI Wall Map — SENSEX (10-Sep expiry)**

| Type | Strike | OI | Note |
|---|---|---|---|
| CE (resistance) | 76,500 | 1,608,480 | |
| CE (resistance) | 77,000 | 1,372,540 | |
| CE (resistance) | 76,300 | 1,146,260 | |
| PE (support) | 76,000 | 937,980 | Current spot near this level |
| PE (support) | 75,000 | 768,560 | |
| PE (support) | 74,000 | 747,400 | |

Resistance: 76,300–76,500 · Support: 76,000 (spot is right at this level)

---

**OI Wall Map — BANKNIFTY (29-Sep expiry)**

| Type | Strike | OI | Note |
|---|---|---|---|
| CE (resistance) | 57,500 | 2,107,980 | Just above spot — tight ceiling |
| CE (resistance) | 58,000 | 1,466,070 | |
| CE (resistance) | 60,000 | 1,095,570 | |
| PE (support) | 57,500 | 1,985,580 | Symmetric with CE — pin at 57,500? |
| PE (support) | 58,000 | 1,006,350 | |
| PE (support) | 57,000 | 905,100 | |

---

**Classification: Slightly Bearish · Conviction: Medium · as of 12:10 IST**

**Participant-by-participant (T-1 = 04-Sep-2026, NSE OI CSV):**

| Participant | Index Fut | CE | PE | Reading | Implication |
|---|---|---|---|---|---|
| FII | −736 | +8,753 (bought) | −69,138 (sold) | **Bullish F&O** | Sold puts significantly — floor-writing. Bullish on the index. |
| Pro | −1,192 | +148,130 (bought massively) | −16,493 (sold) | **Long gamma / bullish** | Massive call-buying — Pro is long gamma, positioned for a move up OR hedging short books. Not a ceiling signal. |
| Client | +3,846 | −156,668 (sold) | +85,563 (bought) | **Bearish (contrarian → slight bullish signal)** | Retail selling calls and buying puts heavily = retail bearish → contrarian: lean slightly bullish. |
| DII | −1,918 | −215 | +68 | Negligible | Ignore. |

```
GATE 5 INPUTS   (T-1 = 04-Sep-2026 vs T-2 = 03-Sep-2026)   source: fao_participant_oi_*.csv
  net_CE_short = |Opt Idx Call Short| − |Opt Idx Call Long|      ΔCE = net(T-1) − net(T-2)

           level T-1     level T-2       ΔCE          ΔPE       limit (TC §9)   verdict
  FII      303,454        312,207       −8,753       +69,138       65,000        ΔPE FIRES → FORBIDS Bear Call
  Pro      −73,689         74,441      −148,130      +16,493      100,000        silent

  → Structures FORBIDDEN: Bear Call (FII ΔPE ≥ 65,000).
    Bull Put NOT thereby authorised — hands decision back to gates.
    Both forbidden would be NO TRADE; only Bear Call is forbidden here.
```

**[Synthesis]**

NIFTY and SENSEX are both gapping down from Friday's close (~0.5% each) with VIX flat at 11.24 — this is a low-vol drift lower, not a panic move. US markets closed mildly red; Nikkei strongly positive (+1.97%) is diverging from domestic weakness, suggesting the move is India-specific (possibly RBI/macro related).

FII F&O on Thursday was bullish (sold puts, bought calls), but the 5-day count shows 3 bearish sessions vs 2 bullish — the aggregate sentiment is bearish. FII cash: selling (−₹3,112 Cr). DII providing strong counter-support (+₹8,930 Cr). This DII buying is significant and preventing a sharper fall.

PCR at 0.558 (NIFTY) is very low — heavy call-writing or put-unwinding. At 2 DTE this partly reflects expiry dynamics. The 23,800 strike has symmetric OI (32.7M calls vs 20.6M puts) — this is the pin zone for tomorrow's expiry.

FII Gate 5: PE change +69,138 (FII added to put-short book significantly) — sold puts bullishly but the threshold fires to FORBID Bear Call. This is counter-intuitive: FII selling puts = they expect a floor. Gate 5's ΔPE ≥ 65K fires as a mechanical veto, not a directional signal.

What invalidates the bias intraday: sustained break below 23,750 NIFTY / 75,900 SENSEX with falling OI → long unwinding, not a bounce setup.

**Key Levels, Bias & Conviction**
* Bias: Slightly Bearish · Range 23,700–23,900 NIFTY
* Conviction: Medium — PCR and price action are bearish; FII F&O and DII cash buying are bullish; mixed signals.
* NIFTY: Support 23,750 (PE wall + pin) / 23,700 · Resistance 23,800 (CE wall) / 23,850–23,900 · Pin zone 23,750–23,800
* SENSEX: F=76,312 · Support 76,000 (spot is right at it) / 75,900 · Resistance 76,300–76,500
* BANKNIFTY: F=57,438 · Support 57,000 · Resistance 57,500 · **σ_ATM = 11.52%** (own implied vol, TC §10b Form B, N=17 sessions) ⛔ UNPAID (< 16% floor)

**What to Watch Before Taking a Trade**
1. ⛔ **NOT APPLICABLE TODAY — ALL THREE INDEXES UNPAID (VIX 11.24 < 13)**
2. VIX must recover to ≥ 13 before any trade is considered
3. Tomorrow's NIFTY expiry is at 23,750–23,800 — watch for expiry volatility, not a trading opportunity

---

**⛔ SESSION VERDICT: NO TRADE**
* NIFTY: India VIX 11.24 < 13 → `UNPAID`
* SENSEX: India VIX 11.24 (proxy) < 13 → `UNPAID`
* BANKNIFTY: σ_ATM 11.52% < 16% → `UNPAID`

**No-trade code: `UNPAID`** — premium is not being priced above realised vol. Wait for VIX to recover above 13.
