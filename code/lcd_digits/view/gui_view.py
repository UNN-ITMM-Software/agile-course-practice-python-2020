import tkinter
from tkinter import ttk

from lcd_digits.view_model import view_model


class LcdDigitGUIView(ttk.Frame):
    default_sticky = tkinter.W + tkinter.E + tkinter.N + tkinter.S
    view_model = view_model.LcdDigitViewModel()

    def set_weight_to_grid(self):
        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=1)

    def bind_events(self):
        self.btn_convert.bind('<Button-1>', self.convert_clicked)
        self.txt_digits.bind('<KeyRelease>', self.txt_digits_changed)

    def mvvm_bind(self):
        self.view_model.set_digits(
            self.txt_digits.get("1.0", tkinter.END))

    def mvvm_back_bind(self):
        self.txt_digits.delete(1.0, tkinter.END)
        self.txt_digits.insert(
            tkinter.END, self.view_model.get_digits())

        self.btn_convert.config(state=self.view_model.get_button_convert_state())
        self.lbl_result.config(text='%s\n' % (self.view_model.get_msg_text()))

    def __init__(self):
        ttk.Frame.__init__(self)
        self.master.title("LCD digits")

        ttk.Frame.rowconfigure(self, 0, weight=1)
        ttk.Frame.columnconfigure(self, 0, weight=1)

        self.grid(sticky=self.default_sticky)

        self.btn_convert = ttk.Button(self, text='Get LCD digits')
        self.btn_convert.grid(row=0, column=1, rowspan=2,
                              sticky=self.default_sticky)
        self.txt_digits = tkinter.Text(self, height=1, relief="groove")
        self.txt_digits.grid(row=0, column=0, sticky=self.default_sticky)

        self.lbl_result = ttk.Label(self, text="Here will be your result", relief="groove")
        self.lbl_result.grid(row=1, column=0, sticky=self.default_sticky)

        ttk.Style().configure("TLabel", font='Consolas 12', wraplength=1000)

        self.bind_events()
        self.set_weight_to_grid()
        self.mvvm_back_bind()

    def convert_clicked(self, event):
        self.mvvm_bind()
        self.view_model.click_convert()
        self.mvvm_back_bind()

    def txt_digits_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()
