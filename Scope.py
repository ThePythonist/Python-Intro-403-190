balance = 0  # global

print(balance)


def variz(x):
    print("dar hale variz ...")
    global balance  # ejaze dastresi va taghir rooye balance
    balance += x


variz(500)
print(balance)
