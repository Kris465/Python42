a = 9
while not (a <= 8):
    a = int(input('Введите позицию: '))

b = 9
while not (b <= 8):
    b = int(input('Введите позицию: '))

c = 9
while not (c <= 8):
    c = int(input('Введите позицию: '))

d = 9
while not (d <= 8):
    d = int(input('Введите позицию: '))

# a)  На поле (a, b) расположена ладья. Записать условие, при котором она угрожает полю (c, d).

if a == 1 and b == 2 and c == 2 and d == 3:
    print('Ладья угрожает полю (c, d)')
else:
    print('Ладья не угрожает полю (c, d)')