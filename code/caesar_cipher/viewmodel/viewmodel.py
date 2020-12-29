from caesar_cipher.model.caesar_cipher import CaesarCipher
from caesar_cipher.logger.reallogger import RealLogger


class CaesarCipherViewModel:
    def __init__(self, logger=RealLogger()):
        self.logger = logger
        self.offset = 0
        self.input_text = ''
        self.output_text = ''
        self.logger.log('Welcome!')

    def set_offset(self, value):
        self.offset = int(value)
        self.logger.log('Offset: %s' % self.offset)

    def set_input_text(self, value):
        self.input_text = value
        self.logger.log('Input text: %s' % self.input_text)

    def get_offset(self):
        return self.offset

    def get_input_text(self):
        return self.input_text

    def get_output_text(self):
        return self.output_text

    def encipher(self):
        self.logger.log('Encipher')
        cipher = CaesarCipher(self.offset)
        self.output_text = cipher.encode(self.input_text)
        self.logger.log('Encipher text: %s' % self.output_text)

    def decipher(self):
        self.logger.log('Decipher')
        cipher = CaesarCipher(self.offset)
        self.output_text = cipher.decode(self.input_text)
        self.logger.log('Decipher text: %s' % self.output_text)
