import tkinter as Tk

from triangle.viewmodel import viewmodel
from tkinter import ttk


class GuiView(ttk.Frame):
    default_sticky = Tk.W + Tk.E + Tk.N + Tk.S
    VALID_OPERATIONS = ["det ab", "get bc", "get ca",
                        "get area", "get perimeter",
                        "get circumcircle", "get incircle",
                        "get side type", "get angle type"]

    def __init__(self):
        ttk.Frame.__init__(self)
        self.master.title("Triangle calculator")
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=6)
        self.grid(sticky=Tk.W + Tk.E + Tk.N + Tk.S)

        self.vertices_lable = ttk.Label(self, text="Set vertices: ")
        self.vertices_lable.grid(row=0, column=0, sticky=self.default_sticky)

        self.x1 = Tk.Text(self, height=1, width=15)
        self.x1.grid(row=0, column=1, sticky=self.default_sticky)
        self.y1 = Tk.Text(self, height=1, width=15)
        self.y1.grid(row=0, column=2, sticky=self.default_sticky)

        self.x2 = Tk.Text(self, height=1, width=15)
        self.x2.grid(row=1, column=1, sticky=self.default_sticky)
        self.y2 = Tk.Text(self, height=1, width=15)
        self.y2.grid(row=1, column=2, sticky=self.default_sticky)

        self.x3 = Tk.Text(self, height=1, width=15)
        self.x3.grid(row=2, column=1, sticky=self.default_sticky)
        self.y3 = Tk.Text(self, height=1, width=15)
        self.y3.grid(row=2, column=2, sticky=self.default_sticky)

        self.cmb_operation = ttk.Combobox(self, height=1, width=15, values=self.VALID_OPERATIONS)
        self.cmb_operation.current(0)
        self.cmb_operation.grid(row=3, column=1, sticky=self.default_sticky)
        self.do_button = ttk.Button(self, text="DO IT!")
        self.do_button.grid(row=3, column=2, sticky=self.default_sticky)

        self.separator = ttk.Label(self, text=" ")
        self.separator.grid(row=4, column=0, sticky=self.default_sticky)

        self.a_label = ttk.Label(self, text="ANSWER: ")
        self.a_label.grid(row=5, column=0, sticky=self.default_sticky)
        self.result_label = ttk.Label(self, text="")
        self.result_label.grid(row=5, column=1, sticky=self.default_sticky)
