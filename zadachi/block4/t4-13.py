import Math

a = float(input("Напишите мне пеже число, дробное: "))
b = float(input("Напишите мне пеже второе число, дробное: "))
c = float(input("Напишите мне пеже третье число, дробное: "))

d = b**2 + 4 * a * c

if d > 0:
    x1 = (-b + Math.sqrt(d))/(2*a)
    x2 = (-b - Math.sqrt(d))/(2*a)
if d == 0:
    pass

# Надо доработать