# а
total = 1

for i in range(8, 16):
    total *= i
print(total)

# б
total = 1
a = int(input('Введите любое число "a" (a < 20): '))

for i in range(a, 21):
    total *= i
print(total)

# в
b = int(input('Введите любое число "b" (1 < b < 20): '))
total = 1

for i in range(1, b + 1):
    total *= i
print(total)

# г
a = int(input('Введите любое число "a": '))
b = int(input('Введите любое число "b" (b > a): '))
total = 1

for i in range(a, b + 1):
    total *= i
print(total)
