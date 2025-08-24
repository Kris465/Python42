
# 1 вариант

# m = int(input("Введите номер месяца:"))
# n = int(input("Введите число:"))
# days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# if n > 1:
#     n -= 1
# else:
#     if m == 1:
#         m = 12
#         n = 31
#     else:
#         m -= 1
#         n = days_in_month[m - 1]

# print("Предыдущий день:", n, ".", m)


# 2 вариант

m = int(input("Введите номер месяца:"))
n = int(input("Введите число:"))
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if n < days_in_month[m - 1]:
    n += 1
else:
    if m == 12:
        m = 1
        n = 1
    else:
        m += 1
        n = 1

print("Следующий день:", n, ".", m)
