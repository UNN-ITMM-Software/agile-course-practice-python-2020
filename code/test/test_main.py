import unittest

from main import f, z


class TestF(unittest.TestCase):
    def test_return(self):
        self.assertEqual(f(), 'qqq')


class TestZ(unittest.TestCase):
    def test_return(self):
        self.assertEqual(z(), 'www')
