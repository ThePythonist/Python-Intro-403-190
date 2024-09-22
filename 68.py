items = [16.5, "digikala", 24, "snapp", 10, 0.67]
print(list(filter(lambda x: True if type(x) in [int, float] else False, items)))
