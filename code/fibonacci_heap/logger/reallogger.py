import logging
import os

from fibonacci_heap.logger.ilogger import ILogger


class RealLogger(ILogger):
    def __init__(self):
        super(RealLogger, self).__init__()
        logging.basicConfig(filename=os.path.join('..', 'logger', 'info.log'),
                            level=logging.INFO)

    def log(self, message):
        self.log_messages.append(message)
        logging.info(message)

    def error(self, message):
        self.log_messages.append(message)
        logging.error(message)
