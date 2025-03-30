import tkinter as tk
from tkinter import messagebox


class ClickerGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Кликер-игра")
        self.root.geometry("400x300")

        self.score = 0
        self.click_power = 1
        self.theme = "light"
        self.font_size = 12

        self.score_label = tk.Label(root,
                                    text=f"Очки: {self.score}",
                                    font=("Arial", 14))
        self.score_label.pack(pady=20)

        self.click_button = tk.Button(
            root,
            text="Кликни меня!",
            command=self.add_score,
            bg="lightblue",
            font=("Arial", self.font_size)
        )
        self.click_button.pack(pady=10)

        self.settings_button = tk.Button(
            root,
            text="Настройки",
            command=self.open_settings
        )
        self.settings_button.pack(pady=10)

    def add_score(self):
        self.score += self.click_power
        self.score_label.config(text=f"Очки: {self.score}")

    def open_settings(self):
        settings_window = tk.Toplevel(self.root)
        settings_window.title("Настройки игры")
        settings_window.geometry("300x250")

        tk.Label(settings_window, text="Сила клика: ").pack()
        click_power_entry = tk.Entry(settings_window)
        click_power_entry.insert(0, str(self.click_power))
        click_power_entry.pack()

        tk.Label(settings_window, text="Тема").pack()
        theme_var = tk.StringVar(value=self.theme)
        tk.Radiobutton(settings_window,
                       text="Светлая",
                       variable=theme_var,
                       value="light").pack()
        tk.Radiobutton(settings_window,
                       text="Темная",
                       variable=theme_var,
                       value="dark").pack()

        tk.Label(settings_window, text="Размер шрифта: ").pack()

        font_size_slider = tk.Scale(
            settings_window, from_=10, to=20, orient="horizontal",
            command=lambda x: self.change_font_size(int(x))
        )
        font_size_slider.set(self.font_size)
        font_size_slider.pack()

        def apply_settings():
            try:
                self.click_power = int(click_power_entry.get())
                self.theme = theme_var.get()
                self.update_theme()
                settings_window.destroy()
            except ValueError:
                messagebox.showerror("Ошибка",
                                     "Сила клика должна быть числом!")

        tk.Button(settings_window, text="Применить",
                  command=apply_settings).pack(pady=10)

    def change_font_size(self, size):
        self.font_size = size
        self.click_button.config(font=("Arial", size))

    def update_theme(self):
        bg_color = "white" if self.theme == "light" else "#333333"
        fg_color = "black" if self.theme == "light" else "white"
        btn_color = "lightblue" if self.theme == "light" else "#555555"

        self.root.config(bg=bg_color)
        self.score_label.config(bg=bg_color, fg=fg_color)
        self.click_button.config(bg=btn_color, fg=fg_color)
        self.settings_button.config(bg=btn_color, fg=fg_color)


if __name__ == '__main__':
    root = tk.Tk()
    game = ClickerGame(root)
    root.mainloop()
