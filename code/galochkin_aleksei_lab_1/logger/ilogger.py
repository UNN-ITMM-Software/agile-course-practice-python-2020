class ILogger:

    def __init__(self):
        self.messages = []

    def get_messages(self):
        return self.messages

    def log(self, message):
        self.messages.append(message)

    def get_last_message(self):
        return self.messages[-1]
