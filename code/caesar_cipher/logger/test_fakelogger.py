import unittest

from caesar_cipher.logger.fakelogger import FakeLogger


class TestCaesarCipherFakeLogger(unittest.TestCase):
    def setUp(self):
        self.logger = FakeLogger()

    def test_can_create_logger(self):
        self.assertTrue(isinstance(self.logger, FakeLogger))

    def test_by_default_log_is_empty(self):
        log = self.logger.get_log_messages()
        self.assertEqual(log, [])

    def test_after_logging_message_in_log(self):
        self.logger.log('Log')
        self.assertEqual(['Log'], self.logger.get_log_messages())

    def test_can_log_several_messages(self):
        self.logger.log('Log1')
        self.logger.log('Log2')
        self.assertEqual(['Log1', 'Log2'], self.logger.get_log_messages())

    def test_can_get_last_log(self):
        self.logger.log('Log1')
        self.logger.log('Log2')
        self.assertEqual('Log2', self.logger.get_last_message())
