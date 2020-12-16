import tkinter as tk
from tkinter import ttk

from mortgage_calculator.viewmodel.viewmodel import MortgageViewModel


class GUI(ttk.Frame):
    default_sticky = tk.W + tk.E + tk.N + tk.S
    TERM_TYPES = ['months', 'years']

    view_model = MortgageViewModel()

    def bind_events(self):
        self.amount_textbox.bind('<KeyRelease>', self.amount_textbox_changed)
        self.initial_payment_textbox.bind('<KeyRelease>', self.initial_payment_textbox_changed)
        self.rate_textbox.bind('<KeyRelease>', self.rate_textbox_changed)
        self.term_textbox.bind('<KeyRelease>', self.term_textbox_changed)
        self.monthly_payment_textbox.bind('<KeyRelease>', self.monthly_payment_textbox_changed)
        self.term_type_combobox.bind('<<ComboboxSelected>>', self.term_type_changed)

        self.button_calculate_monthly_payment.bind('<Button-1>', self.calculate_monthly_payment_clicked)
        self.button_calculate_expected_term.bind('<Button-1>', self.calculate_expected_term_clicked)
        self.button_calculate_overpaid_amount.bind('<Button-1>', self.calculate_overpaid_amount_clicked)

    def mvvm_bind(self):
        self.view_model.set_amount(self.amount_textbox.get())
        self.view_model.set_initial_payment(self.initial_payment_textbox.get())
        self.view_model.set_rate(self.rate_textbox.get())
        self.view_model.set_term(self.term_textbox.get())
        self.view_model.set_monthly_payment(self.monthly_payment_textbox.get())
        self.view_model.set_term_type(self.term_type_combobox.get())

    def mvvm_back_bind(self):
        self.button_calculate_monthly_payment.config(
            state=self.view_model.get_button_calculate_monthly_payment_state())
        self.button_calculate_expected_term.config(
            state=self.view_model.get_button_calculate_expected_term_state())
        self.button_calculate_overpaid_amount.config(
            state=self.view_model.get_button_calculate_overpaid_amount_state())

        self.amount_textbox.delete(0, tk.END)
        self.amount_textbox.insert(tk.INSERT, self.view_model.get_amount())
        self.initial_payment_textbox.delete(0, tk.END)
        self.initial_payment_textbox.insert(tk.INSERT, self.view_model.get_initial_payment())
        self.rate_textbox.delete(0, tk.END)
        self.rate_textbox.insert(tk.INSERT, self.view_model.get_rate())
        self.term_textbox.delete(0, tk.END)
        self.term_textbox.insert(tk.INSERT, self.view_model.get_term())
        self.monthly_payment_textbox.delete(0, tk.END)
        self.monthly_payment_textbox.insert(tk.INSERT, self.view_model.get_monthly_payment())

        self.calculate_monthly_payment_result.configure(
            text=self.view_model.get_click_calculate_monthly_payment_result())
        self.calculate_expected_term_result.configure(
            text=self.view_model.get_click_calculate_expected_term_result())
        self.calculate_overpaid_amount_result.configure(
            text=self.view_model.get_click_calculate_overpaid_amount_result())

        self.txt_error_message.configure(
            text=self.view_model.get_error_message())

    def __init__(self):
        ttk.Frame.__init__(self)
        self.master.title('Mortgage calculator')

        self.grid(sticky=self.default_sticky)

        # Amount
        self.amount_label = tk.Label(self, text='Cost of property:')
        self.amount_label.grid(row=0, column=0, sticky="w")

        self.amount_textbox = tk.Entry(self, width=25)
        self.amount_textbox.grid(row=0, column=1)

        # Initial payment
        self.initial_payment_label = tk.Label(self, text='Initial payment:')
        self.initial_payment_label.grid(row=1, column=0, sticky="w")

        self.initial_payment_textbox = tk.Entry(self, width=25)
        self.initial_payment_textbox.grid(row=1, column=1)

        # Rate
        self.rate_label = tk.Label(self, text='Loan interest rate:')
        self.rate_label.grid(row=2, column=0, sticky="w")

        self.rate_textbox = tk.Entry(self, width=25)
        self.rate_textbox.grid(row=2, column=1)

        # Term
        self.term_label = tk.Label(self, text='Desired mortgage term:')
        self.term_label.grid(row=3, column=0, sticky="w")

        self.term_textbox = tk.Entry(self, width=25)
        self.term_textbox.grid(row=3, column=1)

        # Monthly payment
        self.monthly_payment_label = tk.Label(self, text='Desired monthly payment:')
        self.monthly_payment_label.grid(row=4, column=0, sticky="w")

        self.monthly_payment_textbox = tk.Entry(self, width=25)
        self.monthly_payment_textbox.grid(row=4, column=1)

        # Term type
        self.term_type_label = tk.Label(self, text='Term type:')
        self.term_type_label.grid(row=5, column=0, sticky="w")

        self.term_type_combobox = ttk.Combobox(self, height=1, width=15, values=self.TERM_TYPES)
        self.term_type_combobox.current(0)
        self.term_type_combobox.grid(row=5, column=1, sticky=self.default_sticky)

        # Calculate monthly payment
        self.calculate_monthly_payment_label = tk.Label(self, text='Monthly payment:')
        self.calculate_monthly_payment_label.grid(row=6, column=0, sticky="w")

        self.calculate_monthly_payment_result = tk.Label(self, text='')
        self.calculate_monthly_payment_result.grid(row=6, column=1, sticky="w")

        self.button_calculate_monthly_payment = ttk.Button(self, text='calculate')
        self.button_calculate_monthly_payment.grid(row=6, column=2, rowspan=1, sticky=self.default_sticky)

        # Calculate expected term
        self.calculate_expected_term_label = tk.Label(self, text='Expected term:')
        self.calculate_expected_term_label.grid(row=7, column=0, sticky="w")

        self.calculate_expected_term_result = tk.Label(self, text='')
        self.calculate_expected_term_result.grid(row=7, column=1, sticky="w")

        self.button_calculate_expected_term = ttk.Button(self, text='calculate')
        self.button_calculate_expected_term.grid(row=7, column=2, rowspan=1, sticky=self.default_sticky)

        # Calculate overpaid amount
        self.calculate_overpaid_amount_label = tk.Label(self, text='Overpaid amount:')
        self.calculate_overpaid_amount_label.grid(row=8, column=0, sticky="w")

        self.calculate_overpaid_amount_result = tk.Label(self, text='')
        self.calculate_overpaid_amount_result.grid(row=8, column=1, sticky="w")

        self.button_calculate_overpaid_amount = ttk.Button(self, text='calculate')
        self.button_calculate_overpaid_amount.grid(row=8, column=2, rowspan=1, sticky=self.default_sticky)

        # Error message
        self.txt_error_message = tk.Label(self, height=30, width=50, wraplength=150)
        self.txt_error_message.grid(row=9, column=1, rowspan=3, sticky="w")

        self.bind_events()
        self.mvvm_back_bind()

    def calculate_monthly_payment_clicked(self, event):
        self.mvvm_bind()
        self.view_model.click_calculate_monthly_payment()
        self.mvvm_back_bind()

    def calculate_expected_term_clicked(self, event):
        self.mvvm_bind()
        self.view_model.click_calculate_expected_term()
        self.mvvm_back_bind()

    def calculate_overpaid_amount_clicked(self, event):
        self.mvvm_bind()
        self.view_model.click_calculate_overpaid_amount()
        self.mvvm_back_bind()

    def amount_textbox_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def initial_payment_textbox_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def rate_textbox_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def term_textbox_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def monthly_payment_textbox_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def term_type_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()
