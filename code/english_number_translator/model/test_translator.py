import unittest

from model.translator import Translator


class TestTranslator(unittest.TestCase):

    def test_0_dig_to_str(self):
        self.assertEquals("zero", Translator.num_to_string(0))

    def test_1_dig_to_str(self):
        self.assertEquals("one", Translator.num_to_string(1))

    def test_2_dig_to_str(self):
        self.assertEquals("two", Translator.num_to_string(2))

    def test_7_dig_to_str(self):
        self.assertEquals("seven", Translator.num_to_string(7))

    def test_10_to_str(self):
        self.assertEquals("ten", Translator.num_to_string(10))

    def test_11_to_str(self):
        self.assertEquals("eleven", Translator.num_to_string(11))

    def test_12_to_str(self):
        self.assertEquals("twelve", Translator.num_to_string(12))

    def test_17_to_str(self):
        self.assertEquals("seventeen", Translator.num_to_string(17))

    def test_21_to_str(self):
        self.assertEquals("twenty-one", Translator.num_to_string(21))

    def test_20_to_str(self):
        self.assertEquals("twenty", Translator.num_to_string(20))

    def test_49_to_str(self):
        self.assertEquals("forty-nine", Translator.num_to_string(49))

    def test_100_to_str(self):
        self.assertEquals("one hundred", Translator.num_to_string(100))

    def test_101_to_str(self):
        self.assertEquals("one hundred one", Translator.num_to_string(101))

    def test_110_to_str(self):
        self.assertEquals("one hundred ten", Translator.num_to_string(110))

    def test_111_to_str(self):
        self.assertEquals("one hundred eleven", Translator.num_to_string(111))

    def test_987_to_str(self):
        self.assertEquals("nine hundred eighty-seven", Translator.num_to_string(987))

    def test_1000_to_str(self):
        self.assertEquals("one thousand", Translator.num_to_string(1000))

    def test_1001_to_str(self):
        self.assertEquals("one thousand one", Translator.num_to_string(1001))

    def test_1010_to_str(self):
        self.assertEquals("one thousand ten", Translator.num_to_string(1010))

    def test_1100_to_str(self):
        self.assertEquals("one thousand one hundred", Translator.num_to_string(1100))

    def test_1101_to_str(self):
        self.assertEquals("one thousand one hundred one", Translator.num_to_string(1101))

    def test_1110_to_str(self):
        self.assertEquals("one thousand one hundred ten", Translator.num_to_string(1110))

    def test_1121_to_str(self):
        self.assertEquals("one thousand one hundred twenty-one", Translator.num_to_string(1121))

    def test_4373_to_str(self):
        self.assertEquals("four thousand three hundred seventy-three", Translator.num_to_string(4373))
