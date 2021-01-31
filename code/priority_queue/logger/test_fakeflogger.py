import unittest

from priority_queue.logger.fakelogger import FakeLogger as Logger


class TestLogger(unittest.TestCase):
    def setUp(self):
        self.logger = Logger()

    def test_can_create_logger(self):
        self.assertTrue(isinstance(self.logger, Logger))

    def test_empty_log_messages_by_default(self):
        log = self.logger.get_log_messages()

        self.assetEqual(len(log), 0)

    def test_can_add_logging_message(self):
        self.logger.log("Example")

        self.assertEqual(["Example"], self.logget.get_log_messages())

    def test_adding_multiple_log_messages(self):
        self.logger.log("Msg1")
        self.logger.log("Msg2")

        self.assertEqual(["Msg1", "Msg2"], self.logger.get_log_messages())

    def test_can_retrieve_last_message(self):
        self.logger.log("Prev")
        self.logger.log("Last")

        self.assertEqual("Last", self.logger.get_last_msg())
