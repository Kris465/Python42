number = 0

while number != 7:
    number = int(input("Введите число: "))
    if number > 0 and number != 7:
        print("Число больше нуля!")
    elif number < 0:
        print("Число меньше нуля!")
    elif number == 0:
        print("Число равно нулю!")
    else:
        print("Пока!")
