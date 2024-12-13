number = int(input("Введите трехзначное число: "))
edinici = number % 10
desyatki = (number // 10) % 10
sotie = number // 100
suma = edinici + desyatki + sotie
proizv = edinici * desyatki * sotie
print(f" в числе {number},\n едениц - {edinici}, \n десяток - {desyatki},\n"
      f" сумма - {suma},\n произведение - {proizv},")