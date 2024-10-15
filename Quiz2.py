def show_prime_divs(number):
    prime_divs = []
    divs = []
    for i in range(1, number + 1):
        if number % i == 0:
            divs.append(i)

    for i in divs:
        idivs = []
        for j in range(1, i + 1):
            if i % j == 0:
                idivs.append(j)

        if len(idivs) == 2:
            prime_divs.append(i)

    print(prime_divs)


show_prime_divs(16)
