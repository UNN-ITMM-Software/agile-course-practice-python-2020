import unittest

from queue.viewmodel.viewmodel import QueueViewModel


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
        self.view_model.set_input_info('replace')
        self.view_model.arrive_btn_clicked()
        self.view_model.leave_btn_clicked()
        self.assertEqual('', self.view_model.get_arrived_info())

    def test_are_there_no_arrived_info(self):
        arrived_info = self.view_model.get_arrived_info()
        self.assertFalse(self.view_model.set_arrived_info(arrived_info))

    def test_are_there_any_arrived_info(self):
        self.view_model.set_input_info('power')
        self.view_model.arrive_btn_clicked()
        self.view_model.get_arrived_info()
        arrived_info = self.view_model.get_arrived_info()
        self.view_model.set_arrived_info(arrived_info)
        self.assertEqual('normal', self.view_model.get_arrive_btn_state())
        self.assertEqual('normal', self.view_model.get_leave_btn_state())
