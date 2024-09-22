def divisors(x):
    return [i for i in range(1, x + 1) if x % i == 0]


items = [15, 12, 8, 21]
divs_map = list(map(divisors, items))
print(dict(zip(items, divs_map)))
