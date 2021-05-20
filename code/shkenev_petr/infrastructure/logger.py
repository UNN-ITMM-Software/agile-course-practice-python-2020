import logging

from ..logger.ilogger import ILogger


class Logger(ILogger):
    def __init__(self):
        self.messages = []
        logging.basicConfig(filename='queue.log', level=logging.INFO)

    def get_messages_list(self):
        return self.messages

    def log(self, message):
        self.messages.append(message)
        logging.info(message)
 