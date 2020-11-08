import unittest

from harry_potter_store.src.store import Store


class TestMain(unittest.TestCase):

    def test_can_create_store(self):
        Store()

    def test_store_contain_five_book_types(self):
        self.assertTrue(len(Store.book_types) == 5)

    def test_get_price_1(self):
        store = Store()
        self.assertTrue(store.get_price({"1": 1}) == 8)

    def test_get_price_2(self):
        store = Store()
        self.assertTrue(store.get_price({"1": 2}) == 16)

    def test_get_price_with_discount(self):
        store = Store()
        self.assertTrue(store.get_price({"1": 1, "2": 1}) == 16*0.95)