import tkinter as tk

from tkinter import ttk
from viewmodel import viewmodel


class GUIView(object):

    view_model = viewmodel.BisymmetricMatrixViewModel()

    def __init__(self):
        self.root = tk.Tk()
        self.root['bg'] = '#333'
        self.root.title('Бисимметричные матрицы')
        self.root.geometry('500x400')
        self.root.resizable(width=True, height=True)

        val = ['2x2', '3x3', '4x4', '5x5', '6x6']

        self.frame1 = tk.LabelFrame(self.root, text='Создание рандомной бисимметричной матрицы',
                                    bg='#619eb3', bd=5)
        self.frame2 = tk.LabelFrame(self.root, text='Создание бисимметричной матрицы из заданного вектора',
                                    bg='#619eb3', bd=5)
        self.label1 = tk.Label(self.frame1, text='Выбор размера матрицы')
        self.combobox1 = ttk.Combobox(self.frame1, values=val)
        self.button1 = tk.Button(self.frame1, text='Создать')
        self.result1 = tk.Label(self.frame1, text='Здесь будет результат')
        self.label2 = tk.Label(self.frame2, text='Ввод вектора')
        self.input_vector = tk.Entry(self.frame2)
        self.button2 = tk.Button(self.frame2, text='Создать')
        self.result2 = tk.Label(self.frame2, text='Здесь будет результат')

        self.set_weight_to_grid()

        self.mvvm_bind()
        self.mvvm_back_bind()
        self.root.mainloop()

    def set_weight_to_grid(self):
        self.root.grid_rowconfigure(2, minsize=30)
        self.root.grid_rowconfigure(5, minsize=30, weight=60)
        self.frame1.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)
        self.frame2.place(relx=0.05, rely=0.50, relwidth=0.9, relheight=0.9)
        self.label1.grid(row=0, column=0, padx=5, pady=5)
        self.combobox1.grid(row=0, column=1, padx=5, pady=5)
        self.button1.grid(row=1, column=0, padx=5, pady=5)
        self.result1.grid(row=1, column=1, padx=5, pady=5)
        self.label2.grid(row=0, column=0, padx=5, pady=5)
        self.input_vector.grid(row=0, column=1, padx=5, pady=5)
        self.button2.grid(row=1, column=0, padx=5, pady=5)
        self.result2.grid(row=1, column=1, padx=5, pady=5)

    def bind_events(self):
        self.input_vector.bind('<KeyRelease', self.write_vector)

    def write_vector(self):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def mvvm_back_bind(self):
        self.view_model.get_vector(self.input_vector.get())

    def mvvm_bind(self):
        self.button2.config(state=self.view_model.is_create_matrix_from_vector_button_enabled())
