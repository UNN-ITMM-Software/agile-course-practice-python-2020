from itertools import chain
from math import log10


class RadixSort():
    def __init__(self, arr):
        if not isinstance(arr, list):
            raise TypeError("%s is not a list" % type(arr))

        if all(isinstance(val, int) for val in arr):
            self.arr = arr
        else:
            raise ValueError("not all items are integers")

    def sort(self):
        if len(self.arr) == 0:
            return self.arr

        max_val = max(abs(val) for val in self.arr)
        if max_val > 0:
            digits = int(log10(max_val) + 1)
        else:
            digits = 1
        for i in range(digits):
            self.arr = self.__counting_sort(self.arr, i)

        return self.arr

    def __counting_sort(self, arr, digit):
        num_buckets = 20
        buckets = [[] for i in range(num_buckets)]
        divisor = 10 ** digit
        for n in arr:
            if n >= 0:
                buckets[(n // divisor) % 10 + 10].append(n)
            else:
                buckets[(n // divisor) % 10].append(n)

        return list(chain.from_iterable(buckets))
