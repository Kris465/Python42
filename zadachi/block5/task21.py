cost = int(input('Введите цену за 1кг сыра: '))

print("Вес        |          цена")

for i in range(50, 1001, 50):
    price = (i * cost) / 1000
    print(f'{i:4}      |        {price}')
