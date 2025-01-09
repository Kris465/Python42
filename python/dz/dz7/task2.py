num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

# Все числа диапазона
user_list = [i for i in range(num1, num2 + 1)]
print(*user_list)

# От максимального к минимальному
print(*user_list[::-1])

# Кратные семи
print(*[i for i in user_list if i % 7 == 0])

# Количество кратных пяти
print(len([i for i in user_list if i % 5 == 0]))
