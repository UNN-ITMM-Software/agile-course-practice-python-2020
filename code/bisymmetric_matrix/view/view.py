import tkinter as tk

from viewmodel import viewmodel


class GUIView(object):

    view_model = viewmodel.BisymmetricMatrixViewModel()
    value_of_combobox = ['2x2', '3x3', '4x4', '5x5', '6x6']

    def __init__(self):
        self.root = tk.Tk()
        self.root['bg'] = '#333'
        self.root.title('Бисимметричные матрицы')
        self.root.geometry('500x400')
        self.root.resizable(width=True, height=True)

        self.frame1 = tk.LabelFrame(self.root, text='Создание рандомной бисимметричной матрицы',
                                    bg='#619eb3', bd=5)
        self.frame2 = tk.LabelFrame(self.root, text='Создание бисимметричной матрицы из заданного вектора',
                                    bg='#619eb3', bd=5)

        self.input_size_lbl = tk.Label(self.frame1, text='Ввод размера матрицы')
        self.input_size_ent = tk.Entry(self.frame1)
        self.create_rndm_mtrx_btn = tk.Button(self.frame1, text='Создать')
        self.result_rndm_mtrx_txt = tk.Text(self.frame1, height=0, width=0)

        self.input_vector_lbl = tk.Label(self.frame2, text='Ввод вектора')
        self.input_vector_txt = tk.Text(self.frame2, height=1, width=20)
        self.create_mtrx_by_vector_btn = tk.Button(self.frame2, text='Создать')
        self.result_mtrx_by_vector_txt = tk.Text(self.frame2, height=0, width=0)

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

        self.input_size_lbl.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        self.input_size_ent.grid(row=0, column=2, columnspan=2, padx=5, pady=5)
        self.create_rndm_mtrx_btn.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W+tk.E)
        self.result_rndm_mtrx_txt.grid(row=1, column=1, columnspan=4, padx=5, pady=5)

        self.input_vector_lbl.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky=tk.W)
        self.input_vector_txt.grid(row=0, column=2, columnspan=3, padx=5, pady=5, sticky=tk.E)
        self.create_mtrx_by_vector_btn.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W+tk.E)
        self.result_mtrx_by_vector_txt.grid(row=1, column=2, columnspan=5, padx=5, pady=5, sticky=tk.W)

    def bind_events(self):
        self.input_size_ent.bind('<KeyRelease>', self.size_changed)
        self.create_rndm_mtrx_btn.bind('<Button-1>', self.create_random_matrix_clicked)

        self.input_vector_txt.bind('<KeyRelease>', self.txt_changed)
        self.create_mtrx_by_vector_btn.bind('<Button-1>', self.create_matrix_from_vector_clicked)

    def mvvm_bind(self):
        self.view_model.set_matrix_size(self.input_size_ent.get())

    def mvvm_back_bind(self):
        self.create_rndm_mtrx_btn.config(state=self.view_model.get_button_convert_state())
        self.result_rndm_mtrx_txt.delete('1.0', tk.END)
        self.result_rndm_mtrx_txt.config(height=self.view_model.matrix_size)
        self.result_rndm_mtrx_txt.config(width=self.view_model.matrix_size * 2 + 1)
        self.result_rndm_mtrx_txt.insert(tk.END, self.view_model.get_str_created_random_matrix())

    def create_random_matrix_clicked(self, event):
        self.mvvm_bind()
        self.view_model.create_random_matrix()
        self.mvvm_back_bind()

    def size_changed(self, event):
        self.mvvm_bind()
        self.create_rndm_mtrx_btn.config(state=self.view_model.get_button_convert_state())

    def mvvm_bind_from_vector(self):
        self.view_model.set_vector(self.input_vector_txt.get("1.0", tk.END).strip())

    def mvvm_back_bind_from_vector(self):
        self.create_mtrx_by_vector_btn.config(state=self.view_model.get_button_convert_state())
        self.result_mtrx_by_vector_txt.delete('1.0', tk.END)
        self.result_mtrx_by_vector_txt.config(height=self.view_model.matrix_size)
        self.result_mtrx_by_vector_txt.config(width=self.view_model.matrix_size*2+1)
        self.result_mtrx_by_vector_txt.insert(tk.END, self.view_model.get_str_created_matrix_by_vector())

    def txt_changed(self, event):
        self.mvvm_bind_from_vector()
        self.create_mtrx_by_vector_btn.config(state=self.view_model.get_button_convert_state())

    def create_matrix_from_vector_clicked(self, event):
        self.mvvm_bind_from_vector()
        self.view_model.create_matrix_by_vector()
        self.mvvm_back_bind_from_vector()
