numbers = []

for i in range(3):
    entry = input("Entry : ")  # hameye input ha be sorat pishfarz str hastand

    try:
        entry = float(entry)
        # if str(entry)[-2:] == ".0": # adad sahih ast
        if entry == int(entry):  # adad sahih ast
            numbers.append(int(entry))
        else:
            numbers.append(entry)
    except ValueError:
        # print("entry was not a number")
        pass

print(numbers)
