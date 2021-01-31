import unittest

from caesar_cipher.logger.fakelogger import FakeLogger
from caesar_cipher.logger.reallogger import RealLogger
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


class TestViewModelFakeLogging(unittest.TestCase):
    def setUp(self):
        self.view_model = CaesarCipherViewModel(FakeLogger())

    def test_logging_init(self):
        self.assertEqual('Welcome!', self.view_model.logger.get_last_message())

    def test_logging_offset(self):
        self.view_model.set_offset(2)
        self.assertEqual('Offset: 2', self.view_model.logger.get_last_message())

    def test_logging_input_text(self):
        self.view_model.set_input_text("abcd")
        self.assertEqual('Input text: abcd', self.view_model.logger.get_last_message())

    def test_logging_encipher(self):
        self.view_model.set_offset(1)
        self.view_model.set_input_text("abcd")
        self.view_model.encipher()
        self.assertEqual(['Welcome!', 'Offset: 1', 'Input text: abcd', 'Encipher', 'Encipher text: bcde'],
                         self.view_model.logger.get_log_messages())

    def test_logging_decipher(self):
        self.view_model.set_offset(1)
        self.view_model.set_input_text("bcde")
        self.view_model.decipher()
        self.assertEqual(['Welcome!', 'Offset: 1', 'Input text: bcde', 'Decipher', 'Decipher text: abcd'],
                         self.view_model.logger.get_log_messages())


class TestViewModelRealLogging(TestViewModelFakeLogging):
    def setUp(self):
        self.view_model = CaesarCipherViewModel(RealLogger())
