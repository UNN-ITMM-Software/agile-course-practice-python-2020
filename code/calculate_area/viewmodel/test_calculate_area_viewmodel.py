import unittest

from calculate_area.viewmodel.calculate_area_viewmodel import CalculateAreaViewModel


class TestCalculateAreaViewModel(unittest.TestCase):
    def setUp(self):
        self.viewmodel = CalculateAreaViewModel()

    def test_calc_button_disabled_by_default(self):
        self.assertEqual("disabled", self.viewmodel.get_calc_button_state())

    def test_calc_button_enabled_with_values_for_cone(self):
        self.viewmodel.set_figure_type("CONE")
        self.viewmodel.set_a("abc")
        self.viewmodel.set_r("1.0")
        self.viewmodel.set_h("def")
        self.viewmodel.set_l("2.2")
        self.assertEqual("normal", self.viewmodel.get_calc_button_state())

    def test_calc_button_enabled_with_values_for_cube(self):
        self.viewmodel.set_figure_type("CUBE")
        self.viewmodel.set_a("1")
        self.viewmodel.set_r("abc")
        self.viewmodel.set_h("def")
        self.viewmodel.set_l("ghi")
        self.assertEqual("normal", self.viewmodel.get_calc_button_state())

    def test_calc_button_enabled_with_values_for_sphere(self):
        self.viewmodel.set_figure_type("SPHERE")
        self.viewmodel.set_a("abc")
        self.viewmodel.set_r("1")
        self.viewmodel.set_h("def")
        self.viewmodel.set_l("ghi")
        self.assertEqual("normal", self.viewmodel.get_calc_button_state())

    def test_calc_button_enabled_with_values_for_cylinder(self):
        self.viewmodel.set_figure_type("CYLINDER")
        self.viewmodel.set_a("abc")
        self.viewmodel.set_r("1")
        self.viewmodel.set_h("3")
        self.viewmodel.set_l("def")
        self.assertEqual("normal", self.viewmodel.get_calc_button_state())

    def test_calc_button_disabled_after_incorrect_value_input(self):
        self.viewmodel.set_figure_type("CYLINDER")
        self.viewmodel.set_r("1")
        self.viewmodel.set_h("3")
        self.viewmodel.set_h("hello, i'm incorrect value")
        self.assertEqual("disabled", self.viewmodel.get_calc_button_state())

    def test_calc_button_disabled_after_changed_figure_type(self):
        self.viewmodel.set_figure_type("CYLINDER")
        self.viewmodel.set_r("1")
        self.viewmodel.set_h("3")
        self.viewmodel.set_figure_type("CUBE")
        self.assertEqual("disabled", self.viewmodel.get_calc_button_state())

    def test_message_empty_with_valid_r_l_cone(self):
        self.viewmodel.set_figure_type("CONE")
        self.viewmodel.set_a("abc")
        self.viewmodel.set_r("1.0")
        self.viewmodel.set_h("def")
        self.viewmodel.set_l("2.2")
        self.assertEqual("", self.viewmodel.get_message())

    def test_message_empty_with_valid_a_cube(self):
        self.viewmodel.set_figure_type("CUBE")
        self.viewmodel.set_a("1")
        self.viewmodel.set_r("abc")
        self.viewmodel.set_h("def")
        self.viewmodel.set_l("ghi")
        self.assertEqual("", self.viewmodel.get_message())

    def test_message_empty_with_valid_r_sphere(self):
        self.viewmodel.set_figure_type("SPHERE")
        self.viewmodel.set_a("abc")
        self.viewmodel.set_r("1")
        self.viewmodel.set_h("def")
        self.viewmodel.set_l("ghi")
        self.assertEqual("", self.viewmodel.get_message())

    def test_message_empty_with_valid_r_h_cylinder(self):
        self.viewmodel.set_figure_type("CYLINDER")
        self.viewmodel.set_a("abc")
        self.viewmodel.set_r("1")
        self.viewmodel.set_h("3")
        self.viewmodel.set_l("def")
        self.assertEqual("", self.viewmodel.get_message())

    def test_correct_message_with_invalid_r_l_cone(self):
        self.viewmodel.set_figure_type("CONE")
        self.viewmodel.set_a("abc")
        self.viewmodel.set_r("1.0 privet")
        self.viewmodel.set_h("def")
        self.viewmodel.set_l("2.2")
        self.assertEqual("r or l has incorrect value", self.viewmodel.get_message())

    def test_correct_message_with_invalid_a_cube(self):
        self.viewmodel.set_figure_type("CUBE")
        self.viewmodel.set_a("1b")
        self.viewmodel.set_r("abc")
        self.viewmodel.set_h("7")
        self.viewmodel.set_l("ghi")
        self.assertEqual("a has incorrect value", self.viewmodel.get_message())

    def test_correct_message_with_invalid_r_sphere(self):
        self.viewmodel.set_figure_type("SPHERE")
        self.viewmodel.set_a("5")
        self.viewmodel.set_r("1a")
        self.viewmodel.set_h("def")
        self.viewmodel.set_l("ghi")
        self.assertEqual("r has incorrect value", self.viewmodel.get_message())

    def test_correct_message_with_invalid_r_h_cylinder(self):
        self.viewmodel.set_figure_type("CYLINDER")
        self.viewmodel.set_a("abc")
        self.viewmodel.set_r("1a")
        self.viewmodel.set_h("3")
        self.viewmodel.set_l("def")
        self.assertEqual("r or h has incorrect value", self.viewmodel.get_message())

    def test_check_area_with_valid_r_l_cone(self):
        self.viewmodel.set_figure_type("CONE")
        self.viewmodel.set_r("2.3")
        self.viewmodel.set_l("3.8")
        self.viewmodel.calculate()
        self.assertEqual("44.077", self.viewmodel.get_area())

    def test_check_area_with_valid_a_cube(self):
        self.viewmodel.set_figure_type("CUBE")
        self.viewmodel.set_a("5.9")
        self.viewmodel.calculate()
        self.assertEqual("208.86", self.viewmodel.get_area())

    def test_check_area_with_valid_r_sphere(self):
        self.viewmodel.set_figure_type("SPHERE")
        self.viewmodel.set_r("2.3")
        self.viewmodel.calculate()
        self.assertEqual("66.476", self.viewmodel.get_area())

    def test_check_area_with_valid_r_h_cylinder(self):
        self.viewmodel.set_figure_type("CYLINDER")
        self.viewmodel.set_r("2.3")
        self.viewmodel.set_h("4.2")
        self.viewmodel.calculate()
        self.assertEqual("93.934", self.viewmodel.get_area())
