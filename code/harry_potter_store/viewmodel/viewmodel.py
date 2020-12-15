from harry_potter_store.src.store import Store


class HPStoreViewModel:
    def __init__(self):
        self.store = Store()
        self.message_text = ''
        self.amount = {}
        self.price = 0.0
        self.result_message = 'Total Price: 0.0'

    def click_calculate(self):
        try:
            self.price = self.store.get_price(self.amount)
            self.result_message = 'Total Price: %.1f' % self.price
        except ValueError as e:
            self.price = 0
            self.result_message = 'ERROR: Book amount should be a positive value'

    def set_books_amount(self, amount_dict):
        self.amount = {}
        for idx, val in amount_dict.items():
            try:
                value = int(val)
                self.amount[str(idx + 1)] = value
            except:
                pass

    def get_books_amount(self):
        return {(int(k)-1): v for k, v in self.amount.items()}

    def get_result_message(self):
        return self.result_message

    def get_price(self):
        return self.price
