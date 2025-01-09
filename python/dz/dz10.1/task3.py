start_mul = int(input(
    "\nВведите начальное число диапазона для таблицы умножения: "))
end_mul = int(input(
    "Введите конечное число диапазона для таблицы умножения: "))

print("\nТаблица умножения:")
for number in range(start_mul, end_mul + 1):
    print(f"Таблица умножения для {number}:")
    for i in range(1, 11):
        print(f"{number} * {i} = {number * i}")
    print("..................................................")
