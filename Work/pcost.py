# pcost.py
#
# Exercise 1.27
import sys
from fileparse import parse_csv

def portfolio_cost(filename):
    'Gets the total cost of all shares in the CSV file'

    total_cost = 0.0
    portfolio = parse_csv(filename, select=['shares', 'price'], types=[int, float])
    for row in portfolio:
        total_cost += row['shares'] * row['price']

    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data\\portfoliodate.csv'

def main(argv):
    cost = portfolio_cost(argv[1])
    print('Total cost:', cost)

if __name__ == '__main__':
    import sys
    main(sys.argv)
