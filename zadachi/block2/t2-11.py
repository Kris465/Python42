number = input("Введите двузначное чило: \n")
print(number[::-1])

number1 = int(input("Другой метод, Введите число: \n"))
print(f"{number1 % 10}{number1 // 10}")

number2 = int(input("Введите двузначное чило: \n"))

if 10 <= number2 < 100:
    str_number = str(number)
    swapped_number = int(str_number[1] + str_number[0])
    print("Ответ: ", swapped_number)
else:
    print("Введенo не корректное число!")
