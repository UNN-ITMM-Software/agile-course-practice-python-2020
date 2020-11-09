from copy import deepcopy
from typing import Dict


class Store:
    book_types = ["1", "2", "3", "4", "5"]

    def __init__(self, book_price=8):
        self.book_price = book_price
        pass

    def _validate(self, to_buy_books: Dict[str, int]):
        for book_type, amount in to_buy_books.items():
            if book_type not in Store.book_types:
                raise ValueError("Book type %s must be in %s".format(book_type, Store.book_types))
            if amount <= 0:
                raise ValueError("Book amount %s for type %s must be > 0".format(amount, book_type))

    def _clean(self, to_buy_books: Dict[str, int]) -> dict:
        return dict(filter(lambda item: item[1] > 0 and item[0] in Store.book_types, to_buy_books.items()))

    def _decrement(self, to_buy_books: Dict[str, int], count: int) -> dict:
        first_part = {book: amount - 1 for book, amount in list(to_buy_books.items())[:count]}
        second_part = dict(list(to_buy_books.items())[count:])
        first_part.update(second_part)
        return self._clean(first_part)

    def _discount_2(self, to_buy_books, price, predicate):
        if predicate(len(to_buy_books), 2):
            price += 2 * self.book_price * 0.95
            to_buy_books = self._decrement(to_buy_books, 2)
        return to_buy_books, price

    def _discount_3(self, to_buy_books, price, predicate):
        if predicate(len(to_buy_books), 3):
            price += 3 * self.book_price * 0.90
            to_buy_books = self._decrement(to_buy_books, 3)
        return to_buy_books, price

    def _discount_4(self, to_buy_books, price, predicate):
        if predicate(len(to_buy_books), 4):
            price += 4 * self.book_price * 0.80
            to_buy_books = self._decrement(to_buy_books, 4)
        return to_buy_books, price

    def _discount_5(self, to_buy_books, price, predicate):
        if predicate(len(to_buy_books), 5):
            price += 5 * self.book_price * 0.75
            to_buy_books = self._decrement(to_buy_books, 5)
        return to_buy_books, price

    """
    to_buy_books - dictionary from book type and book amount
    key of dict -- book type
    value of dict -- book amount
    """

    def get_price(self, to_buy_books: Dict[str, int]) -> float:
        self._validate(to_buy_books)
        discounts = [self._discount_5, self._discount_4, self._discount_3, self._discount_2]
        prices = []
        for i in range(len(discounts)):
            prices.append(self._get_price(to_buy_books,
                                          [discounts[i]], len(discounts) - i, lambda x, y: x >= y))
            prices.append(self._get_price(to_buy_books,
                                          discounts[0:i + 1], len(discounts) - i, lambda x, y: x == y))
        return min(prices)

    def _get_price(self, to_buy_books: Dict[str, int],
                   discount_funcs: list, min_value: int, predicate) -> float:
        to_buy_books = deepcopy(to_buy_books)
        price = 0
        while len(to_buy_books) > min_value:
            for discount_func in discount_funcs:
                to_buy_books, price = discount_func(to_buy_books, price, predicate)

        count = sum(to_buy_books.values())
        return price + self.book_price * count
