a = int(input("Введите целое число a: "))
b = int(input("Введите целое число b: "))

result = (a % b == 0) or (b % a == 0)

print(int(result))
