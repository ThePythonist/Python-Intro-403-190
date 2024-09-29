file1 = open("words.txt").read().split("\n")

file2 = open("one_line_words.txt", "w")

file2.writelines(file1)
