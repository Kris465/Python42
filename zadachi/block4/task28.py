x = input("Введите трехзначное число: ")
if int(x[0]) > int(x[2]):
    print("Первая цифра больше третьей")
elif int(x[0]) > int(x[1]):
    print("Первая цифра больше второй")
elif int(x[1]) < int(x[2]):
    print("Вторая цифра больше третьей")
else:
    print("Цифры одинаковые")
