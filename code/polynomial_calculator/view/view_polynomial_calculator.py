import tkinter as Tk
from tkinter import ttk

from polynomial_calculator.viewmodel.viewmodel_polynomial_calculator import PolyViewModel

class GuiView(Tk.Frame):
    VALID_OPERATIONS = ['+', '-', '*']
    N_LOG_MESSAGES_TO_DISPLAY = 8
    view_model = PolyViewModel()
    
    def convert_clicked(self, event):
            self.mvvm_bind()
            self.view_model.computing()
            self.mvvm_back_bind()

    def first_poly_txt_changed(self, event):
            self.mvvm_bind()
            self.mvvm_back_bind()

    def second_poly_txt_changed(self, event):
            self.mvvm_bind()
            self.mvvm_back_bind()

    def operation_changed(self, event):
            self.mvvm_bind()
            self.mvvm_back_bind()     

    def bind_events(self):
        self.calculate.bind('<Button-1>', self.convert_clicked)
        self.first_poly_txt.bind('<KeyRelease>', self.first_poly_txt_changed)
        self.second_poly_txt.bind('<KeyRelease>', self.second_poly_txt_changed)
        self.cmb_operation.bind('<<ComboboxSelected>>', self.operation_changed)

    def mvvm_bind(self):
        self.view_model.set_first_poly(
            self.first_poly_txt.get("1.0", Tk.END))
        self.view_model.set_second_poly(
            self.second_poly_txt.get("1.0", Tk.END))
        self.view_model.set_operation(
            self.VALID_OPERATIONS[self.cmb_operation.current()])

    def mvvm_back_bind(self):
        self.first_poly_txt.delete(1.0, Tk.END)
        self.first_poly_txt.insert(
            Tk.END, self.view_model.get_first_poly())

        self.second_poly_txt.delete(1.0, Tk.END)
        self.second_poly_txt.insert(
            Tk.END, self.view_model.get_second_poly())

        logger_text = '\n'.join(self.view_model.logger.get_log_messages()[-self.N_LOG_MESSAGES_TO_DISPLAY:])
        self.result_label.config(text='%s\n%s' % (self.view_model.get_result(), logger_text))

    def __init__(self):
        Tk.Frame.__init__(self)
        self.master.title("Polynomial calculator")
        self.master.minsize(width=150, height=150)

        self.grid(sticky=Tk.W + Tk.E + Tk.N + Tk.S)
        self.first_poly_label = Tk.Label(self, text="Enter the coefficients of the " +
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
        self.second_poly_label = Tk.Label(self, text="Enter the coefficients of the " +
                                          "second polynomial (type int) using ','",
                                          fg='black', font="Arial 12", bg="light yellow")

        self.second_poly_label.pack()
        self.second_poly_txt = Tk.Text(self, height=1, width=40)
        self.second_poly_txt.pack()
        self.calculate = Tk.Button(self, text="Calculate", width=15, height=1, font="Arial 12",
                                   bg="light blue")

        self.calculate.pack()
        self.result_label = Tk.Label(self, fg='black',
                                     font="Arial 12", bg="light yellow")

        self.result_label.pack()

        self.bind_events()
        self.mvvm_bind()
        self.mvvm_back_bind()   
