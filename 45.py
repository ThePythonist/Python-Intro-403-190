info = {
    "name": "johnny depp",
    "born": 1963,
    "movies": ["pirates", "alice", "chocolate factory"],
    "height": 178
}

while True:
    key = input("Search for key : ")

    if key == "exit":
        break
    else:
        if key in info:
            print(info[key])
        else:
            print("Key not found")
