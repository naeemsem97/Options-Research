# Data Directory

This directory is for storing local data files used in research and backtesting.

## Usage

Place data files here such as:
- Historical options data
- Volatility indices
- Custom datasets
- Exported backtest results

## Note

Large data files (CSV, Parquet, HDF5, etc.) are automatically excluded from git via `.gitignore`. This keeps the repository size manageable while allowing you to work with data locally.

## QuantConnect Data

When using QuantConnect, most data access is handled through their platform. This directory is primarily for:
- Local research and analysis
- Custom datasets not available on QuantConnect
- Exported results for offline analysis
