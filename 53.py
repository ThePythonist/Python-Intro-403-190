def has_duplicate1(word):
    chars = []
    for i in word:
        if i not in chars:  # AGAR TEKRARI NABOOD
            chars.append(i)
        else:  # AGAR TEKRARI BOOD
            return True

    return False


# print(has_duplicate1("ali"))

def has_duplicate2(word):
    if len(set(word)) == len(word):
        print("Tekrari nadarad")
    else:
        print("Tekrari darad")


has_duplicate2("java")
