import tkinter as tk
from tkinter import ttk

from bit_array.viewmodel.operation import Operation
from bit_array.viewmodel.viewmodel import BitArrayViewModel


class GUIView(ttk.Frame):
    view_model = BitArrayViewModel()

    def __init__(self):
        ttk.Frame.__init__(self)
        self.master.title("Bit array")

        self.left_bit_array_label = ttk.Label(text="Left bit array", font="Arial 16")
        self.left_bit_array_label.grid(row=0, column=0)
        self.left_bit_array_entry = ttk.Entry()
        self.left_bit_array_entry.grid(row=0, column=1)
        self.operation_combobox = ttk.Combobox(values=Operation.ALL,
                                               state="readonly",
                                               width="6")
        self.operation_combobox.grid(row=0, column=2)
        self.right_bit_array_label = ttk.Label(text="Right bit array", font="Arial 16")
        self.right_bit_array_label.grid(row=0, column=3)
        self.right_bit_array_entry = ttk.Entry()
        self.right_bit_array_entry.grid(row=0, column=4)
        self.calc_button = ttk.Button(text="Calculate")
        self.calc_button.grid(row=1, column=0)
        self.result_entry = ttk.Label()
        self.result_entry.grid(row=1, column=1)

        self.bind_events()

    def bind_events(self):
        self.left_bit_array_entry.bind('<KeyRelease>', self.entry_changed)
        self.operation_combobox.bind('<<ComboboxSelected>>', self.operation_changed)

    def entry_changed(self, event):
        self.result_entry.text = None

    def operation_changed(self, event):
        operation = self.operation_combobox.get()
        self.view_model.set_operation(operation)
        if self.view_model.get_left_bit_array_enabled():
            self.left_bit_array_entry.configure(state=tk.NORMAL)
        else:
            self.left_bit_array_entry.configure(state=tk.DISABLED)
        print(self.view_model.get_left_bit_array_enabled())
        self.update()
