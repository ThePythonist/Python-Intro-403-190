n = int(input("چند عدد مد نظر دارید ؟ "))
nums = list()

for i in range(n):
    x = int(input("عددی را وارد کنید : "))
    nums.append(x)

print("بزرگترین عدد : ", max(nums))
