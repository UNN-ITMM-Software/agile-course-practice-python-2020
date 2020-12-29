import logging
import os

from gerasimov_dmitry_lab1.logger.ilogger import ILogger


class RealLogger(ILogger):
    def __init__(self):
        super(RealLogger, self).__init__()
        logging.basicConfig(filename=os.path.join('..', 'logger', 'statistics.log'), level=logging.INFO)

    def log(self, message):
        self.log_messages.append(message)
        logging.info(message)
