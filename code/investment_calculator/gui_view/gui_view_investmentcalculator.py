import tkinter

from tkinter import ttk

from investment_calculator.viewmodel import viewmodel


class GuiView(ttk.Frame):
    default_sticky = tkinter.W + tkinter.E + tkinter.N + tkinter.S
    viewmodel = viewmodel.InvestmentCalculatorViewModel()

    def __init__(self):
        ttk.Frame.__init__(self)
        self.master.title("Калькулятор инвестиций")
        self.master.geometry('900x200')
        self.grid(sticky=tkinter.W + tkinter.E + tkinter.N + tkinter.S)


        self.K_label = ttk.Label(self, text="Размер инвестиций (K)   ")
        self.K_label.grid(row=1, column=0, sticky=tkinter.W)

        self.K_txt = tkinter.Text(self, height=1, width=15)
        self.K_txt.grid(row=1, column=0, sticky=tkinter.N)

        self.R_label = ttk.Label(self, text="Размер ежегодного дохода (R)   ")
        self.R_label.grid(row=2, column=0, sticky=tkinter.W)

        self.R_txt = tkinter.Text(self, height=1, width=15)
        self.R_txt.grid(row=2, column=0, sticky=tkinter.N)

        self.n_label = ttk.Label(self, text="Количество лет (n)  ")
        self.n_label.grid(row=3, column=0, sticky=tkinter.W)

        self.n_txt = tkinter.Text(self, height=1, width=15)
        self.n_txt.grid(row=3, column=0, sticky=tkinter.N)

        self.q_label = ttk.Label(self, text="Ставка сравнения (q)  ")
        self.q_label.grid(row=4, column=0, sticky=tkinter.W)

        self.q_txt = tkinter.Text(self, height=1, width=15)
        self.q_txt.grid(row=4, column=0, sticky=tkinter.N)

        self.calc_button = ttk.Button(self, text="Рассчитать")
        self.calc_button.grid(row=5, column=0, sticky=tkinter.N)

        self.answer_label = ttk.Label(self, text="Чистый приведенный доход:                                                                                                         ")
        self.answer_label.grid(row=7, column=0, sticky=self.default_sticky)

        self.result_of_losers_label = ttk.Label(self, text="")
        self.result_of_losers_label.grid(row=7, column=1, sticky=self.default_sticky)

        self.bind_events()
        self.mvvm_back_bind_btn()
        self.mvvm_back_bind_lbls()

    def mvvm_bind(self):
        self.viewmodel.set_instr(self.K_txt.get("1.0", tkinter.END).strip(),
                                 self.R_txt.get("1.0", tkinter.END).strip(),
                                 self.n_txt.get("1.0", tkinter.END).strip(),
                                 self.q_txt.get("1.0", tkinter.END).strip())

    def mvvm_back_bind_btn(self):
        self.calc_button.config(state=self.viewmodel.get_button_convert_state())

    def mvvm_back_bind_lbls(self):
        self.result_of_losers_label.config(text=self.viewmodel.get_answer())

    def button_clicked(self, event):
        self.mvvm_bind()
        self.viewmodel.click_button()
        self.mvvm_back_bind_lbls()

    def instr_txt_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind_btn()

    def bind_events(self):
        self.calc_button.bind('<Button-1>', self.button_clicked)
        self.K_txt.bind('<KeyRelease>', self.instr_txt_changed)
        self.R_txt.bind('<KeyRelease>', self.instr_txt_changed)
        self.n_txt.bind('<KeyRelease>', self.instr_txt_changed)
        self.q_txt.bind('<KeyRelease>', self.instr_txt_changed)
