import unittest

from viewmodel import QueueViewModel
from model import Queue


class TestQueueViewModel(unittest.TestCase):
    def setUp(self):
        self.view_model = QueueViewModel()

    def test_by_default_button_disabled(self):
        self.assertEqual('disabled', self.view_model.get_arrive_btn_state())
        self.assertEqual('disabled', self.view_model.get_leave_btn_state())

    def test_when_added_input_info_button_enabled(self):
        self.view_model.set_input_info('word')
        self.assertNotEqual('disabled', self.view_model.get_arrive_btn_state())
        self.assertNotEqual('disabled', self.view_model.get_leave_btn_state())

    def test_can_retrieve_input_info_text(self):
        self.view_model.set_input_info('qwerty')
        input_info = self.view_model.get_input_info()
        self.assertEqual('qwerty', input_info)

    def test_work_correctly_with_arrived_info(self):
        self.view_model.set_input_info('power')
        self.view_model.arrive_btn_clicked()
        self.assertEqual('power', self.view_model.get_arrived_info())

    def test_work_correctly_with_left_info(self):
        queue = Queue()
        queue.addToQueue(1)
        queue.addToQueue(2)
        queue.addToQueue(3)
        queue.removefromQueue()
        self.assertEqual('3 2', queue.get_elements())

if __name__ == '__main__':
    unittest.main()