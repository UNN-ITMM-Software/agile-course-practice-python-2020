import math


class RangeError(Exception):
    pass


class Range(object):
    def __init__(self, start, end):
        if start > end:
            raise RangeError
        self.start = start
        self.end = end

    def __str__(self):
        return 'range({0}, {1})'.format(self.start, self.end)

    def __iter__(self):
        return iter(range(self.start, self.end))


def is_prime(number):
    if number <= 1:
        return False
    for delimeter in range(2, int(math.sqrt(number))+1):
        if number % delimeter == 0:
            return False

    return True


def get_primers(prime_range):
    primers = list(filter(lambda x: is_prime(x), prime_range))
    return primers
