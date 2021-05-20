from .ilogger import ILogger


class Logger(ILogger):
    def __init__(self):
        self.messages = []

    def get_messages_list(self):
        return self.messages

    def log(self, message):
        self.messages.append(message)
