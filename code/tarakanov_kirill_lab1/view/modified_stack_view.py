import tkinter as tk
from tkinter import ttk

from tarakanov_kirill_lab1.viewmodel.modified_stack_viewmodel import ModifiedStackViewModel


class GUIView:
    view_model = ModifiedStackViewModel()

    # ttk_custom_style = ttk.Style()
    # ttk_custom_style.configure('Custom.TRadiobutton', background="gray21", foreground='white')

    def __init__(self):
        self.root = tk.Tk()
        self.root['bg'] = '#fafafa'
        self.root.title('Модифицированный стек')
        self.root.geometry('600x400')
        self.root.resizable(width=False, height=False)

        self.frame = tk.Frame(self.root, bg='White')

        self.state = tk.StringVar()
        self.state.set('one')

        self.top = tk.Button(self.frame, text="top", state='normal', bg='Azure', width=10, height=1)
        self.min = tk.Button(self.frame, text="min", state='normal', bg='Azure', width=10, height=1)
        self.pop = tk.Button(self.frame, text="pop", state='normal', bg='Azure', width=10, height=1)
        self.push = tk.Button(self.frame, text="push", state='normal', bg='Azure', width=10, height=3)

        self.push_one_element = ttk.Radiobutton(
            self.frame, text="One value", variable=self.state,
            value="one", width=10)
        self.push_array = ttk.Radiobutton(
            self.frame, text="Array", variable=self.state,
            value="arr", width=10)

        self.one_value = tk.Entry(self.frame, width=10)

        self.min_value = tk.Label(self.frame, text='')
        self.top_value = tk.Label(self.frame, text='')
        self.error = tk.Label(self.frame, text='')

        # self.lbl_num_vertex = tk.Label(self.root, text="vertex count:")
        # self.input_num_vertex = tk.Entry(self.root, width=3)
        # self.input_graph = tk.Button(self.root, text="create graph", state='disabled')
        self.errors = tk.Label(self.root, text="", bg='#fafafa')
        # self.lbl_start_vertex = tk.Label(self.root, text="start vertex:")
        # self.input_start_vertex = tk.Entry(self.root, width=3)
        # self.run = tk.Button(self.root, text="run dijksta")
        # self.entries = []

        self.set_weight_to_grid()
        self.bind_events()
        self.root.mainloop()

    def set_weight_to_grid(self):
        self.root.grid_rowconfigure(2, minsize=30)
        self.root.grid_rowconfigure(5, minsize=30, weight=60)
        self.frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

        self.top.grid(row=1, column=0, pady=5)
        self.min.grid(row=3, column=0, pady=5)
        self.pop.grid(row=5, column=0, pady=5)
        self.push.grid(row=7, column=0, pady=5, rowspan=2)

        self.push_one_element.grid(row=7, column=1, pady=5, padx=10)
        self.push_array.grid(row=8, column=1, pady=5, padx=10)

        self.one_value.grid(row=7, column=2, padx=10, pady=5)

        self.error.grid(row=13, column=0)

        self.hide_all_labels()

    def bind_events(self):
        self.top.bind('<Button-1>', self.top_button_clicked)
        self.min.bind('<Button-1>', self.min_button_clicked)
        self.pop.bind('<Button-1>', self.pop_button_clicked)
        self.push.bind('<Button-1>', self.push_button_clicked)

    def top_button_clicked(self, event):
        self.view_model.get_top()
        self.mvvm_back_bind_top()

    def min_button_clicked(self, event):
        self.view_model.get_min()
        self.mvvm_back_bind_min()

    def pop_button_clicked(self, event):
        self.hide_all_labels()
        self.view_model.pop()

    def push_button_clicked(self, event):
        self.hide_all_labels()
        self.mvvm_bind_btn_push()
        self.view_model.push()
        self.mvvm_back_bind_push()

    def mvvm_back_bind_top(self):
        self.top_value.grid(row=1, column=1)
        self.top_value.config(text=f'Top value: {self.view_model.top}')

    def mvvm_back_bind_min(self):
        self.min_value.grid(row=3, column=1)
        self.min_value.config(text=f'Min value: {self.view_model.min}')

    def mvvm_bind_btn_push(self):
        self.view_model.set_pushed_element(self.one_value.get())

    def mvvm_back_bind_push(self):
        pass

    def hide_all_labels(self):
        self.top_value.grid_forget()
        self.min_value.grid_forget()
        self.error.grid_forget()

    def mvvm_bind(self, event):
        error_message = 'Error'
        self.error.grid()
        self.error.config(text=f'{error_message}\n')

