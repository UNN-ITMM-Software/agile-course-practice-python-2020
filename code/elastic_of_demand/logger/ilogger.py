class ILogger(object):

    def __init__(self):
        self.logs = []

    def get_logs(self, num=0):
        return self.logs[(-1) * num:]

    def log(self, message):
        self.logs.append(message)