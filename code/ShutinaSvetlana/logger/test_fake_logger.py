import unittest


from ShutinaSvetlana.logger.ilogger import FakeLogger


class TestCaesarCipherFakeLogger(unittest.TestCase):
    def setUp(self):
        self.logger = FakeLogger()

    def test_can_create_logger(self):
        self.assertTrue(isinstance(self.logger, FakeLogger))

    def test_default_log_is_empty(self):
        log = self.logger.get_logs()
        self.assertEqual(log, [])

    def test_added_message_in_log(self):
        self.logger.log('Hello')
        self.assertEqual(['Hello'], self.logger.get_logs())

    def test_added_a_few_messages(self):
        self.logger.log('Hello')
        self.logger.log('Start app')
        self.assertEqual(['Hello', 'Start app'], self.logger.get_logs())

    def test_get_last_log(self):
        self.logger.log('Hello')
        self.logger.log('Start app')
        self.assertEqual('Start app', self.logger.get_last_log())
