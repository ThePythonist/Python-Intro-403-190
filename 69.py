def findlongest1(entry):
    entry = entry.split()
    lengths = []

    for i in entry:
        lengths.append(len(i))

    maxlen = max(lengths)

    for i in entry:
        if len(i) == maxlen:
            # print(i)  # momkene chand ta bashe
            return i


def findlongest2(entry):
    entry = entry.split()
    return max(entry, key=len)


def findlongest3(entry):
    entry = entry.split()
    # return sorted(entry, key=len)[-1]
    return sorted(entry, key=len)[0]


txt = "python is a good programming language"
print(findlongest3(txt))
