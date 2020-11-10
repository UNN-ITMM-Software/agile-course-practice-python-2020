import unittest

from vigenere_cipher.model.vigenere_cipher import VigenereCipher


class TestVigenereCipher(unittest.TestCase):
    def test_init(self):
        cipher = VigenereCipher()
        self.assertTrue(isinstance(cipher, VigenereCipher))
