import unittest

from calculate_area.logger.fakelogger import FakeLogger
from calculate_area.logger.reallogger import RealLogger
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


class TestViewModelFakeLogging(unittest.TestCase):
    def setUp(self):
        self.view_model = CalculateAreaViewModel(FakeLogger())

    def test_logging_init(self):
        self.assertEqual('Starting...', self.view_model.logger.get_last_message())

    def test_logging_changing_side(self):
        self.view_model.set_a('1')
        self.assertEqual('Setting the side to 1', self.view_model.logger.get_last_message())

    def test_logging_changing_radius(self):
        self.view_model.set_h('2')
        self.assertEqual('Setting the height to 2', self.view_model.logger.get_last_message())

    def test_logging_changing_height(self):
        self.view_model.set_r('3')
        self.assertEqual('Setting the radius to 3', self.view_model.logger.get_last_message())

    def test_logging_changing_length_of_reference(self):
        self.view_model.set_l('4')
        self.assertEqual('Setting the length of reference to 4', self.view_model.logger.get_last_message())

    def test_logging_changing_figure_type(self):
        self.view_model.set_figure_type("CUBE")
        self.assertEqual('Setting figure type to CUBE', self.view_model.logger.get_last_message())

    def test_logging_calculating_area(self):
        expected_messages = ['Button clicked', 'Selected figure type to CYLINDER', 'Result: 93.934']

        self.view_model.set_r("2.3")
        self.view_model.set_h("4.2")
        self.view_model.set_figure_type("CYLINDER")
        self.view_model.calculate()

        self.assertEqual(expected_messages, self.view_model.logger.get_log_messages()[-3:])


class TestViewModelRealLogging(TestViewModelFakeLogging):
    def setUp(self):
        self.view_model = CalculateAreaViewModel(RealLogger())
