class ILogger:

    def __init__(self):
        self.logs = []

    def get_logs(self):
        return self.logs

    def log(self, msg):
        self.logs.append(msg)

    def get_last_log(self):
        return self.logs[-1]
