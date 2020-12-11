from tarakanov_kirill_lab1.model.modified_stack import ModifiedStack


class ModifiedStackViewModel(object):
    def __init__(self):
        self.pushed_element = None
        self.top = None
        self.min = None
        self.pop_size = None
        self.modified_stack = ModifiedStack()
        self.error_message = None

    def set_pushed_element(self, value):
        self.pushed_element = int(value)

    def push(self):
        self.modified_stack.push(self.pushed_element)

    def pop(self):
        try:
            self.modified_stack.pop(int(self.pop_size))
            self.clear_error_message()
        except Exception as e:
            self.error_message = str(e)

    def get_top(self):
        self.top = self.modified_stack.look_top()

    def get_min(self):
        self.min = self.modified_stack.find_min()

    def set_pop_size(self, size):
        self.pop_size = size

    def get_error_message(self):
        return self.error_message

    def clear_error_message(self):
        self.error_message = None
