num1 = int(input("Введите перове число: "))
num2 = int(input("Введите второе число: "))

# Число единиц
a1 = num1 % 10
# Число дсятков
a2 = num1 // 10

# Число единиц
b1 = num2 % 10
# Число дсятков
b2 = num2 // 10

number1 = 10 * a1 + a2
number2 = 10 * b1 + b2

diff = number1 - number2
# Число единиц
c1 = diff // 10
# Число дсятков
c2 = diff % 10

print(f"Разность: {diff}")
print(f"Десятки {c1}, единицы {c2}")
