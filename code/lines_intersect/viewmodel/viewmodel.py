import re
from lines_intersect.model.lines_intersect import Line


class LinesIntersectViewModel:
    VALID_COORD = r"([-]?\d+[\.]?\d* [-]?\d+[\.]?\d*)"

    def __init__(self):
        self.__line1 = ""
        self.__line2 = ""
        self.__calculate_button_state = "disabled"
        self.__info_message = ""
        self.__result = ""

    @staticmethod
    def is_valid_coord(value):
        return re.fullmatch(LinesIntersectViewModel.VALID_COORD, value) is not None

    def set_line(self, val1, val2):
        if LinesIntersectViewModel.is_valid_coord(val1):
            self.__line1 = Line(val1.split()[0], val1.split()[1])
        if LinesIntersectViewModel.is_valid_coord(val2):
            self.__line1 = Line(val2.split()[0], val2.split()[1])
