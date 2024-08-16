# number = int(input("Enter any number : "))
# numbers = [124, 198, 256, 420]
#
# if number % 2 == 0 and 99 < number < 1000:
#     numbers.append(number)
#
# print(numbers)


number = int(input("Enter any number : "))

numbers = [124, 198, 256, 420]

if number % 2 == 0 and str(number)[0] != "-" and len(str(number)) == 3:
    numbers.append(number)
elif number % 2 == 0 and str(number)[0] == "-" and len(str(number)) == 4:
    numbers.append(number)

print(numbers)
