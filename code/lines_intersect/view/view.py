from tkinter import ttk
import tkinter as tk

from lines_intersect.viewmodel.viewmodel import LinesIntersectViewModel


class GUIView(tk.Frame):
    default_sticky = tk.W + tk.E + tk.N + tk.S
    view_model = LinesIntersectViewModel()

    def __init__(self):
        tk.Frame.__init__(self, background="bisque")

        self.master.geometry("340x150")
        self.master.title("GUI")

        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=self.default_sticky)

        self.btn_run = tk.Button(self, text='Calculate', pady=30, padx = 20)
        self.btn_run.grid(row=0, column=2, rowspan=3, sticky=self.default_sticky)

        self.text1 = ttk.Label(self, background="bisque", text='line segment1  ')
        self.text1.grid(row=0, column=0, sticky=self.default_sticky)

        self.text2 = ttk.Label(self, background="bisque", text='line segment2  ')
        self.text2.grid(row=2, column=0, sticky=self.default_sticky)

        self.line1 = ttk.Entry(self)
        self.line1.grid(row=0, column=1, sticky=self.default_sticky, padx = 10)

        self.line2 = ttk.Entry(self)
        self.line2.grid(row=2, column=1, sticky=self.default_sticky, padx = 10)
