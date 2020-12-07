import tkinter
from tkinter import ttk


class GUIView(ttk.Frame):
    VALID_OPERATIONS = ['+', '-', '*', '/']
    N_LOG_MESSAGES_TO_DISPLAY = 15
    default_sticky = tkinter.W + tkinter.E + tkinter.N + tkinter.S

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
        self.btn_calculate.bind('<Button-1>', self.calculate_clicked)
        self.txt_first_frac.bind('<KeyRelease>', self.first_frac_txt_changed)
        self.txt_second_frac.bind('<KeyRelease>', self.second_frac_txt_changed)
        self.cmb_operation.bind('<<ComboboxSelected>>', self.operation_changed)

    def mvvm_bind(self):
        pass

    def mvvm_back_bind(self):
        pass

    def __init__(self):
        ttk.Frame.__init__(self)
        self.master.title("Fraction calculator")

        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=5)
        self.grid(sticky=tkinter.W + tkinter.E + tkinter.N + tkinter.S)

        self.txt_first_frac = tkinter.Text(self, height=1, width=10, borderwidth=2, relief="groove")
        self.txt_first_frac.grid(row=0, column=0, sticky=self.default_sticky)

        self.cmb_operation = ttk.Combobox(self, height=1, width=5, values=self.VALID_OPERATIONS)
        self.cmb_operation.current(0)
        self.cmb_operation.grid(row=0, column=1, sticky=self.default_sticky)

        self.txt_second_frac = tkinter.Text(self, height=1, width=10, borderwidth=2, relief="groove")
        self.txt_second_frac.grid(row=0, column=2, sticky=self.default_sticky)

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
        self.mvvm_back_bind()

    def first_frac_txt_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def second_frac_txt_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def operation_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()


GUIView().mainloop()
