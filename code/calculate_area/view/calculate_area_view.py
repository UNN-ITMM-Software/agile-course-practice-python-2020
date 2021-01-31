import tkinter
from tkinter import ttk

from calculate_area.viewmodel.calculate_area_viewmodel import CalculateAreaViewModel


class GUIView(ttk.Frame):
    default_sticky = tkinter.W + tkinter.E + tkinter.N + tkinter.S

    viewmodel = CalculateAreaViewModel()

    def __init__(self):
        ttk.Frame.__init__(self)
        self.master.title("Figure area calculator")
        self.master.geometry('200x150')
        self.master.resizable(width=False, height=False)

        self.lbl_figure_type = ttk.Label(text="Figure type:")

        self.cmb_figure_types = ttk.Combobox(
            values=["CONE", "CUBE", "SPHERE", "CYLINDER"],
            state="readonly", width=10)
        self.cmb_figure_types.current(0)

        self.lbl_a = ttk.Label(text="a =")
        self.txt_a = tkinter.Text(height=1, width=8)

        self.lbl_r = ttk.Label(text="r =")
        self.txt_r = tkinter.Text(height=1, width=8)

        self.lbl_h = ttk.Label(text="h =")
        self.txt_h = tkinter.Text(height=1, width=8)

        self.lbl_l = ttk.Label(text="l =")
        self.txt_l = tkinter.Text(height=1, width=8)

        self.btn_calculate = ttk.Button(text='Calculate area')
        self.lbl_result = ttk.Label(text="result", relief="sunken", width=18)

        self.lbl_message = ttk.Label(text="Info message", relief="sunken", width=30)

        self.mvvm_bind_events()
        self.set_weight_to_grid()
        self.mvvm_back_bind()

    def set_weight_to_grid(self):
        self.lbl_figure_type.grid(row=0, column=0)
        self.cmb_figure_types.grid(row=0, column=1)

        self.lbl_a.grid(row=1, column=0)
        self.lbl_r.grid(row=2, column=0)
        self.lbl_h.grid(row=3, column=0)
        self.lbl_l.grid(row=4, column=0)

        self.txt_a.grid(row=1, column=1)
        self.txt_r.grid(row=2, column=1)
        self.txt_h.grid(row=3, column=1)
        self.txt_l.grid(row=4, column=1)

        self.btn_calculate.grid(row=5, column=0)
        self.lbl_result.grid(row=5, column=1)

        self.lbl_message.grid(row=6, column=0, columnspan=2, sticky=tkinter.W + tkinter.N)

    def mvvm_bind_events(self):
        self.txt_a.bind('<KeyRelease>', self.txt_a_changed)
        self.txt_r.bind('<KeyRelease>', self.txt_r_changed)
        self.txt_h.bind('<KeyRelease>', self.txt_h_changed)
        self.txt_l.bind('<KeyRelease>', self.txt_l_changed)
        self.cmb_figure_types.bind('<<ComboboxSelected>>', self.figure_type_changed)
        self.btn_calculate.bind('<Button-1>', self.calculate_clicked)

    def mvvm_bind(self):
        self.viewmodel.set_a(self.txt_a.get("1.0", tkinter.END))
        self.viewmodel.set_r(self.txt_r.get("1.0", tkinter.END))
        self.viewmodel.set_h(self.txt_h.get("1.0", tkinter.END))
        self.viewmodel.set_l(self.txt_l.get("1.0", tkinter.END))
        self.viewmodel.set_figure_type(self.cmb_figure_types.get())

    def mvvm_back_bind(self):
        self.btn_calculate.config(state=self.viewmodel.get_calc_button_state())
        self.lbl_message.config(text=self.viewmodel.get_message())
        self.lbl_result.config(text=self.viewmodel.get_area())

    def txt_a_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def txt_r_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def txt_h_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def txt_l_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def figure_type_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def calculate_clicked(self, event):
        self.mvvm_bind()
        self.viewmodel.calculate()
        self.mvvm_back_bind()


if __name__ == '__main__':
    GUIView().mainloop()
