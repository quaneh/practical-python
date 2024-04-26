# report.py
#
# Exercise 2.4
from fileparse import parse_csv

def read_portfolio(filename):
    '''Opens a given portfolio file and reads it into a list of tuples'''
    with open(filename) as f:
        return parse_csv(f, select=['name', 'shares', 'price'], types=[str, int, float])

def read_prices(filename):
    '''Opens a prices file and reads it into a dictionary of stock prices'''
    with open(filename) as f:
        return dict(parse_csv(f, types=[str, float], has_headers=False))

def calculate_value():
    initial_portfolio = read_portfolio('Data\\portfolio.csv')
    current_prices = read_prices('Data\\prices.csv')

    total_value = 0.0
    for share in initial_portfolio:
        price_diff = current_prices[share['name']] - share['price']
        total_value += share['shares'] * price_diff

    return total_value

def make_report(portfolio, prices):
    report = []
    for stock in portfolio:
        name = stock['name']
        current_price = prices[name]
        change = current_price - stock['price']
        row = (name, stock['shares'], current_price, change)
        report.append(row)

    return report

def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print((('-' * 10) + ' ') * len(headers) )
    for name, shares, price, change in report:
        price = '$' + str(round(price, 2))
        print(f'{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}')

def portfolio_report(portfolio_filename: str, prices_filename: str) -> None:
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)

def main(argv):
    portfolio_report(argv[1], argv[2])

if __name__ == '__main__':
    import sys
    main(sys.argv)
