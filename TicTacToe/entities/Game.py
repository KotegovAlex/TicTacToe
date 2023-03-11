from tkinter import *
from tkinter import messagebox as mbox
from tkinter.ttk import Frame

from TicTacToe.config import *


class Game(Frame):
    @staticmethod
    def init_main_field():
        root = Tk()
        tictac = Game()
        root.mainloop()

    def __init__(self):
        super().__init__()
        self.__init_game()

    def __init_game(self):
        self.master.title(GAME_TITLE)
        screen_width = self.winfo_screenwidth() // 2
        screen_height = self.winfo_screenheight() // 2

        screen_pos_x = screen_width - WINDOW_WIDTH // 2
        screen_pos_y = screen_height - WINDOW_HEIGHT // 2

        self.master.geometry(
            f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{screen_pos_x}+{screen_pos_y}')
        self.master.resizable(False, False)

        self.back_img = PhotoImage(file=BACK_IMG_PATH)
        self.background_lbl = Label(self, image=self.back_img)
        self.background_lbl.grid(row=0, column=0)
        self.pack()

        self.rules = Button(self, text=RULES_TITLE, width=14, bg='black', fg='lime',
                            font=('Comic Sans MS', 12, 'bold'),
                            command=lambda: mbox.showinfo(RULES_TITLE, RULES_CONTENT)
                            )
        self.rules.place(relx=1, rely=0, anchor=NE)

        self.quit_btn = Button(self, text='Выход', width=14, height=1, bg='black', fg='lime',
                               font=('Comic Sans MS', 12, 'bold'), command=quit
                               )
        self.quit_btn.place(relx=1, rely=1, anchor=SE)

        self.new_game = Button(self, text='Новая игра', width=14, height=1, bg='black', fg='lime',
                               font=('Comic Sans MS', 12, 'bold'), command=self.__start_game
                               )
        self.new_game.place(relx=0, rely=0, anchor=NW)

        self.stats = Button(self, text='Статистика', width=14, height=1, bg='black', fg='lime',
                            font=('Comic Sans MS', 12, 'bold')
                            )
        self.stats.place(relx=0.5, rely=0, anchor=N)

        self.info = Label(text='Начните игру!', width=20, height=2, bg='black', fg='lime',
                          font=('Comic Sans MS', 12, 'bold')
                          )
        self.info.place(relx=0.5, rely=1, anchor=S)

    def __start_game(self):
        self.turn = 'x'
        self.count = 1

        self.cells = []

        self.x_marks = []
        self.o_marks = []

        self.win_marks = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

        self.cell1 = Button(self, text="", width=16, height=8, bg='gray', fg='gray',
                            command=lambda: self.__on_click(self.cell1)
                            )
        self.cell1.place(x=153, y=140, anchor=CENTER)
        self.cells.append(self.cell1)

        self.cell2 = Button(self, text="", width=16, height=8, bg='gray', fg='gray',
                            command=lambda: self.__on_click(self.cell2)
                            )
        self.cell2.place(x=275, y=140, anchor=CENTER)
        self.cells.append(self.cell2)

        self.cell3 = Button(self, text="", width=16, height=8, bg='gray', fg='gray',
                            command=lambda: self.__on_click(self.cell3)
                            )
        self.cell3.place(x=397, y=140, anchor=CENTER)
        self.cells.append(self.cell3)

        self.cell4 = Button(self, text="", width=16, height=8, bg='gray', fg='gray',
                            command=lambda: self.__on_click(self.cell4)
                            )
        self.cell4.place(x=153, y=271, anchor=CENTER)
        self.cells.append(self.cell4)

        self.cell5 = Button(self, text="", width=16, height=8, bg='gray', fg='gray',
                            command=lambda: self.__on_click(self.cell5)
                            )
        self.cell5.place(x=275, y=271, anchor=CENTER)
        self.cells.append(self.cell5)

        self.cell6 = Button(self, text="", width=16, height=8, bg='gray', fg='gray',
                            command=lambda: self.__on_click(self.cell6)
                            )
        self.cell6.place(x=397, y=271, anchor=CENTER)
        self.cells.append(self.cell6)

        self.cell7 = Button(self, text="", width=16, height=8, bg='gray', fg='gray',
                            command=lambda: self.__on_click(self.cell7)
                            )
        self.cell7.place(x=153, y=402, anchor=CENTER)
        self.cells.append(self.cell7)

        self.cell8 = Button(self, text="", width=16, height=8, bg='gray', fg='gray',
                            command=lambda: self.__on_click(self.cell8)
                            )
        self.cell8.place(x=275, y=402, anchor=CENTER)
        self.cells.append(self.cell8)

        self.cell9 = Button(self, text="", width=16, height=8, bg='gray', fg='gray',
                            command=lambda: self.__on_click(self.cell9)
                            )
        self.cell9.place(x=397, y=402, anchor=CENTER)
        self.cells.append(self.cell9)

        self.info["text"] = 'Игра началась!'

    def __player_turn(self):
        if self.turn == 'x':
            self.turn = 'o'
        else:
            self.turn = 'x'

    def __end_game(self, text=NO_ONE):
        self.__start_game()
        self.info['text'] = text
        for cell in self.cells:
            cell['state'] = DISABLED

    def __on_click(self, cell):
        print(self.cells[0] == cell)
        value = None
        cell['bg'] = 'white'
        for item in self.cells:
            if item == cell:
                value = self.cells.index(item) + 1
        if self.turn == 'x':
            cell['text'] = 'X'
            self.x_marks.append(value)
        else:
            cell['text'] = 'O'
            self.o_marks.append(value)

        cell['state'] = DISABLED
        self.count += 1
        self.__get_mark()

    def __get_mark(self):
        if self.count == 9:
            self.__end_game()
        else:
            for win_comb in self.win_marks:
                a = set(win_comb).issubset(self.x_marks)
                b = set(win_comb).issubset(self.o_marks)
                match (a, b):
                    case (True, False):
                        self.__end_game(CROSS_WIN)
                    case (False, True):
                        self.__end_game(ZERO_WIN)
            self.__player_turn()
