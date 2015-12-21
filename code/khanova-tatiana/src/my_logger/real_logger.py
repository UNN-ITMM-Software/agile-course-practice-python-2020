from ilogger import ILogger


class Logger(ILogger):
    def __init__(self, filename="log.txt"):
        self.log_filename = filename
        open(filename, 'w').close()
        self.log_file = open(self.log_filename, "r+")

    def log(self, string):
        self.log_file.write(string + "\n")
        self.log_file.flush()

    def get_log(self):
        self.log_file.seek(0)
        return "".join(self.log_file.readlines()).rstrip()

    def clear(self):
        self.log_file.truncate(0)

    def __del__(self):
        self.log_file.close()
