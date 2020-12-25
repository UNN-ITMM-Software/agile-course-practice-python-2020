import logging

from float_vector_metrics.logger.ilogger import ILogger


class RealLogger(ILogger):
    def __init__(self):
        super(RealLogger, self).__init__()
        logging.basicConfig(filename='../../tmp/float_vector_metrics.log', level=logging.INFO)

    def log(self, message):
        self.log_messages.append(message)
        logging.info(message)
