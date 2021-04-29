import unittest

from radix.logger.fake_logger import FakeLogger


class TestRadixFakeLogger(unittest.TestCase):
    def setUp(self):
        self.logger = FakeLogger()

    def test_can_create_logger(self):
        self.assertTrue(isinstance(self.logger, FakeLogger))

    def test_default_log_is_empty(self):
        log = self.logger.get_logs()
        self.assertEqual(log, [])

    def test_added_message_in_log(self):
        self.logger.log('Hi there')
        self.assertEqual(['Hi there'], self.logger.get_logs())

    def test_added_a_few_messages(self):
        self.logger.log('Hello World')
        self.logger.log('Start the app')
        self.assertEqual(['Hello World', 'Start the app'], self.logger.get_logs())

    def test_get_last_log(self):
        self.logger.log('Hello')
        self.logger.log('NNRC')
        self.assertEqual('NNRC', self.logger.get_last_log())
