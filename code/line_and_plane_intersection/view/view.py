import tkinter as tk
from tkinter import ttk

from line_and_plane_intersection.viewmodel import viewmodel


class GUI(ttk.Frame):
    default_sticky = tk.W + tk.E + tk.N + tk.S

    view_model = viewmodel.ViewModel()

    def bind_events(self):
        self.btn_intercept.bind('<Button-1>', self.is_intercept_clicked)

        self.txt_x_in.bind('<KeyRelease>', self.txt_changed)
        self.txt_y_in.bind('<KeyRelease>', self.txt_changed)
        self.txt_z_in.bind('<KeyRelease>', self.txt_changed)

        self.line_point_1.bind('<Button-1>', self.line_point_clicked)
        self.line_point_2.bind('<Button-1>', self.line_point_clicked)

        self.plane_point_1.bind('<Button-1>', self.plane_point_clicked)
        self.plane_point_2.bind('<Button-1>', self.plane_point_clicked)
        self.plane_point_3.bind('<Button-1>', self.plane_point_clicked)


        self.a_param.bind('<KeyRelease>', self.txt_changed)
        self.b_param.bind('<KeyRelease>', self.txt_changed)
        self.c_param.bind('<KeyRelease>', self.txt_changed)
        self.d_param.bind('<KeyRelease>', self.txt_changed)

    def mvvm_bind(self):
        self.view_model.set_x_y_z(
            [self.txt_x_in.get(), self.txt_y_in.get(), self.txt_z_in.get()])

        self.view_model.set_abcd([self.a_param.get(), self.b_param.get(), self.c_param.get(), self.d_param.get()])

        self.label_is_interception.config(text=self.view_model.interception_or_error_msg)
        self.label_is_interception.update_idletasks()

    def mvvm_back_bind(self):
        self.label_is_interception.config(text=self.view_model.interception_or_error_msg)
        self.label_is_interception.update_idletasks()

    def __init__(self):
        ttk.Frame.__init__(self)
        self.master.title("Line/plane interception")

        self.grid(sticky=self.default_sticky)

        self.line_label = tk.Label(self, width=30, text="Line", borderwidth=2, relief="groove")
        self.line_label.grid(row=0, column=0, columnspan=2)

        self.test = tk.IntVar()
        self.test.set(None)
        self.line_point_1 = ttk.Radiobutton(text="line pnt 1", variable=self.test, value=0, width=15)
        self.line_point_1.grid(row=1, column=0, sticky=self.default_sticky, rowspan=3)
        self.line_point_2 = ttk.Radiobutton(text="line pnt 2", variable=self.test, value=1, width=15)
        self.line_point_2.grid(row=1, column=1, sticky=self.default_sticky)

        self.plane_label = tk.Label(self, width=30, text="Plane", borderwidth=2, relief="groove")
        self.plane_label.grid(row=0, column=2, columnspan=3)

        self.plane_point_1 = ttk.Radiobutton(text="plane pnt 1", variable=self.test, value=3, width=10)
        self.plane_point_1.grid(row=1, column=2,
                                sticky=self.default_sticky)
        self.plane_point_2 = ttk.Radiobutton(text="plane pnt 2", variable=self.test, value=4, width=10)
        self.plane_point_2.grid(row=1, column=3,
                                sticky=self.default_sticky)
        self.plane_point_3 = ttk.Radiobutton(text="plane pnt 3", variable=self.test, value=5, width=10)
        self.plane_point_3.grid(row=1, column=4,
                                sticky=self.default_sticky)

        self.txt_x_in = tk.Entry(self, width=10)
        self.txt_x_in.grid(row=3, column=0, sticky=self.default_sticky)
        self.txt_y_in = tk.Entry(self, width=10)
        self.txt_y_in.grid(row=3, column=1, sticky=self.default_sticky)
        self.txt_z_in = tk.Entry(self, width=10)
        self.txt_z_in.grid(row=3, column=2, sticky=self.default_sticky)

        self.abcd_label = tk.Label(self, width=30, text="abcd params: ", borderwidth=2, relief="groove")
        self.abcd_label.grid(row=4, column=0, columnspan=2)

        self.a_param = tk.Entry(self, width=10)
        self.a_param.grid(row=4, column=1, sticky=self.default_sticky)
        self.b_param = tk.Entry(self, width=10)
        self.b_param.grid(row=4, column=2, sticky=self.default_sticky)
        self.c_param = tk.Entry(self, width=10)
        self.c_param.grid(row=4, column=3, sticky=self.default_sticky)
        self.d_param = tk.Entry(self, width=10)
        self.d_param.grid(row=4, column=4, sticky=self.default_sticky)

        self.btn_intercept = ttk.Button(self, text='Is interception')
        self.btn_intercept.grid(row=0, column=5,
                                sticky=self.default_sticky)

        self.label_is_interception = tk.Label(self, height=3, width=15, wraplength=150, relief="groove")
        self.label_is_interception.grid(row=1, column=5)

        self.bind_events()
        self.mvvm_back_bind()

    def is_intercept_clicked(self, event):
        self.mvvm_bind()
        self.view_model.is_intersect()
        self.mvvm_back_bind()

    def txt_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def plane_point_clicked(self, event):
        self.view_model.set_current_point_for_plane(str(event.widget))
        self._point_clicked(event)

    def line_point_clicked(self, event):
        self.view_model.set_current_point_for_line(str(event.widget))
        self._point_clicked(event)

    def _point_clicked(self, event):
        for i, entry in enumerate([self.txt_x_in, self.txt_y_in, self.txt_z_in]):
            entry.delete(0, tk.END)
            entry.insert(0, self.view_model.get_x_y_z()[i])
