import tkinter as tk

from caesar_cipher.viewmodel.viewmodel import CaesarCipherViewModel


class GUIView(tk.Frame):
    view_model = CaesarCipherViewModel()

    def encipher(self):
        self.view_model.set_offset(self.offset_value.get("1.0", tk.END))
        self.view_model.set_input_text(self.input_value.get("1.0", tk.END))
        self.view_model.encipher()
        self.output_label.configure(text=self.view_model.get_output_text())

    def decipher(self):
        self.view_model.set_offset(self.offset_value.get("1.0", tk.END))
        self.view_model.set_input_text(self.input_value.get("1.0", tk.END))
        self.view_model.decipher()
        self.output_label.configure(text=self.view_model.get_output_text())

    def __init__(self):
        tk.Frame.__init__(self)
        self.master.title("Caesar Cipher")
        self.master.minsize(width=300, height=250)
        self.grid(sticky=tk.W + tk.E + tk.N + tk.S)

        self.offset_label = tk.Label(self, text="Offset", font="Arial 14")
        self.offset_label.pack()

        self.offset_value = tk.Text(self, width=30, height=1, font="Arial 14")
        self.offset_value.pack()

        self.input_label = tk.Label(self, text="Input text", font="Arial 14")
        self.input_label.pack()

        self.input_value = tk.Text(self, width=30, height=1, font="Arial 14")
        self.input_value.pack()

        self.encipher = tk.Button(self, text="encipher", width=15, height=1, font="Arial 14", bg="gold",
                                  command=self.encipher)
        self.encipher.pack()

        self.decipher = tk.Button(self, text="decipher", width=15, height=1, font="Arial 14", bg="gold",
                                  command=self.decipher)
        self.decipher.pack()

        self.output_label = tk.Label(self, text="Output text", font="Arial 14")
        self.output_label.pack()
