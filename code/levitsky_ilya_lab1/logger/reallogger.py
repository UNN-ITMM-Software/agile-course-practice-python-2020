import logging
import os

from levitsky_ilya_lab1.logger.ilogger import ILogger


class RealLogger(ILogger):
    def __init__(self):
        super(RealLogger, self).__init__()
        logging.basicConfig(filename=os.path.join('..', 'logger', 'calculate_volume.log'), level=logging.INFO)

    def log(self, message):
        self.log_messages.append(message)
        logging.info(message)
