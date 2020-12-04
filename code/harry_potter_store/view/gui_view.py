import tkinter
from tkinter import ttk

from harry_potter_store.viewmodel.viewmodel import HPStoreViewModel


class GUIView(ttk.Frame):
    BOOKS_LIST = ["Harry Potter and the Philosopher's Stone",
                  "Harry Potter and the Chamber of Secrets",
                  "Harry Potter and the Prisoner of Azkaban",
                  "Harry Potter and the Goblet of Fire",
                  "Harry Potter and the Order of the Phoenix"]
    N_LOG_MESSAGES_TO_DISPLAY = 15
    default_sticky = tkinter.W + tkinter.E + tkinter.N + tkinter.S

    view_model = HPStoreViewModel()

    def __init__(self):
        ttk.Frame.__init__(self)
        self.master.title("Harry Potter Book Price Calculator")

        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=5)
        self.grid(sticky=tkinter.W + tkinter.E + tkinter.N + tkinter.S)

        self.book = []
        self.book_text = []
        for i in range(0, 5):
            self.book.append(ttk.Label(self, text=self.BOOKS_LIST[i]))
            self.book[i].grid(row=i, column=0, columnspan=3, sticky=tkinter.W + tkinter.N)

            self.book_text.append(tkinter.Text(self, height=1, width=1))
            self.book_text[i].grid(row=i, column=3, sticky=self.default_sticky)

        self.calc_btn = ttk.Button(self, text='Calculate')
        self.calc_btn.grid(row=6, column=3, rowspan=1, sticky=self.default_sticky)

        self.lbl_result = ttk.Label(self, text="Total Price: ")
        self.lbl_result.grid(row=7, column=0, columnspan=3, sticky=tkinter.W + tkinter.N)

        self.bind_events()
        self.set_weight_to_grid()

        self.mvvm_back_bind()

    def set_weight_to_grid(self):
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=5)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(2, weight=1)

    def bind_events(self):
        self.calc_btn.bind('<Button-1>', self.calculate_clicked)

    def mvvm_bind(self):
        books_amount = {i: v.get("1.0", tkinter.END) for i, v in enumerate(self.book_text)}
        self.view_model.set_books_amount(books_amount)

    def mvvm_back_bind(self):
        books_amount = self.view_model.get_books_amount()
        for idx, val in enumerate(self.book_text):
            self.book_text[idx].delete(1.0, tkinter.END)
            self.book_text[idx].insert(tkinter.END, books_amount.get(idx, ''))

        self.lbl_result.config(text='%s' % (self.view_model.get_result_message()))

    def calculate_clicked(self, event):
        self.mvvm_bind()
        self.view_model.click_calculate()
        self.mvvm_back_bind()
