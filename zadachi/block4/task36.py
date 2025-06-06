t = float(input("Введите время в минутах с начала часа: "))

cycle_position = t % 5

if cycle_position < 3:
    print("Горит зелёный сигнал")
else:
    print("Горит красный сигнал")