from lcd_digits.logger.log import Log
from lcd_digits.logger.log import Log_types


class ILogger(object):

    def __init__(self):
        self.logs = []

    def get_log_messages(self):
        messages = []
        for log in self.logs:
            messages.append(log.get_message())
        return messages

    def _add_info(self, info_message):
        pass

    def _add_error(self, error_message):
        pass

    def add_log(self, log_message, log_type):
        self.logs.append(Log(log_message, log_type))
        if log_type == Log_types.Info:
            self._add_info(log_message)
        elif log_type == Log_types.Error:
            self._add_error(log_message)
        else:
            raise ValueError('Value error: no type found')

    def get_last_log_message(self):
        return self.logs[-1].get_message()
