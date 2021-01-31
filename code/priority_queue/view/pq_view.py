import tkinter as tk

from priority_queue.viewmodel.pq_viewmodel import PriorityQueueViewModel


class PQView:

    def __init__(self):
        self.pqviewmodel = PriorityQueueViewModel()
        self.window = tk.Tk()
        self.window.title("PQSandbox")
        self.listview = tk.Label(self.window, text="")
        self.field_push = tk.Entry(self.window, width=10)
        self.btn_push = tk.Button(self.window, text="Вставить",
                                  command=self.pushed, state='disabled')
        self.btn_pop = tk.Button(self.window, text="Извлечь",
                                 command=self.popped, state='disabled')
        self.field_push.bind("<KeyRelease>", self.entry_changed)
        self.listview.grid(column=0, row=0)
        self.btn_push.grid(column=0, row=1)
        self.field_push.grid(column=1, row=1)
        self.btn_pop.grid(column=2, row=1)
        self.window.geometry("235x80")
        self.window.mainloop()

    def entry_changed(self, event):
        if(self.field_push.get().isnumeric()):
            self.btn_push.configure(state='normal')
        elif(len(self.field_push.get()) == 0):
            self.btn_push.configure(state='disabled')

    def pushed(self):
        self.pqviewmodel.push(self.field_push.get())
        self.listview.configure(text=self.pq.top())
        self.btn_pop.configure(state='normal')

    def popped(self):
        self.pqviewmodel.pop()
        if(self.pqviewmodel.is_empty()):
            self.btn_pop.configure(state='disabled')
            self.listview.configure(text="")
        else:
            self.listview.configure(text=self.pqviewmodel.top())
