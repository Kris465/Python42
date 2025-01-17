n = int(input("Введите число: "))
num1 = n // 100
print(num1)
num2 = (n // 10) % 10
print(num2)
num3 = n % 10
print(num3)
print(f"{num2}{num1}{num3}")
