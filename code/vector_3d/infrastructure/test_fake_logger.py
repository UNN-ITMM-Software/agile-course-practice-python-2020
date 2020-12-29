import unittest

from vector_3d.infrastructure.fake_logger import FakeLogger


class TestLogger(unittest.TestCase):
    def setUp(self):
        self.logger = FakeLogger()

    def test_create_log(self):
        self.assertTrue(isinstance(self.logger, FakeLogger))

    def test_empty_logger(self):
        log = self.logger.get_log_messages()
        self.assertEqual(log, [])

    def test_return_log_message(self):
        self.logger.log('log message')
        self.assertEqual('log message', self.logger.get_last_message())

    def test_return_last_log_message(self):
        self.logger.log('log message 1')
        self.logger.log('log message 2')
        self.assertEqual('log message 2', self.logger.get_last_message())

    def test_return_all_log_messages(self):
        self.logger.log('log message 1')
        self.logger.log('log message 2')
        self.assertEqual(['log message 1', 'log message 2'], self.logger.get_log_messages())

    def test_return_2_log_messages(self):
        self.logger.log('log message 1')
        self.logger.log('log message 2')
        self.logger.log('log message 3')
        self.logger.log('log message 4')
        self.assertEqual(['log message 3', 'log message 4'], self.logger.get_several_messages(2))
