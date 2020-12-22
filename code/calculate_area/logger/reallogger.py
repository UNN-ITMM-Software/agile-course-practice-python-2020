import logging
from calculate_area.logger.ilogger import ILogger


class RealLogger(ILogger):
    def __init__(self):
        super(RealLogger, self).__init__()
        logging.basicConfig(filename='../../tmp/calc_area.log', level=logging.INFO)

    def log(self, message):
        self.log_messages.append(message)
        logging.info(message)
