import unittest

from lines_intersect.logger.fakelogger import FakeLogger


class TestFakeLogger(unittest.TestCase):
    def setUp(self):
        self.logger = FakeLogger()

    def test_can_create_logger(self):
        self.assertTrue(isinstance(self.logger, FakeLogger))

    def test_default_log_is_empty(self):
        log = self.logger.get_logs()

        self.assertEqual(log, [])

    def test_log_one_message(self):
        self.logger.log("Message")

        log = self.logger.get_logs()

        self.assertEqual(log, ["Message"])

    def test_log_few_messages(self):
        messages = ["Message1", "Message2"]
        for message in messages:
            self.logger.log(message)

        log = self.logger.get_logs()

        self.assertEqual(log, messages)

    def test_can_gen_two_last_messages(self):
        messages = ["Message1", "Message2", "Message3", "Message4"]
        for message in messages:
            self.logger.log(message)

        log = self.logger.get_logs(2)

        self.assertEqual(log, ["Message3", "Message4"])
