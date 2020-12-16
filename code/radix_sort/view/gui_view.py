import tkinter as tk
from radix_sort.view_model.gui_view_model import RadixSortViewModel


class Application(tk.Frame):
    def __init__(self):
        self.root = tk.Tk()
        super().__init__(self.root)
        self.view_model = RadixSortViewModel()
        self.init_ui()

    def init_ui(self):
        self.root.title("Radix Sort")
        self.root.geometry('800x500')
        self.root.resizable(width=False, height=False)
        self.pack(fill='both', expand=True)
        self.create_widgets()
        self.setup_grid()
        self.bind_events()
        self.mvvm_bind()
        self.mvvm_back_bind()

    def create_widgets(self):
        self.radix = tk.Frame(self)
        self.label_input = tk.Label(self.radix, text='Enter an array to sort:', font=60)
        self.label_output = tk.Label(self.radix, text='Sorted array:', font=60)
        self.text_input = tk.Entry(self.radix, width=50, font=60)
        self.text_output = tk.Label(self.radix, width=50, font=60, anchor='w')
        self.sort_button = tk.Button(self, text="Sort", font=60)

    def setup_grid(self):
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.radix.grid(row=0, column=0, sticky='swe')
        self.sort_button.grid(row=1, column=0, sticky='n', pady=20)

        self.radix.rowconfigure(0, weight=1)
        self.radix.rowconfigure(1, weight=1)
        self.radix.columnconfigure(0, weight=1)
        self.radix.columnconfigure(1, weight=1)

        self.label_input.grid(column=0, row=0, sticky='se', padx=10, pady=10)
        self.text_input.grid(column=1, row=0, sticky='sw', padx=10, pady=10)
        self.label_output.grid(column=0, row=1, sticky='ne', padx=10)
        self.text_output.grid(column=1, row=1, sticky='nw', padx=10)

    def bind_events(self):
        self.text_input.bind('<KeyRelease>', self.text_input_changed)
        self.sort_button.bind('<Button-1>', self.sort_button_clicked)

    def mvvm_bind(self):
        self.view_model.set_input_data(self.text_input.get())

    def mvvm_back_bind(self):
        self.text_input.delete(0, tk.END)
        self.text_input.insert(tk.END, self.view_model.get_input_data())
        self.text_output.config(text=str(self.view_model.get_output_data()))
        self.sort_button.config(state=self.view_model.get_sort_button_state())

    def text_input_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def sort_button_clicked(self, event):
        self.mvvm_bind()
        self.view_model.start_sort()
        self.mvvm_back_bind()
