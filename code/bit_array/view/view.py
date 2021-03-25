import tkinter as tk
from tkinter import ttk

from bit_array.viewmodel.operation import Operation
from bit_array.viewmodel.viewmodel import BitArrayViewModel


class GUIView(ttk.Frame):
    N_LOG_MESSAGES_TO_DISPLAY = 15

    view_model = BitArrayViewModel()

    def __init__(self):
        self.view_model.set_operation(Operation.OR)
        ttk.Frame.__init__(self)
        self.master.title("Bit array")
        self.master.geometry("460x480")

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
        self.result_entry.grid(row=2, column=1, columnspan=3)

        self.lbl_result = ttk.Label(self.master, text="Here will be your result")
        self.lbl_result.grid(row=3, column=0, columnspan=3, sticky=tk.W + tk.N)

        self.bind_events()
        self.mvvm_bind()

    def bind_events(self):
        self.operation_combobox.bind('<<ComboboxSelected>>', self.operation_changed)
        self.calc_button.bind('<Button-1>', self.calculate_clicked)

    def operation_changed(self, event):
        self.view_model.set_operation(self.operation_combobox.get())
        if self.view_model.get_left_bit_array_enabled():
            self.left_bit_array_entry.configure(state=tk.NORMAL)
        else:
            self.left_bit_array_entry.configure(state=tk.DISABLED)

    def calculate_clicked(self, event):
        try:
            self.mvvm_back_bind()
        except ValueError:
            self.result_entry.configure(text='Wrong input. Expected: word of 0 and 1.')

            logger_text = \
                '\n'.join(self.view_model.logger.get_log_messages()[:-self.N_LOG_MESSAGES_TO_DISPLAY:-1])
            self.lbl_result.config(text=logger_text)
            return

        self.view_model.calculate()
        self.mvvm_bind()

        logger_text = \
            '\n'.join(self.view_model.logger.get_log_messages()[:-self.N_LOG_MESSAGES_TO_DISPLAY:-1])
        self.lbl_result.config(text=logger_text)

    def mvvm_bind(self):
        self.update_text(self.left_bit_array_entry, self.view_model.get_left_bit_array_string())
        self.operation_combobox.set(self.view_model.get_operation())
        self.update_text(self.right_bit_array_entry, self.view_model.get_right_bit_array_string())
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

    @staticmethod
    def update_text(obj, text):
        obj.delete(0, tk.END)
        obj.insert(0, text)
