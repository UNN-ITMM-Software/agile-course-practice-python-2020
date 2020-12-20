import re
from lines_intersect.logger.reallogger import RealLogger
from lines_intersect.model.lines_intersect import Line


class LinesIntersectViewModel:
    VALID_COORD = r"([-]?\d+[\.]?\d*[ ]+[-]?\d+[\.]?\d*)"
    RESULT_STR = "Intersection: %s"

    def __init__(self, logger=RealLogger()):
        self.logger = logger
        self._point1 = ""
        self._point2 = ""
        self._point3 = ""
        self._point4 = ""
        self.set_button_calculate_disabled()
        self._result = ""

    def set_button_calculate_enabled(self):
        self._button_calculate_state = "normal"

    def set_button_calculate_disabled(self):
        self._button_calculate_state = "disabled"

    def get_button_calculate_state(self):
        return self._button_calculate_state

    def validate_text(self):
        if self.is_valid_coord(self._point1) and \
           self.is_valid_coord(self._point2) and \
           self.is_valid_coord(self._point3) and \
           self.is_valid_coord(self._point4):
            self.set_button_calculate_enabled()
        else:
            self.set_button_calculate_disabled()

    def get_point1(self):
        return self._point1

    def get_point2(self):
        return self._point2

    def get_point3(self):
        return self._point3

    def get_point4(self):
        return self._point4

    def set_point1(self, value):
        self.logger.log(f"Set point 1 to {value}")
        self._point1 = value
        self.validate_text()

    def set_point2(self, value):
        self.logger.log(f"Set point 2 to {value}")
        self._point2 = value
        self.validate_text()

    def set_point3(self, value):
        self.logger.log(f"Set point 3 to {value}")
        self._point3 = value
        self.validate_text()

    def set_point4(self, value):
        self.logger.log(f"Set point 4 to {value}")
        self._point4 = value
        self.validate_text()

    def get_result(self):
        return self._result

    @staticmethod
    def is_valid_coord(value):
        return re.fullmatch(LinesIntersectViewModel.VALID_COORD, value) is not None

    def click_calculate(self):
        self.logger.log("Calculate clicked")

        if self.get_button_calculate_state() == "disabled":
            return

        def str_to_point(s):
            return [float(el) for el in s.split()]

        line1 = Line(str_to_point(self._point1), str_to_point(self._point2))
        line2 = Line(str_to_point(self._point3), str_to_point(self._point4))

        self._result = self.RESULT_STR % (str(Line.is_intersect(line1, line2)))
        self.logger.log(self._result)

