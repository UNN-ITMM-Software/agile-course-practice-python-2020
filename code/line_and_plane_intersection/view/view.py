import tkinter as tk
from tkinter import ttk

from line_and_plane_intersection.viewmodel import viewmodel

class GUI(ttk.Frame):
    default_sticky = tk.W + tk.E + tk.N + tk.S

    view_model = viewmodel.ViewModel()

    def bind_events(self):
        self.btn_intercept.bind('<Button-1>', self.is_intercept_clicked)
        self.txt_x_in.bind('<KeyRelease>', self.txt_x_in_changed)
        self.txt_y_in.bind('<KeyRelease>', self.txt_y_in_changed)
        self.txt_z_in.bind('<KeyRelease>', self.txt_z_in_changed)
        self.line_point_1.bind('<Button-1>', self.point_clicked)
        self.line_point_2.bind('<Button-1>', self.point_clicked)
        self.plane_point_1.bind('<Button-1>', self.point_clicked)
        self.plane_point_2.bind('<Button-1>', self.point_clicked)
        self.plane_point_3.bind('<Button-1>', self.point_clicked)

    def mvvm_bind(self):
        self.view_model.set_x_y_z(
            [self.txt_x_in.get(), self.txt_y_in.get(), self.txt_z_in.get()])

        # self.view_model.set_color_space_in(self.txt_color_space.get())
        # self.view_model.set_color_space_out(self.txt_out_color_space.get())
        #
        # self.txt_error_message.config(text=self.view_model.logger.get_log())
        # self.txt_error_message.update_idletasks()

    def mvvm_back_bind(self):
        pass
        # self.txt_color_space.delete(0, tk.END)
        # # self.txt_color_space.insert(tk.INSERT, self.view_model.get_color_space_in())
        #
        # # color_in = self.view_model.get_color_in()
        #
        # self.txt_x_in.delete(0, tk.END)
        # # self.txt_x_in.insert(0, color_in[0])
        # self.txt_y_in.delete(0, tk.END)
        # # self.txt_y_in.insert(0, color_in[1])
        # self.txt_z_in.delete(0, tk.END)
        # # self.txt_z_in.insert(0, color_in[2])
        #
        # self.txt_out_color_space.delete(0, tk.END)
        # # self.txt_out_color_space.insert(tk.INSERT, self.view_model.get_color_space_out())
        #
        # # color_out = self.view_model.get_color_out()
        #
        # self.txt_x_out.delete(0, tk.END)
        # # self.txt_x_out.insert(0, color_out[0])
        # self.txt_y_out.delete(0, tk.END)
        # # self.txt_y_out.insert(0, color_out[1])
        # self.txt_z_out.delete(0, tk.END)
        # # self.txt_z_out.insert(0, color_out[2])
        #
        # # self.btn_convert.config(state=self.view_model.get_button_convert_state())
        #
        # # self.txt_error_message.config(text=self.view_model.logger.get_log())
        # self.txt_error_message.update_idletasks()

    def __init__(self):
        ttk.Frame.__init__(self)
        self.master.title("Line/plane interception")

        self.grid(sticky=self.default_sticky)

        self.line_label = tk.Label(self, width=30, text="Line", borderwidth=2, relief="groove")
        self.line_label.grid(row=0, column=0, columnspan=2)

        self.line_point_1 = ttk.Button(self, text='point 1', width=15)
        self.line_point_1.grid(row=1, column=0, sticky=self.default_sticky, rowspan=3)
        self.line_point_2 = ttk.Button(self, text='point 2', width=15)
        self.line_point_2.grid(row=1, column=1, sticky=self.default_sticky)

        self.plane_label = tk.Label(self, width=30, text="Plane", borderwidth=2, relief="groove")
        self.plane_label.grid(row=0, column=2, columnspan=3)

        self.plane_point_1 = ttk.Button(self, text='point 1', width=10)
        self.plane_point_1.grid(row=1, column=2,
                                sticky=self.default_sticky)
        self.plane_point_2 = ttk.Button(self, text='point 2', width=10)
        self.plane_point_2.grid(row=1, column=3,
                                sticky=self.default_sticky)
        self.plane_point_3 = ttk.Button(self, text='point 3', width=10)
        self.plane_point_3.grid(row=1, column=4,
                                sticky=self.default_sticky)

        self.txt_x_in = tk.Entry(self, width=10)
        self.txt_x_in.grid(row=3, column=0, sticky=self.default_sticky)
        self.txt_y_in = tk.Entry(self, width=10)
        self.txt_y_in.grid(row=3, column=1, sticky=self.default_sticky)
        self.txt_z_in = tk.Entry(self, width=10)
        self.txt_z_in.grid(row=3, column=2, sticky=self.default_sticky)

        self.btn_intercept = ttk.Button(self, text='Is interception')
        self.btn_intercept.grid(row=0, column=5,
                              sticky=self.default_sticky)

        self.label_is_interception = tk.Label(self, height=3, width=15, wraplength=150, relief="groove")
        self.label_is_interception.grid(row=1, column=5)

        self.bind_events()
        self.mvvm_back_bind()

    def is_intercept_clicked(self, event):
        self.mvvm_bind()
        self.view_model.is_intercept()
        self.mvvm_back_bind()
    #
    def txt_x_in_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def txt_y_in_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def txt_z_in_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def point_clicked(self, event):
        self.view_model.set_current_point(str(event.widget))

        self.txt_x_in.delete(0, tk.END)
        self.txt_x_in.insert(0, self.view_model.get_x_y_z()[0])

        self.txt_y_in.delete(0, tk.END)
        self.txt_y_in.insert(0, self.view_model.get_x_y_z()[1])

        self.txt_z_in.delete(0, tk.END)
        self.txt_z_in.insert(0, self.view_model.get_x_y_z()[2])

        # self.mvvm_bind()
        # self.mvvm_back_bind()


