import tkinter

from tkinter import ttk
from string_calculator.viewmodel import viewmodel


class GuiView(ttk.Frame):
    default_sticky = tkinter.W + tkinter.E + tkinter.N + tkinter.S
    viewmodel = viewmodel.StrCalculatorViewModel()

    def __init__(self):
        ttk.Frame.__init__(self)
        self.master.title("String calculator")
        self.grid(sticky=tkinter.W + tkinter.E + tkinter.N + tkinter.S)

        self.instr_label = ttk.Label(self, text="Input string:")
        self.instr_label.grid(row=0, column=0, sticky=self.default_sticky)

        self.instr_txt = tkinter.Text(self, height=3, width=15)
        self.instr_txt.grid(row=0, column=1, sticky=self.default_sticky)

        self.add_button = ttk.Button(self, text="Add")
        self.add_button.grid(row=0, column=2, sticky=self.default_sticky)

        self.answ_label = ttk.Label(self, text="Answer: ")
        self.answ_label.grid(row=1, column=0, sticky=self.default_sticky)

        self.result_label = ttk.Label(self, text="")
        self.result_label.grid(row=1, column=1, sticky=self.default_sticky)

        self.bind_events()
        self.mvvm_back_bind()  # To disable the button immediately after starting the GUI

    def mvvm_bind(self):
        self.viewmodel.set_instr(self.instr_txt.get("1.0", tkinter.END).strip())

    def mvvm_back_bind(self):
        self.instr_txt.delete(1.0, tkinter.END)
        self.instr_txt.insert(tkinter.END, self.viewmodel.get_instr())
        self.result_label.config(text=self.viewmodel.get_answer())
        self.add_button.config(state=self.viewmodel.get_button_convert_state())

    def button_clicked(self, event):
        self.mvvm_bind()
        self.viewmodel.click_button()
        self.mvvm_back_bind()

    def instr_txt_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def bind_events(self):
        self.add_button.bind('<Button-1>', self.button_clicked)
        self.instr_txt.bind('<Motion>', self.instr_txt_changed)
