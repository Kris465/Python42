numbers = [int(i) for i in input("Введите три числа: ") if i.isdigit()]
sign = input("Введите знак: ")
multiple = 1
if sign == "*":
    for i in numbers:
        multiple *= i
    print(multiple)
elif sign == "+":
    summa = sum(numbers)
    print(summa)
else:
    print("Я не знаю такого знака!")
