import tkinter as tk

from tkinter import ttk
from viewmodel import viewmodel


class GUIView(object):

    view_model = viewmodel.BisymmetricMatrixViewModel()
    value_of_combobox = ['2x2', '3x3', '4x4', '5x5', '6x6']

    def __init__(self):
        self.root = tk.Tk()
        self.root['bg'] = '#333'
        self.root.title('Бисимметричные матрицы')
        self.root.geometry('450x400')
        self.root.resizable(width=True, height=True)

        self.frame1 = tk.LabelFrame(self.root, text='Создание рандомной бисимметричной матрицы',
                                    bg='#619eb3', bd=5)
        self.frame2 = tk.LabelFrame(self.root, text='Создание бисимметричной матрицы из заданного вектора',
                                    bg='#619eb3', bd=5)
        self.label1 = tk.Label(self.frame1, text='Выбор размера матрицы')
        self.select_size_of_matrix = ttk.Combobox(self.frame1, state="readonly",
                                                  values=self.value_of_combobox)
        self.button1 = tk.Button(self.frame1, text='Создать')
        self.result1 = tk.Label(self.frame1, height=10, width=30)
        self.label2 = tk.Label(self.frame2, text='Ввод вектора')
        self.input_vector = tk.Text(self.frame2, height=1, width=38)
        self.button2 = tk.Button(self.frame2, text='Создать')
        self.result2 = tk.Label(self.frame2, height=10, width=30)

        self.bind_events()
        self.mvvm_back_bind()
        self.mvvm_back_bind_from_vector()

        self.set_weight_to_grid()
        self.root.mainloop()

    def set_weight_to_grid(self):
        self.root.grid_rowconfigure(2, minsize=30)
        self.root.grid_rowconfigure(5, minsize=30, weight=60)
        self.frame1.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)
        self.frame2.place(relx=0.05, rely=0.50, relwidth=0.9, relheight=0.9)
        self.label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        self.select_size_of_matrix.grid(row=0, column=2, columnspan=2, padx=5, pady=5)
        self.button1.grid(row=1, column=0, padx=5, pady=5, sticky=tk.NW)
        self.result1.grid(row=1, column=1, columnspan=4, padx=5, pady=5)
        self.label2.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky=tk.W)
        self.input_vector.grid(row=0, column=2, columnspan=3, padx=5, pady=5, sticky=tk.E)
        self.button2.grid(row=1, column=0, padx=5, pady=5, sticky=tk.NW)
        self.result2.grid(row=1, column=2, columnspan=5, padx=5, pady=5, sticky=tk.E)

    def bind_events(self):
        self.input_vector.bind('<KeyRelease>', self.txt_changed)
        self.select_size_of_matrix.bind('<<ComboboxSelected>>', self.matrix_size_selected)
        self.button1.bind('<Button-1>', self.create_random_matrix_clicked)
        self.button2.bind('<Button-1>', self.create_matrix_from_vector_clicked)

    def matrix_size_selected(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def create_random_matrix_clicked(self, event):
        self.mvvm_bind()
        self.view_model.create_random_matrix()
        self.mvvm_back_bind()

    def mvvm_back_bind(self):
        self.button1.config(state=self.view_model.get_button_convert_state())
        self.result1.config(text=self.view_model.get_created_random_matrix(), anchor=tk.N)

    def mvvm_bind(self):
        self.view_model.set_matrix_size(self.value_of_combobox[self.select_size_of_matrix.current()])

    def txt_changed(self, event):
        self.mvvm_bind_from_vector()
        self.mvvm_back_bind_from_vector()

    def create_matrix_from_vector_clicked(self, event):
        self.mvvm_bind_from_vector()
        self.view_model.create_matrix_from_vector()
        self.mvvm_back_bind_from_vector()

    def mvvm_back_bind_from_vector(self):
        self.button2.config(state=self.view_model.get_button_convert_state())
        self.result2.config(text=self.view_model.get_created_matrix_from_vector())

    def mvvm_bind_from_vector(self):
        self.view_model.set_vector(self.input_vector.get("1.0", tk.END).strip())
