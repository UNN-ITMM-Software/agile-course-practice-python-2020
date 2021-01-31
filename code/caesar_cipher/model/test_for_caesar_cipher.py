import unittest

from caesar_cipher.model.caesar_cipher import CaesarCipher


class CaesarCipherTests(unittest.TestCase):

    def simple_offset_constructor_test(self):
        actual = CaesarCipher(5)
        self.assertTrue(actual.offset == 5)

    def overflow_offset_constructor_test(self):
        actual = CaesarCipher(31)
        self.assertTrue(actual.offset == 5)

    def reverse_offset_constructor_test(self):
        actual = CaesarCipher(-5)
        self.assertTrue(actual.offset == 21)

    def none_offset_constructor_test(self):
        actual = CaesarCipher(0)
        self.assertTrue(actual.offset == 0)

    def simple_char_encode_test(self):
        actual = CaesarCipher(10)
        self.assertTrue(actual.encode("a") == "k")

    def simple_char_with_overflow_encode_test(self):
        actual = CaesarCipher(36)
        self.assertTrue(actual.encode("a") == "k")

    def simple_char_with_reverse_encode_test(self):
        actual = CaesarCipher(-16)
        self.assertTrue(actual.encode("a") == "k")

    def simple_message_encode_test(self):
        actual = CaesarCipher(1)
        self.assertTrue(actual.encode("abcd") == "bcde")

    def simple_message_reverse_encode_test(self):
        actual = CaesarCipher(-1)
        self.assertTrue(actual.encode("bcde") == "abcd")

    def message_encode_test_offset_15(self):
        actual = CaesarCipher(15)
        self.assertTrue(actual.encode("this is a simple message") == "iwxh xh p hxbeat bthhpvt")

    def message_encode_test_offset_7(self):
        actual = CaesarCipher(7)
        self.assertTrue(actual.encode("this is a simple message") == "aopz pz h zptwsl tlzzhnl")

    def message_decode_after_encode_test(self):
        message = "this is a simple message"
        actual = CaesarCipher(63)
        self.assertTrue(actual.decode(actual.encode(message)) == message)

    def simple_upeer_char_encode_test(self):
        actual = CaesarCipher(10)
        self.assertTrue(actual.encode("A") == "K")

    def upper_message_encode_test(self):
        actual = CaesarCipher(7)
        self.assertTrue(actual.encode("This is a simple Message") == "Aopz pz h zptwsl Tlzzhnl")

    def incorrect_char_encode_test(self):
        actual = CaesarCipher(10)
        self.assertTrue(actual.encode("!") == "!")

    def upper_message_with_incorrect_letters_encode_test(self):
        actual = CaesarCipher(7)
        self.assertTrue(actual.encode("This is a 'simple' Message!") == "Aopz pz h 'zptwsl' Tlzzhnl!")

    def complex_message_decode_after_encode_test(self):
        message = "whHU6DnQhGD8STBpua5!t0BVnE51EqCORsRqKCFSINSH44?GsGZ2Pgo7imir0Z"
        actual = CaesarCipher(63)
        self.assertTrue(actual.decode(actual.encode(message)) == message)
