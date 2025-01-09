num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
spisok = []
for i in range(num1, num2 + 1):
    spisok.append(i)

print(spisok)
for i in spisok:
    if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
        print(i)
