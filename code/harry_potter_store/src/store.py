class Store:
    book_types = ["1", "2", "3", "4", "5"]

    def __init__(self):
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
            if len(to_buy_books) == 4:
                price += 32 * 0.80
            if len(to_buy_books) == 3:
                price += 24 * 0.90
            if len(to_buy_books) == 2:
                price += 16 * 0.95
            to_buy_books = self._decrement(to_buy_books)

        count = sum(to_buy_books.values())
        return price + 8 * count
