import tkinter as Tk

from big_integer.viewmodel import viewmodel
from big_integer.viewmodel.viewmodel import Operation
from big_integer.viewmodel.viewmodel import CalculateState
from tkinter import ttk, messagebox


class GuiView(ttk.Frame):
    default_sticky = Tk.W + Tk.E + Tk.N + Tk.S
    OPERATIONS = ["addition", "subtraction", "multiplication"]
    viewmodel = viewmodel.BigIntegerViewModel()

    def __init__(self):
        ttk.Frame.__init__(self)
        self.master.title("BigInteger calculator")
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=6)
        self.grid(sticky=Tk.W + Tk.E + Tk.N + Tk.S)

        self.ab_prompt = ttk.Label(self, text="Set a, b: ")
        self.ab_prompt.grid(row=0, column=0, sticky=self.default_sticky)

        self.a = Tk.Text(self, height=1, width=10)
        self.a.grid(row=0, column=1, sticky=self.default_sticky)
        self.a.bind('<KeyRelease>', self.a_changed)

        self.b = Tk.Text(self, height=1, width=10)
        self.b.grid(row=0, column=2, sticky=self.default_sticky)
        self.b.bind('<KeyRelease>', self.b_changed)

        self.operation = ttk.Combobox(self, height=1, width=15, values=self.OPERATIONS)
        self.operation.current(0)
        self.operation.grid(row=3, column=1, sticky=self.default_sticky)
        self.operation.bind('<<ComboboxSelected>>', self.operation_changed)

        self.calculate = ttk.Button(self, text="Calculate")
        self.calculate.grid(row=3, column=2, sticky=self.default_sticky)
        self.calculate.bind('<Button-1>', self.calculate_clicked)

        self.separator = ttk.Label(self, text=" ")
        self.separator.grid(row=4, column=0, sticky=self.default_sticky)

        self.result_prompt = ttk.Label(self, text="Result: ")
        self.result_prompt.grid(row=5, column=0, sticky=self.default_sticky)
        self.result = ttk.Label(self, text="")
        self.result.grid(row=5, column=1, sticky=self.default_sticky)

        self.mvvm_back_bind()

    def calculate_clicked(self, event):
        if self.calculate.state()[0] == 'active':
            self.mvvm_bind()
            self.viewmodel.calculate()
            self.mvvm_back_bind()

    def a_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def b_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def operation_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def mvvm_back_bind(self):
        self.a.delete(1.0, Tk.END)
        self.b.delete(1.0, Tk.END)
        self.a.insert(Tk.END, self.viewmodel.get_a())
        self.b.insert(Tk.END, self.viewmodel.get_b())
        if self.viewmodel.get_calculate_state() == CalculateState.DISABLE:
            self.calculate.config(state="disabled")
        elif self.viewmodel.get_calculate_state() == CalculateState.ENABLE:
            self.calculate.config(state="normal")
        self.result.config(text=self.viewmodel.get_result())

    def mvvm_bind(self):
        self.viewmodel.set_a(self.a.get("1.0", Tk.END).strip())
        self.viewmodel.set_b(self.b.get("1.0", Tk.END).strip())
        if self.operation.get() == "addition":
            self.viewmodel.set_operation(Operation.ADDITIONAL)
        if self.operation.get() == "subtraction":
            self.viewmodel.set_operation(Operation.SUBTRACTION)
        if self.operation.get() == "multiplication":
            self.viewmodel.set_operation(Operation.MULTIPLICATION)
