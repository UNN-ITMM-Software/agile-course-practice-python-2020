from modified_stack.model.modified_stack import ModifiedStack


def to_int(value):
    try:
        return int(value)
    except ValueError:
        raise ValueError('Input contains non int value')


class ModifiedStackViewModel(object):
    def __init__(self):
        self.modified_stack = ModifiedStack()
        self.pushed_element = None
        self.push_state = None
        self.pop_size = None
        self.top = None
        self.min = None
        self.input_array = None
        self.error_message = None

    def size(self):
        return self.modified_stack.size()

    def push(self):
        self.clear_error_message()
        try:
            if self.push_state == 'One':
                self.modified_stack.push(to_int(self.pushed_element))
            elif self.push_state == 'N':
                self.modified_stack.push([to_int(element) for element in self.input_array])
        except Exception as e:
            self.set_error_message(str(e))

    def pop(self):
        self.clear_error_message()
        try:
            self.modified_stack.pop(to_int(self.pop_size))
        except Exception as e:
            self.set_error_message(str(e))

    def get_top(self):
        self.clear_error_message()
        if self.modified_stack.is_empty():
            self.set_error_message('Stack is empty')
        else:
            self.top = self.modified_stack.look_top()

    def get_min(self):
        self.clear_error_message()
        if self.modified_stack.is_empty():
            self.set_error_message('Stack is empty')
        else:
            self.min = self.modified_stack.find_min()

    def set_pop_size(self, size):
        self.pop_size = size

    def set_push_state(self, state):
        self.push_state = state

    def set_pushed_element(self, value):
        self.pushed_element = value

    def set_input_array(self, input_array):
        self.input_array = input_array

    def set_error_message(self, message):
        self.error_message = message

    def get_error_message(self):
        return self.error_message

    def clear_error_message(self):
        self.error_message = None
