# а
total = 0

for i in range(100, 501):
    total += i
print(total)

# б
total = 0
a = int(input('Введите любое число "a" (a < 500): '))

for i in range(a, 501):
    total += i
print(total)

# в
b = int(input('Введите любое число "b" (b > -10): '))
total = 0

for i in range(-10, b + 1):
    total += i
print(total)

# г
a = int(input('Введите любое число "a": '))
b = int(input('Введите любое число "b" (b > a): '))
total = 0

for i in range(a, b + 1):
    total += i
print(total)
