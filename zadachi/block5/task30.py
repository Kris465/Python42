def kvad(a, b):
    total = 0
    for i in range(a, b + 1):
        total += i**2
    print(total)


# а
total = 0
for i in range(20, 40 + 1):
    total += i**2
print(total)

# б
a = int(input('Введите значение числа "a" (0 < a < 50): '))
kvad(a, 50)

# в
n = int(input('Введите значение числа "n" (1 < n < 100): '))
kvad(1, n)

# г
a = int(input('Введите значение числа "a": '))
b = int(input('Введите значение числа "b" (b > a): '))
kvad(a, b)
