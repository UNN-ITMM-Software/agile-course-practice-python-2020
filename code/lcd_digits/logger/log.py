from enum import Enum

Log_types = Enum('Types', 'Unknown Info Error')


class Log:
    def __init__(self, log_message, log_type):
        self.__log_message = log_message
        self.__log_type = log_type

    def get_message(self):
        return self.__log_message

    def get_type(self):
        return self.__log_type
