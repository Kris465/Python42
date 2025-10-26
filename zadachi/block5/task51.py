n = input("Введите натуральное число: ")
a = input(f'Введите "{n}" десятичных чисел через пробел: ').split(' ')

if len(a) == int(n):
    sum = 0
    for i in a:
        sum += float(i)
    sr = round(sum / len(a), 2)
    print(f'Среднее арифметическое ваших чисел: {sr}')
else:
    print('Вы ввели неправильное кол-во чисел!')
