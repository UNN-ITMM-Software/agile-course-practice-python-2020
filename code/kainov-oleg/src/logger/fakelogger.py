from logger.ilogger import ILogger


class FakeLogger(ILogger):

    def log(self, message):
        self.log_messages.append(message)
