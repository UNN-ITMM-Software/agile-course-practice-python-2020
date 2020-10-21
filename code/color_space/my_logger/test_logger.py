import unittest

from .real_logger import Logger
from .ilogger import ILogger


class TestILogger(unittest.TestCase):
    def test_cannot_log_from_interface(self):
        interface = ILogger()
        with self.assertRaises(NotImplementedError):
            interface.log("QQQ")

    def test_cannot_get_log_from_interface(self):
        interface = ILogger()
        with self.assertRaises(NotImplementedError):
            interface.get_log()


class TestLogger(unittest.TestCase):
    def setUp(self):
        self.logger = Logger("tmp/Logger_Tests-lab3.log")

    def test_can_create_logger(self):
        self.assertIsInstance(self.logger, Logger)

    def test_log_is_empty_by_default(self):
        self.assertEqual(self.logger.get_log(), "")

    def test_can_write_log_message(self):
        self.logger.log("Test")
        self.assertEqual(self.logger.get_log(), "Test")

    def test_can_write_several_log_messages(self):
        self.logger.log("Test")
        self.logger.log("QQQ")
        self.assertEqual(self.logger.get_log(), "Test\nQQQ")

    def test_log_is_empty_after_clear(self):
        self.logger.log("Test")
        self.logger.clear()
        self.assertEqual(self.logger.get_log(), "")
