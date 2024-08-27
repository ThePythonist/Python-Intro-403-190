number = int(input("Enter any number : "))
divisors = []

for i in range(1, number + 1):
    if number % i == 0:
        divisors += [i, ]

# if len(divisors) == 2:
if divisors == [1, number]:
    print("Prime")  # aval
else:
    print("Composite")  # morakab
