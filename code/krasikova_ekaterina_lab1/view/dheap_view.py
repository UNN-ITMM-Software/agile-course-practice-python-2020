import tkinter as tk

from krasikova_ekaterina_lab1.viewmodel import dheap_viewmodel


class DHeapView:

    view_model = dheap_viewmodel.DHeapViewModel()
    N_LOG_MESSAGES_TO_DISPLAY = 8

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('D-Heap')
        self.root.geometry('900x600')
        self.root.resizable(width=False, height=False)

        self.frame = tk.Frame(self.root)

        self.entry_param_d_label = tk.Label(self.root, text="D:")
        self.entry_param_d = tk.Entry(self.root, width=10)
        self.input_data_label = tk.Label(self.root, text="Input data:")
        self.input_data = tk.Entry(self.root, width=60)
        self.create_btn = tk.Button(self.root, text="Create", state='disabled')

        self.current_data_label = tk.Label(self.root, text="Current data:")
        self.current_data = tk.Entry(self.root, width=60)

        self.insert_label = tk.Label(self.root, text="Insert element:")
        self.insert_data = tk.Entry(self.root, width=10)
        self.insert_btn = tk.Button(self.root, text="Insert", state='disabled')

        self.delete_label = tk.Label(self.root, text="Delete element:")
        self.delete_data = tk.Entry(self.root, width=10)
        self.delete_btn = tk.Button(self.root, text="Delete", state='disabled')

        self.decrease_label = tk.Label(self.root, text="Decrease weight:")
        self.decrease_data = tk.Entry(self.root, width=10)
        self.decrease_btn = tk.Button(self.root, text="Decrease", state='disabled')

        self.logger_lbl = tk.Label(self.root, text="log: ")

        self.set_weight_to_grid()
        self.bind_events()
        self.root.mainloop()

    def set_weight_to_grid(self):
        self.frame.place(relx=0.2, rely=0.2, relwidth=0.8, relheight=0.8)
        self.entry_param_d.grid(row=0, column=1, stick='wens', padx=5, pady=5)
        self.entry_param_d_label.grid(row=0, column=0, stick='wens', padx=5, pady=5)
        self.input_data_label.grid(row=0, column=2, stick='wens', padx=5, pady=5)
        self.input_data.grid(row=0, column=3, stick='wens', padx=5, pady=5)
        self.create_btn.grid(row=0, column=4, stick='wens', padx=5, pady=5)
        self.current_data_label.grid(row=1, column=2, stick='wens', padx=5, pady=5)
        self.current_data.grid(row=1, column=3, stick='wens', padx=5, pady=5)

        self.insert_label.grid(row=2, column=0, stick='wens', padx=5, pady=5)
        self.insert_data.grid(row=2, column=1, stick='wens', padx=5, pady=5)
        self.insert_btn.grid(row=2, column=2, stick='wens', padx=5, pady=5)

        self.delete_label.grid(row=3, column=0, stick='wens', padx=5, pady=5)
        self.delete_data.grid(row=3, column=1, stick='wens', padx=5, pady=5)
        self.delete_btn.grid(row=3, column=2, stick='wens', padx=5, pady=5)

        self.decrease_label.grid(row=4, column=0, stick='wens', padx=5, pady=5)
        self.decrease_data.grid(row=4, column=1, stick='wens', padx=5, pady=5)
        self.decrease_btn.grid(row=4, column=2, stick='wens', padx=5, pady=5)

        self.logger_lbl.grid(row=6, column=0, sticky='wens', padx=5, pady=5)

    def bind_events(self):
        self.entry_param_d.bind('<KeyRelease>', self.input_data_changed)
        self.input_data.bind('<KeyRelease>', self.input_data_changed)
        self.insert_data.bind('<KeyRelease>', self.insert_data_changed)
        self.delete_data.bind('<KeyRelease>', self.delete_data_changed)
        self.decrease_data.bind('<KeyRelease>', self.decrease_data_changed)

        self.create_btn.bind('<Button-1>', self.create_btn_clicked)
        self.insert_btn.bind('<Button-1>', self.insert_btn_clicked)
        self.delete_btn.bind('<Button-1>', self.delete_btn_clicked)
        self.decrease_btn.bind('<Button-1>', self.decrease_btn_clicked)

    def input_data_changed(self, event):
        self.mvvm_create_bind()
        self.mvvm_create_back_bind()

    def insert_data_changed(self, event):
        self.mvvm_insert_bind()
        self.mvvm_insert_back_bind()

    def delete_data_changed(self, event):
        self.mvvm_delete_bind()
        self.mvvm_delete_back_bind()

    def decrease_data_changed(self, event):
        self.mvvm_decrease_bind()
        self.mvvm_decrease_back_bind()

    def create_btn_clicked(self, event):
        self.mvvm_create_bind()
        self.view_model.create_btn_clicked()
        self.mvvm_create_back_bind()

    def insert_btn_clicked(self, event):
        self.mvvm_insert_bind()
        self.view_model.insert_btn_clicked()
        self.mvvm_insert_back_bind()

    def delete_btn_clicked(self, event):
        self.mvvm_delete_bind()
        self.view_model.delete_btn_clicked()
        self.mvvm_delete_back_bind()

    def decrease_btn_clicked(self, event):
        self.mvvm_decrease_bind()
        self.view_model.decrease_btn_clicked()
        self.mvvm_decrease_back_bind()

    def mvvm_create_bind(self):
        self.view_model.set_input_data(self.entry_param_d.get(), self.input_data.get())

    def mvvm_insert_bind(self):
        self.view_model.set_inserting_elem(self.insert_data.get())

    def mvvm_delete_bind(self):
        self.view_model.set_deleting_elem(self.delete_data.get())

    def mvvm_decrease_bind(self):
        self.view_model.set_decreasing_elem(self.decrease_data.get())

    def mvvm_create_back_bind(self):
        self.create_btn.config(state=self.view_model.get_create_btn_state())
        self.current_data.delete(0, tk.END)
        self.current_data.insert(tk.END, self.view_model.get_current_data())
        logger_text = '\n'.join(
            self.view_model.logger.get_log_messages()[:-self.N_LOG_MESSAGES_TO_DISPLAY:-1])
        self.logger_lbl.config(text=logger_text)

    def mvvm_insert_back_bind(self):
        self.insert_btn.config(state=self.view_model.get_insert_btn_state())
        self.current_data.delete(0, tk.END)
        self.current_data.insert(tk.END, self.view_model.get_current_data())
        logger_text = '\n'.join(
            self.view_model.logger.get_log_messages()[:-self.N_LOG_MESSAGES_TO_DISPLAY:-1])
        self.logger_lbl.config(text=logger_text)

    def mvvm_delete_back_bind(self):
        self.delete_btn.config(state=self.view_model.get_delete_btn_state())
        self.current_data.delete(0, tk.END)
        self.current_data.insert(tk.END, self.view_model.get_current_data())
        logger_text = '\n'.join(
            self.view_model.logger.get_log_messages()[:-self.N_LOG_MESSAGES_TO_DISPLAY:-1])
        self.logger_lbl.config(text=logger_text)

    def mvvm_decrease_back_bind(self):
        self.decrease_btn.config(state=self.view_model.get_decrease_btn_state())
        self.current_data.delete(0, tk.END)
        self.current_data.insert(tk.END, self.view_model.get_current_data())
        logger_text = '\n'.join(
            self.view_model.logger.get_log_messages()[:-self.N_LOG_MESSAGES_TO_DISPLAY:-1])
        self.logger_lbl.config(text=logger_text)
