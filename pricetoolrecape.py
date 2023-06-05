from statistics import mean
print("_________________COD_______________")

class PriceRange:

    def __init__(self, kind, symbol, low, high):
        self.kind = kind
        self.symbol = symbol
        self.low = low
        self.high = high


    @property
    def midpoint(self):
        return (self.high + self.low) / 2

    def __repr__(s):
        return f'{s.__class__.__name__}({s.kind!r}, {s.symbol!r}, {s.low!r}, {s.high!r})'
print("____________________LACK_______________________________")
if __name__ == '__main__':
    from pprint import pprint


    portfolio = [
        PriceRange('stock', 'CSCO', 26, 35),
        PriceRange('option', 'HP', 11, 45),
        PriceRange('stockk', 'BOA', 32, 46),
        PriceRange('stock', 'WLP', 12.87, 334.15),
        PriceRange('option', 'WLPWLP', 1.87, 14.15),
        PriceRange('option', 'boa', 34, 45),
        PriceRange('bond', 'HP', -62, 67)]

    print('Stock Securities:')
    print([s for s in portfolio if s.kind == 'Stock'])

    print('\nWLP securities:')
    pprint([s for s in portfolio if s.symbol == 'WLP'])

    print('\nBOA securities:')
    pprint([s for s in portfolio if s.symbol == 'BOA'])

    print('\nMininum low:')
    print(min(s.low for s in portfolio))

    print('\nMinimum high:')
    print(max(s.high for s in portfolio))

    print('\nAverage midpoint:')
    print(mean(s.midpoint for s in portfolio))
print("_____________________________TOOL__________________")