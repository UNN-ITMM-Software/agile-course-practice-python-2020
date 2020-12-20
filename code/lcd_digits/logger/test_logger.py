
import unittest

from lcd_digits.logger.fakelogger import FakeLogger
from lcd_digits.logger.log import Log
from lcd_digits.logger.log import Log_types


class TestLoggerAndLog(unittest.TestCase):
    def setUp(self):
        self.logger = FakeLogger()

    def test_can_create_log(self):
        self.assertTrue(isinstance(Log('Test', Log_types.Info), Log))

    def test_get_log_message(self):
        log = Log('Test', Log_types.Info)
        self.assertTrue('Test', log.get_message())

    def test_get_log_type(self):
        log = Log('Test', Log_types.Error)
        self.assertTrue(Log_types.Error, log.get_type())

    def test_can_create_logger(self):
        self.assertTrue(isinstance(self.logger, FakeLogger))

    def test_by_default_log_is_empty(self):
        log = self.logger.get_log_messages()
        self.assertEqual(log, [])

    def test_after_logging_message_in_log(self):
        self.logger.add_log('Test', Log_types.Info)
        self.assertEqual(['Test'], self.logger.get_log_messages())

    def test_can_log_several_messages(self):
        self.logger.add_log('Test', Log_types.Info)
        self.logger.add_log('Another one', Log_types.Info)
        self.assertEqual(['Test', 'Another one'], self.logger.get_log_messages())

    def test_can_get_last_log(self):
        self.logger.add_log('Test', Log_types.Info)
        self.logger.add_log('Another one', Log_types.Info)
        self.assertEqual('Another one', self.logger.get_last_log_message())

    def test_not_can_add_other_log(self):
        with self.assertRaises(ValueError):
            self.logger.add_log('Test', Log_types.Unknown)
