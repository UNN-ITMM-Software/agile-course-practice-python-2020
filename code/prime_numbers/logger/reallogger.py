import logging

from prime_numbers.logger.ilogger import ILogger


class RealLogger(ILogger):
    def __init__(self):
        super(RealLogger, self).__init__()
        logging.basicConfig(filename='../logger/prime_numbers.log', level=logging.INFO)

    def log(self, message):
        self.log_messages.append(message)
        logging.info(message)
