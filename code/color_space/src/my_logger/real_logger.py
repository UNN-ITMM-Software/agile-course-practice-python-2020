from ilogger import ILogger


class Logger(ILogger):
    def __init__(self, filename="one_more.log"):
        self.log_filename = filename
        open(filename, 'w').close()

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
