class ILogger(object):

    def __init__(self):
        self.logs_list = []

    def get_log_messages(self):
        return self.logs_list

    def append_messages_in_logs_list(self, message):
        self.logs_list.append(message)

    def get_last_message_from_logs_list(self):
        return self.logs_list[-1]
