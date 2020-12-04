import unittest

from harry_potter_store.viewmodel.viewmodel import HPStoreViewModel


class TestFractionCalculatorViewModel(unittest.TestCase):

    def setUp(self):
        self.view_model = HPStoreViewModel()

    def test_get_price_empty(self):
        self.view_model.set_books_amount({})
        self.view_model.click_calculate()
        self.assertEqual(0.0, self.view_model.get_price())

    def test_get_price_only_not_numbers(self):
        self.view_model.set_books_amount({0: 'test', 3: 'test2'})
        self.view_model.click_calculate()
        self.assertEqual(0.0, self.view_model.get_price())

    def test_get_price_1(self):
        self.view_model.set_books_amount({0: 1})
        self.view_model.click_calculate()
        self.assertEqual(8.0, self.view_model.get_price())

    def test_get_price_2(self):
        self.view_model.set_books_amount({1: 2})
        self.view_model.click_calculate()
        self.assertEqual(16.0, self.view_model.get_price())

    def test_get_price_with_discount_2_books(self):
        self.view_model.set_books_amount({0: 1, 1: 1})
        self.view_model.click_calculate()
        self.assertEqual(16.0 * 0.95, self.view_model.get_price())

    def test_get_price_with_discount_3_books(self):
        self.view_model.set_books_amount({0: 1, 1: 1, 2: 1})
        self.view_model.click_calculate()
        self.assertEqual(24.0 * 0.9, self.view_model.get_price())

    def test_get_price_with_discount_4_books(self):
        self.view_model.set_books_amount({0: 1, 1: 1, 2: 1, 3: 1})
        self.view_model.click_calculate()
        self.assertEqual(32.0 * 0.8, self.view_model.get_price())

    def test_get_price_with_discount_5_books(self):
        self.view_model.set_books_amount({0: '1', 1: '1', 2: '1', 3: '1', 4: '1'})
        self.view_model.click_calculate()
        self.assertEqual(40.0 * 0.75, self.view_model.get_price())

    def test_get_price_complex_pack(self):
        self.view_model.set_books_amount({0: '1', 1: '2'})
        self.view_model.click_calculate()
        self.assertEqual(16 * 0.95 + 8, self.view_model.get_price())

    def test_get_price_check_result_message(self):
        self.view_model.set_books_amount({0: '1', 1: '2'})
        self.view_model.click_calculate()
        self.assertEqual("Total Price: 23.2", self.view_model.get_result_message())

    def test_get_price_with_negative_amount(self):
        self.view_model.set_books_amount({0: '1', 1: '1', 2: '-1', 3: '1', 4: '1'})
        self.view_model.click_calculate()
        self.assertEqual("ERROR: Book amount should be a positive value",
                         self.view_model.get_result_message())

    def test_get_price_ignore_not_number_amount(self):
        self.view_model.set_books_amount({0: '1', 1: 'test', 2: '2'})
        self.view_model.click_calculate()
        self.assertEqual("Total Price: 23.2", self.view_model.get_result_message())
