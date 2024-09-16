def even_or_odd(number):
    print("even") if number % 2 == 0 else print("odd")


def is_number(entry):
    if type(entry) in [int, float]:
        even_or_odd(entry)
    else:
        print("entry is not a number")


is_number(13)
