from abc import ABCMeta, abstractmethod


class ILogger(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def log(self, string):
        pass

    @abstractmethod
    def get_log(self):
        pass
