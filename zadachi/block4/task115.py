N = int(input("Введите год: "))

animals = ["Крыса", "Корова", "Тигр", "Заяц", "Дракон", "Змея", "Лошадь", "Овца", "Обезьяна", "Петух", "Собака", "Свинья"]
colors = ["Зеленый", "Красный", "Желтый", "Белый", "Чёрный"]

offset = N - 1984
animals_index = offset % 12
color_index = (offset % 10) // 2

print(f"{animals[animals_index]}, {colors[color_index]}")
