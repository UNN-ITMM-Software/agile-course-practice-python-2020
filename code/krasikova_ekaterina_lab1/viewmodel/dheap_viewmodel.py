from krasikova_ekaterina_lab1.model.dheap import DHeap
from krasikova_ekaterina_lab1.logger.reallogger import RealLogger


class DHeapViewModel:
    def __init__(self, logger=RealLogger()):
        self.logger = logger
        self.is_heap_init = False
        self.set_create_btn_disabled()
        self.set_insert_btn_disabled()
        self.set_delete_btn_disabled()
        self.set_decrease_btn_disabled()
        self.logger.log('Welcome!')

    def set_create_btn_enabled(self):
        self.create_btn_state = 'normal'

    def set_create_btn_disabled(self):
        self.create_btn_state = 'disabled'

    def set_insert_btn_enabled(self):
        self.insert_btn_state = 'normal'

    def set_insert_btn_disabled(self):
        self.insert_btn_state = 'disabled'

    def set_delete_btn_enabled(self):
        self.delete_btn_state = 'normal'

    def set_delete_btn_disabled(self):
        self.delete_btn_state = 'disabled'

    def set_decrease_btn_enabled(self):
        self.decrease_btn_state = 'normal'

    def set_decrease_btn_disabled(self):
        self.decrease_btn_state = 'disabled'

    def get_create_btn_state(self):
        return self.create_btn_state

    def get_insert_btn_state(self):
        return self.insert_btn_state

    def get_delete_btn_state(self):
        return self.delete_btn_state

    def get_decrease_btn_state(self):
        return self.decrease_btn_state

    def get_current_data(self):
        return self.current_data

    def set_inserting_elem(self, elem):
        if self.is_heap_init:
            try:
                self.inserting_elem = float(elem)
                self.set_insert_btn_enabled()
            except:
                self.set_insert_btn_disabled()

    def set_deleting_elem(self, elem):
        if self.is_heap_init:
            try:
                self.deleting_elem = int(elem)
                self.set_delete_btn_enabled()
            except:
                self.set_delete_btn_disabled()

    def set_decreasing_elem(self, data):
        if self.is_heap_init:
            try:
                decrease_data = [float(elem) for elem in data.split(' ')]
                self.decrease_key = int(decrease_data[0])
                self.decrease_value = float(decrease_data[1])
                self.set_decrease_btn_enabled()
            except:
                self.set_decrease_btn_disabled()

    def set_input_data(self, param_d, input_data):
        self.is_d = False
        self.is_input_data = False
        try:
            input_data = [float(elem) for elem in input_data.split(' ')]
            self.input_data = input_data
            self.is_input_data = True
        except:
            self.set_create_btn_disabled()
        try:
            if int(param_d) >= 1:
                self.param_d = int(param_d)
                self.is_d = True
            else:
                self.set_create_btn_disabled()
        except:
                self.set_create_btn_disabled()
        if all([self.is_input_data, self.is_d]):
            self.set_create_btn_enabled()

    def create_btn_clicked(self):
        self.DHeap = DHeap(self.param_d, self.input_data)
        self.current_data = ' '.join([str(elem) for elem in self.DHeap.heap])
        self.logger.log('Entering d parameter: %s' % self.param_d)
        self.logger.log('Entering input data: %s' % self.input_data)
        self.logger.log('current data: %s' % self.current_data)
        self.is_heap_init = True

    def insert_btn_clicked(self):
        if self.is_heap_init:
            self.DHeap.insert(self.inserting_elem)
            self.logger.log('Entering element you want to insert: %s' % self.inserting_elem)
            self.current_data = ' '.join([str(elem) for elem in self.DHeap.heap])
            self.logger.log('current data after insert: %s' % self.current_data)

    def delete_btn_clicked(self):
        self.DHeap.delete(self.deleting_elem)
        self.logger.log('Entering element you want to delete: %s' % self.deleting_elem)
        self.current_data = ' '.join([str(elem) for elem in self.DHeap.heap])
        self.logger.log('current data after delete: %s' % self.current_data)

    def decrease_btn_clicked(self):
        self.DHeap.decrease_weight(self.decrease_key, self.decrease_value)
        self.logger.log('Entering element you want to decrease: %s' % self.decrease_value)
        self.current_data = ' '.join([str(elem) for elem in self.DHeap.heap])
        self.logger.log('current data after decrease: %s' % self.current_data)
