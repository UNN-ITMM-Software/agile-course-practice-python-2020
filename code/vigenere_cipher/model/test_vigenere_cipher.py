import unittest

from vigenere_cipher.model.vigenere_cipher import VigenereCipher


class TestVigenereCipher(unittest.TestCase):
    def test_init(self):
        cipher = VigenereCipher()
        self.assertTrue(isinstance(cipher, VigenereCipher))

    def test_key_good(self):
        key = "amo"
        cipher = VigenereCipher(key)
        self.assertEqual(key.upper(), cipher.key)

    def test_key_to_upper(self):
        key = "BiMo"
        cipher = VigenereCipher(key)
        self.assertEqual(key.upper(), cipher.key)

    def test_key_remove_bad_characters(self):
        key = "A m1oЪ*"
        res = "AMO"
        cipher = VigenereCipher(key)
        self.assertEqual(res, cipher.key)

    def test_key_type_error(self):
        key = 1
        self.assertRaises(TypeError, VigenereCipher, key)

    def test_key_empty(self):
        key = ""
        self.assertRaises(ValueError, VigenereCipher, key)

    def test_key_all_bad_characters(self):
        key = " 1Ъ*"
        self.assertRaises(ValueError, VigenereCipher, key)

    def test_encipher_good(self):
        key = "mo"
        string = "abba"
        res = "MPNO"
        cipher = VigenereCipher(key)
        self.assertEqual(res, cipher.encipher(string))

    def test_encipher_adding_non_letters(self):
        key = "MmO"
        string = "a b b a"
        res = "M N P M"
        cipher = VigenereCipher(key)
        self.assertEqual(res, cipher.encipher(string))

    def test_decipher_good(self):
        key = "cimo"
        string = "anpa"
        res = "YFDM"
        cipher = VigenereCipher(key)
        self.assertEqual(res, cipher.decipher(string))

    def test_decipher_adding_non_letters(self):
        key = "DiMo"
        string = "L M O"
        res = "I E C"
        cipher = VigenereCipher(key)
        self.assertEqual(res, cipher.decipher(string))

    def test_encipher_decipher_good(self):
        key = "amo"
        string = "gmo"
        cipher = VigenereCipher(key)
        self.assertEqual(string.upper(), cipher.decipher(cipher.encipher(string)))

    def test_decipher_encipher_good(self):
        key = "amo"
        string = "F M O"
        cipher = VigenereCipher(key)
        self.assertEqual(string.upper(), cipher.encipher(cipher.decipher(string)))

    def test_i2a_good(self):
        i = 53
        cipher = VigenereCipher()
        res = 'B'
        self.assertEqual(res, cipher.i2a(i))

    def test_i2a_type_error(self):
        i = "EmO"
        cipher = VigenereCipher()
        self.assertRaises(TypeError, cipher.i2a, i)

    def test_a2i_good(self):
        ch = 'B'
        cipher = VigenereCipher()
        res = 1
        self.assertEqual(res, cipher.a2i(ch))

    def test_a2i_type_error(self):
        ch = 1
        cipher = VigenereCipher()
        self.assertRaises(TypeError, cipher.a2i, ch)

    def test_a2i_one_letter(self):
        ch = "amo"
        cipher = VigenereCipher()
        self.assertRaises(ValueError, cipher.a2i, ch)

    def test_a2i_english(self):
        ch = "ф"
        cipher = VigenereCipher()
        self.assertRaises(ValueError, cipher.a2i, ch)

    def test_check_string(self):
        string = 123
        cipher = VigenereCipher()
        self.assertRaises(TypeError, cipher.encipher, string)

    def test_check_key_string(self):
        string = "abba"
        cipher = VigenereCipher()
        cipher.key = 123
        self.assertRaises(TypeError, cipher.encipher, string)

    def test_check_key_empty(self):
        string = "abba"
        cipher = VigenereCipher()
        cipher.key = ""
        self.assertRaises(ValueError, cipher.encipher, string)

    def test_check_key_bad(self):
        string = "abba"
        cipher = VigenereCipher()
        cipher.key = "абба"
        self.assertRaises(ValueError, cipher.encipher, string)
