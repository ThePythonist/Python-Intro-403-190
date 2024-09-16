def is_binary(number):
    for i in number:
        if i not in ["0", "1"]:
            return False
    # else:  # baad az inke for tamam shod ( false return nashod )
    #     return True
    return True


numbers = ["512", "01101", "110", "24", "10"]
for i in numbers:
    print(is_binary(i))
