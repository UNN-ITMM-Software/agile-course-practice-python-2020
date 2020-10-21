from .ilogger import ILogger


class MockUpLogger(ILogger):
    def __init__(self):
        self.log_messages = []

    def log(self, message):
        self.log_messages.append(message)

    def get_log(self):
        return "\n".join(self.log_messages)

    def clear(self):
        self.log_messages = []
