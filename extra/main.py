'''
https://ru.wikipedia.org/wiki/%D0%98%D0%B3%D1%80%D0%B0_%D0%B2_15
'''

import tkinter as tk
import random


class FifteenPuzzle:
    def __init__(self, master):
        self.master = master
        self.master.title("Игра в пятнашки")

        self.board = [i for i in range(1, 16)] + [0]
        random.shuffle(self.board)

        self.buttons = []
        self.empty_index = self.board.index(0)

        self.create_buttons()
        self.update_buttons()

    def create_buttons(self):
        for i in range(4):
            row = []
            for j in range(4):
                button = tk.Button(self.master, text='', font=('Arial', 24), width=5, height=2,
                                   command=lambda index=i * 4 + j: self.move(index))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def update_buttons(self):
        for i in range(4):
            for j in range(4):
                index = i * 4 + j
                if self.board[index] == 0:
                    self.buttons[i][j]['text'] = ''
                    self.buttons[i][j]['bg'] = 'white'
                else:
                    self.buttons[i][j]['text'] = str(self.board[index])
                    self.buttons[i][j]['bg'] = 'lightblue'

    def move(self, index):
        if self.is_adjacent(index, self.empty_index):
            self.board[self.empty_index], self.board[index] = self.board[index], self.board[self.empty_index]
            self.empty_index = index
            self.update_buttons()
            if self.is_solved():
                self.show_win_message()

    def is_adjacent(self, index1, index2):
        return (index1 == index2 - 1 and index1 % 4 != 3) or (index1 == index2 + 1 and index1 % 4 != 0) or (index1 == index2 - 4) or (index1 == index2 + 4)

    def is_solved(self):
        return self.board == [i for i in range(1, 16)] + [0]

    def show_win_message(self):
        win_message = tk.Toplevel(self.master)
        win_message.title("Поздравляем!")
        label = tk.Label(win_message, text="Вы выиграли!", font=('Arial', 24))
        label.pack(pady=20)
        button = tk.Button(win_message, text="Закрыть", command=win_message.destroy)
        button.pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    game = FifteenPuzzle(root)
    root.mainloop()
