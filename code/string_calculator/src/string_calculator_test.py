import unittest

from string_calculator import StrCalculator
from string_calculator import StrCalculatorType
from string_calculator import StrCalculatorParser


class TestStrCalculatorClass(unittest.TestCase):
    def test_can_create_calculator(self):
        strcalc = StrCalculator()
        self.assertTrue(isinstance(strcalc, StrCalculator))

    def test_add_empty_string_is_0(self):
        strcalc = StrCalculator()
        result = strcalc.add("")
        self.assertEqual(result, 0)

    def test_add_string_1(self):
        strcalc = StrCalculator()
        result = strcalc.add("1")
        self.assertEqual(result, 1)

    def test_add_strings_1_2(self):
        strcalc = StrCalculator()
        result = strcalc.add("1,2")
        self.assertEqual(result, 3)

    def test_can_add_unknown_amount_strings(self):
        strcalc = StrCalculator()
        result = strcalc.add("2,3,1,0,5,6,0,1,2")
        self.assertEqual(result, 20)

    def test_can_use_newline_delimiter(self):
        strcalc = StrCalculator()
        result = strcalc.add("1\n2,3")
        self.assertEqual(result, 6)

    def test_can_use_newline_delimiter_mix(self):
        strcalc = StrCalculator()
        result = strcalc.add("1\n2,3,4\n5,6\n7")
        self.assertEqual(result, 28)

    def test_can_use_custom_delimiter(self):
        strcalc = StrCalculator()
        result = strcalc.add(";\n1;2")
        self.assertEqual(result, 3)

    def test_can_use_custom_delimiter_hard(self):
        strcalc = StrCalculator()
        result = strcalc.add(";\n1;2;3;4;5;6;7")
        self.assertEqual(result, 28)

    def test_check_negative_numbers_exception(self):
        strcalc = StrCalculator()
        msg = 'negatives not allowed: -1, -2'
        with self.assertRaisesRegex(ValueError, msg):
            strcalc.add("-1,-2")


class TestStrCalculatorTypeClass(unittest.TestCase):
    def test_can_create_calctype(self):
        calctype = StrCalculatorType("1,1", ',', "1,1", [1, 1])
        self.assertTrue(isinstance(calctype, StrCalculatorType))


class TestStrCalculatorParserClass(unittest.TestCase):
    def test_can_create_parser(self):
        parser = StrCalculatorParser()
        self.assertTrue(isinstance(parser, StrCalculatorParser))

    def test_parse_check_string_with_default_delim(self):
        parser = StrCalculatorParser()
        result = parser.parse("1,2").string
        self.assertEqual(result, "1,2")

    def test_parse_check_delimiters_with_default_delim(self):
        parser = StrCalculatorParser()
        result = parser.parse("1,2").delimiters
        self.assertEqual(result, ["\n", ","])

    def test_parse_check_numstring_with_default_delim(self):
        parser = StrCalculatorParser()
        result = parser.parse("1,2").numstring
        self.assertEqual(result, "1,2")

    def test_parse_check_numbers_with_default_delim(self):
        parser = StrCalculatorParser()
        result = parser.parse("1,2").numbers
        self.assertEqual(result, [1, 2])

    def test_parse_check_string_with_custom_delim(self):
        parser = StrCalculatorParser()
        result = parser.parse(";\n1;2").string
        self.assertEqual(result, ";\n1;2")

    def test_parse_check_delimiters_with_custom_delim(self):
        parser = StrCalculatorParser()
        result = parser.parse(";\n1;2").delimiters
        self.assertEqual(result, ";")

    def test_parse_check_numstring_with_custom_delim(self):
        parser = StrCalculatorParser()
        result = parser.parse(";\n1;2").numstring
        self.assertEqual(result, "1,2")

    def test_parse_check_numbers_with_custom_delim(self):
        parser = StrCalculatorParser()
        result = parser.parse(";\n1;2").numbers
        self.assertEqual(result, [1, 2])
