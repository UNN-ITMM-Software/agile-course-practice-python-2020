import tkinter as tk
from number_operations.viewmodel.viewmodel import NumberOperationsViewModel


class GUI(tk.Frame):
    def __init__(self):
        self.root = tk.Tk()
        super().__init__(self.root)
        self.viewmodel = NumberOperationsViewModel()
        self.init_ui()

    def init_ui(self):
        self.root.title('Number Operations')
        self.root.geometry('1000x500')
        self.root.resizable(width=False, height=False)
        self.pack(fill='both', expand=True)
        self.create_widgets()
        self.setup_grid()
        self.bind_events()
        self.mvvm_bind()
        self.mvvm_backbind()

    def create_widgets(self):
        self.create_calculator_widgets()

    def create_calculator_widgets(self):
        self.calculator = tk.Frame(self)
        self.calculator.numbers = tk.Frame(self.calculator)

        self.warning = tk.Label(self.calculator.numbers, text='', font=60)
        self.label_log = tk.Label(self.calculator.numbers, text="Logging", font=60)

        # labels
        self.calculator.labels = tk.Frame(self.calculator.numbers)
        self.calculator.label_base = tk.Label(self.calculator.labels, text='', font=60)
        self.calculator.label_dec = tk.Label(self.calculator.labels, text='Decimal', font=60)
        self.calculator.label_bin = tk.Label(self.calculator.labels, text='Binary', font=60)
        self.calculator.label_hex = tk.Label(self.calculator.labels, text='Hex', font=60)

        # numbers
        self.calculator.first_number = tk.Frame(self.calculator.numbers)
        self.calculator.label_first = tk.Label(self.calculator.first_number, text='First Number', font=60)
        self.calculator.first_dec = tk.Entry(self.calculator.first_number)
        self.calculator.first_bin = tk.Entry(self.calculator.first_number)
        self.calculator.first_hex = tk.Entry(self.calculator.first_number)

        self.calculator.second_number = tk.Frame(self.calculator.numbers)
        self.calculator.label_second = tk.Label(self.calculator.second_number, text='Second Number', font=60)
        self.calculator.second_dec = tk.Entry(self.calculator.second_number)
        self.calculator.second_bin = tk.Entry(self.calculator.second_number)
        self.calculator.second_hex = tk.Entry(self.calculator.second_number)

        # buttons
        self.calculator.buttons = tk.Frame(self.calculator.numbers)
        self.calculator.label_action = tk.Label(self.calculator.buttons, text='Action', font=60)
        self.calculator.button_add = tk.Button(self.calculator.buttons, text='Add', font=60)
        self.calculator.button_sub = tk.Button(self.calculator.buttons, text='Subtract', font=60)
        self.calculator.button_mult = tk.Button(self.calculator.buttons, text='Multiply', font=60)
        self.calculator.button_div = tk.Button(self.calculator.buttons, text='Divide', font=60)

        # results
        self.calculator.results = tk.Frame(self.calculator.numbers)
        self.calculator.label_results = tk.Label(self.calculator.results, text='Results', font=60)
        self.calculator.result_dec = tk.Entry(self.calculator.results, state='disabled')
        self.calculator.result_bin = tk.Entry(self.calculator.results, state='disabled')
        self.calculator.result_hex = tk.Entry(self.calculator.results, state='disabled')

    def setup_grid(self):
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1, uniform='half')
        self.calculator.grid(row=0, column=0, sticky='nswe')
        self.setup_calculator_grid()

    def setup_calculator_grid(self):
        self.calculator.rowconfigure(0, weight=1)
        self.calculator.columnconfigure(0, weight=1)
        self.label_log.pack(side='bottom')
        self.warning.pack(side='bottom', pady=100)

        # labels
        self.calculator.label_base.pack(pady=10)
        self.calculator.label_dec.pack()
        self.calculator.label_bin.pack()
        self.calculator.label_hex.pack()
        self.calculator.labels.pack(side='left')

        # first number
        self.calculator.label_first.pack(pady=10)
        self.calculator.first_dec.pack()
        self.calculator.first_bin.pack()
        self.calculator.first_hex.pack()
        self.calculator.first_number.pack(side='left', padx=15)

        # second number
        self.calculator.label_second.pack(pady=10)
        self.calculator.second_dec.pack()
        self.calculator.second_bin.pack()
        self.calculator.second_hex.pack()
        self.calculator.second_number.pack(side='left')

        # buttons
        self.calculator.label_action.pack(pady=20)
        self.calculator.button_add.pack(fill='x')
        self.calculator.button_sub.pack(fill='x')
        self.calculator.button_mult.pack(fill='x')
        self.calculator.button_div.pack(fill='x')
        self.calculator.buttons.pack(side='left', padx=50)

        # results
        self.calculator.label_results.pack(pady=10)
        self.calculator.result_dec.pack()
        self.calculator.result_bin.pack()
        self.calculator.result_hex.pack()
        self.calculator.results.pack(side='left')

        self.calculator.numbers.grid(row=0, sticky='')

    def bind_events(self):
        self.calculator.first_dec.bind('<KeyRelease>', self.first_dec_changed)
        self.calculator.first_bin.bind('<KeyRelease>', self.first_bin_changed)
        self.calculator.first_hex.bind('<KeyRelease>', self.first_hex_changed)

        self.calculator.second_dec.bind('<KeyRelease>', self.second_dec_changed)
        self.calculator.second_bin.bind('<KeyRelease>', self.second_bin_changed)
        self.calculator.second_hex.bind('<KeyRelease>', self.second_hex_changed)

        self.calculator.button_add.bind('<Button-1>', self.button_add_clicked)
        self.calculator.button_sub.bind('<Button-1>', self.button_sub_clicked)
        self.calculator.button_mult.bind('<Button-1>', self.button_mult_clicked)
        self.calculator.button_div.bind('<Button-1>', self.button_div_clicked)

    def button_add_clicked(self, event):
        self.mvvm_bind()
        self.viewmodel.add()
        self.mvvm_backbind()

    def button_sub_clicked(self, event):
        self.mvvm_bind()
        self.viewmodel.subtract()
        self.mvvm_backbind()

    def button_mult_clicked(self, event):
        self.mvvm_bind()
        self.viewmodel.multiply()
        self.mvvm_backbind()

    def button_div_clicked(self, event):
        self.mvvm_bind()
        self.viewmodel.divide()
        self.mvvm_backbind()

    def first_dec_changed(self, event):
        self.mvvm_bind()
        self.viewmodel.convert_first_dec()
        self.mvvm_backbind()

    def first_bin_changed(self, event):
        self.mvvm_bind()
        self.viewmodel.convert_first_bin()
        self.mvvm_backbind()

    def first_hex_changed(self, event):
        self.mvvm_bind()
        self.viewmodel.convert_first_hex()
        self.mvvm_backbind()

    def second_dec_changed(self, event):
        self.mvvm_bind()
        self.viewmodel.convert_second_dec()
        self.mvvm_backbind()

    def second_bin_changed(self, event):
        self.mvvm_bind()
        self.viewmodel.convert_second_bin()
        self.mvvm_backbind()

    def second_hex_changed(self, event):
        self.mvvm_bind()
        self.viewmodel.convert_second_hex()
        self.mvvm_backbind()

    def mvvm_bind(self):
        self.viewmodel.set_first(self.calculator.first_dec.get(),
                                 self.calculator.first_bin.get(),
                                 self.calculator.first_hex.get())

        self.viewmodel.set_second(self.calculator.second_dec.get(),
                                  self.calculator.second_bin.get(),
                                  self.calculator.second_hex.get())

    def mvvm_backbind(self):
        self.calculator.first_dec.delete(0, tk.END)
        self.calculator.first_dec.insert(tk.END, self.viewmodel.get_first_dec())
        self.calculator.first_bin.delete(0, tk.END)
        self.calculator.first_bin.insert(tk.END, self.viewmodel.get_first_bin())
        self.calculator.first_hex.delete(0, tk.END)
        self.calculator.first_hex.insert(tk.END, self.viewmodel.get_first_hex())

        self.calculator.second_dec.delete(0, tk.END)
        self.calculator.second_dec.insert(tk.END, self.viewmodel.get_second_dec())
        self.calculator.second_bin.delete(0, tk.END)
        self.calculator.second_bin.insert(tk.END, self.viewmodel.get_second_bin())
        self.calculator.second_hex.delete(0, tk.END)
        self.calculator.second_hex.insert(tk.END, self.viewmodel.get_second_hex())

        self.calculator.result_dec.config(state='normal')
        self.calculator.result_bin.config(state='normal')
        self.calculator.result_hex.config(state='normal')
        self.calculator.result_dec.delete(0, tk.END)
        self.calculator.result_dec.insert(tk.END, self.viewmodel.get_result_dec())
        self.calculator.result_bin.delete(0, tk.END)
        self.calculator.result_bin.insert(tk.END, self.viewmodel.get_result_bin())
        self.calculator.result_hex.delete(0, tk.END)
        self.calculator.result_hex.insert(tk.END, self.viewmodel.get_result_hex())
        self.calculator.result_dec.config(state='readonly')
        self.calculator.result_bin.config(state='readonly')
        self.calculator.result_hex.config(state='readonly')

        self.warning.config(text=self.viewmodel.get_warning())

        logger_text = '\n'.join(self.viewmodel.logger.get_last_messages(3))
        self.label_log.config(text=logger_text)
