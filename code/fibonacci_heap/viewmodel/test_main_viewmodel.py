import unittest

from fibonacci_heap.logger.fakelogger import FakeLogger
from fibonacci_heap.logger.reallogger import RealLogger
from fibonacci_heap.viewmodel.main_viewmodel import HeapViewModel, State, NodeOperations


class TestFibonacciHeapViewModel(unittest.TestCase):

    def setUp(self):
        self.view_model = HeapViewModel()

    def test_default_button_state(self):
        self.assertEqual(State.DISABLED.value, self.view_model.get_main_button_state())

    # Field states
    def test_insert_state_enabled(self):
        self.view_model.set_operation(NodeOperations.INSERT)
        self.assertEqual(State.ENABLED.value, self.view_model.get_value_textbox_state())

    def test_delete_state_disabled(self):
        self.view_model.set_operation(NodeOperations.DELETE)
        self.assertEqual(State.DISABLED.value, self.view_model.get_value_textbox_state())

    def test_insert_filled_enabled(self):
        self.view_model.set_operation(NodeOperations.INSERT)
        self.view_model.set_key('0')
        self.view_model.set_value('value')
        self.assertEqual(State.ENABLED.value, self.view_model.get_main_button_state())

    def test_delete_filled_enabled(self):
        self.view_model.set_operation(NodeOperations.INSERT)
        self.view_model.set_key('0')
        self.view_model.set_value('value')
        self.view_model.set_operation(NodeOperations.DELETE)
        self.assertEqual(State.ENABLED.value, self.view_model.get_main_button_state())

    def test_insert_one_key_field_disabled(self):
        self.view_model.set_operation(NodeOperations.INSERT)
        self.view_model.set_key('0')
        self.view_model.set_value('')
        self.assertEqual(State.DISABLED.value, self.view_model.get_main_button_state())

    # Messages
    def test_msg_box_limit(self):
        for i in range(self.view_model.MAX_MESSAGE_NUMBER):
            self.view_model.update_messages(str(i))
        self.view_model.update_messages('last message')
        expected_text = '\n'.join(
                [str(i) for i in range(self.view_model.MAX_MESSAGE_NUMBER-1, 0, -1)]
        )
        expected_text = 'last message\n' + expected_text
        self.assertEqual(expected_text, self.view_model.get_message_text())

    # INSERT
    def test_insert_info_msg(self):
        self.view_model.set_operation(NodeOperations.INSERT)
        self.view_model.set_key('0')
        self.view_model.set_value('value')
        self.view_model.click_run_button()
        expected_msg = HeapViewModel.INFO_MSG['insert'] % (0, 'value')
        self.assertNotEqual(-1, self.view_model.get_message_text().find(expected_msg))

    def test_insert_invalid_error_msg(self):
        self.view_model.heap.insert('not valid key', 'value')
        self.view_model.set_operation(NodeOperations.INSERT)
        self.view_model.set_key('not valid key')
        self.view_model.set_value('value')
        self.view_model.click_run_button()
        expected_msg = HeapViewModel.INFO_MSG['key_invalid'] % 'not valid key'
        self.assertNotEqual(-1, self.view_model.get_message_text().find(expected_msg))

    def test_insert_mess_error_msg(self):
        self.view_model.heap.insert(0, 'value')
        self.view_model.set_key('0')
        self.view_model.set_operation(NodeOperations.INSERT)
        self.view_model.click_run_button()
        expected_msg = HeapViewModel.INFO_MSG['key_mess'] % 0
        self.assertEqual(-1, self.view_model.get_message_text().find(expected_msg))

    # DELETE
    def test_delete_info_msg(self):
        self.view_model.set_operation(NodeOperations.DELETE)
        self.view_model.heap.insert(0, 'value')
        self.view_model.set_key('0')
        self.view_model.click_run_button()
        expected_msg = HeapViewModel.INFO_MSG['delete'] % 0
        self.assertNotEqual(-1, self.view_model.get_message_text().find(expected_msg))

    def test_delete_invalid_error_msg(self):
        self.view_model.set_operation(NodeOperations.DELETE)
        self.view_model.set_key('1')
        self.view_model.click_run_button()
        expected_msg = HeapViewModel.INFO_MSG['key_invalid'] % 1
        self.assertNotEqual(-1, self.view_model.get_message_text().find(expected_msg))

    # FIND MIN
    def test_find_min_info_msg(self):
        self.view_model.set_operation(NodeOperations.FIND_MIN)

        self.view_model.heap.insert(0, 'value')
        min_node = self.view_model.heap.find_min()
        key, val = min_node.key, min_node.val

        self.view_model.click_run_button()
        expected_msg = HeapViewModel.INFO_MSG['find'] % (key, val)
        self.assertNotEqual(-1, self.view_model.get_message_text().find(expected_msg))


class TestViewModelFakeLogging(unittest.TestCase):
    def setUp(self):
        self.view_model = HeapViewModel(FakeLogger())

    def test_logging_init(self):
        self.assertEqual('Welcome!', self.view_model.logger.get_last_message())

    def test_logging_set_value(self):
        self.view_model.set_value('5')
        self.assertEqual('Set value is 5', self.view_model.logger.get_last_message())

    def test_logging_set_key(self):
        self.view_model.set_key('5')
        self.assertEqual('Set key is 5', self.view_model.logger.get_last_message())

    def test_logging_performing_operation(self):
        expected_messages = [
            'Run button clicked',
            'Selected operation is {}'.format(NodeOperations.INSERT),
            'Inserted node: key - {}, value - {}'.format(5, 4)]

        self.view_model.set_key('5')
        self.view_model.set_value('4')
        self.view_model.set_operation(NodeOperations.INSERT)
        self.view_model.click_run_button()

        self.assertEqual(expected_messages, self.view_model.logger.get_log_messages()[-3:])


class TestViewModelRealLogging(TestViewModelFakeLogging):
    def setUp(self):
        self.view_model = HeapViewModel(RealLogger())
