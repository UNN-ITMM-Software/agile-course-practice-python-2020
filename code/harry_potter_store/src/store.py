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

    def _discount_wrapper(self, number, discount):
        return lambda to_buy_books, price: \
            self._discount(to_buy_books, price, number, discount)

    def _discount(self, to_buy_books, price, number, discount):
        if len(to_buy_books) >= number:
            price += number * self.book_price * (1 - discount)
            to_buy_books = self._decrement(to_buy_books, number)
        return to_buy_books, price

    """
    algorithm logic: we have discounts for several books. We give names for it: 3, 2, 1
    and we are doing a full sort out
    we calculate a price just with discount for 3 books
    next for 2 books
    next for 1 books
    and next we calculate a price with discount for 3, 2, 1 books
    next for 2, 1 books
    """
    def get_price(self, to_buy_books: Dict[str, int]) -> float:
        """
        to_buy_books - dictionary from book type and book amount
        key of dict -- book type
        value of dict -- book amount
        """
        self._validate(to_buy_books)
        to_buy_books = {k: v for k, v in sorted(to_buy_books.items(), key=lambda item: item[1], reverse=True)}
        discounts = {2: self._discount_wrapper(2, 0.05), 3: self._discount_wrapper(3, 0.1),
                     4: self._discount_wrapper(4, 0.2), 5: self._discount_wrapper(5, 0.25)}
        min_price = self.book_price * sum(to_buy_books.values())
        for i in range(len(discounts)):
            ith_discount_as_list = list(discounts.items())[i]
            ith_discount_as_dict = {ith_discount_as_list[0]: ith_discount_as_list[1]}
            min_price = min(min_price,
                            self._get_price(to_buy_books, ith_discount_as_dict))
            if i > 1:
                min_price = min(min_price,
                                self._get_price(to_buy_books,
                                                dict(list(discounts.items())[0:i + 1][::-1])))
        return min_price

    def _get_price(self, to_buy_books: Dict[str, int],
                   discount_funcs: dict) -> float:
        """
        to_buy_books - dictionary from book type and book amount
        key of dict -- book type
        value of dict -- book amount
        discount_funcs - functions for calculate discount
        """
        to_buy_books = deepcopy(to_buy_books)
        price = 0
        for number, discount_func in discount_funcs.items():
            while len(to_buy_books) >= number:
                to_buy_books, price = discount_func(to_buy_books, price)

        count = sum(to_buy_books.values())
        return price + self.book_price * count
