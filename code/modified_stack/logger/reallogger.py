import logging
import os

from modified_stack.logger.ilogger import ILogger

TEST_FILEPATH = '../../tmp/'
LOG_FILEPATH = '../../tmp/modified_stack.log'


class RealLogger(ILogger):
    def __init__(self):
        super(RealLogger, self).__init__()
        os.makedirs(TEST_FILEPATH, exist_ok=True)
        logging.basicConfig(filename=LOG_FILEPATH, level=logging.INFO)

    def log(self, message):
        self.log_messages.append(message)
        logging.info(message)
