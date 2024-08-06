# Lists

# names = [1, 2, 3, 1, 4, 5, 1, 6, 7]
# print(names) # tartib darad - tekrari darad
# print(type(names))

# print(names[0]) # index darad

# names[0] = 1000  # mutable ast ! (ghabel taghir)
# del names[-1]  # mutable ast ! (ghabel taghir)
# print(names)

# lst1 = ["spain", "germany", "senegal", "canada", "mexico"]
# lst2 = ["egypt", "greece", "iran", "armenia", "india"]
#
# print(lst2+lst1)

# currencies = ["dollar", "rial", "euro", "pound", "rial"]
# numbers = [10, 5, 3, 4, 1, 2, 3]

# currencies.append("frank") # be enteha ezafe mikone
# print(currencies)

# currencies.insert(0, "rupee") # be yek position khas ezafe mikone
# print(currencies)

# currencies.remove("euro")  # hazf mikone
# print(currencies)

# print(currencies.count("rial"))

# currencies.reverse()
# print(currencies)

# print(currencies[::-1])

# currencies.sort()
# print(currencies)
#
# numbers.sort()
# print(numbers)

# ==============================================================

# products = {"iphone 13 pro": "599$", "samsung s24": '1099$', "asus zenbook 14": "799$"}
# print(products)
# print(len(products))

# print(products["samsung s24"])  # fetching values

# d1 = {"city": "tehran", "age": 24, "email": "myemail@gmail.com"}
# d1 = {"city": "shiraz", "age": 32, "email": "something@gmail.com"}
# print(d1+d2) # jam pazir nistand

# info = {"city": "tehran", "age": 24, "email": "myemail@gmail.com", "age": 30}
# print(info)

# info = {"city": "tehran", "age": 24, "email": "myemail@gmail.com"}
# info.setdefault("name", "shahram")
# print(info)


d1 = {"city": "tehran", "age": 24, "email": "myemail@gmail.com"}
d2 = {"name": "shahram", "city": "shiraz", "age": 32, "email": "something@gmail.com"}

d1.update(d2)
print(d1)
