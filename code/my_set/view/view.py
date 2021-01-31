import tkinter as tk
from tkinter import ttk

from my_set.viewmodel.viewmodel import SetViewModel


class GUI(ttk.Frame):
    view_model = SetViewModel()

    def __init__(self):
        ttk.Frame.__init__(self)
        self.master.title("Set")

        self.set_a_label = tk.Label(self.master, text="Set A")
        self.set_a_label.grid(row=0, column=0)

        self.set_b_label = tk.Label(self.master, text="Set B")
        self.set_b_label.grid(row=0, column=1)

        self.input_for_set_a = tk.Entry(self.master,)
        self.input_for_set_a.grid(row=1, column=0)

        self.button_add_to_set_a = tk.Button(self.master, text='Add to A')
        self.button_add_to_set_a.grid(row=2, column=0)

        self.input_for_set_b = tk.Entry(self.master)
        self.input_for_set_b.grid(row=1, column=1)

        self.button_add_to_set_b = tk.Button(self.master, text='Add to B')
        self.button_add_to_set_b.grid(row=2, column=1)

        self.button_delete_to_set_a = tk.Button(self.master, text='Delete from A')
        self.button_delete_to_set_a.grid(row=3, column=0)

        self.button_delete_to_set_b = tk.Button(self.master, text='Delete from B')
        self.button_delete_to_set_b.grid(row=3, column=1)

        self.button_union_ab = tk.Button(self.master, text="A = Union(A, B)")
        self.button_union_ab.grid(row=5, column=0)

        self.intersection_ab_label = tk.Label(self.master, text="A & B = ")
        self.intersection_ab_label.grid(row=5, column=1)

        self.difference_ab_label = tk.Label(self.master, text="A \ B = ")
        self.difference_ab_label.grid(row=6, column=0)

        self.difference_ba_label = tk.Label(self.master, text="A / B = ")
        self.difference_ba_label.grid(row=6, column=1)

        self.status = tk.Label(self.master, text="STATUS:")
        self.status.grid(row=8, column=2)

        self.bind_events()
        self.mvvm_back_bind()

    def bind_events(self):
        self.button_add_to_set_a.bind('<Button-1>', self.button_add_to_set_a__clicked)
        self.button_add_to_set_b.bind('<Button-1>', self.button_add_to_set_b__clicked)

        self.button_delete_to_set_a.bind('<Button-1>', self.button_delete_from_set_a__clicked)
        self.button_delete_to_set_b.bind('<Button-1>', self.button_delete_from_set_b__clicked)

        self.button_union_ab.bind('<Button-1>', self.button_union_ab__clicked)

        self.input_for_set_a.bind('<FocusOut>', self.change_data)
        self.input_for_set_b.bind('<FocusOut>', self.change_data)

        self.intersection_ab_label.bind('<FocusOut>', self.change_data)
        self.difference_ab_label.bind('<FocusOut>', self.change_data)
        self.difference_ba_label.bind('<FocusOut>', self.change_data)

    def change_data(self, event):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def mvvm_back_bind(self):
        self.input_for_set_a.delete(0, tk.END)
        self.input_for_set_a.insert(tk.INSERT, '')

        self.input_for_set_b.delete(0, tk.END)
        self.input_for_set_b.insert(tk.INSERT, '')

        self.set_a_label.config(text="Set A = {}".format(self.view_model.set_a_to_str()))
        self.set_b_label.config(text="Set B = {}".format(self.view_model.set_b_to_str()))
        self.intersection_ab_label.config(text="A & B = {}".format(self.view_model.intersection()))
        self.difference_ab_label.config(text="A \ B = {}".format(self.view_model.difference(mode='A\B')))
        self.difference_ba_label.config(text="B \ A = {}".format(self.view_model.difference(mode='B\A')))

        self.status.config(text="STATUS: {}".format(self.view_model.get_status()))

    def mvvm_bind(self):
        self.input_for_set_a__obtained = self.input_for_set_a.get()
        self.input_for_set_b__obtained = self.input_for_set_b.get()

    def button_add_to_set_a__clicked(self, event):
        self.mvvm_bind()
        self.view_model.add(self.input_for_set_a__obtained, 'A')
        self.mvvm_back_bind()

    def button_add_to_set_b__clicked(self, event):
        self.mvvm_bind()
        self.view_model.add(self.input_for_set_b__obtained, 'B')
        self.mvvm_back_bind()

    def button_delete_from_set_a__clicked(self, event):
        self.mvvm_bind()
        self.view_model.delete(self.input_for_set_a__obtained, 'A')
        self.mvvm_back_bind()

    def button_delete_from_set_b__clicked(self, event):
        self.mvvm_bind()
        self.view_model.delete(self.input_for_set_b__obtained, 'B')
        self.mvvm_back_bind()

    def button_union_ab__clicked(self, event):
        self.mvvm_bind()
        self.view_model.union()
        self.mvvm_back_bind()
