try:
    number = int(input("Введите число: "))
    if number > 0:
        print("Число больше нуля.")
    elif number == 0:
        print("Число равно нулю.")
    else:
        print("Число меньше нуля.")
# except Exception as e:
#     print(f"Ошибка: {e}")
except ValueError:
    print("Это не число!")
