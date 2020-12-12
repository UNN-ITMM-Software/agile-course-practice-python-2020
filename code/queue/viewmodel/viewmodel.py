from queue.model.model import Queue


class QueueViewModel:
    def __init__(self):
        self.queue = Queue()
        self.input_info = ''
        self.arrived_info = ''
        self.set_arrive_btn_disabled()
        self.set_leave_btn_disabled()

    def set_arrive_btn_enabled(self):
        self.arrive_btn_state = 'normal'

    def set_arrive_btn_disabled(self):
        self.arrive_btn_state = 'disabled'

    def get_arrive_btn_state(self):
        return self.arrive_btn_state

    def set_leave_btn_enabled(self):
        self.leave_btn_state = 'normal'

    def set_leave_btn_disabled(self):
        self.leave_btn_state = 'disabled'

    def get_leave_btn_state(self):
        return self.leave_btn_state

    def get_input_info(self):
        return self.input_info

    def get_arrived_info(self):
        return self.arrived_info

    def set_input_info(self, input_info):
        try:
            self.input_info = input_info
            self.set_arrive_btn_enabled()
            self.set_leave_btn_enabled()
        except:
            self.set_arrive_btn_disabled()
            self.set_leave_btn_disabled()

    def arrive_btn_clicked(self):
        self.queue.addToQueue(self.input_info)
        self.arrived_info = self.queue.get_elements()

    def leave_btn_clicked(self):
        self.queue.removefromQueue()
        self.arrived_info = self.queue.get_elements()
