from harry_potter_store.src.store import Store
from harry_potter_store.logger.fakelogger import FakeLogger


class HPStoreViewModel:
    def __init__(self, logger=FakeLogger()):
        self.logger = logger
        self.store = Store()
        self.message_text = ''
        self.amount = {}
        self.price = 0.0
        self.result_message = 'Total Price: 0.0'
        self.logger.log('Welcome to Harry Potter Store')

    def click_calculate(self):
        try:
            self.price = self.store.get_price(self.amount)
            self.result_message = 'Total Price: %.1f' % self.price
            self.logger.log('Correct price calculation!')
        except ValueError as e:
            self.price = 0
            self.result_message = 'ERROR: Book amount should be a positive value'
            self.logger.log('Can\'t calculate price. {}'.format(self.result_message))

    def set_books_amount(self, amount_dict):
        self.amount = {}
        for idx, val in amount_dict.items():
            try:
                value = int(val)
                self.amount[str(idx + 1)] = value
                self.logger.log('For book #{} set amount {}'.format(idx, value))
            except:
                pass

    def get_books_amount(self):
        return {(int(k)-1): v for k, v in self.amount.items()}

    def get_result_message(self):
        return self.result_message

    def get_price(self):
        return self.price
