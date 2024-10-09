f = open("words.txt").readlines()  # list
open("reversed_words.txt", "w").writelines(f[::-1])
