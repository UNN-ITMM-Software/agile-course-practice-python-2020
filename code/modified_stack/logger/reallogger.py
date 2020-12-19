import logging
import os

from modified_stack.logger.ilogger import ILogger

MAIN_FILEPATH = '../../tmp/modified_stack.log'
TEST_FILEPATH = '../../../tmp/modified_stack.log'


class RealLogger(ILogger):
    def __init__(self):
        super(RealLogger, self).__init__()
        if os.path.exists(MAIN_FILEPATH):
            filepath = MAIN_FILEPATH
        else:
            filepath = TEST_FILEPATH
        logging.basicConfig(filename=filepath, level=logging.INFO)

    def log(self, message):
        self.log_messages.append(message)
        logging.info(message)
