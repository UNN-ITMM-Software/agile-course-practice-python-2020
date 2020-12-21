import unittest

from statistics.logger.fakelogger import FakeLogger


class TestLogger(unittest.TestCase):
    def setUp(self):
        self.logger = FakeLogger()
