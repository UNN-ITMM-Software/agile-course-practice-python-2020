import tkinter as tk
from english_number_translator.viewmodel.numbers_in_words_viewmodel import NumberInWordsViewModel


class GUIView:
    view_model = NumberInWordsViewModel()

    def __init__(self):
        self.master = tk.Tk()
        self.master.title('Translating')
        self.master.geometry('305x100')
        self.master.resizable(width=False, height=False)

        self.lbl_number = tk.Label(self.master, text="Enter the number:")
        self.lbl_english = tk.Label(self.master, text="Spelling in English:")
        self.lbl_err_msg = tk.Label(self.master, foreground="red")
        self.ent_number = tk.Entry(self.master, width=30)
        self.ent_english = tk.Entry(self.master, width=30)
        self.btn_convert = tk.Button(self.master, text="Convert", state='disabled')

        self.set_weight_to_grid()
        self.bind_events()
        self.back_bind()
        self.master.mainloop()

    def set_weight_to_grid(self):
        self.lbl_number.grid(row=0, column=0, sticky="w")
        self.lbl_english.grid(row=1, column=0, sticky="w")
        self.ent_number.grid(row=0, column=1, padx=5, pady=5)
        self.ent_english.grid(row=1, column=1, padx=5, pady=5)
        self.lbl_err_msg.grid(row=2, column=0)
        self.btn_convert.grid(row=2, column=1, padx=5, pady=5, sticky="e")

    def bind_events(self):
        self.btn_convert.bind('<Button-1>', self.convert_clicked)
        self.ent_number.bind('<KeyRelease>', self.ent_number_changed)

    def bind(self):
        self.view_model.set_number_value(self.ent_number.get())
        self.ent_english.config(state='normal')

    def back_bind(self):
        self.ent_number.delete(0, tk.END)
        self.ent_number.insert(tk.END, self.view_model.get_number_value())
        self.ent_english.delete(0, tk.END)
        self.ent_english.insert(tk.END, self.view_model.get_in_english())
        self.ent_english.config(state='disabled')
        self.btn_convert.config(state=self.view_model.get_button_state())
        self.lbl_err_msg.configure(text=self.view_model.get_error_message())

    def ent_number_changed(self, event):
        self.bind()
        self.back_bind()

    def convert_clicked(self, event):
        self.bind()
        self.view_model.click_convert()
        self.back_bind()
