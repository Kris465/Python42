# 1)
# n = [i for i in range(20, 36)]
# print(n)
# for n in n:
#     print(f"Вот {n}")


# 2) квадраты всех целых чисел от 10 до b
# b = int(input("Введите число больше 10: "))
# n = [i for i in range(10, b)]
# print(n)
# for n in n:
#     j = n ** 2
#     print(f"Вот {j}")

# 3) третьи степени всех целых чисел от a до 50 (значение a вводится, a<=50)
# a = int(input("Введите число меньше или равно 50: "))
# n = [i for i in range(a, 51)]
# print(n)
# for n in n:
#     j = n ** 3
#     print(f"Вот {j}")

# 4)все целые числа от a до b (значения a и b вводятся с клавиатуры; b a)
a = int(input("Введите число: "))
b = int(input("Введите число: "))
n = [i for i in range(a, b)]
print(n)