# class GUIView:
#     view_model = DAViewModel()
#
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root['bg'] = '#fafafa'
#         self.root.title('Алгоритм Дейкстры')
#         self.root.geometry('630x400')
#
#         self.frame = tk.Frame(self.root, bg='#fafafa')
#         self.lbl_num_vertex = tk.Label(self.root, text="vertex count:")
#         self.input_num_vertex = tk.Entry(self.root, width=3)
#         self.input_graph = tk.Button(self.root, text="create graph", state='disabled')
#         self.errors = tk.Label(self.root, text="", bg='#fafafa')
#         self.lbl_start_vertex = tk.Label(self.root, text="start vertex:")
#         self.input_start_vertex = tk.Entry(self.root, width=3)
#         self.run = tk.Button(self.root, text="run dijksta")
#         self.entries = []
#
#         self.set_weight_to_grid()
#         self.bind_events()
#         self.root.mainloop()
#
#     def set_weight_to_grid(self):
#         self.lbl_num_vertex.grid(row=0, column=0)
#         self.input_num_vertex.grid(row=0, column=1)
#         self.input_graph.grid(row=1, column=0)
#         self.lbl_start_vertex.grid(row=0, column=2)
#         self.input_start_vertex.grid(row=0, column=3)
#         self.errors.grid(row=1, column=2, columnspan=3)
#         self.run.grid(row=1, column=1)
#         self.frame.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.6)
#
#     def bind_events(self):
#         self.input_num_vertex.bind('<KeyRelease>', self.num_vertex_changed)
#         self.input_start_vertex.bind('<KeyRelease>', self.start_vertex_changes)
#         self.input_graph.bind('<Button-1>', self.input_graph_clicked)
#         self.run.bind('<Button-1>', self.run_clicked)
#
#     def num_vertex_changed(self, event):
#         self.mvvm_bind()
#         self.mvvm_back_bind()
#
#     def start_vertex_changes(self, event):
#         self.mvvm_bind()
#         self.mvvm_back_bind()
#
#     def input_graph_clicked(self, event):
#         self.mvvm_bind()
#         self.draw_table()
#         self.mvvm_back_bind()
#
#     def run_clicked(self, event):
#         self.mvvm_bind()
#         self.draw_result(self.view_model.run_dijkstra(self.read_weights()))
#         self.mvvm_back_bind()
#
#     def draw_table(self):
#
#         if self.view_model.get_btn_create_graph_state() == 'disabled':
#             return
#
#         self.frame.destroy()
#         self.frame = self.frame = tk.Frame(self.root, bg='#fafafa')
#         self.frame.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.6)
#         self.entries = []
#
#         rows = int(self.input_num_vertex.get())
#         cols = int(self.input_num_vertex.get())
#
#         header = tk.Label(self.frame, text="Вершины", bg='#fafafa')
#         header.grid(row=0, column=0)
#
#         for column_id in range(cols):
#             header = tk.Label(self.frame, text=str(column_id), bg='#fafafa')
#             header.grid(row=0, column=column_id + 1)
#
#         for row_id in range(rows):
#
#             header = tk.Label(self.frame, text=str(row_id), bg='#fafafa')
#             header.grid(row=row_id + 1, column=0)
#
#             self.entries.append([])
#             for column_id in range(cols):
#                 self.entries[row_id].append(tk.Entry(self.frame, width=3))
#                 self.entries[row_id][column_id].grid(row=row_id + 1, column=column_id + 1)
#
#     def draw_result(self, result):
#
#         rows = int(self.input_num_vertex.get())
#
#         lbl_result = tk.Label(self.frame, text="dists", bg='#fafafa')
#         lbl_result.grid(row=rows + 1, column=0)
#
#         for column_id, dist in enumerate(result):
#             dist = tk.Label(self.frame, text=str(dist), bg='#fafafa')
#             dist.grid(row=rows + 1, column=column_id + 1)
#
#     def read_weights(self):
#         rows = int(self.input_num_vertex.get())
#         cols = int(self.input_num_vertex.get())
#         matrix = []
#         for i in range(rows):
#             matrix.append([])
#             for j in range(cols):
#                 matrix[i].append(self.entries[i][j].get())
#
#         return matrix
#
#     def mvvm_bind(self):
#         self.view_model.set_num_vertex(self.input_num_vertex.get())
#         self.view_model.set_start_vertex(self.input_start_vertex.get())
#
#     def mvvm_back_bind(self):
#         self.input_num_vertex.delete(0, tk.END)
#         self.input_num_vertex.insert(tk.END, self.view_model.get_num_vertex())
#
#         self.input_graph.config(state=self.view_model.get_btn_create_graph_state())
#
#         self.input_start_vertex.delete(0, tk.END)
#         self.input_start_vertex.insert(tk.END, self.view_model.get_start_vertex())
#
#         self.errors.config(text='%s\n' % (self.view_model.get_error()))
