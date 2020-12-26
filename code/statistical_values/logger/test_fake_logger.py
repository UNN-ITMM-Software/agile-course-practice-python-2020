import unittest

from statistical_values.logger.fakelogger import FakeLogger


class TestLogger(unittest.TestCase):
    def setUp(self):
        self.logger = FakeLogger()

    def test_can_create_logger(self):
        self.assertTrue(isinstance(self.logger, FakeLogger))

    def test_by_default_log_is_empty_list(self):
        default_log_message = self.logger.get_log_messages()

        self.assertEqual(default_log_message, [])
        self.assertTrue(isinstance(default_log_message, list))

    def test_correct_logging_message(self):
        self.logger.log('Log info')

        self.assertEqual(['Log info'], self.logger.get_log_messages())

    def test_can_logging_several_messages(self):
        self.logger.log('Log info 0')
        self.logger.log('Log info 1')

        self.assertEqual(['Log info 0', 'Log info 1'], self.logger.get_log_messages())

    def test_can_get_last_log(self):
        self.logger.log('Log info 0')
        self.logger.log('Log info 1')

        self.assertEqual('Log info 1', self.logger.get_last_message())
