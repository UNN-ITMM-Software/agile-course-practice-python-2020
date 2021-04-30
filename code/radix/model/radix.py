class Sorting:
    """
    Class for sorting positives integers using radix sort
    """
    arr = []

    def __init__(self, arr):
        if not isinstance(arr, list):
            raise TypeError

        for el in arr:
            if not self.is_digit(el):
                raise TypeError
        self.arr = arr

    def _radix_get_max_length(self):
        max_digits = 0
        print(self.arr)
        for num in self.arr:
            digit_count = self._radix_get_length(num)
            if digit_count > max_digits:
                max_digits = digit_count
        return max_digits

    @staticmethod
    def _radix_get_length(value):
        if value == 0:
            return 1

        digits = 0

        while value != 0:
            digits += 1
            value = value // 10
        return digits

    def radix_sort(self):
        buckets = []
        for i in range(10):
            buckets.append([])

        max_digits = self._radix_get_max_length()

        pow_10 = 1
        for digit_index in range(max_digits):
            for num in self.arr:
                bucket_index = (num // pow_10) % 10
                buckets[bucket_index].append(num)

            self.arr.clear()
            for bucket in buckets:
                self.arr.extend(bucket)
                bucket.clear()

            pow_10 = pow_10 * 10

        non_negatives = []
        for num in self.arr:
            non_negatives.append(num)
        self.arr.clear()
        self.arr.extend(non_negatives)

    def result_str(self):
        string = ''
        for j in range(len(self.arr)):
            space = ''
            if j < len(self.arr) - 1:
                space = ' '
            string += str(self.arr[j]) + space
        return string

    @staticmethod
    def is_digit(value):
        if type(value) == int and value >= 0:
            return True
        else:
            return False
