import logging
from hashmap.logger.ilogger import ILogger


class RealLogger(ILogger):

    def __init__(self):
        super(RealLogger, self).__init__()
        logging.basicConfig(filename='../../tmp/myapp.log', level=logging.INFO)

    def log(self, message):
        super(RealLogger, self).log(message)
        logging.info(message)
