# portfolio.py

class Portfolio:
    """A simple portfolio for managing stock holdings."""

    def __init__(self):
        self._holdings = {}

    @property
    def is_empty(self):
        """Checks if the portfolio is empty."""
        return not self._holdings

    def buy(self, ticker, quantity):
        """Buys a number of shares of a stock."""
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        self._holdings[ticker] = self._holdings.get(ticker, 0) + quantity

    def sell(self, ticker, quantity):
        """Sells a number of shares of a stock."""
        if ticker not in self._holdings:
            raise KeyError(f"Stock '{ticker}' not found in portfolio.")
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        if quantity > self._holdings[ticker]:
            raise ValueError("Cannot sell more shares than you own.")
        
        self._holdings[ticker] -= quantity
        if self._holdings[ticker] == 0:
            del self._holdings[ticker]

    def get_holdings(self):
        """Returns the current holdings as a dictionary."""
        return self._holdings.copy()