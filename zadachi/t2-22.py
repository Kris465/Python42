user_input = int(input("Введите трехзначное число: "))

if len(str(user_input)) == 3:
    hundreds = user_input//100
    tens = user_input//10 % 10
print(f"Число содержит {tens} десятков и {hundreds} сотен")
