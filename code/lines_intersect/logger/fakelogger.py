from lines_intersect.logger.ilogger import ILogger


class FakeLogger(ILogger):
    
    def __init__(self):
        self.logs = []

    def get_logs(self, num=0):
        return self.logs[(-1) * num :]

    def log(self, message):
        self.logs.append(message)
