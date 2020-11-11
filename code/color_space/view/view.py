import tkinter as tk
from tkinter import ttk

from color_space.viewmodel import viewmodel


class GUI(ttk.Frame):
    default_sticky = tk.W + tk.E + tk.N + tk.S
    view_model = viewmodel.ViewModel()

    def bind_events(self):
        self.btn_convert.bind('<Button-1>', self.convert_clicked)
        self.txt_x_in.bind('<KeyRelease>', self.txt_x_in_changed)
        self.txt_y_in.bind('<KeyRelease>', self.txt_y_in_changed)
        self.txt_z_in.bind('<KeyRelease>', self.txt_z_in_changed)
        self.txt_color_space.bind('<KeyRelease>', self.color_space_in_changed)
        self.txt_out_color_space.bind('<KeyRelease>', self.color_space_out_changed)

    def mvvm_bind(self):
        self.view_model.set_color_in(
            [self.txt_x_in.get(), self.txt_y_in.get(), self.txt_z_in.get()])

        self.view_model.set_color_space_in(self.txt_color_space.get())
        self.view_model.set_color_space_out(self.txt_out_color_space.get())

        self.txt_error_message.config(text=self.view_model.logger.get_log())
        self.txt_error_message.update_idletasks()

    def mvvm_back_bind(self):
        self.txt_color_space.delete(0, tk.END)
        self.txt_color_space.insert(tk.INSERT, self.view_model.get_color_space_in())

        color_in = self.view_model.get_color_in()

        self.txt_x_in.delete(0, tk.END)
        self.txt_x_in.insert(0, color_in[0])
        self.txt_y_in.delete(0, tk.END)
        self.txt_y_in.insert(0, color_in[1])
        self.txt_z_in.delete(0, tk.END)
        self.txt_z_in.insert(0, color_in[2])

        self.txt_out_color_space.delete(0, tk.END)
        self.txt_out_color_space.insert(tk.INSERT, self.view_model.get_color_space_out())

        color_out = self.view_model.get_color_out()

        self.txt_x_out.delete(0, tk.END)
        self.txt_x_out.insert(0, color_out[0])
        self.txt_y_out.delete(0, tk.END)
        self.txt_y_out.insert(0, color_out[1])
        self.txt_z_out.delete(0, tk.END)
        self.txt_z_out.insert(0, color_out[2])

        self.btn_convert.config(state=self.view_model.get_button_convert_state())

        self.txt_error_message.config(text=self.view_model.logger.get_log())
        self.txt_error_message.update_idletasks()

    def __init__(self):
        ttk.Frame.__init__(self)
        self.master.title("Color space converter")

        self.grid(sticky=self.default_sticky)

        self.txt_color_space = tk.Entry(self, width=15)
        self.txt_color_space.grid(row=0, column=0)

        self.txt_x_in = tk.Entry(self, width=10)
        self.txt_x_in.grid(row=1, column=0, sticky=self.default_sticky)
        self.txt_y_in = tk.Entry(self, width=10)
        self.txt_y_in.grid(row=2, column=0, sticky=self.default_sticky)
        self.txt_z_in = tk.Entry(self, width=10)
        self.txt_z_in.grid(row=3, column=0, sticky=self.default_sticky)

        self.txt_out_color_space = tk.Entry(self, width=15)
        self.txt_out_color_space.grid(row=0, column=2)

        self.txt_x_out = tk.Entry(self, width=10)
        self.txt_x_out.grid(row=1, column=2, sticky=self.default_sticky)
        self.txt_y_out = tk.Entry(self, width=10)
        self.txt_y_out.grid(row=2, column=2, sticky=self.default_sticky)
        self.txt_z_out = tk.Entry(self, width=10)
        self.txt_z_out.grid(row=3, column=2, sticky=self.default_sticky)

        self.btn_convert = ttk.Button(self, text='Convert')
        self.btn_convert.grid(row=0, column=3, rowspan=1,
                              sticky=self.default_sticky)

        self.txt_error_message = tk.Label(self, height=3, width=15, wraplength=150)
        self.txt_error_message.grid(row=1, column=3, rowspan=3)

        self.bind_events()
        self.mvvm_back_bind()

    def convert_clicked(self, event):
        self.mvvm_bind()
        self.view_model.convert()
        self.mvvm_back_bind()

    def txt_x_in_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def txt_y_in_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def txt_z_in_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def color_space_in_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def color_space_out_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()
