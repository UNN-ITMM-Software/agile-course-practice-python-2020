class ILogger(object):

    def __init__(self):
        self.logs = []

    def get_logs(self):
        return self.logs

    def log(self, message):
        self.logs.append(message)

    def get_last_messages(self, count):
        return self.logs[-count:]
