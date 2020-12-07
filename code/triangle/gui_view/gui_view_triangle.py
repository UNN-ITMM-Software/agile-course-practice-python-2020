import re
import tkinter as Tk

from triangle.viewmodel import viewmodel
from tkinter import ttk


class GuiView(ttk.Frame):
    default_sticky = Tk.W + Tk.E + Tk.N + Tk.S
    VALID_OPERATIONS = ["get ab", "get bc", "get ca",
                        "get area", "get perimeter",
                        "get circumcircle", "get incircle",
                        "get side type", "get angle type"]
    viewmodel = viewmodel.TriangleViewModel()

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

        self.bind_events()
        self.mvvm_back_bind()

    def mvvm_bind(self):
        p = re.compile('\d?.?\d*\n')
        if (p.match(self.x1.get("1.0", Tk.END)) and p.match(self.y1.get("1.0", Tk.END)) and
                p.match(self.x2.get("1.0", Tk.END)) and p.match(self.y2.get("1.0", Tk.END)) and
                p.match(self.x3.get("1.0", Tk.END)) and p.match(self.y3.get("1.0", Tk.END))):
            self.viewmodel.set_vertices([self.x1.get("1.0", Tk.END).strip(),
                                         self.y1.get("1.0", Tk.END).strip(),
                                         self.x2.get("1.0", Tk.END).strip(),
                                         self.y2.get("1.0", Tk.END).strip(),
                                         self.x3.get("1.0", Tk.END).strip(),
                                         self.y3.get("1.0", Tk.END).strip()])
        self.viewmodel.set_operation(
            self.VALID_OPERATIONS[self.cmb_operation.current()])

    def bind_events(self):
        self.do_button.bind('<Button-1>', self.button_clicked)
        self.x1.bind('<KeyRelease>', self.x1_txt_changed)
        self.y1.bind('<KeyRelease>', self.y1_txt_changed)
        self.x2.bind('<KeyRelease>', self.x2_txt_changed)
        self.y2.bind('<KeyRelease>', self.y2_txt_changed)
        self.x3.bind('<KeyRelease>', self.x3_txt_changed)
        self.y3.bind('<KeyRelease>', self.y3_txt_changed)
        self.cmb_operation.bind('<<ComboboxSelected>>', self.operation_changed)

    def button_clicked(self, event):
        self.mvvm_bind()
        self.viewmodel.click_button()
        self.mvvm_back_bind()

    def x1_txt_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def y1_txt_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def x2_txt_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def y2_txt_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def x3_txt_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def y3_txt_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def operation_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def mvvm_back_bind(self):
        if (len(self.viewmodel.get_vertices()) == 6):
            self.x1.delete(1.0, Tk.END)
            self.x1.insert(Tk.END, self.viewmodel.get_vertices()[0])
            self.y1.delete(1.0, Tk.END)
            self.y1.insert(Tk.END, self.viewmodel.get_vertices()[1])
            self.x2.delete(1.0, Tk.END)
            self.x2.insert(Tk.END, self.viewmodel.get_vertices()[2])
            self.y2.delete(1.0, Tk.END)
            self.y2.insert(Tk.END, self.viewmodel.get_vertices()[3])
            self.x3.delete(1.0, Tk.END)
            self.x3.insert(Tk.END, self.viewmodel.get_vertices()[4])
            self.y3.delete(1.0, Tk.END)
            self.y3.insert(Tk.END, self.viewmodel.get_vertices()[5])
        self.do_button.config(state=self.viewmodel.get_button_convert_state())
        self.result_label.config(text=self.viewmodel.get_answer())
