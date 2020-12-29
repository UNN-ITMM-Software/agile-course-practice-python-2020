class ILogger:

    def __init__(self):
        self.logs = []

    def get_logs(self):
        return self.messages

    def log(self, log):
        self.logs.append(log)

    def get_last_log(self):
        return self.logs[-1]
