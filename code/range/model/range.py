import re

from range.model.range_constants import RangeConstants


class Range:
    def __init__(self, range_str):
        if not re.fullmatch(RangeConstants.RANGE_REGEXP, range_str):
            raise ValueError('Input error: wrong format')
        numbers = [int(num_str) for num_str in re.findall(RangeConstants.NUMBER_REGEXP, range_str)]
        self.__start_value = numbers[0]
        self.__end_value = numbers[1]
        if range_str.startswith('('):
            self.__start_value += 1
        if range_str.endswith(')'):
            self.__end_value -= 1
        if self.__end_value < self.__start_value:
            raise ValueError('Logic error: no numbers in range')
        self.__range_str = range_str

    def contains_value(self, obj):
        if not isinstance(obj, int):
            raise TypeError('Wrong type of obj. Expected: int')
        return self.__start_value <= obj <= self.__end_value

    def contains_set(self, obj):
        return all(self.contains_value(value) for value in obj)

    def get_all_points(self):
        return list(range(self.__start_value, self.__end_value + 1))

    def contains_range(self, obj):
        if not isinstance(obj, Range):
            raise TypeError('Wrong type of obj. Expected: Range')
        return self.__start_value <= obj.__start_value <= obj.__end_value <= self.__end_value

    def overlaps_range(self, obj):
        if not isinstance(obj, Range):
            raise TypeError('Wrong type of obj. Expected: Range')
        return obj.__start_value <= self.__start_value <= self.__end_value <= obj.__end_value

    def equals(self, obj):
        if not isinstance(obj, Range):
            raise TypeError('Wrong type of obj. Expected: Range')
        return self.__start_value == obj.__start_value and self.__end_value == obj.__end_value

    def end_points(self):
        return [self.__start_value, self.__end_value]

    def to_string(self):
        return self.__range_str
