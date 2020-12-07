from caesar_cipher.model.caesar_cipher import CaesarCipher


class CaesarCipherViewModel:
    def __init__(self):
        self.offset = 0
        self.input_text = ''
        self.output_text = ''
    
    def set_offset(self, value):
        self.offset = int(value)
    
    def set_input_text(self, value):
        self.input_text = value
    
    def get_offset(self):
        return self.offset
    
    def get_input_text(self):
        return self.input_text
    
    def get_output_text(self):
        return self.output_text
    
    def encipher(self):
        cipher = CaesarCipher(self.offset)
        self.output_text = cipher.encode(self.input_text)
    
    def decipher(self):
        cipher = CaesarCipher(self.offset)
        self.output_text = cipher.decode(self.input_text)
