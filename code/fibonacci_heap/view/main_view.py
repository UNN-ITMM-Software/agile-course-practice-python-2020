import tkinter
from tkinter import ttk

from fibonacci_heap.viewmodel.main_viewmodel import HeapViewModel, NodeOperations


class GUIView(ttk.Frame):
    VALID_OPERATIONS = list(NodeOperations)
    default_sticky = tkinter.W + tkinter.E + tkinter.N + tkinter.S

    view_model = HeapViewModel()

    def set_weight_to_grid(self):
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=5)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(2, weight=5)
        self.columnconfigure(3, weight=1)

    def bind_events(self):
        self.btn_run.bind('<Button-1>', self.button_run_clicked)
        self.entry_key.bind('<KeyRelease>', self.entry_changed)
        self.entry_value.bind('<KeyRelease>', self.entry_changed)
        self.cmb_operation.bind('<<ComboboxSelected>>', self.operation_changed)

    def mvvm_bind(self):
        self.view_model.set_key(self.entry_key.get())
        self.view_model.set_value(self.entry_value.get())
        self.view_model.set_operation(self.VALID_OPERATIONS[self.cmb_operation.current()])

    def mvvm_back_bind(self):
        self.entry_key.delete(0, tkinter.END)
        self.entry_key.insert(0, self.view_model.key)

        self.entry_value.delete(0, tkinter.END)
        self.entry_value.insert(0, self.view_model.value)

        self.btn_run.config(state=self.view_model.get_main_button_state())
        self.entry_value.config(state=self.view_model.get_value_textbox_state())

        self.lbl_result.config(text=self.view_model.get_message_text())

    def __init__(self):
        ttk.Frame.__init__(self)
        self.master.title('Fibonacci Heap Creator')

        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=5)
        self.grid(sticky=self.default_sticky)

        self.btn_run = ttk.Button(self, text='Let\'s do')
        self.btn_run.grid(row=0, column=3, rowspan=2, sticky=self.default_sticky)

        tkinter.Label(self, text='SELECT OPERATION', fg='grey').grid(row=0, column=0)
        supported_operations = [member.value for member in self.VALID_OPERATIONS]
        self.cmb_operation = ttk.Combobox(self, height=5, width=15,
                                          state='readonly',
                                          values=supported_operations)
        self.cmb_operation.current(0)
        self.cmb_operation.grid(row=1, column=0, sticky=self.default_sticky)

        tkinter.Label(self, text='KEY', fg='grey').grid(row=0, column=1)
        self.entry_key = tkinter.Entry(self, width=10)
        self.entry_key.grid(row=1, column=1, sticky=self.default_sticky)

        tkinter.Label(self, text='VALUE', fg='grey').grid(row=0, column=2)
        self.entry_value = tkinter.Entry(self, width=10)
        self.entry_value.grid(row=1, column=2, sticky=self.default_sticky)

        self.lbl_result = ttk.Label(self, text='Done operations:')
        self.lbl_result.grid(row=2, column=0, columnspan=4, sticky=tkinter.W + tkinter.N)

        self.bind_events()
        self.set_weight_to_grid()

        self.mvvm_back_bind()

    def button_run_clicked(self, event):
        self.mvvm_bind()
        self.view_model.click_run_button()
        self.mvvm_back_bind()

    def entry_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def operation_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()


if __name__ == '__main__':
    root = ttk.Frame()
    GUIView().pack(side='top', fill='both', expand=True)
    root.mainloop()
