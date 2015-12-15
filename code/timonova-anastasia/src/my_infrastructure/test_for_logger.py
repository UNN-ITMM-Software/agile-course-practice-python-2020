import unittest

from my_infrastructure.fake_logger import FakeLogger


class TestForLogger(unittest.TestCase):
    def setUp(self):
        self.my_logger = FakeLogger()

    def test_can_create_logger(self):
        self.assertTrue(isinstance(self.my_logger, FakeLogger))

    def test_by_default_log_is_empty(self):
        log = self.my_logger.get_logs_list()
        self.assertEqual(log, [])

    def test_state_after_append_message_to_logs_list(self):
        self.my_logger.append_message_to_logs_list('## testing line0 ##')
        self.assertEqual(['## testing line0 ##'], self.my_logger.get_last_messages_from_logs_list(1))

    def test_can_get_last_log(self):
        self.my_logger.append_message_to_logs_list('## testing line1 ##')
        self.my_logger.append_message_to_logs_list('## testing line2 ##')
        self.assertEqual(['## testing line2 ##'], self.my_logger.get_last_messages_from_logs_list(1))

    def test_can_log_several_messages(self):
        self.my_logger.append_message_to_logs_list('## testing line3 ##')
        self.my_logger.append_message_to_logs_list('## testing line4 ##')
        self.assertEqual(['## testing line3 ##', '## testing line4 ##'], self.my_logger.get_logs_list())
