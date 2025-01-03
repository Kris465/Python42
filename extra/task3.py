'''
1. Доска 8x8
2. Пользователь вводит начальную позицию коня (2 числа)
3. Конь обходит всю доску не наступая на одну и туже клетку дважды.

https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B4%D0%B0%D1%87%D0%B0_%D0%BE_%D1%85%D0%BE%D0%B4%D0%B5_%D0%BA%D0%BE%D0%BD%D1%8F

'''


def is_safe(x, y, board):
    return 0 <= x < 8 and 0 <= y < 8 and board[x][y] == -1


def print_solution(board):
    for row in board:
        print(" ".join(str(cell).rjust(2, ' ') for cell in row))
    print()


def knight_tour_util(x, y, move_i, board, x_moves, y_moves):
    if move_i == 64:
        return True

    for i in range(8):
        next_x = x + x_moves[i]
        next_y = y + y_moves[i]
        if is_safe(next_x, next_y, board):
            board[next_x][next_y] = move_i
            if knight_tour_util(next_x, next_y, move_i + 1,
                                board, x_moves, y_moves):
                return True
            board[next_x][next_y] = -1

    return False


def knight_tour(start_x, start_y):
    board = [[-1 for _ in range(8)] for _ in range(8)]
    x_moves = [2, 1, -1, -2, -2, -1, 1, 2]
    y_moves = [1, 2, 2, 1, -1, -2, -2, -1]

    board[start_x][start_y] = 0

    if knight_tour_util(start_x, start_y, 1, board, x_moves, y_moves):
        print_solution(board)
    else:
        print(f"С ({start_x}, {start_y}) конь не может обойти всю доску.")

try:
    start_x = int(input("Введите координату X (0-7): "))
    start_y = int(input("Введите координату Y (0-7): "))

    if 0 <= start_x < 8 and 0 <= start_y < 8:
        knight_tour(start_x, start_y)
    else:
        print("Координаты должны быть в диапазоне от 0 до 7.")
except ValueError:
    print("Пожалуйста, введите корректные целые числа.")
