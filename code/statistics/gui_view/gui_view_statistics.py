import tkinter

from tkinter import ttk
from statistics.viewmodel import viewmodel


class GuiView(ttk.Frame):
    default_sticky = tkinter.W + tkinter.E + tkinter.N + tkinter.S
    viewmodel = viewmodel.StatisticsViewModel()

    def __init__(self):
        ttk.Frame.__init__(self)
        self.master.title("Журнал")
        self.grid(sticky=tkinter.W + tkinter.E + tkinter.N + tkinter.S)

        self.label1 = ttk.Label(self, text="Студенты:")
        self.label1.grid(row=0, column=0, sticky=self.default_sticky)

        self.label2 = ttk.Label(self, text="Оценки:")
        self.label2.grid(row=0, column=1, sticky=self.default_sticky)

        self.stud1_label = ttk.Label(self, text="Студент 1")
        self.stud1_label.grid(row=1, column=0, sticky=self.default_sticky)

        self.stud1_txt = tkinter.Text(self, height=1, width=15)
        self.stud1_txt.grid(row=1, column=1, sticky=self.default_sticky)

        self.stud2_label = ttk.Label(self, text="Студент 2")
        self.stud2_label.grid(row=2, column=0, sticky=self.default_sticky)

        self.stud2_txt = tkinter.Text(self, height=1, width=15)
        self.stud2_txt.grid(row=2, column=1, sticky=self.default_sticky)

        self.stud3_label = ttk.Label(self, text="Студент 3")
        self.stud3_label.grid(row=3, column=0, sticky=self.default_sticky)

        self.stud3_txt = tkinter.Text(self, height=1, width=15)
        self.stud3_txt.grid(row=3, column=1, sticky=self.default_sticky)

        self.calc_button = ttk.Button(self, text="Рассчитать")
        self.calc_button.grid(row=4, column=0, sticky=self.default_sticky)

        self.count_of_losers_label = ttk.Label(self, text="Количество двоечников: ")
        self.count_of_losers_label.grid(row=5, column=0, sticky=self.default_sticky)

        self.result_label1 = ttk.Label(self, text="")
        self.result_label1.grid(row=5, column=1, sticky=self.default_sticky)

        self.count_of_students_who_successfully_pass_label = ttk.Label(self, text="Количество хорошистов: ")
        self.count_of_students_who_successfully_pass_label.grid(row=6, column=0, sticky=self.default_sticky)

        self.result_label2 = ttk.Label(self, text="")
        self.result_label2.grid(row=6, column=1, sticky=self.default_sticky)

        self.count_of_excellent_label = ttk.Label(self, text="Количество отличников: ")
        self.count_of_excellent_label.grid(row=7, column=0, sticky=self.default_sticky)

        self.result_label3 = ttk.Label(self, text="")
        self.result_label3.grid(row=7, column=1, sticky=self.default_sticky)

        self.bind_events()
        self.mvvm_back_bind()

    def mvvm_bind(self):
        self.viewmodel.set_instr(self.stud1_txt.get("1.0", tkinter.END).strip(),
                                 self.stud2_txt.get("1.0", tkinter.END).strip(),
                                 self.stud3_txt.get("1.0", tkinter.END).strip())

    def mvvm_back_bind(self):
        self.stud1_txt.delete(1.0, tkinter.END)
        self.stud1_txt.insert(tkinter.END, self.viewmodel.get_stud1_txt())
        self.stud2_txt.delete(1.0, tkinter.END)
        self.stud2_txt.insert(tkinter.END, self.viewmodel.get_stud2_txt())
        self.stud3_txt.delete(1.0, tkinter.END)
        self.stud3_txt.insert(tkinter.END, self.viewmodel.get_stud3_txt())

        self.result_label1.config(text=self.viewmodel.get_answer1())
        self.result_label2.config(text=self.viewmodel.get_answer2())
        self.result_label3.config(text=self.viewmodel.get_answer3())
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
        self.stud1_txt.bind('<Motion>', self.instr_txt_changed)
