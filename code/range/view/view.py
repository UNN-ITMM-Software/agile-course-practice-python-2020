import tkinter as tk
from tkinter import ttk

from range.viewmodel.operation import Operation
from range.viewmodel.viewmodel import RangeViewModel

class View(ttk.Frame):
    view_model = RangeViewModel()

    def __init__(self):
        ttk.Frame.__init__(self)
        self.master.title("Range")
        self.master.geometry("450x160")

        self.value_1_label = ttk.Label(text="Range", font="Arial 16")
        self.value_1_label.grid(row=0, column=0)

        self.value_1_entry = ttk.Entry()
        self.value_1_entry.grid(row=0, column=1)

        self.operation_combobox = ttk.Combobox(values=Operation.ALL,
                                               state="readonly",
                                               justify=tk.CENTER,
                                               width="12")
        self.operation_combobox.grid(row=1, column=1, pady=(10, 10))

        self.value_2_label = ttk.Label(text="Value/Set/Range", font="Arial 16")
        self.value_2_label.grid(row=2, column=0, padx=(10, 10))

        self.value_2_entry = ttk.Entry()
        self.value_2_entry.grid(row=2, column=1, pady=(10, 10))

        self.res_button = ttk.Button(text="Result")
        self.res_button.grid(row=3, column=0)

        self.result_entry = ttk.Entry()
        self.result_entry.insert(0, '')
        self.result_entry.configure(state='readonly')
        self.result_entry.grid(row=3, column=1, columnspan=3)
