import unittest

from deposit_calc.logger.fakelogger import FakeLogger as Logger


class TestLogger(unittest.TestCase):
    def setUp(self):
        self.logger = Logger()

    def test_can_create_logger(self):
        self.assertTrue(isinstance(self.logger, Logger))

    def test_by_default_log_is_empty(self):
        log = self.logger.get_log_messages()

        self.assertEqual(log, [])

    def test_after_logging_message_in_log(self):
        self.logger.log('Test')

        self.assertEqual(['Test'], self.logger.get_log_messages())

    def test_can_log_several_messages(self):
        self.logger.log('Test')
        self.logger.log('Another one')

        self.assertEqual(['Test', 'Another one'], self.logger.get_log_messages())

    def test_can_get_last_log(self):
        self.logger.log('Test')
        self.logger.log('Another one')

        self.assertEqual('Another one', self.logger.get_last_message())
