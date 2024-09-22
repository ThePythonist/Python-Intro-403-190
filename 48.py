word = "python"

# chars = {}
# for i in range(len(word)):
#     chars.setdefault(i,word[i])

chars = dict(zip(range(len(word)), word))
print(chars)
