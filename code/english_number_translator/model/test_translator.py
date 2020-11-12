import unittest

from model.translator import Translator


class TestTranslator(unittest.TestCase):

    def test_can_create_class_object(self):
        Translator()
