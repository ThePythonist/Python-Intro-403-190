words = ("nan", "rar", "noon", "pop")

word = input("Enter any word : ")

if word == word[::-1]:
    words += (word,)

print(words)
