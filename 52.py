# def summation(items):
#     total = 0
#     for i in items:
#         total += i
#
#     print(total)


def is_perfect(number):
    divisors = [i for i in range(1, number) if number % i == 0]

    if sum(divisors) == number:
        return True
    else:
        return False


print(is_perfect(28))
