import os
import logging

from segment_tree.logger.ilogger import ILogger


class RealLogger(ILogger):
    def __init__(self, log_file_path=None):
        super(RealLogger, self).__init__()
        if log_file_path is None:
            log_file_path = os.path.join('..', '..', '..', 'tmp', 'segment_tree.log')
        logging.basicConfig(filename=log_file_path, level=logging.INFO)

    def log(self, message):
        self.log_messages.append(message)
        logging.info(message)
