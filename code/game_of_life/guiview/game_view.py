import tkinter as tk
from tkinter import ttk

from game_of_life.viewmodel.game_viewmodel import GameOfLifeViewModel


class GUIView(ttk.Frame):
    view_model = GameOfLifeViewModel()

    def __init__(self):
        ttk.Frame.__init__(self)

        self.master.title("Игра 'Жизнь' ")
        self.master.geometry('550x350')
        self.master.resizable(width=True, height=True)

        self.next_step_btn = tk.Button(self.master, text='Next\nstep')
        self.next_step_btn.grid(row=1, column=0, sticky=tk.W, padx=10, pady=10)

        self.remove_column_btn = tk.Button(self.master, text='-', width=3,)
        self.remove_column_btn.grid(row=1, column=1, sticky=tk.W, padx=0, pady=10)

        self.add_column_btn = tk.Button(self.master, text='+', width=3,)
        self.add_column_btn.grid(row=1, column=2, sticky=tk.W, padx=0, pady=10)

        self.remove_row_btn = tk.Button(self.master, text='-', width=3,)
        self.remove_row_btn.grid(row=2, column=0, sticky=tk.W, padx=10, pady=0)

        self.add_row_btn = tk.Button(self.master, text='+', width=3,)
        self.add_row_btn.grid(row=3, column=0, sticky=tk.W, padx=10, pady=0)

        self.field = []

        self.bind_events()
        self.mvvm_back_bind_next_btn()
        self.mvvm_back_bind_remove_btns()

    def get_field(self):
        self.field.clear()
        for i in range(self.rows):
            self.field.append([])
            for j in range(self.columns):
                self.field[i].append(tk.Button(
                    self.master,
                    height=1,
                    width=3,
                    bg="White",
                    command=(lambda x=i, y=j: self.change_color_clicked(x, y))
                ))
                self.field[i][j].grid(row=i + 2, column=j + 1)

    def delete_field(self):
        for i in range(self.rows):
            for j in range(self.columns):
                self.field[i][j].destroy()

    def bind_events(self):
        self.next_step_btn.bind('<Button-1>', self.next_btn_clicked)

        self.add_column_btn.bind('<Button-1>', lambda e: self.add_clicked(e, 'column'))
        self.add_row_btn.bind('<Button-1>', lambda e: self.add_clicked(e, 'row'))

        self.remove_column_btn.bind('<Button-1>', lambda e: self.remove_clicked(e, 'column'))
        self.remove_row_btn.bind('<Button-1>', lambda e: self.remove_clicked(e, 'row'))

    def mvvm_bind(self):
        self.view_model.set_current_color_field(self.field)

    def mvvm_back_bind_next_btn(self):
        self.field = self.view_model.get_next_color_field()
        self.next_step_btn.config(state=self.view_model.get_next_step_btn_state())

    def mvvm_back_bind_remove_btns(self):
        self.rows = self.view_model.get_number_of_rows()
        self.columns = self.view_model.get_number_of_columns()
        self.get_field()
        self.remove_row_btn.config(state=self.view_model.get_remove_row_btn_state(self.rows))
        self.remove_column_btn.config(state=self.view_model.get_remove_column_btn_state(self.columns))

    def next_btn_clicked(self, event):
        self.mvvm_bind()
        self.view_model.compute_next_step()
        self.mvvm_back_bind_next_btn()

    def change_color_clicked(self, i, j):
        self.mvvm_bind()
        self.view_model.color_changed(i, j)
        self.mvvm_back_bind_next_btn()

    def add_clicked(self, event, new):
        self.delete_field()
        self.view_model.clicked_add(new)
        self.mvvm_back_bind_remove_btns()

    def remove_clicked(self, event, new):
        self.delete_field()
        self.view_model.clicked_remove(new)
        self.mvvm_back_bind_remove_btns()
