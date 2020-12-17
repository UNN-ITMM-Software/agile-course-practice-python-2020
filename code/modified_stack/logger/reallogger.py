import logging

from modified_stack.logger.ilogger import ILogger


class RealLogger(ILogger):
    def __init__(self):
        super(RealLogger, self).__init__()
        logging.basicConfig(filename='tmp/modified_stack.log', level=logging.INFO)

    def log(self, message):
        self.log_messages.append(message)
        logging.info(message)
