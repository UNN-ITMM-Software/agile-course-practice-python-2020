from sorting.model.sorting import Sorting
from sorting.logger.reallogger import RealLogger


class SortingViewModel:
    def __init__(self, logger=RealLogger()):
        self.logger = logger
        self.input_array = ''
        self.sorted_array = ''
        self.set_sort_btn_disabled()
        self.logger.log('Welcome!')

    def set_sort_btn_enabled(self):
        self.sort_btn_state = 'normal'

    def set_sort_btn_disabled(self):
        self.sort_btn_state = 'disabled'

    def get_sort_btn_state(self):
        return self.sort_btn_state

    def get_input_array(self):
        return self.input_array

    def get_sorted_array(self):
        return self.sorted_array

    def set_input_array(self, input_array):
        try:
            [float(i) for i in input_array.split(' ')]
            self.input_array = input_array
            self.logger.log('Entering input array: %s' % self.input_array)
            self.set_sort_btn_enabled()
        except:
            self.set_sort_btn_disabled()

    def sort_btn_clicked(self):
        self.logger.log('Button clicked')
        self.sorted_array = ' '.join(map(str, Sorting([
            float(i) for i in self.input_array.split(' ')]).insertion_sort()))
        self.logger.log('Sorted array: %s' % self.sorted_array)
