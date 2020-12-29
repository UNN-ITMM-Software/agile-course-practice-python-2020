import logging

from galochkin_aleksei_lab_1.logger.ilogger import ILogger


class RealLogger(ILogger):
    def __init__(self):
        super(RealLogger, self).__init__()
        logging.basicConfig(filename='../logs/node.log', level=logging.INFO)

    def log(self, message):
        self.messages.append(message)
        logging.info(message)
