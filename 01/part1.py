from itertools import combinations

with open('input.txt') as f:
    numbers = f.read().splitlines()
    comb = combinations(numbers, 2)
    product = 0
    for x,y in comb:
        if int(x) + int(y) == 2020:
            product = int(x) * int(y)
    print(product)
