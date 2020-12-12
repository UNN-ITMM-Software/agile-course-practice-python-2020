import unittest

from model.translator import Translator


class TestTranslator(unittest.TestCase):

    def test_0_dig_to_str(self):
        self.assertEqual("zero", Translator.num_to_string(0))

    def test_1_dig_to_str(self):
        self.assertEqual("one", Translator.num_to_string(1))

    def test_2_dig_to_str(self):
        self.assertEqual("two", Translator.num_to_string(2))

    def test_7_dig_to_str(self):
        self.assertEqual("seven", Translator.num_to_string(7))

    def test_10_to_str(self):
        self.assertEqual("ten", Translator.num_to_string(10))

    def test_11_to_str(self):
        self.assertEqual("eleven", Translator.num_to_string(11))

    def test_12_to_str(self):
        self.assertEqual("twelve", Translator.num_to_string(12))

    def test_17_to_str(self):
        self.assertEqual("seventeen", Translator.num_to_string(17))

    def test_21_to_str(self):
        self.assertEqual("twenty-one", Translator.num_to_string(21))

    def test_20_to_str(self):
        self.assertEqual("twenty", Translator.num_to_string(20))

    def test_49_to_str(self):
        self.assertEqual("forty-nine", Translator.num_to_string(49))

    def test_100_to_str(self):
        self.assertEqual("one hundred", Translator.num_to_string(100))

    def test_101_to_str(self):
        self.assertEqual("one hundred one", Translator.num_to_string(101))

    def test_110_to_str(self):
        self.assertEqual("one hundred ten", Translator.num_to_string(110))

    def test_111_to_str(self):
        self.assertEqual("one hundred eleven", Translator.num_to_string(111))

    def test_987_to_str(self):
        self.assertEqual("nine hundred eighty-seven", Translator.num_to_string(987))

    def test_1000_to_str(self):
        self.assertEqual("one thousand", Translator.num_to_string(1000))

    def test_1001_to_str(self):
        self.assertEqual("one thousand one", Translator.num_to_string(1001))

    def test_1010_to_str(self):
        self.assertEqual("one thousand ten", Translator.num_to_string(1010))

    def test_1100_to_str(self):
        self.assertEqual("one thousand one hundred", Translator.num_to_string(1100))

    def test_1101_to_str(self):
        self.assertEqual("one thousand one hundred one", Translator.num_to_string(1101))

    def test_1110_to_str(self):
        self.assertEqual("one thousand one hundred ten", Translator.num_to_string(1110))

    def test_1121_to_str(self):
        self.assertEqual("one thousand one hundred twenty-one", Translator.num_to_string(1121))

    def test_4373_to_str(self):
        self.assertEqual("four thousand three hundred seventy-three", Translator.num_to_string(4373))

    def test_10000_to_str(self):
        self.assertEqual("ten thousand", Translator.num_to_string(10000))

    def test_21000_to_str(self):
        self.assertEqual("twenty-one thousand", Translator.num_to_string(21000))

    def test_21121_to_str(self):
        self.assertEqual("twenty-one thousand one hundred twenty-one", Translator.num_to_string(21121))

    def test_111111_to_str(self):
        self.assertEqual("one hundred eleven thousand one hundred eleven", Translator.num_to_string(111111))

    def test_1000000_to_str(self):
        self.assertEqual("one million", Translator.num_to_string(1000000))

    def test_1000001_to_str(self):
        self.assertEqual("one million one", Translator.num_to_string(1000001))

    def test_1000011_to_str(self):
        self.assertEqual("one million eleven", Translator.num_to_string(1000011))

    def test_1000111_to_str(self):
        self.assertEqual("one million one hundred eleven", Translator.num_to_string(1000111))

    def test_1011111_to_str(self):
        self.assertEqual("one million eleven thousand one hundred eleven", Translator.num_to_string(1011111))

    def test_1111111_to_str(self):
        self.assertEqual(
            "one million one hundred eleven thousand one hundred eleven", Translator.num_to_string(1111111))

    def test_11111111_to_str(self):
        self.assertEqual(
            "eleven million one hundred eleven thousand one hundred eleven",
            Translator.num_to_string(11111111))

    def test_111111111_to_str(self):
        self.assertEqual(
            "one hundred eleven million one hundred eleven thousand one hundred eleven",
            Translator.num_to_string(111111111))

    def test_1111111111_to_str(self):
        self.assertEqual(
            "one billion one hundred eleven million one hundred eleven thousand one hundred eleven",
            Translator.num_to_string(1111111111))

    def test_not_int_raise_error(self):
        try:
            Translator.num_to_string(111.0)
        except TypeError:
            self.assertTrue(True)

    def test_negative_number_raise_error(self):
        try:
            Translator.num_to_string(-55)
        except ValueError:
            self.assertTrue(True)
