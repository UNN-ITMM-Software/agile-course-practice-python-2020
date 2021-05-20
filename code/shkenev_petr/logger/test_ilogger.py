import unittest

from .ilogger import ILogger


class TestILogger(unittest.TestCase):

    def test_get_messages_list(self):
        with self.assertRaises(NotImplementedError):
                logger = ILogger()
                logger.get_messages_list()

    def test_log(self):
        with self.assertRaises(NotImplementedError):
                logger = ILogger()
                logger.log()
