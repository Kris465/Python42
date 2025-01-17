# В трехзначном числе x зачеркнули его вторую цифру. Когда к образованному 
# при этом двузначному числу справа приписали вторую цифру числа x, то получилось число n.
# По заданному n найти число x (значение n вводится с клавиатуры, 100 ≤ n ≤ 999).

# Наш вариант с Натальей:

# n = 101
# p = 'asd'
# while (n < 100) or (n > 999):
#     p = input('Введите трехзначное число в диапазоне 100 ≤ n ≤ 999: ')
#     n = int(p)
# print(f'Чичло x было таким:{p[0] + p[2] + p[1]}')

# Мой вариант:

n = 0
while (n < 100) or (n > 999):
    n = int(input('Введите трехзначное число в диапазоне 100 ≤ n ≤ 999: '))
p = str(n)
print(f'Чичло x было таким:{p[0] + p[2] + p[1]}')

