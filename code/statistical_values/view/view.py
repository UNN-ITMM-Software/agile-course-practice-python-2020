import tkinter as tk
from tkinter import ttk

from statistical_values.viewmodel.viewmodel import StatisticalValuesViewModel


class GUI(ttk.Frame):
    view_model = StatisticalValuesViewModel()
    statistics = ['mean', 'variance', 'median', 'begining moment', 'central moment']

    def __init__(self):
        ttk.Frame.__init__(self)

        self.master.title("Statistical values calculator")
        self.master.geometry('300x300')
        self.master.resizable(width=True, height=False)

        self.x_label = tk.Label(self.master, text="Values list")
        self.x_label.grid(row=0, column=0, sticky=tk.W, pady=10, padx=10)
        self.x_values = tk.Entry(self.master)
        self.x_values.grid(row=0, column=1, columnspan=3, sticky=tk.W + tk.E, padx=10)

        self.k_label = tk.Label(self.master, text="Value k")
        self.k_label.grid(row=1, column=0, sticky=tk.W, pady=10, padx=10)
        self.k_value = tk.Entry(self.master)
        self.k_value.grid(row=1, column=1, columnspan=3, sticky=tk.W + tk.E, padx=10)

        self.statistic_label = tk.Label(self.master, text="Statistic type")
        self.statistic_label.grid(row=2, column=0, sticky=tk.W, padx=10, pady=10)
        self.statistics_listbox = tk.Listbox(self.master, width=30, height=6)
        for statistic in self.statistics:
            self.statistics_listbox.insert(tk.END, statistic)
        self.statistics_listbox.grid(row=2, column=1, padx=10)

        self.button = tk.Button(self.master, text='Calculate')
        self.button.grid(row=3, column=0, sticky=tk.W, padx=10, pady=10)

        self.result = tk.Label(self.master, text='Result: ')
        self.result.grid(row=4, column=0, sticky=tk.W, pady=10, padx=10, columnspan=3)

        self.error_message = tk.Label(self.master, text='')
        self.error_message.grid(row=5, column=0, sticky=tk.W, pady=10, padx=10, columnspan=3)

        self.bind_events()
        self.mvvm_back_bind()

    def bind_events(self):
        self.button.bind('<Button-1>', self.button_clicked)
        self.x_values.bind('<FocusOut>', self.x_values_changed)
        self.k_value.bind('<FocusOut>', self.k_value_changed)
        self.statistics_listbox.bind('<<ListboxSelect>>', self.statistics_listbox_changed)

    def mvvm_bind(self):
        x_set = self.view_model.set_x(self.x_values.get())
        if not x_set:
            self.view_model.set_button_state('disabled')

        current_selection = self.statistics_listbox.curselection()
        if current_selection:
            if (current_selection[0] == 3 or current_selection[0] == 4):
                k_set = self.view_model.set_k(self.k_value.get())
                if not k_set:
                    self.view_model.set_button_state('disabled')

    def mvvm_back_bind(self):
        self.x_values.delete(0, tk.END)
        self.x_values.insert(tk.INSERT, self.view_model.get_x())

        self.k_value.delete(0, tk.END)
        self.k_value.insert(tk.INSERT, self.view_model.get_k())

        self.result.config(text='{}'.format(self.view_model.get_result()))

        self.button.config(state=self.view_model.get_button_state())
        self.error_message.config(text='{}'.format(self.view_model.get_error_message()))

    def button_clicked(self, event):
        self.mvvm_bind()
        self.view_model.compute()
        self.mvvm_back_bind()

    def x_values_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def k_value_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def statistics_listbox_changed(self, event):
        self.mvvm_bind()
        current_selection = self.statistics_listbox.curselection()
        if len(current_selection) > 0:
            self.view_model.set_statistic(self.statistics[current_selection[0]])
        else:
            self.view_model.set_button_state('disabled')
        self.mvvm_back_bind()
