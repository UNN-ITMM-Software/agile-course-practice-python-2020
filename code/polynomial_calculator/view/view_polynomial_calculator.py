import tkinter as Tk
from tkinter import ttk

from polynomial_calculator.viewmodel.viewmodel_polynomial_calculator import PolyViewModel


class GuiView(Tk.Frame):
    VALID_OPERATIONS = ['+', '-', '*']
    view_model = PolyViewModel()

    def clck_bttn(self):
        self.view_model.set_first_poly(self.first_poly_txt.get(1.0, Tk.END))
        self.view_model.set_second_poly(self.second_poly_txt.get(1.0, Tk.END))
        self.view_model.set_operation(self.VALID_OPERATIONS[self.cmb_operation.current()])
        self.view_model.computing()
        self.result_label.configure(text=self.view_model.get_result())

    def __init__(self):
        Tk.Frame.__init__(self)
        self.master.title("Polynomial calculator")
        self.master.minsize(width=150, height=150)

        self.grid(sticky=Tk.W + Tk.E + Tk.N + Tk.S)
        self.first_poly_label = Tk.Label(self, text=
                                         "Enter the coefficients of the " +
                                         "first polynomial (type int) using ','",
                                         fg='black', font="Arial 12", bg="light yellow")

        self.first_poly_label.pack()
        self.first_poly_txt = Tk.Text(self, height=1, width=40)
        self.first_poly_txt.pack()
        self.operation_label = Tk.Label(self, text="Select an operation", fg='black',
                                        font="Arial 12", bg="light yellow")

        self.operation_label.pack()
        self.cmb_operation = ttk.Combobox(self, height=1, width=2,
                                          values=self.VALID_OPERATIONS)
        self.cmb_operation.current(0)
        self.cmb_operation.pack()
        self.second_poly_label = Tk.Label(self, text=
                                          "Enter the coefficients of the " + 
                                          "second polynomial (type int) using ','",
                                          fg='black', font="Arial 12", bg="light yellow")

        self.second_poly_label.pack()
        self.second_poly_txt = Tk.Text(self, height=1, width=40)
        self.second_poly_txt.pack()
        self.calculate = Tk.Button(self, text="Calculate", width=15, height=1, font="Arial 12",
                                   bg="light blue", command = self.clck_bttn)

        self.calculate.pack()
        self.result_label = Tk.Label(self, text="", fg='black',
                                     font="Arial 12", bg="light yellow")

        self.result_label.pack()
