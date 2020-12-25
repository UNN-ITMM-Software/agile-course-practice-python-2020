import tkinter as tk
from tkinter import ttk

from range.viewmodel.operation import Operation
from range.viewmodel.viewmodel import RangeViewModel


class View(ttk.Frame):
    N_LOG_MESSAGES_TO_DISPLAY = 9
    view_model = RangeViewModel()

    def __init__(self):
        self.view_model.set_operation(Operation.CONTAINS)
        ttk.Frame.__init__(self)
        self.master.title("Range")
        self.master.geometry("450x300")

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

        self.lbl_result = tk.Label(text="Here will be result")
        self.lbl_result.grid(row=4, column=0, columnspan=3)

        self.bind_events()
        self.mvvm_bind()

        self.__update_logs()

    def bind_events(self):
        self.operation_combobox.bind('<<ComboboxSelected>>', self.operation_changed)
        self.res_button.bind('<Button-1>', self.result_clicked)

    def operation_changed(self, event):
        self.view_model.set_operation(self.operation_combobox.get())
        self.value_1_entry.configure(state=tk.NORMAL)
        if self.view_model.get_value_2_enabled():
            self.value_2_entry.configure(state=tk.NORMAL)
        else:
            self.value_2_entry.configure(state=tk.DISABLED)
        self.__update_logs()

    def result_clicked(self, event):
        try:
            self.mvvm_back_bind()
        except Exception as exception:
            self.__update_result(exception)
            return

        try:
            self.view_model.make_operation()
        except Exception as exception:
            self.__update_result(exception)
            return

        self.mvvm_bind()

    def mvvm_bind(self):
        self.update_text(self.value_1_entry, self.view_model.get_value_1_string())
        self.operation_combobox.set(self.view_model.get_operation())
        self.update_text(self.value_2_entry, self.view_model.get_value_2_string())
        self.__update_result(self.view_model.get_result_string())
        if self.view_model.get_value_2_enabled():
            self.value_1_entry.configure(state=tk.NORMAL)
        else:
            self.value_1_entry.configure(state=tk.DISABLED)

    def mvvm_back_bind(self):
        self.view_model.clear_result()
        self.view_model.set_operation(self.operation_combobox.get())
        self.view_model.set_value_1(self.value_1_entry.get())
        self.view_model.set_value_2(self.value_2_entry.get())

    @staticmethod
    def update_text(obj, text):
        obj.delete(0, tk.END)
        obj.insert(0, text)

    def __update_logs(self):
        logger_text = \
            '\n'.join(self.view_model.logger.get_log_messages()[:-self.N_LOG_MESSAGES_TO_DISPLAY:-1])
        self.lbl_result.config(text=logger_text)

    def __update_result(self, text):
        self.result_entry.configure(state=tk.NORMAL)
        self.update_text(self.result_entry, text)
        self.result_entry.configure(state=tk.DISABLED)
        self.__update_logs()
