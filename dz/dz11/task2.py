# Треугольник 
# def draw_figure(size):
#     for i in range(size):
#         for j in range(size):
#             if i + j >= size - 1 and j - i <= 0:
#                 print("*", end=" ")
#             else:
#                 print("-", end=" ")
#         print()


# draw_figure(5)


def draw_figure(size):
    figure = []

    for i in range(size):
        row = []
        for j in range(size):
            if (i == 0 or i == size - 1 or
                (i == 1 and 1 <= j <= 3) or
                (i == 2 and j == 2) or
                (i == 3 and 1 <= j <= 3)):
                row.append("*")
            else:
                row.append("-")
        figure.append(" ".join(row))
    print("\n".join(figure))


draw_figure(5)
