import unittest

from harry_potter_store.src.store import Store


class TestMain(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.store = Store()

    def test_store_contain_five_book_types(self):
        self.assertEqual(5, len(Store.book_types))

    def test_get_price_1(self):
        self.assertEqual(8, self.store.get_price({"1": 1}))

    def test_get_price_2(self):
        self.assertEqual(16, self.store.get_price({"1": 2}))

    def test_get_price_with_discount_2_books(self):
        self.assertEqual(16 * 0.95, self.store.get_price({"1": 1, "2": 1}))

    def test_get_price_with_discount_3_books(self):
        self.assertEqual(24 * 0.9, self.store.get_price({"1": 1, "2": 1, "3": 1}))

    def test_get_price_with_discount_4_books(self):
        self.assertEqual(32 * 0.8, self.store.get_price({"1": 1, "2": 1, "3": 1, "4": 1}))

    def test_get_price_with_discount_5_books(self):
        self.assertEqual(40 * 0.75, self.store.get_price({"1": 1, "2": 1, "3": 1, "4": 1, "5": 1}))

    def test_get_price_complex_1(self):
        self.assertEqual(16 * 0.95 + 8, self.store.get_price({"1": 1, "2": 2}))

    def test_get_price_complex_2(self):
        self.assertRaises(ValueError, lambda: self.store.get_price({"1": 0, "2": 2}))

    def test_get_price_complex_3(self):
        self.assertRaises(ValueError, lambda: self.store.get_price({"1": -132, "2": -3324}))

    def test_get_price_complex_4(self):
        self.assertRaises(ValueError, lambda: self.store.get_price({"1": -132, "2": -3324, "111": 333}))

    def test_get_price_complex_5(self):
        self.assertEqual(24 * 0.90 + 16 * 0.95 + 8, self.store.get_price({"1": 3, "2": 1, "3": 2}))

    def test_get_price_complex_6(self):
        self.assertEqual((32 * 0.8) * 2, self.store.get_price({"1": 2, "2": 2, "3": 2, "4": 2}))

    def test_get_price_complex_7(self):
        self.assertEqual(32 * 0.8 * 2,
                         self.store.get_price({"1": 2, "2": 2, "3": 2, "4": 1, "5": 1}))

    def test_get_price_complex_8(self):
        self.assertEqual((40 * 0.75 * 2) + (16 * 0.95) + 8,
                         self.store.get_price({"1": 2, "2": 2, "3": 2, "4": 3, "5": 4}))

    def test_another_book_price(self):
        store = Store(10)
        self.assertEqual((50 * 0.75 * 2) + (20 * 0.95) + 10,
                         store.get_price({"1": 2, "2": 2, "3": 2, "4": 3, "5": 4}))
