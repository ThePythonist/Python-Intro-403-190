x = 10  # global


def func():
    x = 20  # local
    print(x)


print(x)
func()
print(x)
