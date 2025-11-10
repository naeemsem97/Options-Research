# Options Volatility Research 📊

My sandbox of vol ideas and strategies I test on QuantConnect. This isn't financial advice—just a guy playing around with random numbers and education on coding.

## 🎯 What's Inside

This repository contains various explorations into options volatility trading concepts, Greeks dynamics, and market microstructure around key events.

### Current Projects

#### Vanna Crush Research
Analysis of vanna exposure dynamics around major market events:
- **CPI Releases**: Examining how dealer vanna positioning impacts price action before and after Consumer Price Index announcements
- **Earnings Events**: *(Coming Soon)* Similar analysis for individual equity earnings releases

The vanna crush phenomenon occurs when dealers hedge their options books, potentially amplifying or dampening price movements around realized volatility events.

#### VIX Calculation Implementation
Custom implementation of the CBOE VIX calculation methodology using SPX options data:
- One year of historical SPX options chain data
- Replicates the official CBOE variance calculation
- Useful for understanding VIX construction and testing VIX-related strategies

## 🛠️ Tech Stack

- **Platform**: QuantConnect
- **Language**: Python (QC framework)
- **Data**: SPX/SPY options chains, market data

## 📝 Disclaimer

This is purely educational and experimental research. Nothing here constitutes financial advice or trading recommendations. All strategies are theoretical exercises in quantitative finance and programming.

## 🚀 Usage

Each file contains standalone research that can be backtested on the QuantConnect platform. Clone and upload to your QuantConnect account to explore the research.

## 🔮 Future Ideas

- Gamma scalping dynamics
- Vol surface skew arbitrage
- Cross-asset vol spillovers
- More event-driven Greek exposure analysis

---

*Feel free to fork, experiment, and share your findings. Happy coding!* 🤓
