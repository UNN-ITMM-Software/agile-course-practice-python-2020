import unittest

from radix_sort.infrastructure.fake_logger import FakeLogger


class TestLogger(unittest.TestCase):
    def setUp(self):
        self.logger = FakeLogger()

    def test_can_create_logger(self):
        self.assertTrue(isinstance(self.logger, FakeLogger))

    def test_by_default_log_is_empty(self):
        log = self.logger.get_logs()
        self.assertEqual(log, [])

    def test_logging(self):
        self.logger.log('logging 0')
        self.assertEqual(['logging 0'], self.logger.get_last_messages(1))

    def test_can_get_last_log(self):
        self.logger.log('logging 1')
        self.logger.log('logging 2')
        self.assertEqual(['logging 2'], self.logger.get_last_messages(1))

    def test_can_log_several_messages(self):
        self.logger.log('logging 3')
        self.logger.log('logging 4')
        self.assertEqual(['logging 3', 'logging 4'], self.logger.get_logs())
