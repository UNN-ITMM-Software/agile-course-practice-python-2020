class ILogger(object):
    # abstractmethod
    def log(self, string):
        raise NotImplementedError

    # abstractmethod
    def get_log(self):
        raise NotImplementedError
