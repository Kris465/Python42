number = int(input("Введите номер дня неедли: "))
match number:
    case 1:
        print("Понедельник.")
    case 2:
        print("Вторник.")
    case 3:
        print("Среда.")
    case 4:
        print("Четверг.")
    case 5:
        print("Пятница.")
    case 6:
        print("Суббота.")
    case 7:
        print("Воскресенье.")
    case _:
        print("Такого дня не существует.")
