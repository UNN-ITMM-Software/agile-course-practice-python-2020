import numpy as np

from .color_space import ColorSpace


class InvalidColorError(Exception):
    pass


class Color:
    COLOR_DIM = 3

    value = np.zeros(COLOR_DIM, np.uint8)
    space = ColorSpace()

    def __init__(self, space=ColorSpace(), value=np.zeros(3, np.uint8)):
        if value.size != self.COLOR_DIM:
            raise InvalidColorError('invalid color size')

        if value[value < 0].size != 0 or value[value > 255].size != 0:
            raise InvalidColorError('invalid color values')

        self.space = space
        self.value = value

    def __str__(self):
        return "{} {}".format(self.space, self.value.tolist())

    def __eq__(self, other_color):
        eq_space = self.space == other_color.space
        eq_value = np.array_equal(self.value, other_color.value)
        return eq_space and eq_value
