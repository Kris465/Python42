def sred(a, b):
    total = 0
    num = 0
    for i in range(a, b + 1):
        total += i
        num += 1
    print(total/num)


# а
sred(1, 1000)

# б
b = int(input('Введите значение числа "b" (b > 100): '))
sred(100, b)

# в
a = int(input('Введите значение числа "a" (a < 200): '))
sred(a, 200)

# г
a = int(input('Введите значение числа "a": '))
b = int(input('Введите значение числа "b" (b > a): '))
sred(a, b)
