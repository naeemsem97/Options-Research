# Options Volatility Research 📊

My sandbox of vol ideas and strategies I test on QuantConnect. This isn't financial advice—just a guy playing around with random numbers and education on coding. I vibe code this using LLM models like Claude Sonnet 4.5 and GPT 5, and my own basic experience debugging and troubleshooting.

## 🎯 What's Inside

This repository contains various explorations into options volatility trading concepts, Greeks dynamics, and market microstructure around key events.

### Current Projects

#### 📉 Selling Strangles Before CPI
Event-driven strategy selling strangles ahead of CPI announcements to capitalize on vol crush post-release. Analysis includes:
- Entry/exit timing optimization
- Strike selection based on IV percentiles
- P&L attribution and risk metrics

#### 🎡 Options Wheel Strategy - Magnificent 7
Classic wheel strategy (selling puts → assignment → covered calls) backtested on the Mag 7 stocks:
- AAPL, MSFT, GOOGL, AMZN, NVDA, TSLA, META
- Premium collection vs. directional exposure analysis
- Rolling adjustments and assignment handling

#### 📊 SPX & NDX Put Selling
Systematic short put strategies on major indices:
- Delta/probability targeting
- DTE optimization
- Comparison of risk-adjusted returns between SPX and NDX

#### 📈 VIX Calculation Research
Custom implementation of the CBOE VIX calculation methodology:
- One year of historical SPX options chain data
- Replicates the official CBOE variance calculation
- Foundation for understanding vol surface dynamics and VIX-based strategies

## 🛠️ Tech Stack

- **Platform**: QuantConnect
- **Language**: Python (QC framework)
- **Data**: SPX/SPY options chains, market data

## 📝 Disclaimer

This is purely educational and experimental research. Nothing here constitutes financial advice or trading recommendations. All strategies are theoretical exercises in quantitative finance and programming.

## 🚀 Usage

Each file contains standalone research that can be backtested on the QuantConnect platform. Clone and upload to your QuantConnect account to explore the research.

## 🔮 Future Ideas

- **Earnings Vol Crush**: Pre-earnings IV expansion → post-announcement collapse dynamics
- **Vol Surface Modeling**: Building and calibrating parametric volatility surfaces (SABR, SVI, etc.)
- **Kelly Criterion**: Optimal position sizing for options strategies based on edge and bankroll
- Gamma scalping dynamics
- Vol surface skew arbitrage
- Cross-asset vol spillovers

---

*Feel free to fork, experiment, and share your findings. Happy coding!* 🤓
