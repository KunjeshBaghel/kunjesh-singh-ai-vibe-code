#!/usr/bin/env python3
"""
Global Market Cues — yfinance fetcher
Prints US/Asian/European indices + Crude + DXY for Indian pre-market view.

Run with the project venv:
  /path/to/tools/fii-dii/.venv/bin/python tools/fii-dii/global_cues.py

Note: GIFT Nifty is unavailable via yfinance. Use the opening 15-min NIFTY candle
      as proxy. GIFT Nifty is a futures price — never compare it to NIFTY spot.
"""

import sys
from datetime import datetime

try:
    import yfinance as yf
except ImportError:
    print("yfinance not found. Activate the venv: tools/fii-dii/.venv/bin/python")
    sys.exit(1)

SYMBOLS = {
    "S&P 500":    "^GSPC",
    "Dow Jones":  "^DJI",
    "Nasdaq":     "^IXIC",
    "US VIX":     "^VIX",
    "S&P Fut":    "ES=F",
    "Nikkei 225": "^N225",
    "Hang Seng":  "^HSI",
    "Shanghai":   "000001.SS",
    "FTSE 100":   "^FTSE",
    "DAX":        "^GDAXI",
    "WTI Crude":  "CL=F",
    "DXY":        "DX-Y.NYB",
    "NIFTY 50":   "^NSEI",
}

GROUPS = {
    "US Markets":    ["S&P 500", "Dow Jones", "Nasdaq", "US VIX", "S&P Fut"],
    "Asian Markets": ["Nikkei 225", "Hang Seng", "Shanghai", "NIFTY 50"],
    "European":      ["FTSE 100", "DAX"],
    "Commodities":   ["WTI Crude", "DXY"],
}

EXCLUDE_FROM_SIGNAL = {"US VIX", "DXY", "S&P Fut"}
BEARISH_THRESHOLD = -0.5
BULLISH_THRESHOLD = +0.5


def fetch_quote(name: str, sym: str) -> dict | None:
    try:
        t = yf.Ticker(sym)
        fi = t.fast_info
        price = fi.get("last_price") or fi.get("regularMarketPrice")
        prev  = fi.get("previous_close") or fi.get("regularMarketPreviousClose")
        if price and prev and prev != 0:
            pct = (price - prev) / prev * 100
            return {"price": float(price), "pct": float(pct)}
        # fallback: use history
        hist = t.history(period="2d", interval="1d")
        if len(hist) >= 2:
            p, c = float(hist["Close"].iloc[-2]), float(hist["Close"].iloc[-1])
            return {"price": c, "pct": (c - p) / p * 100}
    except Exception:
        pass
    return None


def pct_label(pct: float, name: str) -> str:
    if name == "US VIX":
        return "Bearish" if pct >= BULLISH_THRESHOLD else ("Bullish" if pct <= BEARISH_THRESHOLD else "Neutral")
    return "Bullish" if pct >= BULLISH_THRESHOLD else ("Bearish" if pct <= BEARISH_THRESHOLD else "Neutral")


def fmt_pct(pct: float) -> str:
    return f"{'+' if pct >= 0 else ''}{pct:.2f}%"


def main():
    print(f"\n{'=' * 65}")
    print(f"  Global Market Cues  —  {datetime.now().strftime('%d-%b-%Y %H:%M IST')}")
    print(f"  Source: Yahoo Finance / yfinance (no login required)")
    print(f"{'=' * 65}")

    quotes = {}
    all_names = [n for names in GROUPS.values() for n in names]
    for name in all_names:
        sym = SYMBOLS[name]
        print(f"  Fetching {name}...", end="\r", flush=True)
        quotes[name] = fetch_quote(name, sym)
    print(f"  {'':40}")  # clear last status line

    overall_pcts = []

    for group, names in GROUPS.items():
        print(f"\n  {group}")
        print(f"  {'-' * 58}")
        for name in names:
            d = quotes.get(name)
            if d is None:
                print(f"    --  {name:<18} {'N/A':>14}   (unavailable)")
                continue
            label = pct_label(d["pct"], name)
            arrow = "▲" if d["pct"] >= 0 else "▼"
            print(f"    {arrow}  {name:<18} {d['price']:>14,.2f}   {fmt_pct(d['pct']):>8}  {label}")
            if name not in EXCLUDE_FROM_SIGNAL:
                overall_pcts.append((name, d["pct"]))

    if overall_pcts:
        avg = sum(p for _, p in overall_pcts) / len(overall_pcts)
        b  = sum(1 for _, p in overall_pcts if p >= BULLISH_THRESHOLD)
        be = sum(1 for _, p in overall_pcts if p <= BEARISH_THRESHOLD)
        n  = len(overall_pcts) - b - be
        verdict = ("BEARISH  → mild negative India open" if avg <= -0.3
                   else "BULLISH  → mild positive India open" if avg >= 0.3
                   else "NEUTRAL  → flat/mixed India open")
        print(f"\n  {'=' * 58}")
        print(f"  Global signal:  {verdict}")
        print(f"  Breakdown:      {b} bullish · {n} neutral · {be} bearish  |  avg {fmt_pct(avg)}")

    print(f"\n  ⚠ GIFT Nifty: unavailable via yfinance.")
    print(f"    Use NIFTY opening 15-min candle as proxy.")
    print(f"    Rule: GIFT Nifty is a futures price — never compare to NIFTY spot.\n")
    print(f"{'=' * 65}\n")


if __name__ == "__main__":
    main()
