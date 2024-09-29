f = open("words.txt")


def func1(file):
    words = []
    file = file.readlines()
    for i in file:
        words.append(i[:-1])

    print(words)


# func1(f)

def func2(file):
    file = file.read().replace("\n", " ")
    print(file)


# func2(f)

def func3(file):
    file = file.read().split("\n")
    print(file)


func3(f)
