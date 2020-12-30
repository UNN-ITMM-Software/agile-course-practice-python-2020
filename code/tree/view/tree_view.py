import tkinter as tk
import tkinter.scrolledtext as ScrolledText
from tree_viewmodel.viewmodel.tree_viewmodel import TreeViewModel


class GUIView:
    view_model = TreeViewModel()

    def __init__(self):
        pass
        self.window = tk.Tk()

        self.window.title("Tree program")
        self.window.geometry('200x400')
        self.window.resizable(width=False, height=False)

        self.input_frame = tk.Frame(master=self.window, relief=tk.RIDGE, borderwidth=5)
        self.input_frame.pack()

        self.input_text = tk.Label(self.input_frame, text='Input value', width=30)
        self.input_text.pack()

        self.input_value = tk.Entry(self.input_frame, width=20)
        self.input_value.pack()

        self.input_button = tk.Button(self.input_frame, text='Insert', width=20)
        self.input_button.pack()

        self.find_frame = tk.Frame(master=self.window, relief=tk.RIDGE, borderwidth=5)
        self.find_frame.pack()

        self.find_text = tk.Label(self.find_frame, text='Find value', width=20)
        self.find_text.pack()

        self.find_value = tk.Entry(self.find_frame, width=20)
        self.find_value.pack()

        self.find_button = tk.Button(self.find_frame, text='find', width=20)
        self.find_button.pack()

        self.find_result = tk.Label(self.find_frame, text='', bg='#6dcae8', width=30)
        self.find_result.pack()

        self.show_tree_frame = tk.Frame(master=self.window, relief=tk.RIDGE, borderwidth=5, height=100)
        self.show_tree_frame.pack()

        self.error_text = tk.Label(self.show_tree_frame, text='', bg='#ff0000', width=30)
        self.error_text.pack()

        self.show_tree = ScrolledText.ScrolledText(self.show_tree_frame, width=30)
        self.show_tree.pack()

        self.log_frame = tk.Frame(master=self.window, relief=tk.RIDGE, borderwidth=5)
        self.log_frame.pack()

        self.log_text = ScrolledText.ScrolledText(self.log_frame, width=30)
        self.log_text.pack()

        self.bind_events()
        self.window.mainloop()

    def bind_events(self):
        self.input_value.bind('<KeyRelease>', self.input_changed)
        self.find_value.bind('<KeyRelease>', self.find_changed)
        self.input_button.bind('<Button-1>', self.input_button_clicked)
        self.find_button.bind('<Button-1>', self.find_button_clicked)

    def input_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def find_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def input_button_clicked(self, event):
        self.mvvm_bind()
        self.view_model.input_click()
        self.mvvm_back_bind()

    def find_button_clicked(self, event):
        self.mvvm_bind()
        self.view_model.find_click()
        self.mvvm_back_bind()

    def mvvm_bind(self):
        self.view_model.set_input_value(self.input_value.get())
        self.view_model.set_find_value(self.find_value.get())

    def mvvm_back_bind(self):
        self.input_value.delete(0, tk.END)
        self.input_value.insert(tk.END, self.view_model.get_input_value())

        self.find_result.config(text='%s\n' % (self.view_model.get_find_result()))

        self.error_text.config(text='%s\n' % (self.view_model.get_error()))

        self.input_button.config(state=self.view_model.is_input_button_enable())
        self.find_button.config(state=self.view_model.is_find_button_enable())

        self.show_tree.delete(1.0, tk.END)
        self.show_tree.insert(tk.INSERT, self.view_model.get_tree_values())

        self.log_text.delete(1.0, tk.END)
        self.log_text.insert(tk.INSERT, self.view_model.get_log_messages())
