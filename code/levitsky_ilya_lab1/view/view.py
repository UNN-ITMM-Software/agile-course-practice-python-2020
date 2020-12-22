import tkinter as tk
from levitsky_ilya_lab1.viewmodel.viewmodel import VolumeViewModel


def get_result_text(value):
    if value is None:
        return "NaN"
    else:
        return value


def get_error_text(value):
    return value if value is not None else ''


def get_log_messages(messages):
    result_str = '\n'.join([message for message in messages])
    return result_str


class GUIView:
    view_model = VolumeViewModel()

    def __init__(self):
        self.label = None
        self.root = tk.Tk()
        self.root['bg'] = '#fafafa'
        self.root.title('Volume')
        self.root.geometry('450x200')
        self.root.resizable(width=False, height=True)
        self.var = tk.IntVar()
        self.var.set(0)

        self.frame = tk.Frame(self.root, bg='#ebebeb')
        self.title = tk.Label(self.frame, text='Choose figure', bg='#ababab', font=40)
        self.r1 = tk.Radiobutton(self.frame, text='Cube', variable=self.var, value=0)
        self.r2 = tk.Radiobutton(self.frame, text='Sphere', variable=self.var, value=1)
        self.r3 = tk.Radiobutton(self.frame, text='Cylinder', variable=self.var, value=2)

        self.title2 = tk.Label(self.frame, text='Enter height and width', bg='#ababab', font=40)
        self.labradius = tk.Label(self.frame, text='radius =', font=40)
        self.labheight = tk.Label(self.frame, text='height =', font=40)
        self.input_radius = tk.Entry(self.frame, bg='white', state='normal')
        self.input_height = tk.Entry(self.frame, bg='white')
        self.btn = tk.Button(self.frame, text='Calculate volume', bg='#ababab')
        self.res = tk.Label(self.frame, text='', fg='black', bg='#ababab', font=('', 12, 'bold'))
        self.error_field = tk.Label(self.frame, text='', fg='black', bg='#619eb3', font=('', 12, 'bold'))
        self.logger_field = tk.Label(self.frame, text='Log:', bg='#619eb3', font=6)

        self.set_weight_to_grid()
        self.bind_events()

        self.mvvm_bind()
        self.mvvm_back_bind()
        self.root.mainloop()

    def set_weight_to_grid(self):
        self.root.grid_rowconfigure(5, minsize=30, weight=60)
        self.frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)
        self.title.grid(row=0, column=0, columnspan=4, stick='we')
        self.r1.grid(row=1, column=0, padx=5,  pady=5)
        self.r2.grid(row=1, column=1, columnspan=2, stick='wens')
        self.r3.grid(row=1, column=3, padx=5,  pady=5)
        self.title2.grid(row=2, column=0, columnspan=4, stick='we')
        self.labradius.grid(row=3, column=0, stick='wens', padx=5, pady=5)
        self.input_radius.grid(row=3, column=1, stick='wens', padx=5, pady=5)
        self.labheight.grid(row=3, column=2, stick='wens', padx=5, pady=5)
        self.input_height.grid(row=3, column=3, stick='wens', padx=5, pady=5)
        self.btn.grid(row=4, column=1, columnspan=2, stick='ens')
        self.res.grid(row=6, column=0, columnspan=4, stick='wes', pady=5)
        self.logger_field.grid(row=0, column=3, stick='ns', rowspan=30)

    def bind_events(self):
        self.input_radius.bind('<KeyRelease>', self.first_input_changed)
        self.input_height.bind('<KeyRelease>', self.second_input_changed)
        self.btn.bind('<Button-1>', self.btn_clicked)

    def btn_clicked(self, event):
        self.mvvm_bind()
        self.view_model.perform()
        self.mvvm_back_bind()

    def first_input_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def second_input_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def mvvm_bind(self):
        self.view_model.set_start_value(self.input_radius.get())
        self.view_model.set_end_value(self.input_height.get())
        self.view_model.set_figure_type(self.var.get())

    def mvvm_back_bind(self):
        self.input_radius.delete(0, tk.END)
        self.input_radius.insert(tk.END, self.view_model.get_start_value())

        self.input_height.delete(0, tk.END)
        self.input_height.insert(tk.END, self.view_model.get_end_value())

        self.btn.config(state=self.view_model.is_button_enable())

        self.res.config(text='%s\n' % (get_result_text(self.view_model.get_result())))
        self.logger_field.config(text='%s\n' % (get_log_messages(self.view_model.logger.get_log_messages())))
