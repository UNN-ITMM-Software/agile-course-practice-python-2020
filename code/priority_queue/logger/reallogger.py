import logging

from priority_queue.logger.ilogger import ILogger


class RealLogger(ILogger):
    def __init__(self):
        super(RealLogger, self).__init__()
        logging.basicConfig(filename='priority_queue.log', level=logging.INFO)

    def log(self, message):
        self.log_msgs.append(message)
        logging.info(message)
