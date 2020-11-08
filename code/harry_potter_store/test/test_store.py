import unittest

from harry_potter_store.src.store import Store


class TestMain(unittest.TestCase):

    def test_can_create_store(self):
        Store()

    def test_store_contain_five_book_types(self):
        self.assertEqual(len(Store.book_types), 5)

    def test_get_price_1(self):
        store = Store()
        self.assertEqual(store.get_price({"1": 1}), 8)

    def test_get_price_2(self):
        store = Store()
        self.assertEqual(store.get_price({"1": 2}), 16)

    def test_get_price_with_discount_2_books(self):
        store = Store()
        self.assertEqual(store.get_price({"1": 1, "2": 1}), 16 * 0.95)

    def test_get_price_with_discount_3_books(self):
        store = Store()
        self.assertEqual(store.get_price({"1": 1, "2": 1, "3": 1}), 24 * 0.9)

    def test_get_price_with_discount_4_books(self):
        store = Store()
        self.assertEqual(store.get_price({"1": 1, "2": 1, "3": 1, "4": 1}), 32 * 0.8)

    def test_get_price_complex_1(self):
        store = Store()
        self.assertEqual(store.get_price({"1": 1, "2": 2}), 16 * 0.95 + 8)

    def test_get_price_complex_2(self):
        store = Store()
        self.assertEqual(store.get_price({"1": 0, "2": 2}), 16)

    def test_get_price_complex_3(self):
        store = Store()
        self.assertEqual(store.get_price({"1": -132, "2": -3324}), 0)

    def test_get_price_complex_4(self):
        store = Store()
        self.assertEqual(store.get_price({"1": -132, "2": -3324, "111": 333}), 0)

    def test_get_price_complex_5(self):
        store = Store()
        self.assertEqual(store.get_price({"1": 3, "2": 1, "3": 2}), 24 * 0.90 + 16 * 0.95 + 8)

    def test_get_price_complex_6(self):
        store = Store()
        self.assertEqual(store.get_price({"1": 2, "2": 2, "3": 2, "4": 2}), (32 * 0.8) * 2)
