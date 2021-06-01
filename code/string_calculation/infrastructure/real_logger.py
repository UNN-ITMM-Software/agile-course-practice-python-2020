import logging
import os

from infrastructure.ilogger import ILogger


class RealLogger(ILogger):
    def __init__(self):
        super(RealLogger, self).__init__()
        self.logger = logging.getLogger('formula_calculation')
        self.logger.setLevel(logging.INFO)
        for handler in self.logger.handlers[:]:
            self.logger.removeHandler(handler)

        log_filename = 'tmp/formula_calculation.log'
        os.makedirs('tmp', exist_ok=True)
        if not os.path.exists(log_filename):
            open(log_filename, "x")
        fh = logging.FileHandler(log_filename)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

    def log(self, message):
        self.logs.append(message)
        self.logger.info(message)
