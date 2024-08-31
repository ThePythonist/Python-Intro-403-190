numbers = []

while True:
    entry = input("Entry : ")

    if entry == "exit":
        break

    try:
        entry = float(entry)
        if entry == int(entry):
            numbers.append(int(entry))
        else:
            numbers.append(entry)
    except ValueError:
        pass

print(numbers)
