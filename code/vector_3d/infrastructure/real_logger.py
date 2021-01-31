import logging

from vector_3d.infrastructure.ilogger import ILogger


class RealLogger(ILogger):
    def __init__(self):
        super(RealLogger, self).__init__()
        logging.basicConfig(filename='tmp/vector_3d.log', level=logging.INFO)

    def log(self, message):
        self.logs.append(message)
        logging.info(message)
