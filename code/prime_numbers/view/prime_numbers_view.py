import tkinter as tk

from prime_numbers.viewmodel.prime_numbers_viewmodel import PrimeNumberViewModel


def get_result_text(value):
    if value is None:
        return "Здесь будет результат"
    elif not value:
        return "Пусто"
    else:
        return value


def get_error_text(value):
    return value if value is not None else ''


class GUIView:
    view_model = PrimeNumberViewModel()

    def __init__(self):
        self.root = tk.Tk()
        self.root['bg'] = '#fafafa'
        self.root.title('Печать всех простых чисел')
        self.root.geometry('600x300')
        self.root.resizable(width=False, height=True)

        self.frame = tk.Frame(self.root, bg='#2b4a54')
        self.title = tk.Label(self.frame, text='Введите начало и конец промежутка', bg='#619eb3', font=40)
        self.input_start_value = tk.Entry(self.frame, bg='white', state='normal')
        self.input_end_value = tk.Entry(self.frame, bg='white')
        self.btn = tk.Button(self.frame, text='Вывод простых чисел', bg='#6dcae8')
        self.res = tk.Label(self.frame, text='Здесь будет результат', bg='#619eb3', font=40)
        self.error_field = tk.Label(self.frame, text='', fg='red', bg='#619eb3', font=('', 12, 'bold'))

        self.set_weight_to_grid()
        self.bind_events()

        self.mvvm_bind()
        self.mvvm_back_bind()
        self.root.mainloop()

    def set_weight_to_grid(self):
        self.root.grid_rowconfigure(2, minsize=30)
        self.root.grid_rowconfigure(5, minsize=30, weight=60)
        self.frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)
        self.title.grid(row=0, column=0, columnspan=3, stick='we', padx=5)
        self.input_start_value.grid(row=1, column=0, stick='wens', padx=5, pady=5)
        self.input_end_value.grid(row=1, column=2, stick='wens', padx=5, pady=5)
        self.btn.grid(row=2, column=1, stick='wens')
        self.res.grid(row=4, column=0, columnspan=3, stick='we', padx=5)
        self.error_field.grid(row=5, column=0, columnspan=3, stick='we', padx=5)

    def bind_events(self):
        self.input_start_value.bind('<KeyRelease>', self.first_input_changed)
        self.input_end_value.bind('<KeyRelease>', self.second_input_changed)
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
        self.view_model.set_start_value(self.input_start_value.get())
        self.view_model.set_end_value(self.input_end_value.get())

    def mvvm_back_bind(self):
        self.input_start_value.delete(0, tk.END)
        self.input_start_value.insert(tk.END, self.view_model.get_start_value())

        self.input_end_value.delete(0, tk.END)
        self.input_end_value.insert(tk.END, self.view_model.get_end_value())

        self.btn.config(state=self.view_model.is_button_enable())

        self.res.config(text='%s\n' % (get_result_text(self.view_model.get_result())))
        self.error_field.config(text='%s\n' % (get_error_text(self.view_model.get_error_message())))
