from math import sin, radians, fabs
k = int(input("k = "))
x = int(input("x = "))

# def calc(k, x):
print(k * x)
if k < x:
    f = k * x
elif k >= x:
    f = k + x
x42 = sin(radians(x))
if x42 < 0:
    x = x * x
elif x42 >= 0:
    x = fabs(x)


# x = calc(k, x)
# f = calc(k, x)

print(f"вот результат f(x) = {f * x}")
