t = float(input('Введите время в минутах: '))

timers = [3, 1, 2]
stop = False

while stop is False:
    if t > timers[0]:
        t -= timers[0]
    else:
        print('Зелёный')
        break
    if t > timers[1]:
        t -= timers[1]
    else:
        print('Жёлтый')
        break
    if t > timers[2]:
        t -= timers[2]
    else:
        print('Красный')
        break
