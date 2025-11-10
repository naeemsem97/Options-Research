"""
Simple Long Straddle Strategy

Description: 
A basic long straddle strategy that buys ATM call and put options when 
implied volatility is low, betting on an increase in volatility or a 
large price move in either direction.

Strategy Logic:
- Entry: When IV percentile is below a threshold (e.g., 30th percentile)
- Buy ATM call and ATM put with ~30-45 DTE
- Exit: Close position at profit target, stop loss, or expiration

Risk: Limited to premium paid
Reward: Unlimited (theoretically)

Author: Amateur Vibe Coder
Note: This is educational code, not financial advice!
"""

from AlgorithmImports import *


class SimpleLongStraddle(QCAlgorithm):
    """
    A simple long straddle implementation for educational purposes.
    """
    
    def Initialize(self):
        """Initialize the algorithm."""
        self.SetStartDate(2020, 1, 1)
        self.SetEndDate(2023, 1, 1)
        self.SetCash(100000)
        
        # Add underlying
        self.equity = self.AddEquity("SPY", Resolution.Minute)
        self.symbol = self.equity.Symbol
        
        # Add options
        option = self.AddOption("SPY", Resolution.Minute)
        self.option_symbol = option.Symbol
        option.SetFilter(self.OptionFilter)
        
        # Strategy parameters
        self.min_dte = 30  # Minimum days to expiration
        self.max_dte = 45  # Maximum days to expiration
        self.profit_target = 0.50  # 50% profit target
        self.stop_loss = -0.30  # 30% stop loss
        
        # Track positions
        self.position_opened = False
        self.entry_premium = 0
        self.call_contract = None
        self.put_contract = None
        
    def OptionFilter(self, universe):
        """Filter options universe to ATM options with desired DTE."""
        return (universe
                .IncludeWeeklys()
                .Strikes(-2, 2)  # Near ATM
                .Expiration(self.min_dte, self.max_dte))
    
    def OnData(self, slice):
        """Process new data."""
        if not slice.OptionChains:
            return
        
        for chain_kvp in slice.OptionChains:
            chain = chain_kvp.Value
            
            if not chain:
                continue
            
            # Manage existing position
            if self.position_opened:
                self.CheckExit()
            # Look for entry
            else:
                self.TryEnterStraddle(chain)
    
    def TryEnterStraddle(self, chain):
        """
        Attempt to enter a straddle position.
        
        In a real implementation, you would check IV percentile here.
        This simplified version just enters a position.
        """
        # Get current underlying price
        underlying_price = self.Securities[self.symbol].Price
        
        # Find ATM call and put
        calls = [x for x in chain if x.Right == OptionRight.Call]
        puts = [x for x in chain if x.Right == OptionRight.Put]
        
        if not calls or not puts:
            return
        
        # Get closest to ATM
        atm_call = min(calls, key=lambda x: abs(x.Strike - underlying_price))
        atm_put = min(puts, key=lambda x: abs(x.Strike - underlying_price))
        
        # Ensure same expiration
        if atm_call.Expiry != atm_put.Expiry:
            return
        
        # Entry condition: For this example, enter if we have capital
        # In reality, you'd check IV percentile or other indicators
        if self.Portfolio.Cash > (atm_call.AskPrice + atm_put.AskPrice) * 100 * 2:
            
            # Buy 1 ATM call and 1 ATM put
            self.MarketOrder(atm_call.Symbol, 1)
            self.MarketOrder(atm_put.Symbol, 1)
            
            self.call_contract = atm_call.Symbol
            self.put_contract = atm_put.Symbol
            self.entry_premium = (atm_call.AskPrice + atm_put.AskPrice) * 100
            self.position_opened = True
            
            self.Debug(f"Entered Straddle: Call {atm_call.Strike}, Put {atm_put.Strike}")
            self.Debug(f"Total Premium: ${self.entry_premium:.2f}")
    
    def CheckExit(self):
        """Check if we should exit the straddle."""
        if not self.call_contract or not self.put_contract:
            return
        
        # Calculate current P&L
        current_value = 0
        
        if self.call_contract in self.Portfolio and self.Portfolio[self.call_contract].Invested:
            call_holding = self.Portfolio[self.call_contract]
            current_value += call_holding.UnrealizedProfit
        
        if self.put_contract in self.Portfolio and self.Portfolio[self.put_contract].Invested:
            put_holding = self.Portfolio[self.put_contract]
            current_value += put_holding.UnrealizedProfit
        
        if self.entry_premium == 0:
            return
        
        # Calculate P&L percentage
        pnl_pct = current_value / self.entry_premium
        
        # Exit conditions
        if pnl_pct >= self.profit_target:
            self.Liquidate()
            self.Debug(f"Profit target hit! P&L: {pnl_pct:.1%}")
            self.ResetPosition()
            
        elif pnl_pct <= self.stop_loss:
            self.Liquidate()
            self.Debug(f"Stop loss hit! P&L: {pnl_pct:.1%}")
            self.ResetPosition()
    
    def ResetPosition(self):
        """Reset position tracking."""
        self.position_opened = False
        self.entry_premium = 0
        self.call_contract = None
        self.put_contract = None
    
    def OnOrderEvent(self, orderEvent):
        """Log order events."""
        if orderEvent.Status == OrderStatus.Filled:
            self.Debug(f"Order filled: {orderEvent.Symbol} @ ${orderEvent.FillPrice:.2f}")
