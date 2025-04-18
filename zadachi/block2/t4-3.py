x = int(input("Введите значение точки x: "))
y = int(input("Введите значение точки y: "))


def display_point(x, y):
    print("+" + "-" * 10 + "+")
    for row in range(9, -1, -1):
        print("|", end="")
        for col in range(10):
            if col == x and row == y:
                print("*", end="")
            else:
                print(" ", end="")
        print("|")
    print("+" + "-" * 10 + "+")


def check_position(x, y):
    if x < 0 or y < 0:
        print("Координаты должны быть положительными числами")
        return

    if x >= 10 or y >= 10:
        print("Точка находится за пределами графика (10x10)")
        return

    if x < 5:
        print("Точка находится во второй части")
    else:
        print("Точка находится в первой части")

    display_point(x, y)


check_position(x, y)
