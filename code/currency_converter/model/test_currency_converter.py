import unittest

from currency_converter.model.currency_converter import CurrencyConverter


class TestCurrencyConverter(unittest.TestCase):
    def test_create_inst(self):
        curr = CurrencyConverter()
        self.assertTrue(isinstance(curr, CurrencyConverter))

    def test_create_with_default(self):
        curr = CurrencyConverter(10)
        self.assertTrue(curr.convert("EUR", "RUB"), 919.5)

    def test_convert_usd_rub(self):
        curr = CurrencyConverter()
        self.assertTrue(curr.convert("USD", "RUB", 5), 387.15)

    def test_convert_same(self):
        curr = CurrencyConverter()
        self.assertTrue(curr.convert("USD", "USD", 5), 5)
