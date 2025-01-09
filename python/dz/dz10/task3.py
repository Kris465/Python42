def multiplication_table_in_range(start, end):
    for i in range(start, end + 1):
        print(f"Таблица умножения для {i}:")
        for j in range(1, 11):
            print(f"{i} * {j} = {i * j}")
        print()


start_num = int(input("Введите начальное число для таблицы умножения: "))
end_num = int(input("Введите конечное число для таблицы умножения: "))
multiplication_table_in_range(start_num, end_num)
