import logging
import os
import os.path

from lcd_digits.logger.ilogger import ILogger


class RealLogger(ILogger):
    def __init__(self):
        super(RealLogger, self).__init__()
        self.logger = logging.getLogger("lcd_digits.logger.RealLogger")
        self.logger.setLevel(logging.INFO)

        if not os.path.exists("../../tmp/"):
            os.makedirs("../../tmp/")
        fh = logging.FileHandler("../../tmp/digits.log", mode='a', encoding='utf-8')

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)

        self.logger.addHandler(fh)

        self.logger_error = logging.getLogger("lcd_digits.logger.RealLoggerError")
        self.logger_error.setLevel(logging.ERROR)

        fhe = logging.FileHandler("../../tmp/lcd_digits_error.log")
        fhe.setFormatter(formatter)

        self.logger_error.addHandler(fhe)

    def _add_info(self, info_message):
        self.logger.info(info_message)

    def _add_error(self, error_message):
        self.logger.error(error_message)
        self.logger_error.error(error_message)
