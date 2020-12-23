import tkinter as tk
import tkinter.scrolledtext as ScrolledText

from stack.viewmodel.stack_viewmodel import StackViewModel


class GUIView:
    view_model = StackViewModel()

    def __init__(self):
        pass
        self.window = tk.Tk()

        self.window.title("Stack program")
        self.window.geometry('200x800')
        self.window.resizable(width=False, height=False)

        self.size_frame = tk.Frame(master=self.window, relief=tk.RIDGE, borderwidth=5)
        self.size_frame.pack()

        self.input_size = tk.Label(self.size_frame, text='Размер стека', width=30)
        self.input_size.pack()

        self.size_value = tk.Entry(self.size_frame, width=20)
        self.size_value.insert(0, 100)
        self.size_value.pack()

        self.size_button = tk.Button(self.size_frame, text='Set', width=20)
        self.size_button.pack()

        self.input_frame = tk.Frame(master=self.window, relief=tk.RIDGE, borderwidth=5)
        self.input_frame.pack()

        self.input_text = tk.Label(self.input_frame, text='Введите число', width=30)
        self.input_text.pack()

        self.input_value = tk.Entry(self.input_frame, width=20)
        self.input_value.pack()

        self.input_button = tk.Button(self.input_frame, text='Push', width=20)
        self.input_button.pack()

        self.output_frame = tk.Frame(master=self.window, relief=tk.RIDGE, borderwidth=5)
        self.output_frame.pack()

        self.output_text = tk.Label(self.output_frame, text='Pop result', width=20)
        self.output_text.pack()

        self.pop_result = tk.Label(self.output_frame, text='', bg='#6dcae8', width=30)
        self.pop_result.pack()

        self.output_button = tk.Button(self.output_frame, text='Pop', width=20)
        self.output_button.pack()

        self.show_stack_frame = tk.Frame(master=self.window, relief=tk.RIDGE, borderwidth=5)
        self.show_stack_frame.pack()

        self.error_text = tk.Label(self.show_stack_frame, text='', bg='#ff0000', width=30)
        self.error_text.pack()

        self.show_stack = ScrolledText.ScrolledText(self.show_stack_frame, width=30)
        self.show_stack.pack()
        
        self.log_frame = tk.Frame(master=self.window, relief=tk.RIDGE, borderwidth=5)
        self.log_frame.pack()
        
        self.log_text = ScrolledText.ScrolledText(self.log_frame, width=30)
        self.log_text.pack()

        self.bind_events()
        self.window.mainloop()

    def bind_events(self):
        self.input_text.bind('<KeyRelease>', self.input_changed)
        self.size_value.bind('<KeyRelease>', self.size_changed)
        self.size_button.bind('<Button-1>', self.size_button_clicked)
        self.input_button.bind('<Button-1>', self.input_button_clicked)
        self.output_button.bind('<Button-1>', self.output_button_clicked)

    def input_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def size_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def size_button_clicked(self, event):
        self.mvvm_bind()
        self.view_model.size_click()
        self.mvvm_back_bind()

    def input_button_clicked(self, event):
        self.mvvm_bind()
        self.view_model.input_click()
        self.mvvm_back_bind()

    def output_button_clicked(self, event):
        self.mvvm_bind()
        self.view_model.output_click()
        self.mvvm_back_bind()

    def mvvm_bind(self):
        self.view_model.set_size_value(self.size_value.get())
        self.view_model.set_input_value(self.input_value.get())

    def mvvm_back_bind(self):
        self.input_value.delete(0, tk.END)
        self.input_value.insert(tk.END, self.view_model.get_input_value())

        self.pop_result.config(text='%s\n' % (self.view_model.get_pop_result()))

        self.error_text.config(text='%s\n' % (self.view_model.get_error()))

        self.input_button.config(state=self.view_model.is_input_button_enable())
        self.output_button.config(state=self.view_model.is_output_button_enable())

        self.size_button.config(state=self.view_model.is_size_button_enable())
        self.input_button.config(state=self.view_model.is_input_button_enable())
        self.output_button.config(state=self.view_model.is_output_button_enable())

        self.show_stack.delete(1.0, tk.END)
        self.show_stack.insert(tk.INSERT, self.view_model.get_stack_values())

        self.log_text.delete(1.0, tk.END)
        self.log_text.insert(tk.INSERT, self.view_model.get_log_messages())
