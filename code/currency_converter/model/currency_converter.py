
class CurrencyConverter:
    rates = {"RUB_to_USD": 0.013,
             "RUB_to_EUR": 0.011,
             "EUR_to_USD": 1.19,
             "EUR_to_RUB": 91.95,
             "USD_to_EUR": 0.84,
             "USD_to_RUB": 77.43,
             }

    def __init__(self, value=1):
        self.value = value

    def convert(self, src, dest, count=None):
        pass
