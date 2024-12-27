user_input = int(input("Ввведите четрыехзначное число: "))

hundreds = user_input // 100 % 10
thousands = user_input // 1000
    
print(f"Число содержит {thousands} тысяч и {hundreds} сотен")