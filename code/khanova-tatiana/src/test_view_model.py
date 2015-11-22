import unittest
from view_model import ViewModel


class TestColorSpaceConverterViewModel(unittest.TestCase):
    def test_button_enabled(self):
        viewmodel = ViewModel()
        self.assertEqual('enabled', viewmodel.get_button_convert_state())

    def test_when_entered_color_button_enabled(self):
        viewmodel = ViewModel()
        viewmodel.set_color_in(['0', '0', '0'])
        self.assertEqual('enabled', viewmodel.get_button_convert_state())

    def test_when_erased_color_button_disabled(self):
        viewmodel = ViewModel()
        viewmodel.set_color_in(['', '', ''])
        self.assertEqual('disabled', viewmodel.get_button_convert_state())

    def test_when_change_color_in_it_changes(self):
        viewmodel = ViewModel()
        viewmodel.set_color_in(['10', '100', '80'])
        self.assertEqual(['10', '100', '80'], viewmodel.get_color_in())

    def test_when_change_color_space_in_it_changes(self):
        viewmodel = ViewModel()
        viewmodel.set_color_space_in("HSV")
        self.assertEqual("HSV", viewmodel.get_color_space_in())

    def test_when_change_color_space_out_it_changes(self):
        viewmodel = ViewModel()
        viewmodel.set_color_space_out("HSV")
        self.assertEqual("HSV", viewmodel.get_color_space_out())

    def test_convert_button_disabled_incorrect_color_space_in(self):
        viewmodel = ViewModel()
        viewmodel.set_color_space_in("QQQ")
        self.assertEqual("disabled", viewmodel.get_button_convert_state())

    def test_convert_button_disabled_incorrect_color_space_out(self):
        viewmodel = ViewModel()
        viewmodel.set_color_space_out("QQQ")
        self.assertEqual("disabled", viewmodel.get_button_convert_state())

    def test_complains_on_incorrect_color_space_in(self):
        viewmodel = ViewModel()
        viewmodel.set_color_space_in("QQQ")
        self.assertEqual("Unsupported color space.", viewmodel.get_error_message())

    def test_convert_button_disabled_incorrect_color_in(self):
        viewmodel = ViewModel()
        viewmodel.set_color_in(['', '', ''])
        self.assertEqual("disabled", viewmodel.get_button_convert_state())

    def test_complains_on_incorrect_color_in(self):
        viewmodel = ViewModel()
        viewmodel.set_color_in(['', '', ''])
        self.assertEqual("Incorrect values.", viewmodel.get_error_message())

    def test_error_message_is_empty_after_correct_color_in(self):
        viewmodel = ViewModel()
        viewmodel.set_color_in(['0', '-10', '10'])
        self.assertEqual("Incorrect values.", viewmodel.get_error_message())
        viewmodel.set_color_in(['0', '10', '10'])
        self.assertEqual("", viewmodel.get_error_message())

    def test_convert_button_disabled_incorrect_color_in_text(self):
        viewmodel = ViewModel()
        viewmodel.set_color_in(['a', 'b', '10'])
        self.assertEqual("disabled", viewmodel.get_button_convert_state())

    def test_convert_button_disabled_incorrect_color_in_negative(self):
        viewmodel = ViewModel()
        viewmodel.set_color_in(['-1', '-1', '300'])
        self.assertEqual("disabled", viewmodel.get_button_convert_state())

    def test_complains_on_incorrect_color_in_not_in_range(self):
        viewmodel = ViewModel()
        viewmodel.set_color_in(['1000', '0', '0'])
        self.assertEqual("Input values should be in range 0-255.", viewmodel.get_error_message())

    def test_when_convert_def_rgb_to_rgb_display_it(self):
        viewmodel = ViewModel()
        viewmodel.set_color_space_in("RGB")
        viewmodel.set_color_space_out("RGB")
        viewmodel.set_color_in(['0', '0', '0'])
        viewmodel.convert()
        self.assertEqual("RGB", viewmodel.get_color_space_out())
        self.assertEqual(['0', '0', '0'], viewmodel.get_color_out())

    def test_when_convert_rgb_to_hsv_display_it(self):
        viewmodel = ViewModel()
        viewmodel.set_color_space_in("RGB")
        viewmodel.set_color_space_out("HSV")
        viewmodel.set_color_in(['0', '100', '0'])
        viewmodel.convert()
        self.assertEqual("HSV", viewmodel.get_color_space_out())
        self.assertEqual(['85', '255', '100'], viewmodel.get_color_out())

    def test_when_convert_lab_to_rgb_display_it(self):
        viewmodel = ViewModel()
        viewmodel.set_color_space_in("LAB")
        viewmodel.set_color_space_out("RGB")
        viewmodel.set_color_in(['88', '148', '101'])
        viewmodel.convert()
        self.assertEqual("RGB", viewmodel.get_color_space_out())
        self.assertEqual(['90', '72', '124'], viewmodel.get_color_out())
