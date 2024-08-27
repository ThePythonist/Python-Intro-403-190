entry = input("Entry : ")

try:
    entry = int(entry)
    print("entry was number")
except ValueError:
    # print("entry was not a number")
    pass
