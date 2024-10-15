import random


def generate_password(n):
    password = []
    for i in range(n):
        password.append(str(random.randint(0, 9)))

    print("".join(password))


generate_password(6)
