phonenumber = input("Enter your phone number : ")

if len(phonenumber) == 11:
    if phonenumber[0] == "0":
        phonenumber = phonenumber.replace("0", "+98", 1)
        print(phonenumber)
    else:
        print("Phone number must start with 0")
else:
    print("Phone number must have 11 digits")
