# List Comprehension

# lst = []
# for i in range(10):
#     lst.append(i)
# print(lst)
# ==============================================
# lst = [i for i in range(10)]
# print(lst)
# ==============================================
# lst = ["OK" for i in range(10)]
# print(lst)
# ==============================================
# lst = [i**2 for i in range(10)]
# print(lst)
# ==============================================
# lst = []
# for i in range(10):
#     if i % 2 == 0:
#         lst.append(i)
# print(lst)
# ==============================================
lst = [i for i in range(10) if i % 2 == 0]
print(lst)
