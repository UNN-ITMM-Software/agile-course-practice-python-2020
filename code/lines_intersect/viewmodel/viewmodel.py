import re
from lines_intersect.model.lines_intersect import Line


class LinesIntersectViewModel:
    VALID_COORD = r"([-]?\d+[\.]?\d*[ ]+[-]?\d+[\.]?\d*)"

    def __init__(self):
        self._point1 = ""
        self._point2 = ""
        self._point3 = ""
        self._point4 = ""
        set_button_calculate_disabled()
        self._result = ""
        
    def set_button_calculate_enabled(self):
        self._button_calculate_state = "normal"

    def set_button_calculate_disabled(self):
        self._button_calculate_state = "disabled"

    def get_button_calculate_state(self):
        return self._button_calculate_state

    @staticmethod
    def is_valid_coord(value):
        return re.fullmatch(LinesIntersectViewModel.VALID_COORD, value) is not None

    def set_line(self, val1, val2):
        if LinesIntersectViewModel.is_valid_coord(val1):
            self._line1 = Line(val1.split()[0], val1.split()[1])
        if LinesIntersectViewModel.is_valid_coord(val2):
            self._line1 = Line(val2.split()[0], val2.split()[1])

    def click_caclulate(self):
        if self.get_button_calculate_state() == "disabled":
            return
        line1 = Line(self._point1.split(), self._point2.split())
        line2 = Line(self._point3.split(), self._point4.split())

        self._result = str(Line.is_intersect(line1, line2))
