def is_prime1(number):
    divisors = [i for i in range(1, number + 1) if number % i == 0]
    print("Prime") if len(divisors) == 2 else print("Composite")
    # print("Prime") if len(divisors) == 2 else None


# is_prime1(23)

def is_prime2(number):
    divisors = [i for i in range(1, number + 1) if number % i == 0]
    return True if len(divisors) == 2 else False
    # print("Prime") if len(divisors) == 2 else None


print(is_prime2(18))
