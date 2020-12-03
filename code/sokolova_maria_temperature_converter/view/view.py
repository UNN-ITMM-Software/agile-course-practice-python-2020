import tkinter as tk
from tkinter import ttk

from sokolova_maria_temperature_converter.viewmodel.viewmodel import TemperatureConverterViewModel


class GUIView(tk.Frame):
    CAST_TYPES = ['fahrenheit', 'kelvin', 'newton']
    view_model = TemperatureConverterViewModel()

    def convert(self):
        self.view_model.set_input_value(self.text_value.get(1.0, tk.END))
        self.view_model.set_cast_type(self.CAST_TYPES[self.cast_types.current()])
        self.view_model.convert()
        self.result_label.configure(text=self.view_model.get_output_value())
        self.error_label.configure(text=self.view_model.get_error())

    def __init__(self):
        tk.Frame.__init__(self)
        self.master.title("Temperature converter")
        self.master.minsize(width=150, height=150)
        self.grid(sticky=tk.W + tk.E + tk.N + tk.S)

        self.celsius_label = tk.Label(self, text="From celsius", fg='black', font="Arial 14")
        self.celsius_label.pack()

        self.text_value = tk.Text(self, height=1, width=30, font="Arial 14")
        self.text_value.pack()

        self.cast_types_label = tk.Label(self, text="to", fg='black', font="Arial 14")
        self.cast_types_label.pack()

        self.cast_types = ttk.Combobox(self, height=1, width=30, values=self.CAST_TYPES, font="Arial 14")
        self.cast_types.current(0)
        self.cast_types.pack()

        self.convert = tk.Button(self, text="convert", width=15, height=1, font="Arial 14", bg="light blue",
                                 command=self.convert)
        self.convert.pack()

        self.result_label = tk.Label(self, text="", fg='black', font="Arial 14")
        self.result_label.pack()

        self.error_label = tk.Label(self, text="", fg='black', font="Arial 14")
        self.error_label.pack()
