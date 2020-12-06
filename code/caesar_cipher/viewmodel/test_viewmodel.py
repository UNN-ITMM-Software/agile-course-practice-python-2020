import unittest

from caesar_cipher.viewmodel.viewmodel import CaesarCipherViewModel


class TestCaesarCipherViewModel(unittest.TestCase):
    def test_init_offset(self):
        view_model = CaesarCipherViewModel()
        view_model.set_offset(5)
        self.assertEqual(view_model.get_offset(), 5)
    
    def test_init_input_text(self):
        view_model = CaesarCipherViewModel()
        view_model.set_input_text("abcd")
        self.assertEqual(view_model.get_input_text(), "abcd")
    
    def test_encipher(self):
        view_model = CaesarCipherViewModel()
        view_model.set_offset(1)
        view_model.set_input_text("abcd")
        view_model.encipher()
        self.assertEqual(view_model.get_output_text(), "bcde")
    
    def test_decipher(self):
        view_model = CaesarCipherViewModel()
        view_model.set_offset(1)
        view_model.set_input_text("bcde")
        view_model.decipher()
        self.assertEqual(view_model.get_output_text(), "abcd")
    
    def test_decipher_encipher(self):
        view_model = CaesarCipherViewModel()
        view_model.set_offset(1)
        view_model.set_input_text("abcd")
        view_model.encipher()
        view_model.set_input_text(view_model.get_output_text())
        view_model.decipher()
        self.assertEqual(view_model.get_output_text(), "abcd")
