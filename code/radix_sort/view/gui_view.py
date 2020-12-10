import tkinter as tk
from radix_sort.view.view.gui_view_model import RadixSortViewModel


class Application(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.label_input = tk.Label(master=self.master)
        self.label_output = tk.Label(master=self.master)
        self.text_input = tk.Entry(master=self.master, width=70)
        self.text_output = tk.Label(master=self.master, width=60, anchor=tk.W)
        self.sort_button = tk.Button(master=self.master)
        self.view_model = RadixSortViewModel()
        self.init_ui()
        self.bind_events()
        self.mvvm_bind()
        self.mvvm_back_bind()

    def init_ui(self):
        self.master.title("Calculate radix sort application")
        self.master.geometry('560x110')

        self.label_input['text'] = "Enter an array to sort"
        self.label_input.grid(column=0, row=0, padx=5, pady=5)
        self.text_input.grid(column=1, row=0, padx=5, pady=5)

        self.label_output['text'] = "Sorting array"
        self.label_output.grid(column=0, row=1, padx=5, pady=5)
        self.text_output.grid(column=1, row=1, padx=5, pady=5)

        self.sort_button['text'] = "Sort"
        self.sort_button.grid(column=1, row=2, padx=5, pady=15, sticky=tk.E)

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

