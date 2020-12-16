from ShutinaSvetlana.model.batcher import Sorting


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
    def __init__(self):
        self.input_array = ''
        self.sorted_array = ''
        sort_btn_clicked = ''

    def get_input_array(self):
        return self.input_array

    def get_sorted_array(self):
        return self.sorted_array

    def set_input_array(self, input_array):
            self.input_array = input_array

    def set_sort_btn_clicked_ok(self):
        self.sort_btn_clicked = 'OK'

    def set_sort_btn_clicked_error(self):
        self.sort_btn_clicked = 'Error'

    def get_sort_btn_clicked_result(self):
        return self.sort_btn_clicked

    def sort_btn_click(self):
        try:
            array = []
            for i in self.input_array.split(' '):
                if is_int(i):
                    array.append(int(i))
                elif is_float(i):
                    array.append(float(i))
                else:
                    array.append(str(i))
            batcher = Sorting(array)
            batcher.batcher_sort()
            self.sorted_array = batcher.result_str()
            self.set_sort_btn_clicked_ok()
        except:
            self.set_sort_btn_clicked_error()
