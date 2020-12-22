from levitsky_ilya_lab1.calculating_volume_3d_figures import calculate_volume_cube, calculate_volume_sphere, \
    calculate_volume_cylinder
import re
from levitsky_ilya_lab1.logger.reallogger import RealLogger


def is_number_entered(value):
    if value is None or len(str(value).strip()) == 0:
        return False
    else:
        is_int_value = re.match("\\d+$", str(value))
        if is_int_value is None:
            return False
        else:
            return True


class VolumeViewModel:
    button_enabled = 'disabled'
    figure_type = 0
    result = None
    error_message = None

    def __init__(self, rad=None, height=None, logger=RealLogger()):
        self.rad_val = rad
        self.height_val = height
        self.validate_values()
        self.logger = logger
        self.logger.log('Hi!')

    def is_button_enable(self):
        return self.button_enabled

    def validate_values(self):
        is_start_exist = is_number_entered(self.rad_val)
        is_end_exist = is_number_entered(self.height_val)

        if is_start_exist and is_end_exist:
            self.set_btn_enabled()
        else:
            self.set_btn_disabled()

    def set_start_value(self, value):
        self.rad_val = value
        self.validate_values()
        if self.rad_val != value:
            self.rad_val = value
            self.logger.log('Setting radius value - %s' % self.rad_val)
            self.validate_values()

    def get_start_value(self):
        return self.rad_val

    def get_end_value(self):
        return self.height_val

    def set_end_value(self, value):
        if self.height_val != value:
            self.height_val = value
            self.logger.log('Setting height value - %s' % self.height_val)
            self.validate_values()

    def set_btn_disabled(self):
        self.button_enabled = 'disabled'

    def set_btn_enabled(self):
        self.button_enabled = 'normal'

    def set_figure_type(self, value):
        self.figure_type = value

    def perform(self):
        if self.figure_type == 0:
            self.logger.log('Radiobutton 0 (cube) selected')
            self.result = calculate_volume_cube(int(self.height_val))
            self.logger.log('Result = %s' % self.result)
        elif self.figure_type == 1:
            self.logger.log('Radiobutton 1 (sphere) selected')
            self.result = calculate_volume_sphere(int(self.rad_val))
            self.logger.log('Result = %s' % self.result)
        elif self.figure_type == 2:
            self.logger.log('Radiobutton 2 (cylinder) selected')
            self.result = calculate_volume_cylinder(int(self.rad_val), int(self.height_val))
            self.logger.log('Result = %s' % self.result)

    def get_result(self):
        return self.result
