# Дано трехзначное число. Определить:
# а) является ли сумма его цифр двузначным числом;
# б) является ли произведение его цифр трехзначным числом;
# в) больше ли числа а произведение его цифр;
# г) кратна ли пяти сумма его цифр;
# д) кратна ли сумма его цифр числу а.

# number = int(input("Введите трехзначное число: "))

# if 100 <= abs(number) <= 999:
#     print("123")
# else:
#     print("ты чё")


# def robox(number):
#     num_str = str(abs(number))
#     digit1 = int(num_str[0])
#     digit2 = int(num_str[1])
#     digit3 = int(num_str[2])

#     sum_digits = digit1 + digit2 + digit3
#     proz_digits = digit1 + digit2 + digit3
#     if 10 <= sum_digits <= 99:
#         print("Сумма цифр является двузначным числом.")
#     else:
#         print("Сумма цифр не является двузначным числом.")
#     if 100 <= proz_digits <= 1000:
#         print("Сумма цифр является трёхзначным числом.")
#     else:
#         print("Сумма цифр не является двузначным числом.")

#     return digit1, digit2, digit3


# digit1 = robox(number)
# digit2 = robox(number)
# digit3 = robox(number)

# я передумал

a = int(input("Введите трехзначное число: "))
if 100 <= abs(a) <= 999:
    d1, d2, d3 = map(int, str(abs(a)))
    s = d1 + d2 + d3
    p = d1 * d2 * d3
    print(f"Сумма цифр — {'двухзначное' if 10 <= s <= 99 else 'не двузначное'}")
    print(f"Произведение цифр — {'трехзначное' if 100 <= p <= 999 else 'не трехзначное'}")
    print(f"Число больше произведения — {'да' if abs(a) > p else 'нет'}")
    print(f"Сумма делится на 5 — {'да' if s % 5 == 0 else 'нет'}")
    print(f"Сумма делится на число — {'да' if s != 0 and a % s == 0 else 'нет'}")
else:
    print("Это не трехзначное число.")
