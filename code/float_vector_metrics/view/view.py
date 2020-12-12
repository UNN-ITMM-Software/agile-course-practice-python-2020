import tkinter as tk
from tkinter import ttk

from float_vector_metrics.viewmodel.viewmodel import VectorMetricsViewModel


class GUI(ttk.Frame):
    view_model = VectorMetricsViewModel()
    metrics = ['L1', 'L2', 'L3', 'L4', 'Linf']

    def __init__(self):
        ttk.Frame.__init__(self)
        self.master.title("Vector metrics calculator")

        self.x_label = tk.Label(self.master, text="First vector")
        self.x_label.grid(row=0, column=0)
        self.x_vector = tk.Entry(self.master)
        self.x_vector.grid(row=0, column=1, columnspan=2)

        self.y_label = tk.Label(self.master, text="Second vector")
        self.y_label.grid(row=1, column=0)
        self.y_vector = tk.Entry(self.master)
        self.y_vector.grid(row=1, column=1, columnspan=2)

        self.metric_label = tk.Label(self.master, text="Metric")
        self.metric_label.grid(row=0, column=3)
        self.metrics_listbox = tk.Listbox(self.master, width=5)
        for metr in self.metrics:
            self.metrics_listbox.insert(tk.END, metr)
        self.metrics_listbox.grid(row=1, column=3)

        self.button = tk.Button(self.master, text='Compute')
        self.button.grid(row=3, column=3)

        self.result = tk.Label(self.master, text='Result: ')
        self.result.grid(row=2, column=0, columnspan=2)

        self.error_message = tk.Label(self.master, text='', wraplength=150)
        self.error_message.grid(row=3, column=0, columnspan=2)

        self.bind_events()
        self.mvvm_back_bind()

    def bind_events(self):
        self.button.bind('<Button-1>', self.button_clicked)
        self.x_vector.bind('<FocusOut>', self.x_vector_changed)
        self.y_vector.bind('<FocusOut>', self.y_vector_changed)
        self.metrics_listbox.bind('<<ListboxSelect>>', self.metrics_listbox_changed)

    def mvvm_bind(self):
        x_set = self.view_model.set_x(self.x_vector.get())
        if not x_set:
            self.view_model.set_button_state('disabled')
            return
        y_set = self.view_model.set_y(self.y_vector.get())
        if not y_set:
            self.view_model.set_button_state('disabled')

    def mvvm_back_bind(self):
        self.x_vector.delete(0, tk.END)
        self.x_vector.insert(tk.INSERT, self.view_model.get_x())

        self.y_vector.delete(0, tk.END)
        self.y_vector.insert(tk.INSERT, self.view_model.get_y())

        self.result.config(text='{}'.format(self.view_model.get_result()))

        self.button.config(state=self.view_model.get_button_state())
        self.error_message.config(text='{}'.format(self.view_model.get_error_message()))

    def button_clicked(self, event):
        self.mvvm_bind()
        self.view_model.compute()
        self.mvvm_back_bind()

    def x_vector_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def y_vector_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def metrics_listbox_changed(self, event):
        self.mvvm_bind()
        current_selection = self.metrics_listbox.curselection()
        if len(current_selection) > 0:
            self.view_model.set_metric(self.metrics[current_selection[0]])
        else:
            self.view_model.set_button_state('disabled')
        self.mvvm_back_bind()
