import unittest

from modified_stack.logger.fakelogger import FakeLogger
from modified_stack.logger.reallogger import RealLogger
from modified_stack.viewmodel.modified_stack_viewmodel import ModifiedStackViewModel


class TestModifiedStackViewModel(unittest.TestCase):

    def test_default_stack_is_empty(self):
        model = ModifiedStackViewModel()

        self.assertEqual(0, model.size())

    def test_pop_from_empty_stack(self):
        model = ModifiedStackViewModel()

        model.set_pop_size(1)
        model.pop()

        self.assertEqual('count should be positive', model.get_error_message())

    def test_get_min_from_empty_stack(self):
        model = ModifiedStackViewModel()

        model.get_min()

        self.assertEqual('Stack is empty', model.get_error_message())

    def test_look_top_from_empty_stack(self):
        model = ModifiedStackViewModel()

        model.get_top()

        self.assertEqual('Stack is empty', model.get_error_message())

    def test_correct_min_value(self):
        model = ModifiedStackViewModel()

        model.set_push_state('N')
        model.set_input_array([5, 1, 6, 7])
        model.push()
        model.get_min()

        self.assertEqual(1, model.min)

    def test_correct_top_value(self):
        model = ModifiedStackViewModel()

        model.set_push_state('One')
        model.set_pushed_element(6)
        model.push()
        model.get_top()

        self.assertEqual(6, model.top)

    def test_when_pushed_value_non_int(self):
        model = ModifiedStackViewModel()

        model.set_push_state('One')
        model.set_pushed_element('PUSH ME')
        model.push()

        self.assertEqual('Input contains non int value', model.get_error_message())

    def test_when_pop_size_non_int(self):
        model = ModifiedStackViewModel()

        model.set_pop_size('AND THEN JUST POP ME')
        model.pop()

        self.assertEqual('Input contains non int value', model.get_error_message())


class TestViewModelFakeLogging(unittest.TestCase):
    def setUp(self):
        self.view_model = ModifiedStackViewModel(FakeLogger())

    def test_logging_init(self):
        self.assertEqual('Stack object was successfully created', self.view_model.logger.get_last_message())

    def test_logging_set_one_input_element(self):
        self.view_model.set_pushed_element(5)
        self.assertEqual("Setting pushed element to: 5", self.view_model.logger.get_last_message())

    def test_logging_set_array_input(self):
        self.view_model.set_input_array([1, 2, 3])
        self.assertEqual("Setting input array to: [1, 2, 3]", self.view_model.logger.get_last_message())

    def test_logging_set_push_state(self):
        self.view_model.set_push_state("N")
        self.assertEqual("Setting push state to: N", self.view_model.logger.get_last_message())

    def test_logging_clear_error_message(self):
        self.view_model.clear_error_message()
        self.assertEqual("Error message was successfully cleared", self.view_model.logger.get_last_message())

    def test_logging_push_btn_clicked(self):
        self.view_model.set_push_state('One')
        self.view_model.set_pushed_element(5)
        self.view_model.push()
        self.assertEqual("Push button was clicked",
                         self.view_model.logger.get_log_messages()[-3])

    def test_logging_push_one_element(self):
        self.view_model.set_push_state('One')
        self.view_model.set_pushed_element(5)
        self.view_model.push()
        self.assertEqual("Operation push successfully completed with single element. Push: 5",
                         self.view_model.logger.get_last_message())

    def test_logging_push_array(self):
        self.view_model.set_push_state('N')
        self.view_model.set_input_array([1, 2, 3, 4, 5])
        self.view_model.push()
        self.assertEqual("Operation push successfully completed with array. Push: [1, 2, 3, 4, 5]",
                         self.view_model.logger.get_last_message())

    def test_logging_push_wrong_element(self):
        self.view_model.set_push_state('N')
        self.view_model.set_input_array('abc')
        self.view_model.push()
        self.assertEqual("Push error: Input contains non int value",
                         self.view_model.logger.get_last_message())

    def test_logging_full_log(self):
        expected_logs = ['Stack object was successfully created',
                         'Setting push state to: One',
                         'Setting pushed element to: 5',
                         'Push button was clicked',
                         'Error message was successfully cleared',
                         'Operation push successfully completed with single element. Push: 5']
        self.view_model.set_push_state('One')
        self.view_model.set_pushed_element(5)
        self.view_model.push()
        self.assertEqual(expected_logs,
                         self.view_model.logger.get_log_messages())

    def test_logging_set_pop_size(self):
        self.view_model.set_pop_size(1)
        self.assertEqual("Setting pop size to: 1", self.view_model.logger.get_last_message())

    def test_logging_pop_btn_clicked(self):
        self.view_model.set_pop_size(1)
        self.view_model.pop()
        self.assertEqual("Pop button was clicked",
                         self.view_model.logger.get_log_messages()[2])

    def test_logging_pop_success(self):
        self.view_model.set_push_state('N')
        self.view_model.set_input_array([1, 2, 3, 4, 5])
        self.view_model.push()
        self.view_model.set_pop_size(1)
        self.view_model.pop()
        self.assertEqual("Operation pop successfully completed. Pop: 1",
                         self.view_model.logger.get_last_message())

    def test_logging_pop_exception(self):
        self.view_model.set_pop_size('a')
        self.view_model.pop()
        self.assertEqual("Pop error: Input contains non int value",
                         self.view_model.logger.get_last_message())

    def test_logging_get_top_btn_log(self):
        self.view_model.get_top()
        self.assertEqual("Getting top button was clicked",
                         self.view_model.logger.get_log_messages()[1])

    def test_logging_get_top_empty_stack(self):
        self.view_model.get_top()
        self.assertEqual("Result from getting top element: Stack is empty",
                         self.view_model.logger.get_last_message())

    def test_logging_get_top_happy_path(self):
        self.view_model.set_push_state('N')
        self.view_model.set_input_array([1, 2, 3, 4, 5])
        self.view_model.push()
        self.view_model.get_top()
        self.assertEqual("Result from getting top element: 5",
                         self.view_model.logger.get_last_message())

    def test_logging_get_min_btn_log(self):
        self.view_model.get_min()
        self.assertEqual("Getting min button was clicked",
                         self.view_model.logger.get_log_messages()[1])

    def test_logging_get_min_empty_stack(self):
        self.view_model.get_min()
        self.assertEqual("Result from getting min element: Stack is empty",
                         self.view_model.logger.get_last_message())

    def test_logging_get_min_happy_path(self):
        self.view_model.set_push_state('N')
        self.view_model.set_input_array([1, 2, 3, 4, 5])
        self.view_model.push()
        self.view_model.get_min()
        self.assertEqual("Result from getting min element: 1",
                         self.view_model.logger.get_last_message())


class TestViewModelRealLogging(TestViewModelFakeLogging):
    def setUp(self):
        self.view_model = ModifiedStackViewModel(RealLogger())
