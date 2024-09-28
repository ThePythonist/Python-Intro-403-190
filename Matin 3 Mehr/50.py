def adder(number):
    # summation = 0
    # for i in str(number):
    #     summation +=int(i)
    #
    # print(summation)
    # ==========================================
    digits = []
    for i in str(number):
        digits.append(int(i))

    print(sum(digits))

adder(9412)
