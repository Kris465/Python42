cost = int(input('Введите цену за 1кг сыра: '))

print("Вес       |          цена")

for i in range(100, 2001, 100):
    price = (i * cost) / 2000
    print(f'{i:4}      |        {price}')
