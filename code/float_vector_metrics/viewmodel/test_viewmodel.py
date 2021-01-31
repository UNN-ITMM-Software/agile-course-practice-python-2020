import unittest

from float_vector_metrics.viewmodel.viewmodel import VectorMetricsViewModel

from float_vector_metrics.logger.fakelogger import FakeLogger

from float_vector_metrics.logger.reallogger import RealLogger


class TestVectorMetricsViewModel(unittest.TestCase):
    def setUp(self):
        self.viewmodel = VectorMetricsViewModel(FakeLogger())

    def test_button_disabled_by_default(self):
        self.assertEqual('disabled', self.viewmodel.get_button_state())

    def test_button_enabled_when_metric_set(self):
        self.viewmodel.set_metric('L1')
        self.assertEqual('active', self.viewmodel.get_button_state())

    def test_button_disabled_when_x_value_erased(self):
        self.viewmodel.set_x('')
        self.assertEqual('disabled', self.viewmodel.get_button_state())

    def test_button_disabled_when_incorrect_x_value(self):
        self.viewmodel.set_x('!')
        self.assertEqual('disabled', self.viewmodel.get_button_state())

    def test_set_button_state_changes_state(self):
        self.viewmodel.set_button_state('active')
        self.assertEqual('active', self.viewmodel.get_button_state())

    def test_error_message_on_incorrect_value(self):
        self.viewmodel.set_y('!')
        self.assertEqual('Error: Incorrect expression, only list of float or int values supported',
                         self.viewmodel.get_error_message())

    def test_error_message_on_incorrect_type(self):
        self.viewmodel.set_y('3')
        self.assertEqual('Error: Only list notations supported',
                         self.viewmodel.get_error_message())

    def test_button_enabled_when_correct_x_value(self):
        self.viewmodel.set_x('[1, 2, 3]')
        self.assertEqual('active', self.viewmodel.get_button_state())

    def test_error_message_is_empty_on_correct_value(self):
        self.viewmodel.set_y('[1, 2, 3]')
        self.assertEqual('', self.viewmodel.get_error_message())

    def test_can_change_x_value(self):
        self.viewmodel.set_x('[3, 2, 1]')
        self.assertEqual('[3, 2, 1]', self.viewmodel.get_x())

    def test_can_change_y_value(self):
        self.viewmodel.set_y('[4, 5, 1]')
        self.assertEqual('[4, 5, 1]', self.viewmodel.get_y())

    def test_error_message_is_shown_when_length_unequal(self):
        self.viewmodel.set_x('[1, 2, 3]')
        self.viewmodel.set_y('[1, 2, 3, 4]')
        self.viewmodel.set_metric('L1')
        self.viewmodel.compute()
        self.assertEqual('Error: Vectors of different lengths obtained. Distance can only be '
                         'calculated between vectors of equal length.',
                         self.viewmodel.get_error_message())

    def test_can_compute_metric(self):
        self.viewmodel.set_x('[1.2, 1.5, 1.8]')
        self.viewmodel.set_y('[2.2, 2.5, 2.8]')
        self.viewmodel.set_metric('L1')
        self.viewmodel.compute()
        self.assertEqual('Result: 3.0', self.viewmodel.get_result())


class TestViewModelFakeLogging(unittest.TestCase):
    def setUp(self):
        self.view_model = VectorMetricsViewModel(FakeLogger())

    def test_logging_init(self):
        self.assertEqual('Welcome to The Float Vector Metrics Calculator!',
                         self.view_model.logger.get_last_message())

    def test_logging_changing_x(self):
        self.view_model.set_x('[0, 1, 2]')
        self.assertEqual('Setting x vector to [0, 1, 2]', self.view_model.logger.get_last_message())

    def test_logging_changing_y(self):
        self.view_model.set_y('[0, 1, 2]')
        self.assertEqual('Setting y vector to [0, 1, 2]', self.view_model.logger.get_last_message())

    def test_logging_changing_metric(self):
        self.view_model.set_metric('L1')
        self.assertEqual('Setting metric to L1', self.view_model.logger.get_last_message())

    def test_logging_changing_uncorrect_x(self):
        self.view_model.set_x('{0, 1, 2}')
        self.assertEqual('Error: Only list notations supported', self.view_model.logger.get_last_message())

    def test_logging_changing_uncorrect_y(self):
        self.view_model.set_y('[2, x, 1]')
        self.assertEqual('Error: Incorrect expression, only list of float or int values supported',
                         self.view_model.logger.get_last_message())

    def test_logging_uncorrect_compute(self):
        expected_messages = ['Button clicked',
                             'Error: Vectors of different lengths obtained. Distance can only be '
                             'calculated between vectors of equal length.']
        self.view_model.set_x('[1, 0, 2]')
        self.view_model.set_y('[1, 1, 1, 3]')
        self.view_model.set_metric('L1')
        self.view_model.compute()
        self.assertEqual(expected_messages, self.view_model.logger.get_log_messages()[-2:])

    def test_logging_performing_operation(self):
        expected_messages = ['Button clicked', 'Result: 2']

        self.view_model.set_x('[1, 0, 2]')
        self.view_model.set_y('[1, 1, 1]')
        self.view_model.set_metric('L1')
        self.view_model.compute()

        self.assertEqual(expected_messages, self.view_model.logger.get_log_messages()[-2:])


class TestViewModelRealLogging(TestViewModelFakeLogging):
    def setUp(self):
        self.view_model = VectorMetricsViewModel(RealLogger())
