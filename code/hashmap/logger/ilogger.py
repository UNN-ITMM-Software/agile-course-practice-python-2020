class ILogger:

    def __init__(self):
        self.log_messages = []

    def get_log_messages(self):
        return self.log_messages

    def log(self, message):
        self.log_messages.append(message)

    def get_last_message(self):
        if len(self.log_messages) > 0:
            return self.log_messages[-1]
        return None
