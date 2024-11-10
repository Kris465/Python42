num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
for i in range(num1, num2 + 1):
    if i % 7 == 0:
        print(i, end='')

print(*[i for i in range(num1, num2 + 1) if i % 7 == 0])
[print(i) for i in range(num1, num2 + 1) if i % 7 == 0]
