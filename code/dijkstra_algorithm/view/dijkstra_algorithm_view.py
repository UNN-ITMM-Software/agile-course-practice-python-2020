import tkinter as tk

from dijkstra_algorithm.viewmodel.dijkstra_algorithm_viewmodel import DAViewModel


class GUIView:
    view_model = DAViewModel()

    def __init__(self):
        self.root = tk.Tk()
        self.root['bg'] = '#fafafa'
        self.root.title('Алгоритм Дейкстры')
        self.root.geometry('600x400')
        # self.root.resizable(width=False, height=True)

        self.lbl_num_vertex = tk.Label(self.root, text="Выберете число вершин графа:")
        self.lbl_num_vertex.grid(column=0, row=0)

        self.spin = tk.Spinbox(self.root, from_=2, to=10, width=5)
        self.spin.grid(column=1, row=0)

        self.btn = tk.Button(self.root, text="Запустить алгоритм")
        self.btn.grid(column=2, row=0)

        self.root.mainloop()