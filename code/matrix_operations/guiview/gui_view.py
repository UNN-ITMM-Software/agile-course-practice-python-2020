import tkinter as Tk

from tkinter import ttk
from matrix_operations.viewmodel import viewmodel


class SimpleTableInput(ttk.Frame):
    def __init__(self, parent, rows, value):
        ttk.Frame.__init__(self, parent)

        self._entry = {}
        self.rows = rows

        check_input = self.register(self._validate), "%P"

        for row in range(self.rows):
            for column in range(self.rows):
                index = row, column
                e = Tk.Entry(self, validate="key", validatecommand=check_input)
                e.insert(Tk.END, str(value[row][column]))
                e.grid(row=row, column=column, stick="nsew")
                self._entry[index] = e
        for column in range(self.rows):
            self.grid_columnconfigure(column, weight=1)
        self.grid_rowconfigure(rows, weight=1)

    def get(self):
        result = []
        for row in range(self.rows):
            current_row = []
            for column in range(self.rows):
                index = (row, column)
                current_row.append(self._entry[index].get())
            result.append(current_row)
        return result

    @classmethod
    def _validate(cls, p):
        if p.strip() == "":
            return True
        try:
            float(p)
        except ValueError:
            return False
        return True


class GuiView(ttk.Frame):
    default_sticky = Tk.W + Tk.E + Tk.N + Tk.S

    def __init__(self):
        ttk.Frame.__init__(self)

        self.view_model = viewmodel.MatrixOperationsViewModel()
        self.master.title("Matrix calculator")
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=5)

        self.grid(sticky=Tk.W + Tk.E + Tk.N + Tk.S)

        self.table1 = SimpleTableInput(self, self.view_model.get_number_of_rows(),
                                       self.view_model.get_matrix1_as_list())
        self.table2 = SimpleTableInput(self, self.view_model.get_number_of_rows(),
                                       self.view_model.get_matrix2_as_list())

        self.table1.pack(side="top", fill="both", expand=True)
        self.VALID_OPERATIONS = ['+', '*', 'det1', 'det2', 'Transpose1', 'Transpose2', 'inv1', 'inv2']
        self.cmb_operation = ttk.Combobox(self, height=1, width=10,
                                          values=self.VALID_OPERATIONS)
        self.cmb_operation.current(0)
        self.cmb_operation.pack(side="top", fill=Tk.Y, expand=True)
        self.table2.pack(side="top", fill="both", expand=True)

        self.calculate = Tk.Button(self, text="Calculate", width=15, height=1, font="Arial 12",
                                   bg="light blue", command=self.on_calculate)
        self.calculate.pack()

        self.answer = Tk.Label(self, text="Your result", fg='black', font="Arial 12", bg="light yellow")
        self.answer.pack()

        self.mvvm_back_bind()

    def bind_events(self):
        self.cmb_operation.bind('<<ComboboxSelected>>', self.operation_changed)

    def on_calculate(self):
        self.mvvm_bind()
        self.view_model.calculate()
        self.mvvm_back_bind()

    def first_table_txt_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def second_table_txt_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def operation_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def mvvm_bind(self):
        table1_raw_text = self.table1.get()
        good_table1 = list()
        for l in table1_raw_text:
            good_table1.append(list(map(int, l)))
        table2_raw_text = self.table2.get()
        good_table2 = list()
        for l in table2_raw_text:
            good_table2.append(list(map(int, l)))
        self.view_model.update_matrix1_content(good_table1)
        self.view_model.update_matrix2_content(good_table2)
        self.view_model.set_operation(
            self.VALID_OPERATIONS[self.cmb_operation.current()])

    def mvvm_back_bind(self):
        matrix1_as_list = self.view_model.get_matrix1_as_list()
        matrix2_as_list = self.view_model.get_matrix2_as_list()
        self.table1.pack_forget()
        self.cmb_operation.pack_forget()
        self.table2.pack_forget()
        self.answer.pack_forget()

        self.table1 = SimpleTableInput(self, self.view_model.rows, matrix1_as_list)
        self.table2 = SimpleTableInput(self, self.view_model.rows, matrix2_as_list)

        self.table1.pack(side="top", fill="both", expand=True)
        self.cmb_operation.pack(side="top", fill=Tk.Y, expand=True)
        self.table2.pack(side="top", fill="both", expand=True)
        self.answer.pack()
        self.answer.config(text=self.view_model.answer)
