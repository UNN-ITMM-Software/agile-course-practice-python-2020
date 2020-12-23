import os


from segment_tree.model.segment_tree import SegmentTree
from segment_tree.logger.reallogger import RealLogger


class SegmentTreeViewModel(object):

    def __init__(self, logger=RealLogger(os.path.join('..', '..', 'tmp', 'segment_tree.log'))):
        self.logger = logger
        self.method = None
        self.input_array = None
        self.segment_tree = None
        self.input_size = None

        self.left_border = None
        self.right_border = None

        self.update_value = None
        self.update_index = None

        self.calculate_result = None
        self.error_message = None

        self.success_procedure = False
        self.buttons = {"build_button_enabled": "disabled",
                        "get_button_enabled": "disabled",
                        "update_button_enabled": "disabled"}

        self.logger.log('Welcome to segment tree application')

    def is_build_button_enable(self):
        return self.buttons["build_button_enabled"]

    def is_get_button_enable(self):
        return self.buttons["get_button_enabled"]

    def is_update_button_enable(self):
        return self.buttons["update_button_enabled"]

    def validate_data_build_button(self):
        if isinstance(self.input_size, int) and self.input_size > 0:
            self.set_build_btn_enabled()
        else:
            self.set_build_btn_disabled()

    def validate_data_get_button(self):
        if isinstance(self.left_border, int) and isinstance(self.right_border, int):
            self.set_get_btn_enabled()
        else:
            self.set_get_btn_disabled()

    def validate_data_update_button(self):
        if isinstance(self.update_index, int) and isinstance(self.update_value, int) and self.input_array:
            self.set_update_btn_enabled()
        else:
            self.set_update_btn_disabled()

    def set_build_btn_enabled(self):
        self.buttons["build_button_enabled"] = 'normal'

    def set_build_btn_disabled(self):
        self.buttons["build_button_enabled"] = 'disabled'

    def set_get_btn_enabled(self):
        self.buttons["get_button_enabled"] = 'normal'

    def set_get_btn_disabled(self):
        self.buttons["get_button_enabled"] = 'disabled'

    def set_update_btn_enabled(self):
        self.buttons["update_button_enabled"] = 'normal'

    def set_update_btn_disabled(self):
        self.buttons["update_button_enabled"] = 'disabled'

    def set_input_size(self, input_size):
        try:
            self.input_size = None
            self.input_size = int(input_size)
            if self.input_size <= 0:
                self.error_message = 'Incorrect value of input size'
                self.success_procedure = False
            self.logger.log('Set tree size = {}'.format(self.input_size))
        except Exception:
            self.clear_output()
            self.error_message = 'Incorrect type of input size'
            self.success_procedure = False
            self.logger.log('{}'.format(self.error_message))
        self.validate_data_build_button()

    def get_input_size(self):
        return self.input_size

    def set_input_array(self, input_array):
        try:
            self.input_array = None
            self.input_array = [int(element) for element in input_array]
            self.clear_error_message()
            self.logger.log('Set array for tree {}'.format(self.input_array))
        except Exception:
            self.clear_output()
            self.error_message = 'Incorrect input array'
            self.success_procedure = False
            self.logger.log('{}'.format(self.error_message))
        self.validate_data_build_button()

    def get_input_array(self):
        return self.input_array

    def set_method(self, method):
        self.method = method
        self.logger.log('Set method {}'.format(self.method))

    def get_method(self):
        return self.method

    def set_left_border(self, left):
        try:
            self.left_border = None
            self.left_border = int(left)
            self.logger.log('Set left border = {}'.format(self.left_border))
        except Exception:
            self.clear_output()
            self.error_message = 'Incorrect left border'
            self.success_procedure = False
            self.logger.log('{}'.format(self.error_message))
        self.validate_data_get_button()

    def get_left_border(self):
        return self.left_border

    def set_right_border(self, right):
        try:
            self.right_border = None
            self.right_border = int(right)
            self.logger.log('Set right border = {}'.format(self.right_border))
        except Exception:
            self.clear_output()
            self.error_message = 'Incorrect right border'
            self.success_procedure = False
            self.logger.log('{}'.format(self.error_message))
        self.validate_data_get_button()

    def get_right_border(self):
        return self.right_border

    def set_update_index(self, index):
        try:
            self.update_index = None
            self.update_index = int(index)
            self.logger.log('Set update index = {}'.format(self.update_index))
        except Exception:
            self.clear_output()
            self.error_message = 'Incorrect update index'
            self.success_procedure = False
            self.logger.log('{}'.format(self.error_message))
        self.validate_data_update_button()

    def get_update_index(self):
        return self.update_index

    def set_update_value(self, new_value):
        try:
            self.update_value = None
            self.update_value = int(new_value)
            self.logger.log('Set update value = {}'.format(self.update_value))
        except Exception:
            self.clear_output()
            self.error_message = 'Incorrect update value'
            self.success_procedure = False
            self.logger.log('{}'.format(self.error_message))
        self.validate_data_update_button()

    def get_update_value(self):
        return self.update_value

    def get_calculate_result(self):
        return self.calculate_result

    def clear_output(self):
        self.calculate_result = None

    def get_error_message(self):
        return self.error_message

    def clear_error_message(self):
        self.error_message = None

    def get_success_procedure(self):
        return self.success_procedure

    def cut_array_for_given_border(self):
        if self.is_get_button_enable() == "normal":
            self.success_procedure = False
            try:
                self.calculate_result = self.segment_tree.get(self.left_border, self.right_border)
                self.success_procedure = True
                self.clear_error_message()
                self.logger.log('Cut array for given border, result: {}'.format(self.calculate_result))
            except Exception as except_build:
                self.clear_output()
                self.error_message = str(except_build)
                self.success_procedure = False
                self.logger.log('{}'.format(self.error_message))

    def calculate(self):
        if self.is_build_button_enable() == "normal":
            self.success_procedure = False
            try:
                self.segment_tree = SegmentTree(self.method)
                self.segment_tree.build(self.input_array)
                self.success_procedure = True
                self.clear_error_message()
                self.logger.log('Build segment tree')
            except Exception as except_build:
                self.clear_output()
                self.error_message = str(except_build)
                self.success_procedure = False
                self.logger.log('{}'.format(self.error_message))

    def update(self):
        if self.is_update_button_enable() == "normal":
            self.success_procedure = False
            try:
                self.segment_tree.update(self.update_index, self.update_value)
                self.success_procedure = True
                self.clear_error_message()
                self.logger.log('Element updated')
            except Exception as except_build:
                self.clear_output()
                self.error_message = str(except_build)
                self.success_procedure = False
                self.logger.log('{}'.format(self.error_message))
