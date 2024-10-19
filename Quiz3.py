import random

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letter = random.choice(letters)
firstpart = random.randint(10, 99)
secondpart = random.randint(100, 999)
distinct = random.choice(["99", "11", "44", "68", "38", "64", "78"])
plate = f"{firstpart}{letter}{secondpart}|IR{distinct}"
print(plate)
