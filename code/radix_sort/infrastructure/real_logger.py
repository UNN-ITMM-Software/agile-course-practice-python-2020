import logging

from radix_sort.infrastructure.ilogger import ILogger


class RealLogger(ILogger):
    def __init__(self):
        super(RealLogger, self).__init__()
        self.logger = logging.getLogger('radix')
        self.logger.setLevel(logging.INFO)
        for handler in self.logger.handlers[:]:
            self.logger.removeHandler(handler)

        log_filename = 'tmp/radix.log'
        fh = logging.FileHandler(log_filename)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

    def log(self, message):
        self.logs.append(message)
        self.logger.info(message)
