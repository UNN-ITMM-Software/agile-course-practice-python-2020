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
    
    def set_line(val):
        if LinesIntersectViewModel.is_valid_coord(val):
            self.__line1 = val.split()[0]
            self.__line2 = val.split()[1]

