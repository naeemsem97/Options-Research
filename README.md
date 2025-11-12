# 📊 Options Volatility Research

My sandbox for exploring volatility trading, market microstructure, and event-driven option strategies on QuantConnect.
This is not financial advice — just me experimenting with data, risk, and code.
I vibe-code this with help from Claude Sonnet 4.5, GPT-5, and plenty of personal debugging.

## 🎯 Overview

This repository contains quantitative explorations into options volatility, Greeks dynamics, and event-based behavior.
Each strategy is tested using QuantConnect’s Python framework with real options chain data.

## 🧠 Featured Research
### 🧾 [Earnings Strangle Analysis (New)](https://github.com/naeemsem97/Options-Research/blob/main/Earnings_Strangle_Analysis.pdf)

Testing the “IV crush” idea by selling 20-delta strangles before earnings and closing the next morning.
Spoiler: the results reveal negative expectancy due to fat-tailed losses.

### [📉 CPI Strangle Strategy](https://github.com/naeemsem97/Options-Research/blob/main/Selling%20Strangles%20%20before%20CPI.ipynb)

Event-driven short-volatility model:
Sell 2-9 DTE strangles before CPI releases, targeting IV crush post-announcement.

### Focus

- Entry/exit timing optimization

- Strike selection via IV percentiles

- P&L decomposition and regime analysis

### [🎡 Options Wheel – Magnificent 7](https://github.com/naeemsem97/Options-Research/blob/main/Options%20Wheel%20Strategy%20-%20Magnificent%207%20Backtest%20Analysis.ipynb.ipynb)

Classic wheel strategy automated for AAPL, MSFT, GOOGL, AMZN, NVDA, TSLA, META.

### Includes

- Put → assignment → covered call cycle

- Premium capture vs. directional exposure

- Rolling adjustments and portfolio aggregation

### [📊 SPX & NDX Put-Selling Framework](https://github.com/naeemsem97/Options-Research/blob/main/Selling%20Puts%20on%20SPX%20and%20NDX.ipynb)

Systematic short-put approach with:

- Delta and probability targeting

- DTE optimization

- Comparison of SPX vs NDX risk-adjusted returns

### [⚙️ VIX Reconstruction Project](https://github.com/naeemsem97/Options-Research/blob/main/VIX%20Calculation%20research.pdf)

Custom Python implementation of the official CBOE VIX methodology.

#### Goals

- Replicate variance calculation using one year of SPX chains

- Study vol-surface behavior and term-structure shifts

- Support vol-regime filters for other models

## 🧰 Tech Stack
Component	Description
Platform	QuantConnect (LEAN Engine)
Language	Python 3
Data	SPX/SPY Options Chains, EODHD Events, FRED Macro Releases
Tools	Pandas, NumPy, Matplotlib, Seaborn

## 🚀 Usage

Each folder is self-contained research you can upload directly to QuantConnect.

Clone this repository

Upload a file or notebook to QuantConnect

Adjust parameters (delta, DTE, entry time, IV filter, etc.)

Run backtests, compare results, and iterate

## 🔮 Roadmap / Future Work

- Vol-surface modeling (SVI, SABR)

- Adaptive Kelly sizing for short-vol portfolios

- Volatility-regime filters (VIX < SMA9, HV/IV spreads)

- Gamma scalping and skew arbitrage

- Cross-asset volatility spillover research

## 🧾 Disclaimer

This repository is for educational and experimental purposes only.
Nothing here constitutes financial advice or a trading recommendation.
All results are hypothetical; use this research at your own risk. I do not trade on any of this and probably never will.

## 🧩 Contribute / Collaborate

Pull requests, data insights, and strategy suggestions are welcome!
If you’ve run a similar backtest or found ways to hedge fat-tail risk — share your results.
Let’s make options research a bit more transparent 💬
