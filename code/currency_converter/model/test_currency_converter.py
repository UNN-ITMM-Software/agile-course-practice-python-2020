import unittest

from currency_converter.model.currency_converter import CurrencyConverter


class TestCurrencyConverter(unittest.TestCase):
    def test_create_inst(self):
        curr = CurrencyConverter()
        self.assertTrue(isinstance(curr, CurrencyConverter))

    def test_convert_same(self):
        curr = CurrencyConverter()
        self.assertTrue(curr.convert("USD", "USD", 5), 5)