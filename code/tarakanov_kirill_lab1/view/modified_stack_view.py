import tkinter as tk
from tkinter import ttk

from tarakanov_kirill_lab1.viewmodel.modified_stack_viewmodel import ModifiedStackViewModel


def get_error_text(value):
    return value if value else ''


class GUIView:
    view_model = ModifiedStackViewModel()

    def __init__(self):
        self.root = tk.Tk()
        self.root['bg'] = 'White'
        self.root.title('Модифицированный стек')
        self.root.geometry('700x400')
        self.root.resizable(width=False, height=False)

        self.box_list = []

        self.frame = tk.Frame(self.root, bg='White')

        self.canvas = tk.Canvas(self.frame)
        self.scrollbar = ttk.Scrollbar(self.frame, orient='horizontal', command=self.canvas.xview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            '<Configure>',
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox('all')
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor='nw')
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side='bottom', fill='both', expand=True)
        self.scrollbar.pack(side='bottom', fill='x')

        self.frame.grid(row=0, column=0)
        self.array_frame = tk.Frame(self.scrollable_frame, bg='LightBlue1')

        self.state_pop = tk.StringVar(value='One')
        self.state_push = tk.StringVar(value='One')

        self.top = tk.Button(self.scrollable_frame, text='top', state='normal', bg='Azure', width=10, height=1)
        self.min = tk.Button(self.scrollable_frame, text='min', state='normal', bg='Azure', width=10, height=1)
        self.pop = tk.Button(self.scrollable_frame, text='pop', state='normal', bg='Azure', width=10, height=3)
        self.push = tk.Button(self.scrollable_frame, text='push', state='normal', bg='Azure', width=10, height=3)

        self.pop_one_element = ttk.Radiobutton(
            self.scrollable_frame, text='One element', variable=self.state_pop,
            value='One', width=15, command=self.pop_strategy)
        self.pop_n_elements = ttk.Radiobutton(
            self.scrollable_frame, text='N element', variable=self.state_pop,
            value='N', width=15, command=self.pop_strategy)

        self.push_one_element = ttk.Radiobutton(
            self.scrollable_frame, text='One value', variable=self.state_push,
            value='One', width=15, command=self.push_strategy)
        self.push_n_elements = ttk.Radiobutton(
            self.scrollable_frame, text='Array', variable=self.state_push,
            value='N', width=15, command=self.push_strategy)

        self.pushed_value = tk.Entry(self.scrollable_frame, width=10)
        self.pop_size = tk.Entry(self.scrollable_frame, width=10)
        self.array_size = tk.Entry(self.scrollable_frame, width=10)

        self.min_value = tk.Label(self.scrollable_frame, text='')
        self.top_value = tk.Label(self.scrollable_frame, text='')

        self.enter_array = tk.Label(self.scrollable_frame, text='Please, enter array size:')
        self.title = tk.Label(self.array_frame, text='Enter your array: ', bg='Gray21', fg='White')

        self.error = tk.Label(self.scrollable_frame, text='Error', bg='Gray21', fg='Red')

        self.set_weight_to_grid()
        self.bind_events()
        self.root.mainloop()

    def set_weight_to_grid(self):
        self.root.grid_rowconfigure(2, minsize=30)
        self.root.grid_rowconfigure(5, minsize=30, weight=60)
        self.frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

        self.top.grid(row=3, column=0, pady=5)
        self.min.grid(row=5, column=0, pady=5)
        self.pop.grid(row=7, column=0, pady=5, rowspan=2)
        self.push.grid(row=9, column=0, pady=5, rowspan=2)

        self.pop_one_element.grid(row=7, column=1, pady=5, padx=10)
        self.pop_n_elements.grid(row=8, column=1, pady=5, padx=10)

        self.push_one_element.grid(row=9, column=1, pady=5, padx=10)
        self.push_n_elements.grid(row=10, column=1, pady=5, padx=10)

        self.pushed_value.grid(row=9, column=2, pady=5, padx=10)

        # self.error.grid(row=1, column=1, rowspan=2, columnspan=2)
        # self.hide_all_labels()

    def bind_events(self):
        self.array_size.bind('<KeyRelease>', self.create_windows_array_elements)

        self.top.bind('<Button-1>', self.top_button_clicked)
        self.min.bind('<Button-1>', self.min_button_clicked)
        self.pop.bind('<Button-1>', self.pop_button_clicked)
        self.push.bind('<Button-1>', self.push_button_clicked)

    def pop_strategy(self):
        if self.state_pop.get() == 'One':
            self.pop_size.grid_forget()
        elif self.state_pop.get() == 'N':
            self.pop_size.grid(row=8, column=2, pady=5, padx=10)

    def push_strategy(self):
        if self.state_push.get() == 'One':
            self.pushed_value.grid(row=9, column=2, pady=5, padx=10)
            self.enter_array.grid_forget()
            self.array_size.grid_forget()
            self.array_frame.grid_forget()
        elif self.state_push.get() == 'N':
            self.pushed_value.grid_forget()
            self.enter_array.grid(row=10, column=2, pady=5, padx=10)
            self.array_size.grid(row=10, column=3, pady=5, padx=10)

    def create_windows_array_elements(self, event):
        self.array_frame.grid(row=11, column=0, columnspan=1000, pady=5, padx=10)


        array_size = int(self.array_size.get())
        for box in self.box_list:
            box.destroy()
        self.box_list = []
        current_size = array_size
        self.title.grid(row=0, column=0, pady=5, padx=10)

        for current_box in range(current_size - 1):
            self.box_list.append(tk.Entry(self.array_frame, bg='gray21', fg='white', bd='1', width='3'))
            self.box_list[-1].grid(row=0, column=2 + current_box)

        self.box_list.append(tk.Entry(self.array_frame, bg='gray21', fg='white', bd='1', width='3'))
        self.box_list[-1].grid(row=0, column=2 + current_size - 1, pady=5, padx=(0,10))
                # self.dif += current_size
                # self.update_position()

    def top_button_clicked(self, event):
        self.view_model.get_top()
        self.mvvm_back_bind_top()

    def min_button_clicked(self, event):
        self.view_model.get_min()
        self.mvvm_back_bind_min()

    def pop_button_clicked(self, event):
        self.mvvm_bind_btn_pop()
        self.view_model.pop()
        self.mvvm_back_bind_bth_pop()

    def push_button_clicked(self, event):
        self.hide_all_labels()
        self.mvvm_bind_btn_push()
        self.view_model.push()
        self.mvvm_back_bind_push()

    def mvvm_back_bind_top(self):
        self.top_value.grid(row=3, column=1)
        self.top_value.config(text=f'Top value: {self.view_model.top}')

    def mvvm_back_bind_min(self):
        self.min_value.grid(row=5, column=1)
        self.min_value.config(text=f'Min value: {self.view_model.min}')

    def mvvm_bind_btn_pop(self):
        self.hide_all_labels()
        if self.state_pop.get() == 'One':
            self.view_model.set_pop_size(1)
        elif self.state_pop.get() == 'N':
            self.view_model.set_pop_size(self.pop_size.get())

    def mvvm_back_bind_bth_pop(self):
        message = get_error_text(self.view_model.get_error_message())
        if message:
            self.error.config(text=f'{message}\n')
            self.error.grid(row=1, column=1, rowspan=2, columnspan=2)

    def mvvm_bind_btn_push(self):
        self.view_model.set_pushed_element(self.pushed_value.get())

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
