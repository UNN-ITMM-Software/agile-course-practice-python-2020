import tkinter as tk

from caesar_cipher.viewmodel.viewmodel import CaesarCipherViewModel


class GUIView:
    view_model = CaesarCipherViewModel()
    
    def __init__(self):
        tk.Frame.__init__(self)
