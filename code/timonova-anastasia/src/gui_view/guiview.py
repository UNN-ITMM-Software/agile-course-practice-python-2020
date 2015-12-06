import tkinter as tk

from view_model import viewmodel


class SimpleTableInput(tk.Frame):
    def __init__(self, parent, rows, value):
        tk.Frame.__init__(self, parent)

        self._entry = {}
        self.rows = rows

        check_input = self.register(self._validate), "%P"

        for row in range(self.rows):
            for column in range(self.rows):
                index = row, column
                e = tk.Entry(self, validate="key", validatecommand=check_input)
                e.insert(tk.END, str(value[row][column]))
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

    def _validate(self, p):
        if p.strip() == "":
            return True
        try:
            float(p)
        except ValueError:
            return False
        return True


class GuiView(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)

        self.view_model = viewmodel.ViewModel()
        self.view_model_error = viewmodel.ViewError()
        self.master.title("Determinant calculator")
        self.master.minsize(width=150, height=150)

        self.grid(sticky=tk.W + tk.E + tk.N + tk.S)
        self.rows_label = tk.Label(self, text="   Enter rows and columns numbers   ", fg='black',
                                   font="Arial 12", bg="light yellow")
        self.rows_label.pack()
        self.rows = tk.Text(self, height=1, width=20)
        self.rows.pack()
        self.enter = tk.Button(self, text="Change matrix rank", width=15, height=1, font="Arial 12",
                               bg="light blue", command=self.on_change)
        self.enter.pack()
        self.table = SimpleTableInput(self, self.view_model.get_number_of_rows(),
                                      self.view_model.get_matrix_as_list())
        self.table.pack(side="top", fill="both", expand=True)
        self.submit_matrix_for_calc_det = tk.Button(self, text="Submit", width=15, height=1, font="Arial 12",
                                                    bg="light blue", command=self.on_submit)
        self.submit_matrix_for_calc_det.pack()

        self.answer = tk.Label(self, text="You result", fg='black', font="Arial 12", bg="light yellow")
        self.answer.pack()
        self.error_msg = tk.Label(self, text="", fg='black', font="Arial 12", bg="light yellow")
        self.error_msg.pack()

        self.my_back_bind()

    def on_submit(self):
        if self.view_model.get_number_of_rows() == int(self.rows.get("1.0", tk.END).strip()):
            self.my_bind()
            self.view_model.calculate_determinant()
            self.my_back_bind()

    def on_change(self):
        self.my_bind()
        self.view_model.init_zero_matrix_with_new_rank_value()
        self.my_back_bind()

    def my_bind(self):
        try:
            self.view_model.set_number_of_rows(int(self.rows.get("1.0", tk.END).strip()))
            self.error_msg.config(text="")
        except ValueError:
            self.error_msg.config(text="Rows count should be number!")
        self.view_model.set_answer('')
        table_raw_text = self.table.get()
        good_table = list()
        for l in table_raw_text:
            good_table.append(list(map(int, l)))
        self.view_model.update_matrix_content(good_table)

    def my_back_bind(self):
        self.rows.delete("1.0", tk.END)
        self.rows.insert(tk.END, self.view_model.get_number_of_rows())
        matrix_as_list = self.view_model.get_matrix_as_list()
        self.table.pack_forget()
        self.table = SimpleTableInput(self, self.view_model.rows, matrix_as_list)
        self.table.pack(side="top", fill="both", expand=True)
        self.answer.config(text=self.view_model.answer)
