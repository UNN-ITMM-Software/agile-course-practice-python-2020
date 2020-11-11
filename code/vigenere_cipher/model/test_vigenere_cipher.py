import unittest

from vigenere_cipher.model.vigenere_cipher import VigenereCipher


class TestVigenereCipher(unittest.TestCase):
    def test_init(self):
        cipher = VigenereCipher()
        self.assertTrue(isinstance(cipher, VigenereCipher))

    def test_key_good(self):
        key = "AMO"
        cipher = VigenereCipher(key)
        self.assertEqual(key, cipher.key)

    def test_key_to_upper(self):
        key = "aMo"
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
        key = "amo"
        string = "abba"
        res = "ANPA"
        cipher = VigenereCipher(key)
        self.assertEqual(res, cipher.encipher(string))

    def test_encipher_adding_non_letters(self):
        key = "amo"
        string = "a b b a"
        res = "A N P A"
        cipher = VigenereCipher(key)
        self.assertEqual(res, cipher.encipher(string))

    def test_i2a_good(self):
        i = 53
        cipher = VigenereCipher()
        res = 'B'
        self.assertEqual(res, cipher.i2a(i))

    def test_i2a_type_error(self):
        i = "amo"
        cipher = VigenereCipher()
        self.assertRaises(TypeError, cipher.i2a, i)

    def test_i2a_value_error(self):
        i = -5
        cipher = VigenereCipher()
        self.assertRaises(ValueError, cipher.i2a, i)

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
