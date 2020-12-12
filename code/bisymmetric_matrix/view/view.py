import tkinter as tk

from tkinter import ttk


class GUIView(object):

    def __init__(self):
        self.root = tk.Tk()
        self.root['bg'] = '#333'
        self.root.title('Бисимметричные матрицы')
        self.root.geometry('500x400')
        self.root.resizable(width=True, height=True)

        val = ['2x2', '3x3', '4x4', '5x5', '6x6']

        self.frame1 = tk.LabelFrame(self.root, text='Создание рандомной бисимметричной матрицы', bg='#619eb3', bd=5)
        self.frame2 = tk.LabelFrame(self.root, text='Создание бисимметричной матрицы из заданного вектора',
                                    bg='#619eb3', bd=5)
        self.frame3 = tk.LabelFrame(self.root, text='Проверка матрицы на бисимметричность', bg='#619eb3', bd=5)
        self.label1 = tk.Label(self.frame1, text='Выбор размера матрицы')
        self.combobox1 = ttk.Combobox(self.frame1, values=val)
        self.label2 = tk.Label(self.frame2, text='Ввод вектора')
        self.input_vector = tk.Entry(self.frame2)
        self.label31 = tk.Label(self.frame3, text='Выбор размера матрицы')
        self.combobox3 = ttk.Combobox(self.frame3, values=val)
        self.label32 = tk.Label(self.frame3, text='Ввод матрицы')
        self.button1 = tk.Button(self.frame1, text='Создать')
        self.button2 = tk.Button(self.frame2, text='Создать')
        self.button3 = tk.Button(self.frame3, text='Результат')

        self.set_weight_to_grid()
        self.create_matrix_window(3)

        self.root.mainloop()

    def set_weight_to_grid(self):
        self.root.grid_rowconfigure(2, minsize=30)
        self.root.grid_rowconfigure(5, minsize=30, weight=60)
        self.frame1.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)
        self.frame2.place(relx=0.05, rely=0.35, relwidth=0.9, relheight=0.9)
        self.frame3.place(relx=0.05, rely=0.65, relwidth=0.9, relheight=0.9)
        self.label1.grid(row=0, column=0, padx=5, pady=5)
        self.combobox1.grid(row=0, column=1, padx=5, pady=5)
        self.button1.grid(row=1, column=0, padx=5, pady=5)
        self.label2.grid(row=0, column=0, padx=5, pady=5)
        self.input_vector.grid(row=0, column=1, padx=5, pady=5)
        self.button2.grid(row=1, column=0, padx=5, pady=5)
        self.label31.grid(row=0, column=0, padx=5, pady=5)
        self.combobox3.grid(row=0, column=1, columnspan=3, padx=5, pady=5)
        self.label32.grid(row=1, column=0, rowspan=3, padx=5, pady=5)
        self.button3.grid(row=4, column=0, padx=5, pady=5)

    def create_matrix_window(self, matrix_size):
        matrix = []
        for i in range(matrix_size):
            matrix.append([])
            for j in range(matrix_size):
                matrix[i].append(tk.Button(
                    self.frame3,
                    height=1,
                    width=3,
                    bg="White"
                ))
                matrix[i][j].grid(row=i+1, column=j+1)
