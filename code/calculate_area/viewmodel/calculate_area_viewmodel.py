import re

from calculate_area.model.calculating_area import Figure


class CalculateAreaViewModel:
    def __init__(self):
        self.a = ""
        self.r = ""
        self.h = ""
        self.l = ""
        self.figure_type = ""
        self.area = ""
        self.msg = ""
        self.calc_button_state = "disabled"

    def get_area(self):
        return self.area

    def get_message(self):
        return self.msg

    def get_calc_button_state(self):
        return self.calc_button_state

    def set_a(self, value):
        self.a = value.strip()
        self.validate_inputs()

    def set_r(self, value):
        self.r = value.strip()
        self.validate_inputs()

    def set_h(self, value):
        self.h = value.strip()
        self.validate_inputs()

    def set_l(self, value):
        self.l = value.strip()
        self.validate_inputs()

    def set_figure_type(self, value):
        self.figure_type = value.strip()
        self.validate_inputs()

    def disable_calc_button(self):
        self.calc_button_state = "disabled"

    def enable_calc_button(self):
        self.calc_button_state = "normal"

    @staticmethod
    def is_positive_float_number(str_num):
        return re.match(r"(^[0-9]*[.])?[0-9]+$", str_num) and float(str_num) != 0.0

    def validate_inputs(self):
        self.msg = ""
        self.area = ""
        a = r = h = l = -1
        if self.is_positive_float_number(self.a):
            a = float(self.a)
        if self.is_positive_float_number(self.r):
            r = float(self.r)
        if self.is_positive_float_number(self.h):
            h = float(self.h)
        if self.is_positive_float_number(self.l):
            l = float(self.l)

        if self.figure_type == "CONE":
            if r == -1 or l == -1:
                self.disable_calc_button()
                self.msg = "r or l has incorrect value"
                return
        elif self.figure_type == "CUBE":
            if a == -1:
                self.disable_calc_button()
                self.msg = "a has incorrect value"
                return
        elif self.figure_type == "SPHERE":
            if r == -1:
                self.disable_calc_button()
                self.msg = "r has incorrect value"
                return
        elif self.figure_type == "CYLINDER":
            if r == -1 or h == -1:
                self.disable_calc_button()
                self.msg = "r or h has incorrect value"
                return

        self.enable_calc_button()

    def calculate(self):
        if self.calc_button_state == "normal":
            if self.figure_type == "CONE":
                figure = Figure(r=float(self.r), l=float(self.l))
                self.area = figure.calculate_area_cone()
            elif self.figure_type == "CUBE":
                figure = Figure(a=float(self.a))
                self.area = figure.calculate_area_cube()
            elif self.figure_type == "SPHERE":
                figure = Figure(r=float(self.r))
                self.area = figure.calculate_area_sphere()
            elif self.figure_type == "CYLINDER":
                figure = Figure(r=float(self.r), h=float(self.h))
                self.area = figure.calculate_area_cylinder()
            self.area = str(self.area)
            return
