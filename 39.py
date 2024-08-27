number = 12
divisors = []

for i in range(1, number + 1):
    if number % i == 0:
        divisors += [i, ]

print(divisors)
