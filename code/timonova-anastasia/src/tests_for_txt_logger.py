import unittest

from txt_logger import TxtLogger
from txt_logger import LoggerError


class TestForTxtLogger(unittest.TestCase):

    def test_can_create_logger_with_filename(self):
        with self.assertRaises(LoggerError):
            self.txt_logger = TxtLogger()

    # def test_can_create_file_on_disk(self):
    #     with self.assertRaises(LoggerError):
