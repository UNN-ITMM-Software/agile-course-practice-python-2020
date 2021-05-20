class ILogger(object):
    def __init__(self):
        pass

    def get_messages_list(self):
        raise NotImplementedError

    def log(self, message):
        raise NotImplementedError
