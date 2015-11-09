import Tkinter
import ttk

from viewmodel import viewmodel


class View(ttk.Frame):
    valid_operations = ['+', '-', '*', '/', 'Convert to continuous']
    default_sticky = Tkinter.W + Tkinter.E + Tkinter.N + Tkinter.S

    view_model = viewmodel.ViewModel()

    def set_weight_to_grid(self):
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=5)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(2, weight=5)
        self.columnconfigure(3, weight=1)

    def bind_events(self):
        self.btn_convert.bind('<Button-1>', self.convert_clicked)
        self.txt_first_frac.bind('<KeyRelease>', self.first_frac_txt_changed)
        self.txt_second_frac.bind('<KeyRelease>', self.second_frac_txt_changed)
        self.cmb_operation.bind('<<ComboboxSelected>>', self.operation_changed)

    def mvvm_bind(self):
        self.view_model.set_first_fraction(
            self.txt_first_frac.get("1.0", Tkinter.END))
        self.view_model.set_second_fraction(
            self.txt_second_frac.get("1.0", Tkinter.END))
        self.view_model.set_operation(
            self.valid_operations[self.cmb_operation.current()])

    def mvvm_back_bind(self):
        self.txt_first_frac.delete(1.0, Tkinter.END)
        self.txt_first_frac.insert(
            Tkinter.END, self.view_model.get_first_fraction())

        self.txt_second_frac.delete(1.0, Tkinter.END)
        self.txt_second_frac.insert(
            Tkinter.END, self.view_model.get_second_fraction())

        self.btn_convert.config(
            state=self.view_model.get_button_convert_state())

        self.txt_second_frac.config(
            state=self.view_model.get_second_fraction_text_state())

        self.lbl_result.config(text=self.view_model.get_msg_text())

    def __init__(self):
        ttk.Frame.__init__(self)
        self.master.title("Fraction calculator")

        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=5)
        self.grid(sticky=Tkinter.W + Tkinter.E + Tkinter.N + Tkinter.S)

        self.btn_convert = ttk.Button(self, text='Do it')
        self.btn_convert.grid(row=0, column=3, rowspan=2,
                              sticky=self.default_sticky)

        self.txt_first_frac = Tkinter.Text(self,
                                           height=1, width=10)
        self.txt_first_frac.grid(row=0, column=0, sticky=self.default_sticky)

        self.cmb_operation = ttk.Combobox(self, height=1, width=15,
                                          values=self.valid_operations)
        self.cmb_operation.current(0)
        self.cmb_operation.grid(row=0, column=1, sticky=self.default_sticky)

        self.txt_second_frac = Tkinter.Text(self,
                                            height=1, width=10)
        self.txt_second_frac.grid(row=0, column=2, sticky=self.default_sticky)

        self.lbl_result = ttk.Label(self, text="Here will be your result")
        self.lbl_result.grid(row=1, column=0, columnspan=3,
                             sticky=Tkinter.W + Tkinter.N)

        self.bind_events()
        self.set_weight_to_grid()

        self.mvvm_back_bind()

    def convert_clicked(self, event):
        self.mvvm_bind()
        self.view_model.click_convert()
        self.mvvm_back_bind()

    def first_frac_txt_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def second_frac_txt_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def operation_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()
