summa = 0
maximum = None
minimum = None

while True:
    number = float(input("Введите число (введите 7 для выхода): "))

    if number == 7:
        print("Good bye!")
        break

    summa += number

    if maximum is None or number > maximum:
        maximum = number

    if minimum is None or number < minimum:
        minimum = number

    print("Сумма введенных чисел:", summa)
    if maximum is not None:
        print("Максимальное введенное число:", maximum)
    if minimum is not None:
        print("Минимальное введенное число:", minimum)
