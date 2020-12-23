from radix_sort.model.radix_sort import RadixSort
from radix_sort.infrastructure.real_logger import RealLogger


def convert_list_into_string(array: list) -> str:
    return str(", ".join([str(i) for i in array]))


class RadixSortViewModel:
    def __init__(self, logger=RealLogger()):
        self.input_data = ''
        self.output_data = ''
        self.sort_button_state = 'disabled'
        self.logger = logger
        self.logger.log('Start Logging')

    def start_sort(self):
        self.logger.log('Start Sorting: ' + self.input_data)
        try:
            if ',' in self.input_data:
                start_array = [int(s) for s in self.input_data.split(',')]
            else:
                start_array = [int(s) for s in self.input_data.split()]

            result_array = RadixSort(start_array).sort()
            result = convert_list_into_string(result_array)
            self.output_data = result
            self.logger.log('Finish Sorting: ' + result)
        except ValueError:
            self.logger.log('Incorrect input: ' + self.input_data)
            self.output_data = "Incorrect input!"

    def set_input_data(self, data: str):
        if data:
            self.sort_button_state = 'active'
        else:
            self.sort_button_state = 'disabled'

        self.input_data = data

    def get_input_data(self) -> str:
        self.logger.log('Getting input: ' + self.input_data)
        return self.input_data

    def get_output_data(self) -> str:
        return self.output_data

    def get_sort_button_state(self):
        return self.sort_button_state
