num = int(input("Введите число: "))


num1 = num // 100
num2 = (num//10) % 10
num3 = num % 10

print(f"{num2}{num1}{num3}")
