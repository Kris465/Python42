num = int(input("Введите, пожалуйста, число больше 9: "))

edinici = num % 10
desyatki = (num // 10) % 10

print(f"в числе {num}, едениц - {edinici}, десяток - {desyatki}")
