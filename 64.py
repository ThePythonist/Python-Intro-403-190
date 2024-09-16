a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

print((lambda first, second: "equal" if first == second else first if first > second else second)(a, b))

# if a == b:
#     print("equal")
# else:
#     if a > b:
#         print(a)
#     else:
#         print(b)
