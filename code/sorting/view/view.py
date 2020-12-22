import tkinter as tk

from sorting.viewmodel import viewmodel


class SortingView:

    view_model = viewmodel.SortingViewModel()

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Sorting numbers')
        self.root.geometry('900x300')
        self.root.resizable(width=False, height=False)

        self.frame = tk.Frame(self.root)
        self.start_message = tk.Label(self.root, text="Enter numbers separated by spaces")
        self.input_array_label = tk.Label(self.root, text="Input array of numbers:")
        self.input_array = tk.Entry(self.root, width=100)
        self.sort_btn = tk.Button(self.root, text="Sort", state='disabled')
        self.sorted_array_label = tk.Label(self.root, text="Sorted array of numbers:")
        self.sorted_array = tk.Entry(self.root, width=100)

        self.set_weight_to_grid()
        self.bind_events()
        self.root.mainloop()

    def set_weight_to_grid(self):
        self.root.grid_rowconfigure(1, minsize=30)
        self.root.grid_rowconfigure(3, minsize=30)
        self.root.grid_rowconfigure(5, minsize=30)
        self.frame.place(relx=0.2, rely=0.2, relwidth=0.8, relheight=0.8)
        self.start_message.grid(row=0, column=0, stick='wens', padx=5, pady=5)
        self.input_array_label.grid(row=2, column=0, stick='wens', padx=5, pady=5)
        self.input_array.grid(row=2, column=1, stick='wens', padx=5, pady=5)
        self.sort_btn.grid(row=4, column=0, stick='wens', padx=5, pady=5)
        self.sorted_array_label.grid(row=6, column=0, stick='wens', padx=5, pady=5)
        self.sorted_array.grid(row=6, column=1, stick='wens', padx=5, pady=5)

    def bind_events(self):
        self.input_array.bind('<KeyRelease>', self.input_array_changed)
        self.sort_btn.bind('<Button-1>', self.sort_btn_clicked)

    def input_array_changed(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def sort_btn_clicked(self, event):
        self.mvvm_bind()
        self.view_model.sort_btn_clicked()
        self.mvvm_back_bind()

    def mvvm_bind(self):
        self.view_model.set_input_array(self.input_array.get())

    def mvvm_back_bind(self):
        self.sort_btn.config(
            state=self.view_model.get_sort_btn_state())
        self.sorted_array.delete(0, tk.END)
        self.sorted_array.insert(tk.END, self.view_model.get_sorted_array())
