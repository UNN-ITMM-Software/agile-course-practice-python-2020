import tkinter as tk

from debt_expenses.viewmodel.debt_viewmodel import DebtViewModel


def format_log(messages):
    result_log = ''
    for message in messages:
        result_log += message + '\n'
    return result_log


class GUIView:
    view_model = DebtViewModel()
    default_sticky = tk.W + tk.E + tk.N + tk.S

    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Debt servicing expenses')
        self.window.geometry('600x250')
        self.window.resizable(width=False, height=False)

        self.frame = tk.Frame(self.window, bg='ghost white')
        self.frame.pack(fill="both", expand=True)
        self.title = tk.Label(master=self.frame,
                              text='Enter "Required Sum", "Percent rate", "Period" and "Year" :',
                              bg='purple1')

        self.req_sum_value = tk.Entry(self.frame, bg='white')
        self.percent_rate_value = tk.Entry(self.frame, bg='white')
        self.period_value = tk.Entry(self.frame, bg='white')
        self.year_value = tk.Entry(self.frame, bg='white')

        self.amounts_res_button = tk.Button(self.frame,
                                            text='Calculate Equal amounts repayment',
                                            bg='snow2')
        self.payments_res_button = tk.Button(self.frame,
                                             text='Calculate Equal payments repayment',
                                             bg='snow2')

        self.res = tk.Label(self.frame, text='Result : ', bg='pale green', font=32)
        self.error_field = tk.Label(self.frame, text='', font=28, bg='ghost white')
        self.logger_field = tk.Label(self.frame, text='Log:', bg='ghost white', font=12)

        self.setup_grid()
        self.bind_events()

        self.view_bind()
        self.view_back_bind()

        self.window.mainloop()

    def setup_grid(self):
        self.frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.title.grid(row=0, column=0, columnspan=4)

        self.req_sum_value.grid(row=1, column=1, sticky=self.default_sticky)
        self.percent_rate_value.grid(row=1, column=2, sticky=self.default_sticky)
        self.period_value.grid(row=2, column=1, sticky=self.default_sticky)
        self.year_value.grid(row=2, column=2, sticky=self.default_sticky)

        self.amounts_res_button.grid(row=3, column=1, sticky=self.default_sticky)
        self.payments_res_button.grid(row=3, column=3, sticky=self.default_sticky)

        self.res.grid(row=4, column=0, columnspan=4, rowspan=4, sticky=self.default_sticky)
        self.error_field.grid(row=8, column=0, columnspan=4, sticky=self.default_sticky)
        self.logger_field.grid(row=7, column=0, columnspan=4, stick=self.default_sticky)

    def bind_events(self):
        self.req_sum_value.bind('<KeyRelease>', self.change_req_sum)
        self.percent_rate_value.bind('<KeyRelease>', self.change_percent_rate)
        self.period_value.bind('<KeyRelease>', self.change_period)
        self.year_value.bind('<KeyRelease>', self.change_year)

        self.amounts_res_button.bind('<Button-1>', self.amounts_res_button_clicked)
        self.payments_res_button.bind('<Button-1>', self.payments_res_button_clicked)

    def amounts_res_button_clicked(self, event):
        self.view_bind()
        self.view_model.perform_repayment('equal_amounts')
        self.view_back_bind()

    def payments_res_button_clicked(self, event):
        self.view_bind()
        self.view_model.perform_repayment('equal_payments')
        self.view_back_bind()

    def change_req_sum(self, event):
        self.view_bind()
        self.view_back_bind()

    def change_percent_rate(self, event):
        self.view_bind()
        self.view_back_bind()

    def change_period(self, event):
        self.view_bind()
        self.view_back_bind()

    def change_year(self, event):
        self.view_bind()
        self.view_back_bind()

    def view_bind(self):
        self.view_model.set_req_sum(self.req_sum_value.get())
        self.view_model.set_percent_rate(self.percent_rate_value.get())
        self.view_model.set_period(self.period_value.get())
        self.view_model.set_year(self.year_value.get())

    def view_back_bind(self):
        self.req_sum_value.delete(0, tk.END)
        self.req_sum_value.insert(tk.END, self.view_model.get_req_sum())

        self.percent_rate_value.delete(0, tk.END)
        self.percent_rate_value.insert(tk.END, self.view_model.get_percent_rate())

        self.period_value.delete(0, tk.END)
        self.period_value.insert(tk.END, self.view_model.get_period())

        self.year_value.delete(0, tk.END)
        self.year_value.insert(tk.END, self.view_model.get_year())

        payment = self.view_model.get_payment()
        expenses = self.view_model.get_expenses()
        self.res.config(text='Payment: {:.0f} - Expenses: {:.0f}'.format(payment if payment else '',
                                                                         expenses if expenses else ''))

        error_msg = self.view_model.get_error_message()
        self.error_field.config(text='{}'.format(error_msg if error_msg else 'Normal work'))
        self.logger_field.config(text='{}\n'.format(get_log_messages(self.view_model.logger.get_log_messages())))
