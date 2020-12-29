
class ILogger(object):
    def __init__(self):
        self.log_messages = []

    def get_log_messages(self):
        return self.log_messages

    def log(self, message):
        self.log_messages.append(message)

    def get_last_message(self):
        return self.log_messages[-1]
