import tkinter as Tk

from elastic_of_demand.videmodel.viewmodel_elastic_of_demand import ViewModelElasticOfDemand


class GuiView(Tk.Frame):
    view_model = ViewModelElasticOfDemand()
    N_LOG_MESSAGES_TO_DISPLAY = 7

    def calc_by_price(self, event):
        self.mvvm_bind()
        self.view_model.calc_by_price()
        self.mvvm_back_bind()

    def calc_by_salary(self, event):
        self.mvvm_bind()
        self.view_model.calc_by_salary()
        self.mvvm_back_bind()

    def arguments_txt_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def bind_events(self):
        self.start_price_txt.bind('<KeyRelease>', self.arguments_txt_changed)
        self.end_price_txt.bind('<KeyRelease>', self.arguments_txt_changed)
        self.start_demand_txt.bind('<KeyRelease>', self.arguments_txt_changed)
        self.end_demand_txt.bind('<KeyRelease>', self.arguments_txt_changed)
        self.start_salary_txt.bind('<KeyRelease>', self.arguments_txt_changed)
        self.end_salary_txt.bind('<KeyRelease>', self.arguments_txt_changed)

        self.btn_by_price.bind('<Button-1>', self.calc_by_price)
        self.btn_by_salary.bind('<Button-1>', self.calc_by_salary)

    def get_array_of_all_txt(self):
        array = [self.start_demand_txt.get("1.0", Tk.END), self.end_demand_txt.get("1.0", Tk.END),
                 self.start_price_txt.get("1.0", Tk.END), self.end_price_txt.get("1.0", Tk.END),
                 self.start_salary_txt.get("1.0", Tk.END), self.end_salary_txt.get("1.0", Tk.END)]
        return array

    def mvvm_bind(self):
        self.view_model.set_arguments_from_array(self.get_array_of_all_txt())

    def mvvm_back_bind(self):
        self.start_price_txt.delete(1.0, Tk.END)
        self.end_price_txt.delete(1.0, Tk.END)
        self.start_demand_txt.delete(1.0, Tk.END)
        self.end_demand_txt.delete(1.0, Tk.END)
        self.start_salary_txt.delete(1.0, Tk.END)
        self.end_salary_txt.delete(1.0, Tk.END)

        array = self.view_model.get_arguments_array()

        self.start_demand_txt.insert(Tk.END, array[0])
        self.end_demand_txt.insert(Tk.END, array[1])
        self.start_price_txt.insert(Tk.END, array[2])
        self.end_price_txt.insert(Tk.END, array[3])
        self.start_salary_txt.insert(Tk.END, array[4])
        self.end_salary_txt.insert(Tk.END, array[5])

        self.result_label_price.config(text=self.view_model.get_type_price())
        self.result_label_salary.config(text=self.view_model.get_type_salary())

        logger_text = '\n'.join(self.view_model.logger.get_log_messages()[-self.N_LOG_MESSAGES_TO_DISPLAY:])
        self.logger_label.configure(text='%s\n%s' % (self.view_model.get_log_message(), logger_text))

    def __init__(self):
        Tk.Frame.__init__(self)
        self.master.title("Elastic of demand")
        self.master.minsize(width=150, height=300)

        self.grid(sticky=Tk.W + Tk.E + Tk.N + Tk.S)

        # Labels and txt for arguments
        self.start_demand_label = Tk.Label(self, text='Start demand', fg='black',
                                           font="Arial 12", bg="light yellow")
        self.start_demand_label.pack()
        self.start_demand_txt = Tk.Text(self, height=1, width=10)
        self.start_demand_txt.pack()

        self.end_demand_label = Tk.Label(self, text='End demand', fg='black',
                                         font="Arial 12", bg="light yellow")
        self.end_demand_label.pack()
        self.end_demand_txt = Tk.Text(self, height=1, width=10)
        self.end_demand_txt.pack()

        self.start_price_label = Tk.Label(self, text='Start price', fg='black',
                                          font="Arial 12", bg="light yellow")
        self.start_price_label.pack()
        self.start_price_txt = Tk.Text(self, height=1, width=10)
        self.start_price_txt.pack()

        self.end_price_label = Tk.Label(self, text='End price', fg='black',
                                        font="Arial 12", bg="light yellow")
        self.end_price_label.pack()
        self.end_price_txt = Tk.Text(self, height=1, width=10)
        self.end_price_txt.pack()

        self.start_salary_label = Tk.Label(self, text='Start salary', fg='black',
                                           font="Arial 12", bg="light yellow")
        self.start_salary_label.pack()
        self.start_salary_txt = Tk.Text(self, height=1, width=10)
        self.start_salary_txt.pack()

        self.end_salary_label = Tk.Label(self, text='End salary', fg='black',
                                         font="Arial 12", bg="light yellow")
        self.end_salary_label.pack()
        self.end_salary_txt = Tk.Text(self, height=1, width=10)
        self.end_salary_txt.pack()

        # labels for types
        self.btn_by_price = Tk.Button(self, text="Calculate by price", width=15, height=1,
                                      font="Arial 12", bg="light blue")
        self.btn_by_price.pack()

        self.result_label_price = Tk.Label(self, fg='black', font="Arial 12", bg="light yellow")
        self.result_label_price.pack()

        self.btn_by_salary = Tk.Button(self, text="Calculate by salary", width=15, height=1,
                                       font="Arial 12", bg="light blue")
        self.btn_by_salary.pack()

        self.result_label_salary = Tk.Label(self, fg='black', font="Arial 12", bg="light yellow")
        self.result_label_salary.pack()

        self.logger_label = Tk.Label(self, fg='black', font="Arial 12", bg="light yellow")
        self.logger_label.pack()

        self.bind_events()
        self.mvvm_bind()
        self.mvvm_back_bind()
