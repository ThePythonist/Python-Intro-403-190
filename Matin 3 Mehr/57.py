def checknumber(number):
    if number % 2 == 0:
        print("ZOJ")
    else:
        print("FARD")

def checktype(entry):
    if type(entry) in [int, float]:
        checknumber(entry)
    else:
        print("Entry is not a number")

checktype("a")
