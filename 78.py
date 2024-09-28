f = open("words.txt").readlines()
sublist = []

for i in f:
    if "ing" == i[-4:-1]:
    # if "ing\n" == i[-4:]:
        sublist.append(i)

print(sublist)
