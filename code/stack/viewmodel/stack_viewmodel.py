from stack.model.stack import Stack

class StackViewModel:
    def __init__(self, size=None):
        self.push_button_enabled = 'disabled'
        self.pop_button_enabled = 'disabled'
        self.size_button_enabled = 'disabled'

        self.stack = Stack(size)
        self.input_value = None
        self.input_size = None
        self.pop_result = None
        self.error = None

    def validate_size(self):
        if isinstance(self.input_size, int) and self.input_size > 0:
            self.set_size_button_enabled()
            return True
        else:
            self.set_size_button_disabled()
            return False

    def validate_input(self):
        if isinstance(self.input_value, int) or isinstance(self.input_value, float):
            self.set_input_button_enabled()
            return True
        else:
            self.set_input_button_disabled()
            return False

    def set_input_button_enabled(self):
        self.push_button_enabled = 'normal'

    def set_input_button_disabled(self):
        self.push_button_enabled = 'disabled'

    def set_output_button_enabled(self):
        self.pop_button_enabled = 'normal'

    def set_output_button_disabled(self):
        self.pop_button_enabled = 'disabled'

    def set_size_button_enabled(self):
        self.size_button_enabled = 'normal'

    def set_size_button_disabled(self):
        self.size_button_enabled = 'disabled'

    def input_click(self):
        if self.is_input_button_enable() == 'normal' and self.validate_input():
           try:
               self.clear_pop_result()
               self.clear_error()
               self.stack.push(self.input_value)
               self.set_output_button_enabled()
               if self.stack.isFull():
                   self.set_input_button_disabled()
                   self.error = 'Стэк переполнен'
           except:
               self.error = 'Ошибка добавления числа'
        else:
            self.error = 'Введение данные неверного типа'

    def output_click(self):
        if self.is_output_button_enable() and not self.stack.isEmpty():
            try:
                self.clear_error()
                self.pop_result = self.stack.pop()
                if self.stack.isEmpty():
                    self.set_output_button_disabled()
                    self.error = 'Стэк пуст'
            except:
                self.error = 'Ошибка получения значения'
        else:
            self.error = 'Стэк пуст'

    def size_click(self):
        if self.is_size_button_enable() and self.validate_size():
            try:
                self.stack.set_size(self.input_size)
            except:
                self.error = 'Ошибка изменения размера стека'


    def set_input_value(self, value):
        try:
            self.input_value = int(value)
        except:
            try:
                self.input_value = float(value)
            except:
                self.input_value = value
        self.validate_input()

    def get_input_value(self):
        return self.input_value

    def get_pop_result(self):
        return self.pop_result

    def clear_pop_result(self):
        self.pop_result = None

    def is_input_button_enable(self):
        return self.push_button_enabled

    def is_output_button_enable(self):
        return self.pop_button_enabled

    def is_size_button_enable(self):
        return self.size_button_enabled

    def get_stack_size(self):
        return self.stack.get_stack_size()

    def set_size_value(self, size):
        try:
            self.input_size = int(size)
        except:
            self.input_size = size
        self.validate_size()

    def set_stack_size(self, size):
        self.stack.set_size(size)

    def get_stack_values(self):
        return self.stack.get_stack()

    def clear_error(self):
        self.error = None

    def get_error(self):
        return self.error
