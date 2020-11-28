class ViewModel:

    def __init__(self, ):
        self.point_values_dict = {"line_point_1": [0, 1, 2]}
        self.current_point_id = None
        # self.error_message_text = {"color": "", "color_space_in": "", "color_space_out": ""}
        # self.color_space_in = "RGB"
        # self.color_space_out = "RGB"
        # self.color_in = ['0', '0', '0']
        # self.color_out = ['', '', '']
        # self.button_convert_state = "enabled"
        # self.converter = ColorSpaceConverter()

    def set_current_point(self, point_id):
        try:
            self.point_values_dict[point_id]
        except:
            self.point_values_dict[point_id] = [0, 0, 0]
        self.current_point_id = point_id

    def set_x_y_z(self, x_y_z):
        self.point_values_dict[self.current_point_id] = x_y_z

    def get_x_y_z(self):
        if self.current_point_id == None:
            return [0, 0, 0]
        else:
            return self.point_values_dict[self.current_point_id]
