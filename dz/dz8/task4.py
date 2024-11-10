summa = 0
number = int(input("Введите число: "))
maximum = number
minimum = number

while number != 7:
    number = int(input("Введите число: "))
    summa += number
    if number < minimum:
        ninimum = number
    elif number > maximum:
        maximum = number

    print(f"Сумма: {summa}", f"Макс: {maximum}", f"Мин: {minimum}")
