from mortgage_calculator.logger.ilogger import ILogger
from pathlib import Path
import re


class Logger(ILogger):
    def __init__(self, filename="tmp/mortgage_calculator.log"):
        super().__init__()
        self._create_dir(filename)
        self.log_filename = filename
        open(filename, 'w').close()

    def _create_dir(self, filename):
        if filename[-4:] != ".log":
            raise AttributeError("Incorrect logger filename.")
        Path(re.sub(r"/[^/]+.log", "", filename)).mkdir(parents=True, exist_ok=True)

    def log(self, string):
        with open(self.log_filename, "a+") as log_file:
            log_file.write(string + "\n")
            log_file.flush()

    def get_log(self):
        with open(self.log_filename, "r") as log_file:
            content = "".join(log_file.readlines()).rstrip()
        return content

    def clear(self):
        open(self.log_filename, 'w').close()
