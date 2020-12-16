import tkinter as tk
from vector_3d.viewmodel.viewmodel import Vector3dViewModel


class GUI(tk.Frame):
    def __init__(self):
        self.root = tk.Tk()
        super().__init__(self.root)
        self.viewmodel = Vector3dViewModel()
        self.init_ui()

    def init_ui(self):
        self.root.title('3d Vectors')
        self.root.geometry('800x500')
        self.root.resizable(width=False, height=False)
        self.pack(fill='both', expand=True)
        self.create_widgets()
        self.setup_grid()
        self.bind_events()
        self.mvvm_bind()
        self.mvvm_backbind()

    def create_widgets(self):
        self.create_norms_widgets()
        self.create_products_widgets()

    def create_products_widgets(self):
        self.products = tk.Frame(self)
        self.products.button = tk.Button(self.products, text='Calculate Products', font=60)

        self.products.coordinates = tk.Frame(self.products)
        self.products.vector1 = tk.Frame(self.products.coordinates)
        self.products.label_vec1 = tk.Label(self.products.vector1, text='Vector 1', font=60)
        self.products.vec1_x = tk.Entry(self.products.vector1)
        self.products.vec1_y = tk.Entry(self.products.vector1)
        self.products.vec1_z = tk.Entry(self.products.vector1)

        self.products.vector2 = tk.Frame(self.products.coordinates)
        self.products.label_vec2 = tk.Label(self.products.vector2, text='Vector 2', font=60)
        self.products.vec2_x = tk.Entry(self.products.vector2)
        self.products.vec2_y = tk.Entry(self.products.vector2)
        self.products.vec2_z = tk.Entry(self.products.vector2)

        self.products.results = tk.Frame(self.products)
        self.products.dot_product = tk.Label(self.products.results, text='Dot Product = ', font=60)
        self.products.cross_product = tk.Label(self.products.results, text='Cross Product = ', font=60)

    def create_norms_widgets(self):
        self.norms = tk.Frame(self)
        self.norms.button = tk.Button(self.norms, text='Calculate Norms', font=60)

        self.norms.coordinates = tk.Frame(self.norms)
        self.norms.label = tk.Label(self.norms.coordinates, text='Coordinates', font=60)
        self.norms.vec0_x = tk.Entry(self.norms.coordinates)
        self.norms.vec0_y = tk.Entry(self.norms.coordinates)
        self.norms.vec0_z = tk.Entry(self.norms.coordinates)

        self.norms.results = tk.Frame(self.norms)
        self.norms.norm_euclid = tk.Label(self.norms.results, text='Euclid Norm = ', font=60)
        self.norms.norm_manhattan = tk.Label(self.norms.results, text='Manhattan Norm = ', font=60)
        self.norms.norm_chebyshev = tk.Label(self.norms.results, text='Chebyshev Norm = ', font=60)
        self.norms.normalized = tk.Label(self.norms.results, text='Normalized vector = ', font=60)

    def setup_grid(self):
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1, uniform='half')
        self.columnconfigure(1, weight=1, uniform='half')
        self.norms.grid(row=0, column=0, sticky='nswe')
        self.products.grid(row=0, column=1, sticky='nswe')
        self.setup_norms_grid()
        self.setup_products_grid()

    def setup_products_grid(self):
        self.products.rowconfigure(0, weight=1, uniform='third')
        self.products.rowconfigure(1, weight=1, uniform='third')
        self.products.rowconfigure(2, weight=1, uniform='third')
        self.products.columnconfigure(0, weight=1)

        self.products.label_vec1.pack()
        self.products.vec1_x.pack()
        self.products.vec1_y.pack()
        self.products.vec1_z.pack()
        self.products.vector1.pack(side='left')

        self.products.label_vec2.pack()
        self.products.vec2_x.pack()
        self.products.vec2_y.pack()
        self.products.vec2_z.pack()
        self.products.vector2.pack(side='right')

        self.products.dot_product.pack()
        self.products.cross_product.pack()

        self.products.coordinates.grid(row=0)
        self.products.button.grid(row=1)
        self.products.results.grid(row=2)

    def setup_norms_grid(self):
        self.norms.rowconfigure(0, weight=1, uniform='third')
        self.norms.rowconfigure(1, weight=1, uniform='third')
        self.norms.rowconfigure(2, weight=1, uniform='third')
        self.norms.columnconfigure(0, weight=1)

        self.norms.label.pack()
        self.norms.vec0_x.pack()
        self.norms.vec0_y.pack()
        self.norms.vec0_z.pack()

        self.norms.norm_euclid.pack()
        self.norms.norm_chebyshev.pack()
        self.norms.norm_manhattan.pack()
        self.norms.normalized.pack()

        self.norms.coordinates.grid(row=0)
        self.norms.button.grid(row=1)
        self.norms.results.grid(row=2)

    def bind_events(self):
        self.norms.vec0_x.bind('<KeyRelease>', self.norms_x_changed)
        self.norms.vec0_y.bind('<KeyRelease>', self.norms_y_changed)
        self.norms.vec0_z.bind('<KeyRelease>', self.norms_z_changed)

        self.products.vec1_x.bind('<KeyRelease>', self.products_vec1_x_changed)
        self.products.vec1_y.bind('<KeyRelease>', self.products_vec1_y_changed)
        self.products.vec1_z.bind('<KeyRelease>', self.products_vec1_z_changed)

        self.products.vec2_x.bind('<KeyRelease>', self.products_vec2_x_changed)
        self.products.vec2_y.bind('<KeyRelease>', self.products_vec2_y_changed)
        self.products.vec2_z.bind('<KeyRelease>', self.products_vec2_z_changed)

        self.norms.button.bind('<Button-1>', self.norms_button_clicked)
        self.products.button.bind('<Button-1>', self.products_button_clicked)

    def norms_button_clicked(self, event):
        self.mvvm_bind()
        self.viewmodel.calc_norms()
        self.mvvm_backbind()

    def products_button_clicked(self, event):
        self.mvvm_bind()
        self.viewmodel.calc_products()
        self.mvvm_backbind()

    def norms_x_changed(self, event):
        self.mvvm_bind()
        self.mvvm_backbind()

    def norms_y_changed(self, event):
        self.mvvm_bind()
        self.mvvm_backbind()

    def norms_z_changed(self, event):
        self.mvvm_bind()
        self.mvvm_backbind()

    def products_vec1_x_changed(self, event):
        self.mvvm_bind()
        self.mvvm_backbind()

    def products_vec1_y_changed(self, event):
        self.mvvm_bind()
        self.mvvm_backbind()

    def products_vec1_z_changed(self, event):
        self.mvvm_bind()
        self.mvvm_backbind()

    def products_vec2_x_changed(self, event):
        self.mvvm_bind()
        self.mvvm_backbind()

    def products_vec2_y_changed(self, event):
        self.mvvm_bind()
        self.mvvm_backbind()

    def products_vec2_z_changed(self, event):
        self.mvvm_bind()
        self.mvvm_backbind()

    def mvvm_bind(self):
        self.viewmodel.set_norm_vector(self.norms.vec0_x.get(),
                                       self.norms.vec0_y.get(),
                                       self.norms.vec0_z.get())
        self.viewmodel.set_product_vectors(self.products.vec1_x.get(),
                                           self.products.vec2_x.get(),
                                           self.products.vec1_y.get(),
                                           self.products.vec2_y.get(),
                                           self.products.vec1_z.get(),
                                           self.products.vec2_z.get())

    def mvvm_backbind(self):
        self.norms.vec0_x.delete(0, tk.END)
        self.norms.vec0_x.insert(tk.END, self.viewmodel.get_vec0_x())
        self.norms.vec0_y.delete(0, tk.END)
        self.norms.vec0_y.insert(tk.END, self.viewmodel.get_vec0_y())
        self.norms.vec0_z.delete(0, tk.END)
        self.norms.vec0_z.insert(tk.END, self.viewmodel.get_vec0_z())

        self.products.vec1_x.delete(0, tk.END)
        self.products.vec1_x.insert(tk.END, self.viewmodel.get_vec1_x())
        self.products.vec1_y.delete(0, tk.END)
        self.products.vec1_y.insert(tk.END, self.viewmodel.get_vec1_y())
        self.products.vec1_z.delete(0, tk.END)
        self.products.vec1_z.insert(tk.END, self.viewmodel.get_vec1_z())

        self.products.vec2_x.delete(0, tk.END)
        self.products.vec2_x.insert(tk.END, self.viewmodel.get_vec2_x())
        self.products.vec2_y.delete(0, tk.END)
        self.products.vec2_y.insert(tk.END, self.viewmodel.get_vec2_y())
        self.products.vec2_z.delete(0, tk.END)
        self.products.vec2_z.insert(tk.END, self.viewmodel.get_vec2_z())

        self.norms.button.config(state=self.viewmodel.get_norms_button_state())
        self.products.button.config(state=self.viewmodel.get_products_button_state())

        self.norms.norm_euclid.config(text='Euclid Norm = ' + str(self.viewmodel.get_euclid_norm()))
        self.norms.norm_manhattan.config(text='Manhattan Norm = ' + str(self.viewmodel.get_manhattan_norm()))
        self.norms.norm_chebyshev.config(text='Chebyshev Norm = ' + str(self.viewmodel.get_chebyshev_norm()))

        normalized_vector = [round(val, 2) for val in self.viewmodel.get_normalized_vector()]
        self.norms.normalized.config(text='Normalized vector = ' + str(normalized_vector))

        self.products.dot_product.config(text='Dot Product = ' + str(self.viewmodel.get_dot_product()))
        cross_product = [round(val, 2) for val in self.viewmodel.get_cross_product()]
        self.products.cross_product.config(text='Cross product = ' + str(cross_product))
