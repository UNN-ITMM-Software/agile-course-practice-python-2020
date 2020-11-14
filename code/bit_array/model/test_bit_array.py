import unittest

from bit_array.model.bit_array import BitArray


class TestBitArray(unittest.TestCase):
    def test_empty_bit_array(self):
        with self.assertRaises(ValueError):
            BitArray()

    def test_zero_bit_array(self):
        with self.assertRaises(ValueError):
            BitArray(0)

    def test_negative_count_of_bits(self):
        with self.assertRaises(ValueError):
            BitArray(-2)

    def test_not_integer_count_of_bits(self):
        with self.assertRaises(TypeError):
            BitArray(9.75)

    def test_get_mem_length_of_array(self):
        bit_array = BitArray(16)

        self.assertEqual(2, bit_array.get_mem_length())

    def test_get_length_of_array(self):
        bit_array = BitArray(12)

        self.assertEqual(12, bit_array.get_length())

    def test_get_mask_for_invalid_argument(self):
        with self.assertRaises(TypeError):
            BitArray(1)._BitArray__get_mask('a')

    def test_get_mask_for_out_of_range_argument(self):
        with self.assertRaises(ValueError):
            BitArray(5)._BitArray__get_mask(7)

    def test_get_mask_for_valid_argument(self):
        bit_array = BitArray(8)
        exp = 128

        self.assertEqual(exp, bit_array._BitArray__get_mask(7))

    def test_get_array_index_for_invalid_argument(self):
        with self.assertRaises(TypeError):
            BitArray(8)._BitArray__get_array_index([2])

    def test_get_array_index_for_out_of_range_argument(self):
        with self.assertRaises(IndexError):
            BitArray(8)._BitArray__get_array_index(10)

    def test_get_array_index_for_valid_bit(self):
        bit_array = BitArray(15)
        exp = 1

        self.assertEqual(exp, bit_array._BitArray__get_array_index(10))

    def test_cant_conver_negative_decimal_to_binary_string(self):
        with self.assertRaises(ValueError):
            BitArray(8)._BitArray__decimal_to_binary(-2)

    def test_conver_decimal_to_binary_string(self):
        bit_array = BitArray(7)
        exp = '00000101'

        self.assertEqual(exp, bit_array._BitArray__decimal_to_binary(5))

    def test_set_bit_with_invalid_argument(self):
         with self.assertRaises(TypeError):
            BitArray(5).set_bit([9.75])

    def test_set_bit_with_out_of_range_argument(self):
         with self.assertRaises(IndexError):
            BitArray(5).set_bit(12)

    def test_set_bit_with_valid_argument(self):
        bit_array = BitArray(12)
        bit_array.set_bit(11)
        exp = [0, 8]

        self.assertEqual(exp, bit_array._BitArray__array)

    def test_get_bit_with_invalid_argument(self):
         with self.assertRaises(TypeError):
            BitArray(5).get_bit('2')

    def test_get_bit_with_out_of_range_argument(self):
         with self.assertRaises(IndexError):
            BitArray(5).get_bit(12)

    def test_get_bit_with_valid_argument(self):
        bit_array = BitArray(12)
        bit_array.set_bit(11)
        exp = 1

        self.assertEqual(exp, bit_array.get_bit(11))

    def test_clear_bit_with_invalid_argument(self):
         with self.assertRaises(TypeError):
            BitArray(5).clear_bit('2')

    def test_clear_bit_with_out_of_range_argument(self):
         with self.assertRaises(IndexError):
            BitArray(5).clear_bit(12)

    def test_clear_bit_with_valid_argument(self):
        bit_array = BitArray(12)
        bit_array.set_bit(11)
        bit_array.clear_bit(11)
        exp = 0

        self.assertEqual(exp, bit_array.get_bit(11))

    def test_convert_array_to_string(self):
        bit_array = BitArray(8)
        bit_array.set_bit(0)
        bit_array.set_bit(2)
        bit_array.set_bit(4)
        bit_array.set_bit(6)
        exp = '01010101'

        self.assertEqual(exp, bit_array.to_string())

    def test_or_operation_with_not_bit_array(self):
        with self.assertRaises(TypeError):
            [0, 0, 1, 0, 0] | BitArray(5)

    def test_or_operation_with_equal_size_arrays(self):
        ba1 = BitArray(12)
        ba1.set_bit(3)
        ba2 = BitArray(12)
        ba2.set_bit(10)
        exp = '0000010000001000'

        self.assertEqual(exp, (ba1 | ba2).to_string())

    def test_or_operation_with_not_equal_size_arrays(self):
        ba1 = BitArray(5)
        ba1.set_bit(3)
        ba2 = BitArray(12)
        ba2.set_bit(10)
        exp = '0000010000001000'

        self.assertEqual(exp, (ba1 | ba2).to_string())

    def test_and_operation_with_not_bit_array(self):
        with self.assertRaises(TypeError):
            [0, 0, 1, 0, 0] & BitArray(5)

    def test_and_operation_with_equal_size_arrays(self):
        ba1 = BitArray(8)
        ba1.set_bit(3)
        ba1.set_bit(5)
        ba2 = BitArray(8)
        ba2.set_bit(5)
        exp = '00100000'

        self.assertEqual(exp, (ba1 & ba2).to_string())

    def test_and_operation_with_not_equal_size_arrays(self):
        ba1 = BitArray(8)
        ba1.set_bit(5)
        ba2 = BitArray(18)
        ba2.set_bit(5)
        ba2.set_bit(17)
        exp = '000000000000000000100000'

        self.assertEqual(exp, (ba1 & ba2).to_string())

    def test_xor_operation_with_not_bit_array(self):
        with self.assertRaises(TypeError):
            [0, 0, 1, 0, 0] ^ BitArray(5)

    def test_xor_operation_with_equal_size_arrays(self):
        ba1 = BitArray(8)
        ba1.set_bit(1)
        ba1.set_bit(5)
        ba2 = BitArray(8)
        ba2.set_bit(2)
        ba2.set_bit(5)
        exp = '00000110'

        self.assertEqual(exp, (ba1 ^ ba2).to_string())

    def test_xor_operation_with_not_equal_size_arrays(self):
        ba1 = BitArray(8)
        ba1.set_bit(5)
        ba1.set_bit(3)
        ba2 = BitArray(18)
        ba2.set_bit(5)
        ba2.set_bit(17)
        exp = '000000100000000000001000'

        self.assertEqual(exp, (ba1 ^ ba2).to_string())

    def test_inversion(self):
        bit_array = BitArray(8)
        bit_array.set_bit(0)
        bit_array.set_bit(2)
        bit_array.set_bit(4)
        exp = '11101010'

        self.assertEqual(exp, (~bit_array).to_string())

    def test_eq_operation_with_not_bit_array(self):
        with self.assertRaises(TypeError):
            BitArray(5) == [0, 0, 0, 0, 0]

    def test_eq_operation_with_equal_size_arrays(self):
        ba1 = BitArray(8)
        ba1.set_bit(0)
        ba2 = BitArray(8)
        ba2.set_bit(0)

        self.assertTrue(ba1 == ba2)

    def test_eq_operation_with_not_equal_size_arrays(self):
        ba1 = BitArray(12)
        ba1.set_bit(0)
        ba2 = BitArray(8)
        ba1.set_bit(0)

        self.assertFalse(ba1 == ba2)

    def test_ne_operation_with_not_bit_array(self):
        with self.assertRaises(TypeError):
            BitArray(5) != [0, 0, 0, 0, 0]

    def test_ne_operation(self):
        ba1 = BitArray(8)
        ba1.set_bit(0)
        ba2 = BitArray(8)

        self.assertTrue(ba1 != ba2)
