from radix_sort.model.radix_sort import RadixSort


def convert_list_into_string(array: list) -> str:
    return str(", ".join([str(i) for i in array]))


class RadixSortViewModel:
    def __init__(self):
        self.input_data = ''
        self.output_data = ''
        self.sort_button_state = 'disabled'

    def start_sort(self):
        try:
            if ',' in self.input_data:
                start_array = [int(s) for s in self.input_data.split(',')]
            else:
                start_array = [int(s) for s in self.input_data.split()]

            result_array = RadixSort(start_array).sort()
            self.output_data = convert_list_into_string(result_array)
        except ValueError:
            self.output_data = "Incorrect input!"

    def set_input_data(self, data: str):
        if data:
            self.sort_button_state = 'active'
        else:
            self.sort_button_state = 'disabled'

        self.input_data = data

    def get_input_data(self) -> str:
        return self.input_data

    def get_output_data(self) -> str:
        return self.output_data

    def get_sort_button_state(self):
        return self.sort_button_state
