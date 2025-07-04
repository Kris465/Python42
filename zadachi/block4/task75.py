# Даны два вещественных числа. Условно принимая, что стандартной функции определения абсолютной величины числа нет, найти:
# а) полусумму абсолютных величин заданных чисел;
# б) квадратный корень из произведения абсолютных величин заданных чисел.

a = int(input("Введите число: "))
b = int(input("Введите число: "))


def my_abs_1(a):
    if a >= 0:
        return a
    else:
        return -a


def my_abs_2(b):
    if b >= 0:
        return b
    else:
        return -b


def sqr_root_1(a):
    if a >= 0:
        return a ** 0.5
    else:
        import cmath
        return cmath.sqrt(a)


def sqr_root_2(b):
    if b >= 0:
        return b ** 0.5
    else:
        import cmath
        return cmath.sqrt(b)


res1 = ((my_abs_1(a) + my_abs_2(b)) / 2)
res2 = ((sqr_root_1(a) * sqr_root_2(b)))

print(f"В общем ответ на первую задачу: {res1}, а ответ на вторую: {res2}")
