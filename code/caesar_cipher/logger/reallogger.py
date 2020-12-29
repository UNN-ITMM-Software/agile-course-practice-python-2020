import logging

from caesar_cipher.logger.ilogger import ILogger


class RealLogger(ILogger):
    def __init__(self):
        super(RealLogger, self).__init__()
        logging.basicConfig(filename='../../tmp/caesar_cipher.log', level=logging.INFO)

    def log(self, message):
        super(RealLogger, self).log(message)
        logging.info(message)
