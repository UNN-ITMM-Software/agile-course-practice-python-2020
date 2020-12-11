import unittest
from lcd_digits.model.lcd_symbol import LcdSymbol
from lcd_digits.model.lcd_digits_model import LcdDigitsModel


class TestLcdSymbol(unittest.TestCase):
    def test_can_create(self):
        lcd_symbol_instance = LcdSymbol('0')
        self.assertTrue(isinstance(lcd_symbol_instance, LcdSymbol))

    def test_cant_create_from_empty_str(self):
        with self.assertRaises(ValueError):
            LcdSymbol('')

    def test_cant_create_with_invalid_character_char(self):
        with self.assertRaises(ValueError):
            LcdSymbol('t')

    def test_cant_create_with_invalid_character_neg(self):
        with self.assertRaises(ValueError):
            LcdSymbol('-1')

    def test_equal_wrong_type_error(self):
        lcd_symbol_instance = LcdSymbol('0')
        other_instance = 't'
        with self.assertRaises(TypeError):
            lcd_symbol_instance.equals(other_instance)

    def test_equal(self):
        lcd_symbol_instance = LcdSymbol('2')
        other_instance = LcdSymbol('2')
        self.assertTrue(lcd_symbol_instance.equals(other_instance))

    def test_not_equal(self):
        lcd_symbol_instance = LcdSymbol('3')
        other_instance = LcdSymbol('4')
        self.assertFalse(lcd_symbol_instance.equals(other_instance))


class TestLcdDigitsModel(unittest.TestCase):
    def test_can_create(self):
        lcd_digits_model_instance = LcdDigitsModel('35227')
        self.assertTrue(isinstance(lcd_digits_model_instance, LcdDigitsModel))

    def test_cant_create_from_empty_str(self):
        with self.assertRaises(ValueError):
            LcdDigitsModel('')

    def test_cant_create_with_invalid_character_str(self):
        with self.assertRaises(ValueError):
            LcdDigitsModel('Hello')

    def test_cant_create_with_invalid_character_neg(self):
        with self.assertRaises(ValueError):
            LcdDigitsModel('-152')

    def test_cant_create_with_invalid_character_float(self):
        with self.assertRaises(ValueError):
            LcdDigitsModel('152.55')

    def test_equal_wrong_type_error(self):
        lcd_digits_model_instance = LcdDigitsModel('522')
        other_instance = 'Hello'
        with self.assertRaises(TypeError):
            lcd_digits_model_instance.equals(other_instance)

    def test_equal(self):
        lcd_digits_model_instance = LcdDigitsModel('245')
        other_instance = LcdDigitsModel('245')
        self.assertTrue(lcd_digits_model_instance.equals(other_instance))

    def test_not_equal(self):
        lcd_digits_model_instance = LcdDigitsModel('354')
        other_instance = LcdDigitsModel('35')
        self.assertFalse(lcd_digits_model_instance.equals(other_instance))

    def test_not_concat(self):
        lcd_digits_model_instance = LcdDigitsModel('354')
        other_instance = LcdDigitsModel('35')
        result = lcd_digits_model_instance + other_instance
        self.assertTrue(result.equals(LcdDigitsModel('35435')))
