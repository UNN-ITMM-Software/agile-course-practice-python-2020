import tkinter as tk
from viewmodel.viewmodel import StringFormulaCalculationViewModel


class GUI(tk.Frame):
    def __init__(self):
        self.root = tk.Tk()
        super().__init__(self.root)
        self.viewmodel = StringFormulaCalculationViewModel()
        self.init_ui()

    def init_ui(self):
        self.root.title('String Calculation')
        self.root.geometry('500x400')
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

        # Formula
        self.calculator.formula = tk.Frame(self.calculator.numbers)
        self.calculator.label_formula = tk.Label(self.calculator.formula, text='Formula', font=60)
        self.calculator.formula_input = tk.Entry(self.calculator.formula)

        # buttons
        self.calculator.buttons = tk.Frame(self.calculator.numbers)
        self.calculator.label_action = tk.Label(self.calculator.buttons, text='Action', font=60)
        self.calculator.button_calculate = tk.Button(self.calculator.buttons, text='Calculate', font=60)

        # results
        self.calculator.results = tk.Frame(self.calculator.numbers)
        self.calculator.label_results = tk.Label(self.calculator.results, text='Results', font=60)
        self.calculator.result = tk.Entry(self.calculator.results, state='disabled')

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

        # formula input
        self.calculator.label_formula.pack(pady=10)
        self.calculator.formula_input.pack()
        self.calculator.formula.pack(side='left', padx=5)

        # buttons
        self.calculator.label_action.pack(pady=20)
        self.calculator.button_calculate.pack(fill='x')
        self.calculator.buttons.pack(side='left', padx=50)

        # results
        self.calculator.label_results.pack(pady=10)
        self.calculator.result.pack()
        self.calculator.results.pack(side='left')

        self.calculator.numbers.grid(row=0, sticky='')

    def bind_events(self):
        self.calculator.formula_input.bind('<KeyRelease>', self.formula_changed)
        self.calculator.button_calculate.bind('<Button-1>', self.button_calculate_clicked)

    def button_calculate_clicked(self, event):
        self.mvvm_bind()
        self.viewmodel.calculate_formula()
        self.mvvm_backbind()

    def formula_changed(self, event):
        self.mvvm_bind()
        # self.viewmodel.convert_first_dec()
        self.mvvm_backbind()

    def mvvm_bind(self):
        self.viewmodel.set_formula(self.calculator.formula_input.get())

    def mvvm_backbind(self):
        self.calculator.formula_input.delete(0, tk.END)
        self.calculator.formula_input.insert(tk.END, self.viewmodel.get_formula())

        # self.calculator.second_dec.delete(0, tk.END)
        # self.calculator.second_dec.insert(tk.END, self.viewmodel.get_second_dec())

        self.calculator.result.config(state='normal')
        self.calculator.result.delete(0, tk.END)
        self.calculator.result.insert(tk.END, self.viewmodel.get_result())
        self.calculator.result.config(state='readonly')

        self.warning.config(text=self.viewmodel.get_warning())

        logger_text = '\n'.join(self.viewmodel.logger.get_last_messages(3))
        self.label_log.config(text=logger_text)
