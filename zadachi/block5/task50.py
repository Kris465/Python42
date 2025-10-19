a = input('Введите 10 чисел через пробел: ').split(' ')
sum = 0

for i in a:
    sum += int(i)

print(f'Среднее арифметическое ваших чисел: {round(sum / int(len(a)), 2)}')
