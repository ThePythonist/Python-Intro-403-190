# def include_digit(file):
#     selection = []
#
#     for line in file:
#         if not line.isdigit():
#             for character in line:
#                 if character.isdigit():
#                     selection.append(line)
#                     break  # check kardan character ha stop mishe va mire soragh line baadi
#
#     print(selection)
#
#
# words = open("words.txt").read().split("\n")
# include_digit(words)

def include_digit(file):
    selection = []

    for line in file:
        if line.isdigit():
            continue

        for character in line:
            if character.isdigit():
                selection.append(line)
                break  # check kardan character ha stop mishe va mire soragh line baadi

    print(selection)


words = open("words.txt").read().split("\n")
include_digit(words)
