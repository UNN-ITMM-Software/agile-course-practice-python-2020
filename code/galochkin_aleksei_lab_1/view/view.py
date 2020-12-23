import tkinter as tk

from galochkin_aleksei_lab_1.viewmodel.viewmodel import NodeViewModel


class GUIView(tk.Frame):
    view_model = NodeViewModel()

    def add_node(self):
        self.view_model.set_input_value(self.text_value.get(1, tk.END))
        self.view_model.add_node()
        self.result_label.configure(text=self.view_model.get_output_value)
        self.error_label.configure(text=self.view_model.get_error)

    def remove_node(self):
        self.view_model.set_input_value(self.text_value.get(1, tk.END))
        self.view_model.remove_node()
        self.result_label.configure(text=self.view_model.get_output_value)
        self.error_label.configure(text=self.view_model.get_error)

    def __init__(self):
        tk.Frame.__init__(self)
        self.master.title("AWL Tree")
        self.master.minsize(width=150, height=150)
        self.grid(sticky=tk.W + tk.E + tk.N + tk.S)

        self.add_button = tk.Button(self, text='Add node', width=25, height=5, bg='black', fg='red',
                                    font='arial 14', command=GUIView.add_node)
        self.add_button.pack()

        self.remove_button = tk.Button(self, text='Remove node', width=25, height=5, bg='black', fg='red',
                                       font='arial 14', command=GUIView.remove_node)
        self.remove_button.pack()

        self.text_value = tk.Text(self, height=1, width=30, font="Arial 14")
        self.text_value.pack()

        self.error_label = tk.Label(self, text="", fg='black', font="Arial 14")
        self.error_label.pack()

        self.result_label = tk.Label(self, text="", fg='black', font="Arial 14")
        self.result_label.pack()
