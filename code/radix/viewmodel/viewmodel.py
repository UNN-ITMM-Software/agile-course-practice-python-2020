from radix.logger.real_logger import RealLogger
from radix.model.radix import Sorting


def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


class SortingViewModel:
    def __init__(self, logger=RealLogger()):
        self.logger = logger
        self.input_array = ''
        self.sorted_array = ''
        self.sort_btn_click = ''
        self.log_message = ''
#        self.sort_btn_state = 'normal'

    def get_input_array(self):
        return self.input_array

    def get_sorted_array(self):
        return self.sorted_array

    def set_input_array(self, input_array):
        self.input_array = input_array.strip()
        self.logger.log('Input array: %s' % self.input_array)

    def set_sort_btn_clicked_ok(self):
        self.sort_btn_clicked = 'OK'
        self.logger.log('Success')

    def set_sort_btn_clicked_error(self):
        self.sort_btn_clicked = 'Error'
        self.logger.log('Failed')

    def get_sort_btn_clicked_result(self):
        return self.sort_btn_clicked

#     def set_sort_btn_disabled(self):
#        self.sort_btn_state = 'normal'

    def get_sort_btn_state(self):
        return self.sort_btn_state

    def sort_btn_clicked(self):
        try:
            self.logger.log('Start reading the array')
            array = []
            for i in self.input_array.split(' '):
                if is_int(i):
                    array.append(int(i))
                elif is_float(i):
                    array.append(float(i))
                else:
                    array.append(str(i))
            self.logger.log('Start sorting')
            radix = Sorting(array)
            radix.radix_sort()
            self.logger.log('Sorting is OK')
            self.sorted_array = radix.result_str()
            self.logger.log('Result array: %s' % self.sorted_array)
            self.set_sort_btn_clicked_ok()
        except:
            self.set_sort_btn_clicked_error()
