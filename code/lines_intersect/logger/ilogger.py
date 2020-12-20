import abc


class ILogger(object, metaclass=abc.ABCMeta):

    @abc.abstractclassmethod
    def get_logs(self, num=0):
        raise NotImplementedError

    @abc.abstractclassmethod
    def log(self, message):
        raise NotImplementedError
