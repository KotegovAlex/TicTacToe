import tkinter as tk
from tkinter import ttk

from config import *


class MainField(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_field()
        self.add_img = tk.PhotoImage(file='./content/tic_tac_back.png')
        # screen_width = self.winfo_screenwidth()
        # screen_height = self.winfo_screenheight()
        #
        # self.geometry(f'650x450+{screen_width // 2}+{screen_height // 2}')
        # self.resizable(False, False)

    def init_field(self):
        toolbar = tk.Frame(bg='gray', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        btn_open_rules = tk.Button(toolbar, text=RULES_TITLE,
                                   command=self.open_rules,
                                   bg='white', bd=0,
                                   compound=tk.TOP)

        btn_open_rules.pack(side=tk.LEFT)

    def open_rules(self):
        Rules()


class Rules(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()

    def init_child(self):
        self.title(RULES_TITLE)

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # self.geometry(f'350x220+{screen_width // 2}+{screen_height // 2}')
        self.geometry(f'350x220')

        self.resizable(False, False)

        label_description = ttk.Label(self, text=RULES_CONTENT, font=("Arial", 10))
        label_description.place(x=10, y=10)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=250, y=170)

        self.grab_set()
        self.focus_set()


if __name__ == "__main__":
    root = tk.Tk()
    app = MainField(root)
    app.pack()
    root.title(GAME_TITLE)
    main_width = root.winfo_screenwidth()
    main_height = root.winfo_screenheight()
    w = main_width // 2
    h = main_height // 2
    w = w - 300
    h = h - 200
    root.geometry(f'650x450+{w}+{h}')
    root.resizable(False, False)
    root.mainloop()
