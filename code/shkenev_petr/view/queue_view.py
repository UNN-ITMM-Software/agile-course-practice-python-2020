import tkinter as tk

from ..viewmodel.queue_viewmodel import QueueViewmodel

class QueueView(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.viewmodel = QueueViewmodel()


    def create_widgets(self):
        # Поле ввода элемента для постановки в очередь
        self.text_box = tk.Text(self, height = 1)
        self.text_box.pack()

        # Кнопка вставки
        self.button_enqueue = tk.Button(self)
        self.button_enqueue["text"] = "Enqueue"
        self.button_enqueue["command"] = self.enqueue
        self.button_enqueue.pack()

        # Отображение содержимого очереди
        self.text_box_queue = tk.Text(self, height = 10)
        self.text_box_queue.pack()

        # Кнопка извлечения элемента из очереди
        self.button_dequeue = tk.Button(self)
        self.button_dequeue["text"] = "Dequeue"
        self.button_dequeue["command"] = self.dequeue
        self.button_dequeue.pack()

        # Отображение первого в очереди элемента
        self.label = tk.Label(self)
        self.label.pack()


    def enqueue(self):
        self.viewmodel.enqueue(self.text_box.get("1.0",'end-1c'))
        self.label['text'] = self.viewmodel.peek
        self.text_box_queue.delete(1.0, "end-1c")
        self.text_box_queue.insert("end-1c", self.viewmodel.string)


    def dequeue(self):
        self.viewmodel.dequeue()
        self.label['text'] = self.viewmodel.peek
        self.text_box_queue.delete(1.0, "end-1c")
        self.text_box_queue.insert("end-1c", self.viewmodel.string)


root = tk.Tk()
app = QueueView(master=root)
app.mainloop()