from itertools import combinations
from math import prod

with open('input.txt') as f:
    numbers = f.read().splitlines()
    comb = combinations(numbers, 3)
    product = 0
    matches = []
    for c in comb:
        c = tuple(int(i) for i in c)
        result = sum(c)
        if result == 2020:
            matches.append(c)
    product = prod(*matches)
    print(product)
