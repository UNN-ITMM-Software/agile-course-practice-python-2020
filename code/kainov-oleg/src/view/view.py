import Tkinter
import ttk


class View(ttk.Frame):
    valid_operations = ['+', '-', '*', '/', 'Convert to continuous']
    default_sticky = Tkinter.W + Tkinter.E + Tkinter.N + Tkinter.S

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

    def __init__(self):
        ttk.Frame.__init__(self)
        self.master.title("Fraction calculator")

        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=5)
        self.grid(sticky=Tkinter.W + Tkinter.E + Tkinter.N + Tkinter.S)

        self.btn_convert = ttk.Button(self, text='Do it')
        self.btn_convert.grid(row=0, column=3, rowspan=2,
                              sticky=self.default_sticky)

        self.txt_first_frac = Tkinter.Text(self, wrap='word',
                                           height=1, width=10)
        self.txt_first_frac.grid(row=0, column=0, sticky=self.default_sticky)

        self.cmb_operation = ttk.Combobox(self, height=1, width=15,
                                          values=self.valid_operations)
        self.cmb_operation.current(0)
        self.cmb_operation.grid(row=0, column=1, sticky=self.default_sticky)

        self.txt_second_frac = Tkinter.Text(self, wrap='word',
                                            height=1, width=10)
        self.txt_second_frac.grid(row=0, column=2, sticky=self.default_sticky)

        self.lbl_result = ttk.Label(self, text="Here will be your result")
        self.lbl_result.grid(row=1, column=0, columnspan=3,
                             sticky=Tkinter.W + Tkinter.N)

        self.bind_events()
        self.set_weight_to_grid()

    def convert_clicked(self, event):
        pass

    def first_frac_txt_changed(self, event):
        pass

    def second_frac_txt_changed(self, event):
        pass

    def operation_changed(self, event):
        pass
        # print self.valid_operations[self.cmb_operation.current()]
