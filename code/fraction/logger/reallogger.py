import logging

from fraction.logger.ilogger import ILogger


class RealLogger(ILogger):
    def __init__(self):
        super(RealLogger, self).__init__()
        logging.basicConfig(filename='myapp.log', level=logging.INFO)

    def log(self, message):
        self.log_messages.append(message)
        logging.info(message)
