import tkinter as tk
from tkinter import ttk

from segment_tree.viewmodel import viewmodel


def get_text(value):
    if value is None:
        return "none"
    elif not value:
        return "empty"
    else:
        return value


def get_error(value):
    return value if value else ''


class GUIView(object):

    view_model = viewmodel.SegmentTreeViewModel()

    def __init__(self):
        self.root = tk.Tk()
        self.box_list = []
        self.root['bg'] = 'gray21'
        self.error_array_size = None

        self.root.title('Find sum / min / max using segment tree')
        self.root.geometry('700x850')
        self.frame = tk.Frame(self.root, bg='gray21')
        self.root.resizable(width=False, height=False)
        self.state = tk.StringVar()
        self.state.set('sum')
        self.dif = 0
        ttk_custom_style = ttk.Style()
        ttk_custom_style.configure('Custom.TRadiobutton', background="gray21", foreground='white')
        self.frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)
        self.title_size_array = tk.Label(self.frame, text="Enter the Size of Array:", bg='gray21', fg='white')
        self.title_size_array.grid(row=0, column=0, stick='w')
        array_size = tk.IntVar()

        self.array_size = tk.Entry(self.frame, textvariable=array_size, bd="1", width="7")
        self.array_size.grid(row=0, column=1)

        self.submit_size = tk.Button(self.frame, text="Submit size",
                                     command=lambda: self.create_windows_array_elements(array_size),
                                     bg='gray21', fg='white')

        self.submit_size.grid(row=0, column=2)

        self.get_indexes_label = tk.Label(self.frame, text="Get result from:", bg='gray21', fg='white')
        start_idx = tk.IntVar()
        self.start_idx = tk.Entry(self.frame, textvariable=start_idx, bd="1", width="2")
        self.get_last_idx_label = tk.Label(self.frame, text="index to:", bg='gray21', fg='white')
        last_idx = tk.IntVar()
        self.last_idx = tk.Entry(self.frame, textvariable=last_idx, bd="1", width="2")
        self.segment_tree_sum_rbtn = ttk.Radiobutton(self.frame, text="sum", variable=self.state,
                                                     value="sum", width=10,
                                                     style='Custom.TRadiobutton')
        self.segment_tree_min_rbtn = ttk.Radiobutton(self.frame, text="min", variable=self.state,
                                                     value="min", width=10,
                                                     style='Custom.TRadiobutton')
        self.segment_tree_max_rbtn = ttk.Radiobutton(self.frame, text="max", variable=self.state,
                                                     value="max", width=10,
                                                     style='Custom.TRadiobutton')

        self.build_button = tk.Button(self.frame, text='Build tree', bg='gray21', fg='white')
        self.get_button = tk.Button(self.frame, text='Get result\n for current boards',
                                    bg='gray21', fg='white')

        self.additional_option = tk.Label(self.frame, text="Change custom element in\n"
                                                           " array and build tree:", bg='gray21', fg='white')
        self.update_idx_label = tk.Label(self.frame, text="Index of update element:", bg='gray21', fg='white')
        self.update_value_label = tk.Label(self.frame, text="New value for element:", bg='gray21', fg='white')
        self.update_idx = tk.Entry(self.frame, bd="1", width="2")
        self.update_value = tk.Entry(self.frame, bd="1", width="2")

        self.update_button = tk.Button(self.frame, text='Update array value', bg='gray21', fg='white')
        self.result_label = tk.Label(self.frame, text='The result will be here later!',
                                     bg='gray21', fg='white')
        self.error_field = tk.Label(self.frame, text='', fg='red', bg='gray21')

        self.update_position()

        self.bind_events()

        self.root.mainloop()

    def create_windows_array_elements(self, array_size):
        if array_size.get() > 0:
            for box in self.box_list:
                box.destroy()
            self.box_list = []
            current_size = array_size.get()
            self.title = tk.Label(self.frame, text='Enter your array: ', bg='gray21', fg='white')
            self.title.grid(row=1, column=0)
            for current_box in range(current_size):
                self.box_list.append(tk.Entry(self.frame, bg='gray21', fg='white', bd="1", width="3"))
                self.box_list[-1].grid(row=2 + current_box)
            self.dif += current_size
            self.update_position()
        else:
            self.error_array_size = "Wrong input array size"
            self.mvvm_back_bind_build()

    def update_position(self):
        self.get_indexes_label.grid(row=3 + self.dif, column=0, sticky=tk.W)
        self.start_idx.grid(row=(3 + self.dif), column=1)
        self.get_last_idx_label.grid(row=3 + self.dif, column=2)
        self.last_idx.grid(row=3 + self.dif, column=3)
        self.segment_tree_sum_rbtn.grid(row=4 + self.dif, column=0)
        self.segment_tree_min_rbtn.grid(row=5 + self.dif, column=0)
        self.segment_tree_max_rbtn.grid(row=6 + self.dif, column=0)
        self.build_button.grid(row=5 + self.dif, column=2)
        self.get_button.grid(row=6 + self.dif, column=2)

        self.additional_option.grid(row=7 + self.dif, column=0)
        self.update_idx_label.grid(row=8 + self.dif, column=0)
        self.update_value_label.grid(row=9 + self.dif, column=0)
        self.update_idx.grid(row=8 + self.dif, column=1)
        self.update_value.grid(row=9 + self.dif, column=1)
        self.update_button.grid(row=9 + self.dif, column=2)

        self.result_label.grid(row=10 + self.dif, column=1)
        self.error_field.grid(row=11 + self.dif, column=1)

    def mvvm_bind_btn_build(self):
        box_values = [box.get() for box in self.box_list]
        self.view_model.set_input_array(box_values)
        self.view_model.set_method(self.state.get())

    def mvvm_bind_btn_get(self):
        self.view_model.set_left_border(self.start_idx.get())
        self.view_model.set_right_border(self.last_idx.get())

    def mvvm_bind_btn_update(self):
        self.view_model.set_update_index(self.update_idx.get())
        self.view_model.set_update_value(self.update_value.get())

        if isinstance(self.view_model.get_update_index(), int) and \
                0 <= self.view_model.get_update_index() < len(self.box_list) and\
                self.box_list[self.view_model.get_update_index()].get() \
                and self.view_model.get_input_array():
            self.box_list[self.view_model.get_update_index()].delete(0, tk.END)
            self.box_list[self.view_model.get_update_index()].\
                insert(0, str(self.view_model.get_update_value()))

    def bind_events(self):
        self.start_idx.bind('<KeyRelease>', self.write_idxs)
        self.last_idx.bind('<KeyRelease>', self.write_idxs)

        self.build_button.bind('<Button-1>', self.build_button_clicked)
        self.update_button.bind('<Button-1>', self.update_button_clicked)
        self.get_button.bind('<Button-1>', self.get_button_clicked)

    def build_button_clicked(self, event):
        self.mvvm_bind_btn_build()
        self.view_model.calculate()
        self.mvvm_back_bind_build()

    def update_button_clicked(self, event):
        self.mvvm_bind_btn_update()
        self.view_model.update()
        self.mvvm_back_bind_update()

    def get_button_clicked(self, event):
        self.mvvm_bind_btn_get()
        self.view_model.cut_array_for_given_border()
        self.mvvm_back_bind_result()

    def write_idxs(self, event):
        self.mvvm_bind_btn_get()
        self.mvvm_back_bind_result()

    def mvvm_back_bind_build(self):
        self.get_button.config(state=self.view_model.is_build_button_enable())
        if self.view_model.get_success_procedure():
            self.result_label.config(text="The tree was successfully created\n")
        else:
            self.result_label.config(text="")
        if not self.error_array_size:
            self.error_field.config(text='{}\n'.format(
                get_error(self.view_model.get_error_message())))
        else:
            self.error_field.config(text='{}\n'.format(self.error_array_size))
            self.error_array_size = None

    def mvvm_back_bind_update(self):
        self.get_button.config(state=self.view_model.is_update_button_enable())
        if self.view_model.get_success_procedure():
            self.result_label.config(text="The tree was successfully updated\n")
        else:
            self.result_label.config(text="")
        if not self.error_array_size:
            self.error_field.config(text='{}\n'.format(
                get_error(self.view_model.get_error_message())))
        else:
            self.error_field.config(text='{}\n'.format(self.error_array_size))
            self.error_array_size = None

    def mvvm_back_bind_result(self):
        self.get_button.config(state=self.view_model.is_get_button_enable())
        if self.view_model.get_success_procedure():
            self.result_label.config(text='Result of operation: {}\n'.format(
                get_text(self.view_model.get_calculate_result())))
        else:
            self.result_label.config(text="")
        if not self.error_array_size:
            self.error_field.config(text='{}\n'.format(
                get_error(self.view_model.get_error_message())))
        else:
            self.error_field.config(text='{}\n'.format(self.error_array_size))
            self.error_array_size = None
