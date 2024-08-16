# entry = input("Type something : ")
# print("-" * 50)
#
# while entry != "exit":
#     entry = input("Type something : ")
#     print("-" * 50)

# ---------------------------------------------

flag = 1

while flag:  # same as flag == True
    entry = input("Type something : ")
    print("-" * 50)
    if entry == "exit":
        flag = 0
        # break  # zamani ke halghe break beshe block else ejra nemishe !
else:
    print("Flag has turned into False")
