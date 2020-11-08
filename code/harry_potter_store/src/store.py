class Store:
    book_types = ["1", "2", "3", "4", "5"]

    def __init__(self):
        pass

    def get_price(self, book_types: list) -> int:
        return 8 * len(book_types)
