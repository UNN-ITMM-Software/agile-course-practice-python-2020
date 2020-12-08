import tkinter
from tkinter import ttk

import sys
sys.path.append("../../")
from rational_number.viewmodel.rational_number_viewmodel import RationalNumberViewModel

class GUIView(ttk.Frame):
    default_sticky = tkinter.W + tkinter.E + tkinter.N + tkinter.S

    viewmodel = RationalNumberViewModel()

    def set_weight_to_grid(self):
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)

    def bind_events(self):
        self.txt_first_number.bind('<KeyRelease>', self.txt_first_number_changed)
        self.txt_second_number.bind('<KeyRelease>', self.txt_second_number_changed)
        self.cmb_operation.bind('<<ComboboxSelected>>', self.operation_changed)
        self.btn_calculate.bind('<Button-1>', self.calculate_clicked)

    def mvvm_bind(self):
        self.viewmodel.set_first_number(self.txt_first_number.get("1.0", tkinter.END))
        self.viewmodel.set_second_number(self.txt_second_number.get("1.0", tkinter.END))
        self.viewmodel.set_operation(self.cmb_operation.get())

    def mvvm_back_bind(self):
        self.btn_calculate.config(state=self.viewmodel.get_calculate_button_state())
        self.lbl_message.config(text=self.viewmodel.get_info_message())
        self.lbl_result.config(text=self.viewmodel.get_result())

    def __init__(self):
        ttk.Frame.__init__(self)
        self.master.title("Rational number calculator")

        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=5)
        self.grid(sticky=self.default_sticky)

        self.txt_first_number = tkinter.Text(self, height=1, width=10, borderwidth=2, relief="groove")
        self.txt_first_number.grid(row=0, column=0, sticky=self.default_sticky)

        self.cmb_operation = ttk.Combobox(self, height=1, width=5, values=RationalNumberViewModel.VALID_OPERATIONS,
                                          state="readonly")
        self.cmb_operation.current(0)
        self.cmb_operation.grid(row=0, column=1, sticky=self.default_sticky)

        self.txt_second_number = tkinter.Text(self, height=1, width=10, borderwidth=2, relief="groove")
        self.txt_second_number.grid(row=0, column=2, sticky=self.default_sticky)

        self.lbl_equal_to = tkinter.Label(self, text="=", height=1, width=5, borderwidth=2, relief="groove")
        self.lbl_equal_to.grid(row=0, column=3, sticky=self.default_sticky)

        self.lbl_result = tkinter.Label(self, text="", height=1, width=10, borderwidth=2, relief="groove")
        self.lbl_result.grid(row=0, column=4, sticky=self.default_sticky)

        self.btn_calculate = ttk.Button(self, text='Calculate')
        self.btn_calculate.grid(row=1, column=1, columnspan=3, sticky=self.default_sticky)

        self.lbl_message = ttk.Label(self, text="Info box")
        self.lbl_message.grid(row=2, column=0, columnspan=5, sticky=tkinter.W + tkinter.N)

        self.bind_events()
        self.set_weight_to_grid()

        self.mvvm_back_bind()

    def calculate_clicked(self, event):
        self.mvvm_bind()
        self.viewmodel.calculate()
        self.mvvm_back_bind()

    def txt_first_number_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def txt_second_number_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def operation_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()


GUIView().mainloop()
