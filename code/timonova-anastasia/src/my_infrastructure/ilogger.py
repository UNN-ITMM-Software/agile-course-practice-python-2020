class ILogger(object):

    def __init__(self):
        self.logs_list = []

    def get_logs_list(self):
        return self.logs_list

    def append_message_to_logs_list(self, message):
        self.logs_list.append(message)

    def get_last_messages_from_logs_list(self, count):
        return self.logs_list[-count:]
