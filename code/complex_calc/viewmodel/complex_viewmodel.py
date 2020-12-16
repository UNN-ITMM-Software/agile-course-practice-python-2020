import re

from complex_calc.model.complex_num import ComplexNum


class ComplexNumViewModel:
    def __init__(self):
        self.answer_text = ''
        self.set_btn_disabled()
        self.first_complex_num = ''
        self.second_complex_num = ''
        self.operation = '+'
        self.set_btn_disabled()

    def get_button_convert_state(self):
        return self.button_convert_state

    def set_second_complex_num(self, value):
        self.second_complex_num = value.strip()
        self.validate_text()

    def validate_text(self):
        is_first_complex_num = self.is_complex(self.first_complex_num)
        is_second_complex_num = self.is_complex(self.second_complex_num)
        if is_first_complex_num and is_second_complex_num:
            self.set_btn_enabled()
        else:
            self.set_btn_disabled()

    def set_btn_enabled(self):
        self.button_convert_state = 'normal'

    def set_btn_disabled(self):
        self.button_convert_state = 'disabled'

    def get_second_complex_num(self):
        return self.second_complex_num

    def set_first_complex_num(self, value):
        self.first_complex_num = value.strip()
        self.validate_text()

    def get_first_complex_num(self):
        return self.first_complex_num

    def is_complex(self, string):
        p = re.compile('^\s*[+-]?((\d+)?[.,])?(\d*)?\s*[+-]\s*((\d+)?[.,])?(\d+)?[*_x]?[ij]\s*$')
        if p.match(string):
            return True
        return False

    def get_complex_num_as_list_from_string(self, string):
        complex_string = ''.join(string.split()).replace('i', 'j')
        c_n = complex(complex_string)
        return c_n

    def click_convert(self):
        first_c_n = self.get_complex_num_as_list_from_string(self.first_complex_num)
        first_complex_num = ComplexNum(first_c_n.real, first_c_n.imag)
        second_c_n = self.get_complex_num_as_list_from_string(self.second_complex_num)
        second_complex_num = ComplexNum(second_c_n.real, second_c_n.imag)
        if self.operation == '+':
            self.answer_text = str(first_complex_num + second_complex_num)
        elif self.operation == '-':
            self.answer_text = str(first_complex_num - second_complex_num)
        elif self.operation == '*':
            self.answer_text = str(first_complex_num * second_complex_num)
        elif self.operation == '/':
            try:
                self.answer_text = str(first_complex_num / second_complex_num)
            except:
                result = 'Error! Cannot divide by zero!'
                self.answer_text = str(result)
        elif self.operation == '==':
            self.answer_text = str(first_complex_num == second_complex_num)
        elif self.operation == '!=':
            self.answer_text = str(first_complex_num != second_complex_num)

    def get_answer_text(self):
        return self.answer_text

    def set_operation(self, operation):
        self.operation = operation
