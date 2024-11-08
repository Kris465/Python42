number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
if number1 == number2:
    print("Числа равны")
elif number1 < number2:
    print(number1, number2)
else:
    print(number2, number1)
