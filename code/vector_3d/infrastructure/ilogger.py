class ILogger(object):

    def __init__(self):
        self.logs = []

    def get_log_messages(self):
        return self.logs

    def log(self, message):
        self.logs.append(message)

    def get_last_message(self):
        return self.logs[-1]

    def get_several_messages(self, count):
        return self.logs[-count:]
