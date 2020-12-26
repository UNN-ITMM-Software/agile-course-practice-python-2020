import unittest

from hashmap.logger.fakelogger import FakeLogger as Logger


class TestLogger(unittest.TestCase):
    def setUp(self):
        self.logger = Logger()

    def test_can_create_logger(self):
        self.assertTrue(isinstance(self.logger, Logger))

    def test_default_log_is_empty(self):
        log = self.logger.get_log_messages()
        self.assertEqual(log, [])

    def test_get_log_message(self):
        self.logger.log('test_log1')
        self.assertEqual(['test_log1'], self.logger.get_log_messages())

    def test_get_log_messages(self):
        self.logger.log('test_log1')
        self.logger.log('test_log2')
        self.logger.log('test_log3')
        self.assertEqual(['test_log1', 'test_log2', 'test_log3'], self.logger.get_log_messages())

    def test_get_last_message(self):
        self.logger.log('test_log1')
        self.logger.log('test_log2')
        self.logger.log('test_log3')
        self.assertEqual('test_log3', self.logger.get_last_message())
    
    def test_last_message_in_empy_log(self):
        self.assertEqual(None, self.logger.get_last_message())
