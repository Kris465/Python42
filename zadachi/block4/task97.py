a = int(input("введите a"))
b = int(input("введите b: "))
c = int(input("введите c: "))
if a > b > c:
    print(f"{a} большое число ,{c} маленькое число")
elif a < b < c:
    print(f"{c} большое число ,{a} маленькое число")
elif a < b > c and a > c:
    print(f"{b} большое число ,{c} маленькое число")
elif a < b > c and a < c:
    print(f"{b} большое число ,{a} маленькое число")
elif a > b < c and a > c:
    print(f"{a} большое число ,{b} маленькое число")
elif a > b < c and a < c:
    print(f"{c} большое число ,{b} маленькое число")
else:
    print("попробуйте еще раз")