a = int(input("введите сторону a"))
b = int(input("введите сторону b"))
c = int(input("введите сторону c"))
if a < b + c or a == 0 or b == 0 or c == 0:
    print("треугольник не существует")
else:
    print("треугольник сущкствеует")
