class InvalidColorSpace(Exception):
    pass


class ColorSpace:
    SUPPORTED_COLOR_SPACES = ["RGB", "HSV", "LAB"]

    color_space = "RGB"

    def __init__(self, color_space="RGB"):
        if color_space not in self.SUPPORTED_COLOR_SPACES:
            raise InvalidColorSpace(
                'unsupported color space: ' + str(color_space))
        self.color_space = color_space

    def __str__(self):
        return self.color_space

    def __eq__(self, other):
        return self.color_space == other.color_space
