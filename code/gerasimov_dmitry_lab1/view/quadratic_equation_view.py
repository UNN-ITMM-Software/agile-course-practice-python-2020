import tkinter as tk

from gerasimov_dmitry_lab1.viewmodel.quadratic_equation_viewmodel import QuadraticEquationViewModel


def get_result_text(value):
    if value is None:
        return "Result"
    elif not value:
        return "Empty"
    else:
        return value


def get_error_text(value):
    return value if value else ''


def get_log_messages(messages):
    result_str = ''
    for message in messages:
        result_str += message + '\n'
    return result_str


class GUIView(object):
    view_model = QuadraticEquationViewModel()

    def __init__(self):
        self.root = tk.Tk()
        self.root['bg'] = 'maroon1'
        self.root.title('Solve quadratic equation')
        self.root.geometry('600x300')
        self.root.resizable(width=False, height=True)

        self.frame = tk.Frame(self.root, bg='SkyBlue1')
        self.title = tk.Label(self.frame, text='Введите начало и конец промежутка', bg='gray21', font=40)

        self.a_value = tk.Entry(self.frame, bg='white', state='normal')
        self.b_value = tk.Entry(self.frame, bg='white')
        self.c_value = tk.Entry(self.frame, bg='white')

        self.btn = tk.Button(self.frame, text='Solve', bg='gray21')
        self.res = tk.Label(self.frame, text='Result', bg='gray21', font=40)
        self.error_field = tk.Label(self.frame, text='', fg='red', bg='gray21', font=('', 12, 'bold'))
        self.logger_field = tk.Label(self.frame, text='Log:', bg='#619eb3', font=6)

        self.set_weight_to_grid()
        self.bind_events()

        self.mvvm_bind()
        self.mvvm_back_bind()
        self.root.mainloop()

    def set_weight_to_grid(self):
        self.root.grid_rowconfigure(2, minsize=30)
        self.root.grid_rowconfigure(5, minsize=30, weight=60)
        self.frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

        self.a_value.grid(row=1, column=0, stick='wens', padx=5, pady=5)
        self.b_value.grid(row=1, column=2, stick='wens', padx=5, pady=5)
        self.c_value.grid(row=1, column=4, stick='wens', padx=5, pady=5)

        self.btn.grid(row=2, column=1, stick='wens')
        self.res.grid(row=4, column=0, columnspan=3, stick='we', padx=5)
        self.error_field.grid(row=5, column=0, columnspan=3, stick='we', padx=5)
        self.logger_field.grid(row=0, column=3, stick='ns', rowspan=30)

    def bind_events(self):
        self.a_value.bind('<KeyRelease>', self.change_a)
        self.b_value.bind('<KeyRelease>', self.change_b)
        self.c_value.bind('<KeyRelease>', self.change_c)
        self.btn.bind('<Button-1>', self.btn_clicked)

    def btn_clicked(self, event):
        self.mvvm_bind()
        self.view_model.perform()
        self.mvvm_back_bind()

    def change_a(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def change_b(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def change_c(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def mvvm_bind(self):
        self.view_model.set_a(self.a_value.get())
        self.view_model.set_b(self.b_value.get())
        self.view_model.set_c(self.c_value.get())

    def mvvm_back_bind(self):
        self.a_value.delete(0, tk.END)
        self.a_value.insert(tk.END, self.view_model.get_a())

        self.b_value.delete(0, tk.END)
        self.b_value.insert(tk.END, self.view_model.get_b())

        self.c_value.delete(0, tk.END)
        self.c_value.insert(tk.END, self.view_model.get_c())

        self.btn.config(state=self.view_model.is_button_enable())

        self.res.config(text='{}\n'.format(get_result_text(self.view_model.get_result())))
        self.error_field.config(text='{}\n'.format(get_error_text(self.view_model.get_error_message())))
        self.logger_field.config(text='%s\n' % (get_log_messages(self.view_model.logger.get_log_messages())))
