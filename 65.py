number = int(input("Enter any number : "))
divs = [i for i in range(1, number) if number % i == 0]
# print(divs)
print((lambda x: "Perfect" if x == sum(divs) else "Not Perfect")(number))
