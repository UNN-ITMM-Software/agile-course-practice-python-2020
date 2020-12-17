import tkinter as tk
from tkinter import ttk

from modified_stack.viewmodel.modified_stack_viewmodel import ModifiedStackViewModel


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

        self.frame = tk.Frame(self.root, bg='White')

        self.canvas = tk.Canvas(self.frame)
        self.scrollbar = ttk.Scrollbar(self.frame, orient='horizontal', command=self.canvas.xview)
        self.scroll_frame = ttk.Frame(self.canvas)

        self.scroll_frame.bind(
            '<Configure>',
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox('all')
            )
        )

        self.canvas.create_window((0, 0), window=self.scroll_frame, anchor='nw')
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side='bottom', fill='both', expand=True)
        self.scrollbar.pack(side='bottom', fill='x')

        self.frame.grid(row=0, column=0)
        self.array_frame = tk.Frame(self.scroll_frame, bg='LightBlue1')

        self.pop_state = tk.StringVar(value='One')
        self.push_state = tk.StringVar(value='One')

        self.top = tk.Button(self.scroll_frame, text='top', bg='Azure', width=10, height=1)
        self.min = tk.Button(self.scroll_frame, text='min', bg='Azure', width=10, height=1)
        self.pop = tk.Button(self.scroll_frame, text='pop', bg='Azure', width=10, height=3)
        self.push = tk.Button(self.scroll_frame, text='push', bg='Azure', width=10, height=3)

        self.pop_one_element = ttk.Radiobutton(
            self.scroll_frame, text='One element', variable=self.pop_state,
            value='One', width=15, command=self.pop_strategy)
        self.pop_n_elements = ttk.Radiobutton(
            self.scroll_frame, text='N element', variable=self.pop_state,
            value='N', width=15, command=self.pop_strategy)

        self.push_one_element = ttk.Radiobutton(
            self.scroll_frame, text='One value', variable=self.push_state,
            value='One', width=15, command=self.push_strategy)
        self.push_n_elements = ttk.Radiobutton(
            self.scroll_frame, text='Array', variable=self.push_state,
            value='N', width=15, command=self.push_strategy)

        self.stack_size = tk.Label(self.scroll_frame, text='Stack size: 0', bg='Gray21', fg='White')

        self.pushed_value = tk.Entry(self.scroll_frame, width=10)
        self.pop_size = tk.Entry(self.scroll_frame, width=10)
        self.array_size = tk.Entry(self.scroll_frame, width=10)

        self.min_value = tk.Label(self.scroll_frame, text='')
        self.top_value = tk.Label(self.scroll_frame, text='')

        self.enter_array = tk.Label(self.scroll_frame, text='Please, enter array size:')
        self.title = tk.Label(self.array_frame, text='Enter your array: ', bg='Gray21', fg='White')

        self.box_list = []

        self.error = tk.Label(self.scroll_frame, text='Error', bg='Gray21', fg='Red')
        self.is_error = False

        self.set_weight_to_grid()
        self.bind_events()
        self.root.mainloop()

    def set_weight_to_grid(self):
        self.root.grid_rowconfigure(2, minsize=30)
        self.root.grid_rowconfigure(5, minsize=30, weight=60)
        self.frame.place(relx=0.025, rely=0.025, relwidth=0.95, relheight=0.95)

        self.stack_size.grid(row=2, column=0, pady=5)
        self.top.grid(row=3, column=0, pady=5)
        self.min.grid(row=5, column=0, pady=5)
        self.pop.grid(row=7, column=0, pady=5, rowspan=2)
        self.push.grid(row=9, column=0, pady=5, rowspan=2)

        self.pop_one_element.grid(row=7, column=1, pady=5, padx=10)
        self.pop_n_elements.grid(row=8, column=1, pady=5, padx=10)

        self.push_one_element.grid(row=9, column=1, pady=5, padx=10)
        self.push_n_elements.grid(row=10, column=1, pady=5, padx=10)

        self.pushed_value.grid(row=9, column=2, pady=5, padx=10)

    def pop_strategy(self):
        self.clean_input()

        state = self.pop_state.get()
        if state == 'One':
            self.pop_size.grid_forget()
        elif state == 'N':
            self.pop_size.grid(row=8, column=2, pady=5, padx=10)

    def push_strategy(self):
        self.clean_input()

        state = self.push_state.get()
        if state == 'One':
            self.enter_array.grid_forget()
            self.array_size.grid_forget()
            self.array_frame.grid_forget()
            self.pushed_value.grid(row=9, column=2, pady=5, padx=10)
        elif state == 'N':
            self.pushed_value.grid_forget()
            self.enter_array.grid(row=10, column=2, pady=5, padx=10)
            self.array_size.grid(row=10, column=3, pady=5, padx=10)

    def bind_events(self):
        self.array_size.bind('<KeyRelease>', self.create_windows_array_elements)
        self.top.bind('<Button-1>', self.top_button_clicked)
        self.min.bind('<Button-1>', self.min_button_clicked)
        self.pop.bind('<Button-1>', self.pop_button_clicked)
        self.push.bind('<Button-1>', self.push_button_clicked)

    def create_windows_array_elements(self, event):
        self.array_frame.grid(row=11, column=0, columnspan=1000, pady=5, padx=10)
        for box in self.box_list:
            box.destroy()

        self.box_list = []
        try:
            array_size = int(self.array_size.get())

            current_size = array_size
            self.title.grid(row=0, column=0, pady=5, padx=10)

            for current_box in range(current_size - 1):
                self.box_list.append(tk.Entry(self.array_frame, bg='gray21', fg='white', bd='1', width='3'))
                self.box_list[-1].grid(row=0, column=2 + current_box)

            self.box_list.append(tk.Entry(self.array_frame, bg='gray21', fg='white', bd='1', width='3'))
            self.box_list[-1].grid(row=0, column=2 + current_size - 1, pady=5, padx=(0, 10))
            self.view_model.set_error_message(None)
        except Exception:
            self.view_model.set_error_message('Error: wrong array size')

        self.mvvm_back_bind()

    def top_button_clicked(self, event):
        self.view_model.get_top()
        self.mvvm_back_bind_top()
        self.clean_input()

    def min_button_clicked(self, event):
        self.view_model.get_min()
        self.mvvm_back_bind_min()
        self.clean_input()

    def pop_button_clicked(self, event):
        self.mvvm_bind_btn_pop()
        self.view_model.pop()
        self.mvvm_back_bind()
        self.clean_input()

    def push_button_clicked(self, event):
        self.mvvm_bind_btn_push()
        self.view_model.push()
        self.mvvm_back_bind()
        self.clean_input()

    def mvvm_back_bind_top(self):
        self.mvvm_back_bind()
        if not self.is_error:
            self.top_value.grid(row=3, column=1)
            self.top_value.config(text='Top value: {}'.format(self.view_model.top))

    def mvvm_back_bind_min(self):
        self.mvvm_back_bind()
        if not self.is_error:
            self.min_value.grid(row=5, column=1)
            self.min_value.config(text='Min value: {}'.format(self.view_model.min))

    def mvvm_bind_btn_pop(self):
        self.hide_all_labels()

        if self.pop_state.get() == 'One':
            self.view_model.set_pop_size(1)
        elif self.pop_state.get() == 'N':
            self.view_model.set_pop_size(self.pop_size.get())

    def mvvm_bind_btn_push(self):
        self.hide_all_labels()
        self.view_model.set_push_state(self.push_state.get())

        if self.push_state.get() == 'One':
            self.view_model.set_pushed_element(self.pushed_value.get())
        elif self.push_state.get() == 'N':
            box_values = [box.get() for box in self.box_list]
            self.view_model.set_input_array(box_values)

    def mvvm_back_bind(self):
        message = get_error_text(self.view_model.get_error_message())
        self.is_error = False
        if message:
            self.error.config(text='Error: {}\n'.format(message))
            self.error.grid(row=1, column=1, rowspan=2, columnspan=2)
            self.is_error = True
        else:
            self.error.grid_forget()
        self.stack_size.config(text='Stack size: {}\n'.format(self.view_model.size()))

    def clean_input(self):
        self.pop_size.delete(0, tk.END)
        self.pop_size.insert(0, '')

        self.pushed_value.delete(0, tk.END)
        self.pushed_value.insert(0, '')

        self.array_size.delete(0, tk.END)
        self.array_size.insert(0, '')

        self.array_frame.grid_forget()

    def hide_all_labels(self):
        self.top_value.grid_forget()
        self.min_value.grid_forget()
        self.error.grid_forget()
