import tkinter as tk

import viewmodel


class QueueView:

    view_model = viewmodel.QueueViewModel()

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Queue')
        self.root.geometry('900x300')
        self.root.resizable(width=False, height=False)

        self.frame = tk.Frame(self.root)
        self.start_message = tk.Label(self.root, text="Enter anything and press 'Arrive' button. Each input info is one element")
        self.input_info_label = tk.Label(self.root, text="Write an element for the queue:")
        self.input_info = tk.Entry(self.root, width=50)
        self.arrive_btn = tk.Button(self.root, text="Arrive", state='disabled')
        self.leave_btn = tk.Button(self.root, text="Leave", state='disabled')
        self.arrived_info_label = tk.Label(self.root, text="Current state of the queue:")
        self.arrived_info = tk.Entry(self.root, width=50)

        self.set_weight_to_grid()
        self.bind_events()
        self.root.mainloop()

    def set_weight_to_grid(self):
        self.root.grid_rowconfigure(1, minsize=30)
        self.root.grid_rowconfigure(3, minsize=30)
        self.root.grid_rowconfigure(5, minsize=30)
        self.frame.place(relx=0.2, rely=0.2, relwidth=0.8, relheight=0.8)
        self.start_message.grid(row=0, column=0, stick='wens', padx=5, pady=5)
        self.input_info_label.grid(row=2, column=0, stick='wens', padx=5, pady=5)
        self.input_info.grid(row=2, column=1, stick='wens', padx=5, pady=5)
        self.arrive_btn.grid(row=4, column=0, columnspan=2, ipadx=30, ipady=6, padx=5, pady=5)
        self.leave_btn.grid(row=4, column=1, columnspan=2, ipadx=30, ipady=6, padx=5, pady=5)
        self.arrived_info_label.grid(row=6, column=0, stick='wens', padx=5, pady=5)
        self.arrived_info.grid(row=6, column=1, stick='wens', padx=5, pady=5)

    def bind_events(self):
        self.input_info.bind('<KeyRelease>', self.input_info_changed)
        self.arrive_btn.bind('<Button-1>', self.arrive_btn_clicked)
        self.leave_btn.bind('<Button-1>', self.leave_btn_clicked)

    def input_info_changed(self, event):
        self.mvvm_bind()
        self.mvvm_arrive_bind()

    def arrive_btn_clicked(self, event):
        self.mvvm_bind()
        self.view_model.arrive_btn_clicked()
        self.mvvm_arrive_bind()

    def leave_btn_clicked(self, event):
        self.mvvm_bind()
        self.view_model.leave_btn_clicked()
        self.mvvm_leave_bind()

    def mvvm_bind(self):
        self.view_model.set_input_info(self.input_info.get())

    def mvvm_arrive_bind(self):
        self.arrive_btn.config(state=self.view_model.get_arrive_btn_state())
        self.arrived_info.delete(0, tk.END)
        self.arrived_info.insert(tk.END, self.view_model.get_arrived_info())

    def mvvm_leave_bind(self):
        self.leave_btn.config(state=self.view_model.get_leave_btn_state())
        self.arrived_info.delete(0, tk.END)
        self.arrived_info.insert(tk.END, self.view_model.get_arrived_info())