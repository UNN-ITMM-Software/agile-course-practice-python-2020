import logging


from ShutinaSvetlana.logger.ilogger import ILogger


class RealLogger(ILogger):
    def __init__(self):
        super(RealLogger, self).__init__()
        logging.basicConfig(filename='../logger/logs.log', level=logging.INFO)

    def log(self, message):
        self.messages.append(message)
        logging.info(message)
