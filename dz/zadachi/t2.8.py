k = int(input("Введите день года: "))
if k % 7 == 0:
    print("Понедельник")
elif (k - 1) % 7 == 0:
    print("Вторник")
elif (k - 2) % 7 == 0:
    print("Среда")
elif (k - 3) % 7 == 0:
    print("Четверг")
elif (k - 4) % 7 == 0:
    print('Пятница')
elif (k - 5) % 7 == 0:
    print("Суббота")
elif (k - 6) % 7 == 0:
    print("Воскресенье")
