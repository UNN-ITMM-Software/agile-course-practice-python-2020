from tkinter import ttk
import tkinter as tk

from lines_intersect.viewmodel.viewmodel import LinesIntersectViewModel


class GUIView(tk.Frame):
    default_sticky = tk.W + tk.E + tk.N + tk.S
    view_model = LinesIntersectViewModel()

    def __init__(self):
        tk.Frame.__init__(self, background="bisque")
        self.master.geometry("460x90")
        self.master.title("GUI")

        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=self.default_sticky)

        self.btn_calculate = tk.Button(self, text='Calculate')
        self.btn_calculate.grid(row=0, column=4, pady=5, sticky=self.default_sticky)

        self.text1 = ttk.Label(self, background="bisque", text=' a: ')
        self.text1.grid(row=0, column=0, sticky=self.default_sticky)
        self.text2 = ttk.Label(self, background="bisque", text=' b:')
        self.text2.grid(row=0, column=2, sticky=self.default_sticky)

        self.text3 = ttk.Label(self, background="bisque", text=' c: ')
        self.text3.grid(row=1, column=0, sticky=self.default_sticky)
        self.text4 = ttk.Label(self, background="bisque", text=' d:')
        self.text4.grid(row=1, column=2, sticky=self.default_sticky)

        self.point1 = ttk.Entry(self)
        self.point1.insert(0, "0 -0.1")
        self.point1.grid(row=0, column=1, pady=10, sticky=self.default_sticky)
        self.point2 = ttk.Entry(self)
        self.point2.insert(0, "1 0")
        self.point2.grid(row=0, column=3, pady=10, sticky=self.default_sticky, padx=10)

        self.point3 = ttk.Entry(self)
        self.point3.insert(0, "0 0")
        self.point3.grid(row=1, column=1, sticky=self.default_sticky)
        self.point4 = ttk.Entry(self)
        self.point4.insert(0, "1. 1")
        self.point4.grid(row=1, column=3, sticky=self.default_sticky, padx=10)

        self.res = ttk.Label(self, width=20, background="white")
        self.res.grid(row=1, column=4, sticky=self.default_sticky)

        self.bind_events()
        self.mvvm_bind()
        self.mvvm_back_bind()

    def bind_events(self):
        self.point1.bind('<KeyRelease>', self.entry_changed)
        self.point2.bind('<KeyRelease>', self.entry_changed)
        self.point3.bind('<KeyRelease>', self.entry_changed)
        self.point4.bind('<KeyRelease>', self.entry_changed)
        self.btn_calculate.bind('<Button-1>', self.calculate_clicked)

    def mvvm_bind(self):
        self.view_model.set_point1(self.point1.get())
        self.view_model.set_point2(self.point2.get())
        self.view_model.set_point3(self.point3.get())
        self.view_model.set_point4(self.point4.get())

    def mvvm_back_bind(self):
        self.point1.delete(0, tk.END)
        self.point1.insert(0, self.view_model.get_point1())

        self.point2.delete(0, tk.END)
        self.point2.insert(0, self.view_model.get_point2())

        self.point3.delete(0, tk.END)
        self.point3.insert(0, self.view_model.get_point3())

        self.point4.delete(0, tk.END)
        self.point4.insert(0, self.view_model.get_point4())

        self.btn_calculate.config(state=self.view_model.get_button_calculate_state())

        self.res.config(text=self.view_model.get_result())

    def calculate_clicked(self, event):
        self.mvvm_bind()
        self.view_model.click_calculate()
        self.mvvm_back_bind()

    def entry_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()
