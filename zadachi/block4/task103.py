
a = int(input("введите a: "))
b = int(input("введите b: "))
c = int(input("введите c: "))
if a > b > c:
    print(f"{a} большое число ,{c} маленькое число")

if a < b < c:
    print(f"{c} большое число ,{a} маленькое число")

if a < b > c and a > c:
    print(f"{b} большое число ,{c} маленькое число")

if a < b > c and a < c:
    print(f"{b} большое число ,{a} маленькое число")
