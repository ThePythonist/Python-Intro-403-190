def reverser(file):
    words = []

    # for i in f1: # in ravesh khoobi nist !
    #     f2.write(i[::-1])

    for i in f1:
        words.append(i[::-1])

    f2 = open("reversed_words2.txt", "w")
    f2.writelines(words)

    print("Done")


f1 = open("words.txt").readlines()
reverser(f1)
