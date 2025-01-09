'''
пятнашки
'''


import random

size = 4
numbers = list(range(size**2))
random.shuffle(numbers)


def is_solvable(numbers):
    inversions = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] and numbers[j] and numbers[i] > numbers[j]:
                inversions += 1
    return inversions % 2 == 0


while True:
    if is_solvable(numbers):
        break
    random.shuffle(numbers)

field = [numbers[i:i + size] for i in range(0, size**2, size)]

def is_proper(field):
    return field == [list(range(i * size, (i + 1) * size)) for i in range(size - 1)] + [[0] + list(range(size - 1))]

def draw_field(field):
    for row in field:
        print(" ".join(str(e) for e in row))

def find_zero(field):
    for i in range(size):
        for j in range(size):
            if field[i][j] == 0:
                return i, j
    return -1, -1

def move(field, direction):
    x, y = find_zero(field)
    if direction == 'right' and y < size - 1:
        field[x][y], field[x][y + 1] = field[x][y + 1], field[x][y]
    elif direction == 'left' and y > 0:
        field[x][y], field[x][y - 1] = field[x][y - 1], field[x][y]
    elif direction == 'down' and x < size - 1:
        field[x][y], field[x + 1][y] = field[x + 1][y], field[x][y]
    elif direction == 'up' and x > 0:
        field[x][y], field[x - 1][y] = field[x - 1][y], field[x][y]
    else:
        return False
    return True

def play_game():
    draw_field(field)
    while not is_proper(field):
        command = input("Введите команду (left, right, up, down): ").strip().lower()
        if command in ['left', 'right', 'up', 'down']:
            if move(field, command):
                draw_field(field)
            else:
                print("Вы не можете так ходить")
        else:
            print("Введите правильную команду")

play_game()
