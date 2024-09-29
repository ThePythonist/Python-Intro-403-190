f = open("words.txt")


def find_longest1(file):
    file = file.readlines()
    # return sorted(entry, key=len)[-1]
    print(sorted(file, key=len)[-1])
    print(len(sorted(file, key=len)[-1]))


def find_longest2(file):
    file = file.readlines()
    print(max(file, key=len))
    print(len(max(file, key=len)))


def find_longest3(file):
    file = file.readlines()
    maxlen = len(max(file, key=len))

    for i in file:
        if len(i) == maxlen:
            print(i)


find_longest3(f)
