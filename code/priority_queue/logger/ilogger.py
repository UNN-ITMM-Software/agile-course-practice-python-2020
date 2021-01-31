
class ILogger(object):
    def __init__(self):
        self.log_msgs = []

    def get_log_messages(self):
        return self.log_msgs

    def log(self, message):
        self.log_msgs.append(message)

    def get_last_msg(self):
        return self.log_msgs[-1]
