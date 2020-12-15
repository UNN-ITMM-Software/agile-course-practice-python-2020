import unittest

from bit_array.model.bit_array import BitArray
from bit_array.viewmodel.operation import Operation
from bit_array.viewmodel.viewmodel import BitArrayViewModel


class TestBitArrayViewModel(unittest.TestCase):

    def test_can_convert_from_string(self):
        string = '000011'
        bit_array = BitArrayViewModel.bit_array_from_string(string)
        self.assertTrue(isinstance(bit_array, BitArray))

    def test_convert_from_string_hold_true_length(self):
        string = '0000110011'
        bit_array = BitArrayViewModel.bit_array_from_string(string)
        self.assertEqual(bit_array.get_length(), len(string))

    def test_can_not_convert_from_invalid_string(self):
        string = 'god_help_me'
        with self.assertRaises(ValueError):
            BitArrayViewModel.bit_array_from_string(string)

    def test_convert_from_string_returns_true_string(self):
        string = '00011110'
        bit_array = BitArrayViewModel.bit_array_from_string(string)
        print(bit_array.to_string())
        self.assertEqual(bit_array.to_string(), string)

    def test_set_operation(self):
        view_model = BitArrayViewModel()
        view_model.set_operation(Operation.AND)
        self.assertEqual(view_model.get_operation(), Operation.AND)

    def test_default_operation(self):
        view_model = BitArrayViewModel()
        self.assertEqual(view_model.get_operation(), Operation.OR)

    def test_set_operation_disable_left_bit_array(self):
        view_model = BitArrayViewModel()
        view_model.set_operation(Operation.INVERT)
        self.assertFalse(view_model.get_left_bit_array_enabled())

    def test_set_operation_not_disable_left_bit_array(self):
        view_model = BitArrayViewModel()
        view_model.set_operation(Operation.OR)
        self.assertTrue(view_model.get_left_bit_array_enabled())

    def test_set_left_bit_array(self):
        string = '000110011'
        view_model = BitArrayViewModel()
        view_model.set_left_bit_array(string)
        self.assertTrue(isinstance(view_model.get_left_bit_array_string(), str))

    def test_set_right_bit_array(self):
        string = '000110011'
        view_model = BitArrayViewModel()
        view_model.set_right_bit_array(string)
        self.assertTrue(isinstance(view_model.get_right_bit_array_string(), str))

    def test_get_left_bit_array(self):
        string = '000110011'
        view_model = BitArrayViewModel()
        view_model.set_left_bit_array(string)
        self.assertEqual(view_model.get_left_bit_array_string(), string)

    def test_get_right_bit_array(self):
        string = '000110011'
        view_model = BitArrayViewModel()
        view_model.set_right_bit_array(string)
        self.assertEqual(view_model.get_right_bit_array_string(), string)

    def test_calculate_and(self):
        left_bit_array_string = '1010111111'
        right_bit_array_string = '00000111'
        view_model = BitArrayViewModel()
        left_bit_array = BitArrayViewModel.bit_array_from_string(left_bit_array_string)
        right_bit_array = BitArrayViewModel.bit_array_from_string(right_bit_array_string)
        result = left_bit_array & right_bit_array
        view_model.set_operation(Operation.AND)
        view_model.set_left_bit_array(left_bit_array_string)
        view_model.set_right_bit_array(right_bit_array_string)
        view_model.calculate()
        self.assertEqual(result, view_model.get_result())

    def test_calculate_or(self):
        left_bit_array_string = '1010111111'
        right_bit_array_string = '00000111'
        view_model = BitArrayViewModel()
        left_bit_array = BitArrayViewModel.bit_array_from_string(left_bit_array_string)
        right_bit_array = BitArrayViewModel.bit_array_from_string(right_bit_array_string)
        result = left_bit_array | right_bit_array
        view_model.set_operation(Operation.OR)
        view_model.set_left_bit_array(left_bit_array_string)
        view_model.set_right_bit_array(right_bit_array_string)
        view_model.calculate()
        self.assertEqual(result, view_model.get_result())

    def test_calculate_xor(self):
        left_bit_array_string = '1010111111'
        right_bit_array_string = '00000111'
        view_model = BitArrayViewModel()
        left_bit_array = BitArrayViewModel.bit_array_from_string(left_bit_array_string)
        right_bit_array = BitArrayViewModel.bit_array_from_string(right_bit_array_string)
        result = left_bit_array ^ right_bit_array
        view_model.set_operation(Operation.XOR)
        view_model.set_left_bit_array(left_bit_array_string)
        view_model.set_right_bit_array(right_bit_array_string)
        view_model.calculate()
        self.assertEqual(result, view_model.get_result())

    def test_calculate_eq(self):
        left_bit_array_string = '1010111111'
        right_bit_array_string = '00000111'
        view_model = BitArrayViewModel()
        left_bit_array = BitArrayViewModel.bit_array_from_string(left_bit_array_string)
        right_bit_array = BitArrayViewModel.bit_array_from_string(right_bit_array_string)
        result = left_bit_array == right_bit_array
        view_model.set_operation(Operation.EQ)
        view_model.set_left_bit_array(left_bit_array_string)
        view_model.set_right_bit_array(right_bit_array_string)
        view_model.calculate()
        self.assertEqual(result, view_model.get_result())

    def test_calculate_neq(self):
        left_bit_array_string = '1010111111'
        right_bit_array_string = '00000111'
        view_model = BitArrayViewModel()
        left_bit_array = BitArrayViewModel.bit_array_from_string(left_bit_array_string)
        right_bit_array = BitArrayViewModel.bit_array_from_string(right_bit_array_string)
        result = left_bit_array != right_bit_array
        view_model.set_operation(Operation.NEQ)
        view_model.set_left_bit_array(left_bit_array_string)
        view_model.set_right_bit_array(right_bit_array_string)
        view_model.calculate()
        self.assertEqual(result, view_model.get_result())

    def test_calculate_invert(self):
        right_bit_array_string = '00000111'
        view_model = BitArrayViewModel()
        right_bit_array = BitArrayViewModel.bit_array_from_string(right_bit_array_string)
        result = ~ right_bit_array
        view_model.set_operation(Operation.INVERT)
        view_model.set_right_bit_array(right_bit_array_string)
        view_model.calculate()
        self.assertEqual(result, view_model.get_result())

    def test_get_string_result(self):
        right_bit_array_string = '00000111'
        view_model = BitArrayViewModel()
        result = '11111000'
        view_model.set_operation(Operation.INVERT)
        view_model.set_right_bit_array(right_bit_array_string)
        view_model.calculate()
        self.assertEqual(result, view_model.get_result_string())

    def test_clear_result(self):
        right_bit_array_string = '00000111'
        view_model = BitArrayViewModel()
        view_model.set_operation(Operation.INVERT)
        view_model.set_right_bit_array(right_bit_array_string)
        view_model.calculate()
        view_model.clear_result()
        self.assertEqual(view_model.get_result(), None)

    def test_get_empty_result(self):
        view_model = BitArrayViewModel()
        self.assertEqual(view_model.get_result_string(), '')
