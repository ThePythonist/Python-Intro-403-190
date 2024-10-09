def extract_numbers(file):
    numbers = []

    for i in file:
        if i.isdigit():
            numbers.append(i)

    print(numbers)


words = open("words.txt").read().split("\n")
extract_numbers(words)
