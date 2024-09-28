f = open("words.txt").readlines()
sublist = []

for i in f:
    if "sub" == i[0:3]:
        sublist.append(i)

print(sublist)
