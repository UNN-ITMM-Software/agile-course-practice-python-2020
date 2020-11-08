class Store:
    book_types = ["1", "2", "3", "4", "5"]

    def __init__(self, book_price=8):
        self.book_price = book_price
        pass

    def _clean(self, to_buy_books: dict) -> dict:
        return dict(filter(lambda item: item[1] > 0 and item[0] in Store.book_types, to_buy_books.items()))

    def _decrement(self, to_buy_books: dict) -> dict:
        return self._clean(dict(map(lambda i: [i[0], i[1] - 1], to_buy_books.items())))

    # book_types = {"str_type": int_count}
    def get_price(self, to_buy_books: dict) -> float:
        price = 0
        to_buy_books = self._clean(to_buy_books)
        while len(to_buy_books) > 1:
            if len(to_buy_books) == 5:
                price += 5*self.book_price * 0.75
                to_buy_books = self._decrement(to_buy_books)
            if len(to_buy_books) == 4:
                price += 4*self.book_price * 0.80
                to_buy_books = self._decrement(to_buy_books)
            if len(to_buy_books) == 3:
                price += 3*self.book_price * 0.90
                to_buy_books = self._decrement(to_buy_books)
            if len(to_buy_books) == 2:
                price += 2*self.book_price * 0.95
                to_buy_books = self._decrement(to_buy_books)

        count = sum(to_buy_books.values())
        return price + self.book_price * count
