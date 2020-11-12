class Range:
    def __init__(self, begin_value, end_value):
        if begin_value > end_value:
            raise ValueError
