import unittest

from rational_number.logger.fakelogger import FakeLogger


class TestLogger(unittest.TestCase):
    def setUp(self):
        self.logger = FakeLogger()

    def test_by_default_log_is_empty(self):
        log = self.logger.get_log_messages()
        self.assertEqual(log, [])

    def test_after_logging_message_in_log(self):
        self.logger.log('Smth')
        self.assertTrue(self.logger.get_log_messages().index("Smth") != -1)

    def test_can_log_several_messages(self):
        self.logger.log('Test1')
        self.logger.log('Test2')
        self.logger.log('Test3')
        self.assertEqual(['Test1', 'Test2', 'Test3'], self.logger.get_log_messages())

    def test_can_get_last_log(self):
        self.logger.log('Test1')
        self.logger.log('Test2')
        self.logger.log('Test3')
        self.assertEqual('Test3', self.logger.get_last_message())
