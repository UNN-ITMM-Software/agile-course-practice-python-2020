import logging

from line_and_plane_intersection.logger.ilogger import ILogger


class RealLogger(ILogger):
    def __init__(self):
        super(RealLogger, self).__init__()
        logging.basicConfig(filename='../../tmp/intersection.log', level=logging.INFO)

    def log(self, message):
        self.log_messages.append(message)
        logging.info(message)
