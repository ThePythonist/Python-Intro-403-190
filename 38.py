shopping_list = [
    "tomato", "carrot",
    "orange", "potato",
    "orange", "orange"
]

unique_shopping_list = []

for i in shopping_list:
    if i not in unique_shopping_list:
        unique_shopping_list.append(i)

print(unique_shopping_list)
