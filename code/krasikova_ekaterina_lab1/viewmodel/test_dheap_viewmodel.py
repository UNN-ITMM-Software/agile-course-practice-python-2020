import unittest

from krasikova_ekaterina_lab1.viewmodel.dheap_viewmodel import DHeapViewModel
from krasikova_ekaterina_lab1.logger.fakelogger import FakeLogger
from krasikova_ekaterina_lab1.logger.reallogger import RealLogger


class TestDHeapViewModel(unittest.TestCase):

    def setUp(self):
        self.view_model = DHeapViewModel()

    def test_by_default_buttons_disabled(self):
        self.assertEqual('disabled', self.view_model.get_create_btn_state())
        self.assertEqual('disabled', self.view_model.get_insert_btn_state())
        self.assertEqual('disabled', self.view_model.get_delete_btn_state())
        self.assertEqual('disabled', self.view_model.get_decrease_btn_state())

    def test_when_entered_d_input_then_create_button_enabled(self):
        self.view_model.set_input_data('2', '1 2 3')
        self.assertNotEqual('disabled', self.view_model.get_create_btn_state())

    def test_can_create_heap(self):
        self.view_model.set_input_data('2', '2 3 4 1')
        self.view_model.create_btn_clicked()
        self.assertEqual(self.view_model.get_current_data(), '1.0 2.0 4.0 3.0')

    def test_cant_create_heap_with_wrong_data1(self):
        self.view_model.set_input_data('2-', '2 3 4 1')
        self.assertEqual('disabled', self.view_model.get_create_btn_state())

    def test_cant_insert_in_heap_with_wrong_data(self):
        self.view_model.set_input_data('2', '2 3 4 1')
        self.view_model.create_btn_clicked()
        self.view_model.set_inserting_elem('~2')
        self.assertEqual('disabled', self.view_model.get_insert_btn_state())

    def test_cant_delete_from_heap_with_wrong_data(self):
        self.view_model.set_input_data('2', '2 3 4 1')
        self.view_model.create_btn_clicked()
        self.view_model.set_deleting_elem('~2')
        self.assertEqual('disabled', self.view_model.get_delete_btn_state())

    def test_cant_create_heap_with_wrong_data2(self):
        self.view_model.set_input_data('2', '~2 3 4 1')
        self.assertEqual('disabled', self.view_model.get_create_btn_state())

    def test_cant_create_heap_with_wrong_data3(self):
        self.view_model.set_input_data('0', '2 3 4 1')
        self.assertEqual('disabled', self.view_model.get_create_btn_state())

    def test_cant_decrease_key_with_wrong_data(self):
        self.view_model.set_input_data('2', '2 3 4 1')
        self.view_model.create_btn_clicked()
        self.view_model.set_decreasing_elem('0 _2')
        self.assertEqual('disabled', self.view_model.get_decrease_btn_state())

    def test_can_insert_in_heap(self):
        self.view_model.set_input_data('2', '2 3 4 1')
        self.view_model.create_btn_clicked()
        self.view_model.set_inserting_elem('2')
        self.view_model.insert_btn_clicked()
        self.assertEqual(self.view_model.get_current_data(), '1.0 2.0 4.0 3.0 2.0')

    def test_can_delete_from_heap(self):
        self.view_model.set_input_data('2', '2 3 4 1')
        self.view_model.create_btn_clicked()
        self.view_model.set_deleting_elem('1')
        self.view_model.delete_btn_clicked()
        self.assertEqual(self.view_model.get_current_data(), '1.0 3.0 4.0')

    def test_can_decrease_key_in_heap(self):
        self.view_model.set_input_data('2', '2 3 4 1')
        self.view_model.create_btn_clicked()
        self.view_model.set_decreasing_elem('1 2')
        self.view_model.decrease_btn_clicked()
        self.assertEqual(self.view_model.get_current_data(), '0.0 1.0 4.0 3.0')

    def test_when_entered_insert_without_heap_then_insert_button_disabled(self):
        self.view_model.set_inserting_elem('2')
        self.assertEqual('disabled', self.view_model.get_insert_btn_state())

    def test_when_entered_delete_without_heap_then_delete_button_disabled(self):
        self.view_model.set_deleting_elem('2')
        self.assertEqual('disabled', self.view_model.get_delete_btn_state())

    def test_when_entered_decrease_without_heap_then_decrease_button_disabled(self):
        self.view_model.set_decreasing_elem('2 3')
        self.assertEqual('disabled', self.view_model.get_decrease_btn_state())


class TestViewModelFakeLogging(unittest.TestCase):
    def setUp(self):
        self.view_model = DHeapViewModel(FakeLogger())

    def test_logging_init(self):
        self.assertEqual('Welcome!', self.view_model.logger.get_last_message())

    def test_logging_create_btn_clicked(self):
        self.view_model.set_input_data('2', '1 2 3')
        self.view_model.create_btn_clicked()
        self.assertEqual('current data: 1.0 2.0 3.0', self.view_model.logger.get_last_message())

    def test_logging_insert_btn_clicked(self):
        self.view_model.set_input_data('2', '1 2 3')
        self.view_model.create_btn_clicked()
        self.view_model.set_inserting_elem('5 ')
        self.view_model.insert_btn_clicked()
        self.assertEqual('current data after insert: 1.0 2.0 3.0 5.0',
                         self.view_model.logger.get_last_message())

    def test_logging_delete_btn_clicked(self):
        self.view_model.set_input_data('2', '1 2 3')
        self.view_model.create_btn_clicked()
        self.view_model.set_deleting_elem('1')
        self.view_model.delete_btn_clicked()
        self.assertEqual('current data after delete: 1.0 3.0', self.view_model.logger.get_last_message())

    def test_logging_decrease_btn_clicked(self):
        self.view_model.set_input_data('2', '1 2 3')
        self.view_model.create_btn_clicked()
        self.view_model.set_decreasing_elem('1 2')
        self.view_model.decrease_btn_clicked()
        self.assertEqual('current data after decrease: 0.0 1.0 3.0',
                         self.view_model.logger.get_last_message())


class TestViewModelRealLogging(TestViewModelFakeLogging):
    def setUp(self):
        self.view_model = DHeapViewModel(RealLogger())
