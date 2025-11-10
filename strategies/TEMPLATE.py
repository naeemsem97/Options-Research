"""
Strategy Template for QuantConnect

Description: [Describe your strategy here]
Author: [Your name]
Date: [Date created]
"""

from AlgorithmImports import *


class StrategyTemplate(QCAlgorithm):
    """
    Template for creating new options trading strategies on QuantConnect.
    
    This template provides the basic structure for:
    - Initialization
    - Universe selection
    - Trade logic
    - Risk management
    """
    
    def Initialize(self):
        """
        Initialize the algorithm parameters and settings.
        """
        # Set start and end dates for backtest
        self.SetStartDate(2020, 1, 1)
        self.SetEndDate(2023, 1, 1)
        
        # Set starting cash
        self.SetCash(100000)
        
        # Add the underlying equity
        self.equity = self.AddEquity("SPY", Resolution.Minute)
        self.symbol = self.equity.Symbol
        
        # Add options universe
        option = self.AddOption("SPY", Resolution.Minute)
        self.option_symbol = option.Symbol
        
        # Set option universe filter
        option.SetFilter(self.OptionFilter)
        
        # Initialize strategy parameters
        self.lookback_period = 20
        self.entry_threshold = 0.0
        self.exit_threshold = 0.0
        
        # Schedule functions (optional)
        # self.Schedule.On(
        #     self.DateRules.EveryDay(self.symbol),
        #     self.TimeRules.AfterMarketOpen(self.symbol, 30),
        #     self.CheckEntry
        # )
    
    def OptionFilter(self, universe):
        """
        Define the options universe to trade.
        
        Args:
            universe: The option chain universe
            
        Returns:
            Filtered option chain
        """
        return (universe
                .IncludeWeeklys()
                .Strikes(-5, 5)  # ATM +/- 5 strikes
                .Expiration(0, 60))  # 0-60 days to expiration
    
    def OnData(self, slice):
        """
        Main event handler for processing new data.
        
        Args:
            slice: Current data slice with market data
        """
        # Check if we have options data
        if not slice.OptionChains:
            return
        
        # Get the option chain
        for chain_kvp in slice.OptionChains:
            chain = chain_kvp.Value
            
            # Skip if empty chain
            if not chain:
                continue
            
            # Example: Get ATM options
            # underlying_price = self.Securities[self.symbol].Price
            # atm_call = sorted(chain, key=lambda x: abs(x.Strike - underlying_price))
            
            # Entry logic
            if not self.Portfolio.Invested:
                self.EnterPosition(chain)
            
            # Exit logic
            else:
                self.ManagePosition(chain)
    
    def EnterPosition(self, chain):
        """
        Logic for entering a new position.
        
        Args:
            chain: Current option chain
        """
        # TODO: Implement entry logic
        # Example:
        # self.MarketOrder(option.Symbol, quantity)
        pass
    
    def ManagePosition(self, chain):
        """
        Logic for managing existing positions.
        
        Args:
            chain: Current option chain
        """
        # TODO: Implement exit/adjustment logic
        # Example:
        # if profit_target_reached or stop_loss_hit:
        #     self.Liquidate()
        pass
    
    def OnOrderEvent(self, orderEvent):
        """
        Handle order events.
        
        Args:
            orderEvent: The order event
        """
        if orderEvent.Status == OrderStatus.Filled:
            self.Debug(f"Order filled: {orderEvent.Symbol} @ {orderEvent.FillPrice}")
    
    def OnEndOfDay(self, symbol):
        """
        End of day processing.
        
        Args:
            symbol: The symbol for end of day
        """
        # Optional: Log portfolio value or perform end-of-day tasks
        pass
