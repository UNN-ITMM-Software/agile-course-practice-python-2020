import unittest

from rational_number.viewmodel.rational_number_viewmodel import RationalNumberViewModel

class TestRationalNumberViewModel(unittest.TestCase):

    def test_calculate_button_disabled_by_default_positive(self):
        viewmodel = RationalNumberViewModel()
        self.assertEqual("disabled", viewmodel.get_calculate_button_state())

    def test_numbers_filled_calculate_button_enabled_positive(self):
        viewmodel = RationalNumberViewModel()
        viewmodel.set_first_number("1/2")
        viewmodel.set_second_number("2/7")
        self.assertEqual("normal", viewmodel.get_calculate_button_state())

    def test_numbers_filled_and_removed_calculate_button_disabled_positive(self):
        viewmodel = RationalNumberViewModel()
        viewmodel.set_first_number("1/2")
        viewmodel.set_second_number("2/7")
        viewmodel.set_second_number("")
        self.assertEqual("disabled", viewmodel.get_calculate_button_state())
