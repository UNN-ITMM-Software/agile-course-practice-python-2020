class Store:
    book_types = ["1", "2", "3", "4", "5"]

    def __init__(self):
        pass

    # book_types = ["str_type": int_count]
    def get_price(self, to_buy_books: dict) -> float:
        price = 0
        to_buy_books = dict(filter(lambda item: item[1] > 0, to_buy_books.items()))
        if len(to_buy_books) == 2:
            price += 16*0.95
            to_buy_books = dict(map(lambda item: [item[0], item[1]-1], to_buy_books.items()))

        count = sum(to_buy_books.values())
        return price + 8 * count
