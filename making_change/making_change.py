#!/usr/bin/python

# penies = 1 , nickles = 5 , dimes = 10 , quarters = 25 , half-dollars = 50
# input = amount of cents
# denominations = array of coin denominations
# total number of ways in which change can be made for input

# create denominations array
# start with largest denomination
# if largest denom is divisible by amount, use it until you cant
#


import sys


def making_change(amount, denominations):
    table = [0 for k in range(amount+1)]
    table[0] = 1
    for i in range(0, len(denominations)):
        for j in range(denominations[i], amount+1):
            table[j] += table[j-denominations[i]]
    return table[amount]


denom = [50, 25, 10, 5, 1]
a = 100

variations = making_change(a, denom)
print(variations)


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
