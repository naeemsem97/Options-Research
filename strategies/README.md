# Strategies

This directory contains various options trading strategies organized by type.

## Directory Structure

- **volatility/**: Strategies focused on volatility trading
  - Straddles, strangles, iron condors
  - Volatility arbitrage
  - VIX-based strategies

- **spreads/**: Various spread strategies
  - Vertical spreads
  - Calendar spreads
  - Diagonal spreads

- **directional/**: Directional trading strategies
  - Covered calls
  - Cash-secured puts
  - Synthetic positions

## Usage

Each strategy should be implemented as a standalone QuantConnect algorithm that can be:
1. Backtested on historical data
2. Paper traded for validation
3. Deployed to live trading (with caution!)

## Strategy Template

When creating a new strategy, include:
- Clear description of the strategy logic
- Entry and exit conditions
- Risk management parameters
- Performance metrics to track
- Comments explaining key decisions
