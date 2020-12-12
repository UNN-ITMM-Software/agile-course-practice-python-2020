from tkinter import ttk
import tkinter as tk

from lines_intersect.viewmodel.viewmodel import LinesIntersectViewModel


class GUIView(tk.Frame):
    default_sticky = tk.W + tk.E + tk.N + tk.S
    view_model = LinesIntersectViewModel()
    VALID_COORD = r"([-]?\d+[\.]?\d* [-]?\d+[\.]?\d*)"

    def __init__(self):
        tk.Frame.__init__(self, background="bisque")
        self.master.geometry("460x115")
        self.master.title("GUI")

        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=self.default_sticky)

        self.btn_run = tk.Button(self, text='Calculate')
        self.btn_run.grid(row=0, column=4, pady = 5, sticky=self.default_sticky)

        self.text1 = ttk.Label(self, background="bisque", text=' x1: ')
        self.text1.grid(row=0, column=0, sticky=self.default_sticky)
        self.text2 = ttk.Label(self, background="bisque", text=' x2:')
        self.text2.grid(row=0, column=2, sticky=self.default_sticky)

        self.text3 = ttk.Label(self, background="bisque", text=' y1: ')
        self.text3.grid(row=1, column=0, sticky=self.default_sticky)
        self.text4 = ttk.Label(self, background="bisque", text=' y2:')
        self.text4.grid(row=1, column=2, sticky=self.default_sticky)

        self.x1 = ttk.Entry(self)
        self.x1.insert(0, "0 -0.1")
        self.x1.grid(row=0, column=1, pady=10, sticky=self.default_sticky)
        self.x2 = ttk.Entry(self)
        self.x2.insert(0, "1 0")
        self.x2.grid(row=0, column=3, pady=10, sticky=self.default_sticky, padx = 10)

        self.y1 = ttk.Entry(self)
        self.y1.insert(0, "0 0")
        self.y1.grid(row=1, column=1, sticky=self.default_sticky)
        self.y2 = ttk.Entry(self)
        self.y2.insert(0, "1. 1")
        self.y2.grid(row=1, column=3, sticky=self.default_sticky, padx = 10)

        self.res = ttk.Entry(self)
        self.res.grid(row=1, column=4, sticky=self.default_sticky)
        self.res.insert(0, "wait result")

    def bind_events(self):
        pass

    def mvvm_bind(self):
        pass

    def mvvm_back_bind(self):
        pass
