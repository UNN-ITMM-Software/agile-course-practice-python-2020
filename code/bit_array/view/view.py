import tkinter as tk
from tkinter import ttk

from bit_array.viewmodel.operation import Operation
from bit_array.viewmodel.viewmodel import BitArrayViewModel


class GUIView(ttk.Frame):
    view_model = BitArrayViewModel()

    def __init__(self):
        self.view_model.set_operation(Operation.OR)
        ttk.Frame.__init__(self)
        self.master.title("Bit array")

        self.left_bit_array_label = ttk.Label(text="Left bit array", font="Arial 16")
        self.left_bit_array_label.grid(row=0, column=0)

        self.left_bit_array_entry = ttk.Entry()
        self.left_bit_array_entry.grid(row=1, column=0)

        self.operation_combobox = ttk.Combobox(values=Operation.ALL,
                                               state="readonly",
                                               width="6")
        self.operation_combobox.grid(row=1, column=1)

        self.right_bit_array_label = ttk.Label(text="Right bit array", font="Arial 16")
        self.right_bit_array_label.grid(row=0, column=2)

        self.right_bit_array_entry = ttk.Entry()
        self.right_bit_array_entry.grid(row=1, column=2)

        self.calc_button = ttk.Button(text="Calculate")
        self.calc_button.grid(row=2, column=0)

        self.result_entry = ttk.Label()
        self.result_entry.grid(row=2, column=1)

        self.bind_events()
        self.mvvm_bind()

    def bind_events(self):
        self.left_bit_array_entry.bind('<KeyRelease>', self.input_changed)
        self.right_bit_array_entry.bind('<KeyRelease>', self.input_changed)
        self.operation_combobox.bind('<<ComboboxSelected>>', self.input_changed)
        self.calc_button.bind('<Button-1>', self.calculate_clicked)

    def input_changed(self, event):
        try:
            self.mvvm_back_bind()
        except ValueError:
            self.result_entry.configure(text='wrong input')
            return
        self.mvvm_bind()

    def calculate_clicked(self, event):
        try:
            self.mvvm_back_bind()
        except ValueError:
            self.result_entry.configure(text='wrong input')
            return
        self.view_model.calculate()
        self.mvvm_bind()

    def mvvm_bind(self):
        self.operation_combobox.set(self.view_model.get_operation())
        self.left_bit_array_entry.configure(text=self.view_model.get_left_bit_array_string())
        self.right_bit_array_entry.configure(text=self.view_model.get_right_bit_array_string())
        self.result_entry.configure(text=self.view_model.get_result_string())
        if self.view_model.get_left_bit_array_enabled():
            self.left_bit_array_entry.configure(state=tk.NORMAL)
        else:
            self.left_bit_array_entry.configure(state=tk.DISABLED)

    def mvvm_back_bind(self):
        self.view_model.clear_result()
        self.view_model.set_operation(self.operation_combobox.get())
        self.view_model.set_left_bit_array(self.left_bit_array_entry.get())
        self.view_model.set_right_bit_array(self.right_bit_array_entry.get())
