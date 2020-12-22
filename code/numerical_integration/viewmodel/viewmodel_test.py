import unittest

from numerical_integration.viewmodel.viewmodel import NumericalIntegratorViewModel, CalculateState, Operation


class TestBigIntegerViewModel(unittest.TestCase):

    def setUp(self):
        self.view_model = NumericalIntegratorViewModel()

    def test_by_default_config(self):
        self.assertEqual("0", self.view_model.get_a())
        self.assertEqual("1", self.view_model.get_b())
        self.assertEqual(Operation.TRAPEZIUM_METHOD, self.view_model.get_operation())
        self.assertEqual(CalculateState.ENABLE, self.view_model.get_calculate_state())
        self.assertEqual("0.5", self.view_model.get_result())

    def test_when_entered_valid_a_b_button_enabled(self):
        self.view_model.set_a("5")
        self.view_model.set_b("6")
        self.assertEqual(CalculateState.ENABLE, self.view_model.get_calculate_state())

    def test_when_entered_invalid_a_button_disabled(self):
        self.view_model.set_a("4as")
        self.view_model.set_b("2")
        self.assertEqual(CalculateState.DISABLE, self.view_model.get_calculate_state())

    def test_when_entered_invalid_b_button_disabled(self):
        self.view_model.set_a("5")
        self.view_model.set_b("21ew")
        self.assertEqual(CalculateState.DISABLE, self.view_model.get_calculate_state())

    def test_can_retrieve_a_text(self):
        self.view_model.set_a("6")
        self.assertEqual("6", self.view_model.get_a())

    def test_can_retrieve_a_float_text(self):
        self.view_model.set_a("6.5")
        self.assertEqual("6.5", self.view_model.get_a())

    def test_can_retrieve_a_sign_float_text(self):
        self.view_model.set_a("-6.5")
        self.assertEqual("-6.5", self.view_model.get_a())

    def test_can_retrieve_b_float_text(self):
        self.view_model.set_b("0.5")
        self.assertEqual("0.5", self.view_model.get_b())

    def test_can_retrieve_b_sign_float_text(self):
        self.view_model.set_b("+1.5")
        self.assertEqual("+1.5", self.view_model.get_b())

    def test_can_retrieve_b_text(self):
        self.view_model.set_b("7")
        self.assertEqual("7", self.view_model.get_b())

    def test_can_retrieve_a_text_invalid(self):
        self.view_model.set_a("1rr")
        self.assertEqual("1rr", self.view_model.get_a())

    def test_can_retrieve_b_text_invalid(self):
        self.view_model.set_b("e12")
        self.assertEqual("e12", self.view_model.get_b())

    def test_can_retrieve_operation_text(self):
        self.view_model.set_operation(Operation.TRAPEZIUM_METHOD)
        self.assertEqual(Operation.TRAPEZIUM_METHOD, self.view_model.get_operation())

    def test_when_entered_a_b_then_clear_a_button_disabled(self):
        self.view_model.set_a("65")
        self.view_model.set_b("12")
        self.view_model.set_a("")
        self.assertEqual(CalculateState.DISABLE, self.view_model.get_calculate_state())

    def test_when_entered_a_b_then_clear_b_button_disabled(self):
        self.view_model.set_a("89")
        self.view_model.set_b("45")
        self.view_model.set_b("")
        self.assertEqual(CalculateState.DISABLE, self.view_model.get_calculate_state())

    def test_when_entered_a_b_then_clear_a_b_button_disabled(self):
        self.view_model.set_a("56")
        self.view_model.set_b("544")
        self.view_model.set_a("")
        self.view_model.set_b("")
        self.assertEqual(CalculateState.DISABLE, self.view_model.get_calculate_state())

    def test_can_get_trapezium_method(self):
        self.view_model.set_a("1")
        self.view_model.set_b("2")
        self.view_model.set_operation(Operation.TRAPEZIUM_METHOD)
        self.view_model.calculate()
        self.assertEqual("1.5", self.view_model.get_result())

    def test_can_get_simpson_method(self):
        self.view_model.set_a("3")
        self.view_model.set_b("4")
        self.view_model.set_operation(Operation.SIMPSON_METHOD)
        self.view_model.calculate()
        self.assertEqual("3.5", self.view_model.get_result())
