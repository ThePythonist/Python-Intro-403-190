number = int(input("How many files : "))
frmt = input("Type of file : ")

for i in range(number):
    open(f"C:/Users/se7en/Desktop/{i}.{frmt}", "w")
