number = int(input("введите двухзначное число: "))
desyatki = number // 10
edenichki = number % 10
suma = desyatki + edenichki
print(f"В числе {number},\n десятки - {desyatki},\n",
      f"еденицы - {edenichki},\n сумма - {suma}")