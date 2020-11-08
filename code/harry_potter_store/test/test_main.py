import unittest

from harry_potter_store.src.store import Store


class TestMain(unittest.TestCase):
    def test_main(self):
        pass

    def test_can_create_store(self):
        Store()

    def test_store_contain_five_book_types(self):
        self.assertTrue(len(Store.book_types) == 5)