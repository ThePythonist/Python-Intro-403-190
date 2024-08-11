names = ["aliakbar", "aliasghar"]
name = input("Enter your name : ")

# if "ali" in name:
if name[0:3] == "ali":
    names.append(name)

print(names)
