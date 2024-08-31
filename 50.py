def sumdigits(number):
    # SUM = 0
    # for i in str(number):
    #     SUM += int(i)
    #
    # print(SUM)
    # --------------------------------------
    # digits = []
    # for i in str(number):
    #     digits.append(int(i))
    #
    # print(sum(digits))
    # --------------------------------------
    digits = [int(i) for i in str(number)]
    print(sum(digits))


sumdigits(45135)
