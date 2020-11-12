import unittest

from model.translator import Translator


class TestTranslator(unittest.TestCase):

    def test_1_dig_to_str(self):
        self.assertEquals("one", Translator.num_to_string(1))

    def test_2_dig_to_str(self):
        self.assertEquals("two", Translator.num_to_string(2))

    def test_7_dig_to_str(self):
        self.assertEquals("seven", Translator.num_to_string(7))
