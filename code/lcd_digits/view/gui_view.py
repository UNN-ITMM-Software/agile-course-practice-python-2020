import tkinter
from tkinter import ttk

from lcd_digits.view_model import view_model
from lcd_digits.logger.reallogger import RealLogger


class LcdDigitGUIView(ttk.Frame):
    N_LOG_MESSAGES_TO_DISPLAY = 20
    default_sticky = tkinter.W + tkinter.E + tkinter.N + tkinter.S
    view_model = view_model.LcdDigitViewModel(RealLogger())

    def set_weight_to_grid(self):
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=8)
        self.columnconfigure(1, weight=1)

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

        logger_text = '\n'.join(self.view_model.logger.get_log_messages()[-self.N_LOG_MESSAGES_TO_DISPLAY:])
        self.lbl_result.config(text='%s\n%s' % (self.view_model.get_msg_text(), logger_text))

    def __init__(self):
        super().__init__()
        self.master.title("LCD digits")
        self.master.resizable(width=False, height=True)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=self.default_sticky)

        self.btn_convert = ttk.Button(self, text='Get LCD digits', width=15)
        self.btn_convert.grid(row=0, column=1, rowspan=3,
                              sticky=self.default_sticky)
        self.txt_digits = tkinter.Text(self, height=1)
        self.txt_digits.grid(row=0, column=0, sticky=self.default_sticky)

        self.lbl_result_name = ttk.Label(self, text="Here will be your result and log")
        self.lbl_result_name.grid(row=1, column=0, sticky=self.default_sticky)

        self.lbl_result = ttk.Label(self)
        self.lbl_result.grid(row=2, column=0, sticky=self.default_sticky)

        ttk.Style().configure("TLabel", font='Consolas 12', wraplength=999)

        self.bind_events()
        self.set_weight_to_grid()
        self.mvvm_back_bind()

    def convert_clicked(self, event):
        self.mvvm_bind()
        self.view_model.click_convert(26)
        self.mvvm_back_bind()

    def txt_digits_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()
