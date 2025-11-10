# Utilities

This directory contains shared utility functions and helpers for strategy development.

## Potential Utilities

- **greeks.py**: Calculate option Greeks (delta, gamma, theta, vega, rho)
- **volatility.py**: Implied volatility calculations and analysis
- **risk_management.py**: Position sizing and risk management tools
- **indicators.py**: Custom technical indicators
- **backtesting_helpers.py**: Common backtesting utilities
- **data_processing.py**: Data cleaning and preprocessing functions

## Usage

Import utilities in your strategy files:

```python
from utils.greeks import calculate_delta
from utils.risk_management import position_size
```
