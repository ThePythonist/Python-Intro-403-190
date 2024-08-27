primes = []

for i in range(2, 100):
    for j in range(2, i):  # 1 va khod i mojaz hastand
        if i % j == 0:
            break
    else:
        primes.append(i)  # zamani ke break nashe

print(primes)
