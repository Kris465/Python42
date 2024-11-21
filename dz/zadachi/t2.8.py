k = int(input("Введите день года: "))
day = int(input("C какого дня недели начинаетя год: "))
if k % 7 == 0:
    print("Воскресенье")
elif (k - 1) % 7 == 0:
    print("Понедельник")
elif (k - 2) % 7 == 0:
    print("Вторик")
elif (k - 3) % 7 == 0:
    print("Среда")
elif (k - 4) % 7 == 0:
    print('Четверг')
elif (k - 5) % 7 == 0:
    print("Пятница")
elif (k - 6) % 7 == 0:
    print("Суббота")
