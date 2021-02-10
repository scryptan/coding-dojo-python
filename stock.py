class Stock:

    def __init__(self):
        self.symbols = {}

    def is_empty(self):
        return False

    def count(self):
        return len(self.symbols)

    def add_symbol(self, symbol):
        self.symbols[symbol] = 0

    def purchaseNumber(self, symbol, share):
        self.symbols[symbol] += share

    def calculate(self, symbol):
        return self.symbols[symbol]

    def sale(self, param, param1):
        pass

