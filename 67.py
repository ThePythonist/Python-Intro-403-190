def is_binary(number):  # Ex 54
    for i in number:
        if i not in ["0", "1"]:
            return False
    return True


items = ["11011", "24", "61", "10", "0101"]
print(list(filter(is_binary, items)))
