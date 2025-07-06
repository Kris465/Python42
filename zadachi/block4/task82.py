a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
d = int(input('Введите четвёртое число: '))


def chek(n):
    if n % 2 == 0:
        print(f"{n} - четное")
    else:
        print(f"{n} - нечетное")


chek(a)
chek(b)
chek(c)
chek(d)
