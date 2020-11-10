import unittest

from vigenere_cipher.model.vigenere_cipher import VigenereCipher


class TestVigenereCipher(unittest.TestCase):
    def test_init(self):
        cipher = VigenereCipher()
        self.assertTrue(isinstance(cipher, VigenereCipher))

    def test_key_good(self):
        key = "amo"
        cipher = VigenereCipher(key)
        self.assertEqual(key, cipher.key)

    def test_key_to_lower(self):
        key = "AmO"
        cipher = VigenereCipher(key)
        self.assertEqual(key.lower(), cipher.key)

    def test_key_remove_bad_characters(self):
        key = "A m1oЪ*"
        res = "amo"
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
