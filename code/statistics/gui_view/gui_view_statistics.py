import tkinter

from tkinter import ttk
from statistics.viewmodel import viewmodel


class GuiView(ttk.Frame):
    default_sticky = tkinter.W + tkinter.E + tkinter.N + tkinter.S
    viewmodel = viewmodel.StatisticsViewModel()

    def __init__(self):
        ttk.Frame.__init__(self)
        self.master.title("Stat")
        self.grid(sticky=tkinter.W + tkinter.E + tkinter.N + tkinter.S)

        self.label1 = ttk.Label(self, text="Students:")
        self.label1.grid(row=0, column=0, sticky=self.default_sticky)

        self.label2 = ttk.Label(self, text="Masrks:")
        self.label2.grid(row=0, column=1, sticky=self.default_sticky)

        self.stud1_label = ttk.Label(self, text="Stud 1")
        self.stud1_label.grid(row=1, column=0, sticky=self.default_sticky)

        self.stud1_txt = tkinter.Text(self, height=1, width=15)
        self.stud1_txt.grid(row=1, column=1, sticky=self.default_sticky)

        self.stud2_label = ttk.Label(self, text="Stud 2")
        self.stud2_label.grid(row=2, column=0, sticky=self.default_sticky)

        self.stud2_txt = tkinter.Text(self, height=1, width=15)
        self.stud2_txt.grid(row=2, column=1, sticky=self.default_sticky)
        self.stud2_txt.configure(state="disabled")
        self.stud2_entry = tkinter.Entry(self, textvariable="dis", state="disabled")
        self.stud2_entry.grid(row=2, column=1, sticky=self.default_sticky)

        self.stud3_label = ttk.Label(self, text="Stud 3")
        self.stud3_label.grid(row=3, column=0, sticky=self.default_sticky)

        self.stud3_txt = tkinter.Text(self, height=1, width=15)
        self.stud3_txt.grid(row=3, column=1, sticky=self.default_sticky)
        self.stud3_txt.configure(state="disabled")
        self.stud3_entry = tkinter.Entry(self, textvariable="dis", state="disabled")
        self.stud3_entry.grid(row=3, column=1, sticky=self.default_sticky)

        self.answ_label = ttk.Label(self, text="Answer: ")
        self.answ_label.grid(row=4, column=0, sticky=self.default_sticky)

        self.result_label = ttk.Label(self, text="")
        self.result_label.grid(row=4, column=1, sticky=self.default_sticky)

        self.add_button = ttk.Button(self, text="Add student")
        self.add_button.grid(row=5, column=0, sticky=self.default_sticky)

        self.calc_button = ttk.Button(self, text="Calc")
        self.calc_button.grid(row=5, column=1, sticky=self.default_sticky)

        self.bind_events()
        self.mvvm_back_bind()

    def mvvm_bind(self):
        self.viewmodel.set_instr(self.stud1_txt.get("1.0", tkinter.END).strip())

    def mvvm_back_bind(self):
        self.stud1_txt.delete(1.0, tkinter.END)
        self.stud1_txt.insert(tkinter.END, self.viewmodel.get_instr())
        self.result_label.config(text=self.viewmodel.get_answer())
        self.calc_button.config(state=self.viewmodel.get_button_convert_state())

    def button_clicked(self, event):
        self.mvvm_bind()
        self.viewmodel.click_button()
        self.mvvm_back_bind()

    def instr_txt_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def bind_events(self):
        self.calc_button.bind('<Button-1>', self.button_clicked)
        self.add_button.bind('<Button-1>', self.button_clicked)
        self.stud1_txt.bind('<Motion>', self.instr_txt_changed)
