items = [10, 20.65, True, [], "Python", 10.25, "Java", 60, -50, False]
numbers = []

for i in items:
    # if type(i) == int or type(i) == float:
    if type(i) in [int, float]:
        numbers.append(i)

print(numbers)
