def determine_area(x, y):
    # Определяем границу
    f_x = x ** 2  # f(x) = x^2

    # Сравниваем y с f(x)
    if y > f_x:
        return "Область I"
    elif y < f_x:
        return "Область II"
    else:
        return "Точка на границе"  # На случай, если точка попадает на границу

# Пример использования
x0 = float(input("Введите координату x точки: "))
y0 = float(input("Введите координату y точки: "))

area = determine_area(x0, y0)
print(area)