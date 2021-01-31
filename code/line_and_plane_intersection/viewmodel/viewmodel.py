from line_and_plane_intersection.model.intersection import Intersection, Line, Plane, Point3D
from line_and_plane_intersection.logger.reallogger import RealLogger


class ViewModel:

    def __init__(self, logger=RealLogger()):
        self.line_point_values_dict = {}
        self.plane_point_values_dict = {}
        self.abcd = []
        self.current_point_id = None
        self.current_dict_type = None
        self.interception_or_error_msg = ""
        self.intersection = Intersection()
        self.logger = logger
        self.logger.log('Line-Plane intersection application init')

    def _set_current_point(self, point_id, point_values_dict):
        if point_id is not None:
            try:
                point_values_dict[point_id]
            except:
                point_values_dict[point_id] = [0, 0, 0]
            self.current_point_id = point_id

    def set_current_point_for_plane(self, point_id):
        self.logger.log('Current plane point = {}'.format(point_id))
        self.current_dict_type = "plane"
        self._set_current_point(point_id, self.plane_point_values_dict)

    def set_current_point_for_line(self, point_id):
        self.logger.log('Current line point = {}'.format(point_id))
        self.current_dict_type = "line"
        self._set_current_point(point_id, self.line_point_values_dict)

    def set_x_y_z(self, x_y_z):
        self.logger.log('dict_type = {}, x_y_z set = {}'.format(self.current_dict_type, x_y_z))
        if self.current_dict_type == "plane":
            self.plane_point_values_dict[self.current_point_id] = x_y_z
        else:
            self.line_point_values_dict[self.current_point_id] = x_y_z

    def set_abcd(self, abcd):
        self.logger.log('abcd set = {}'.format(abcd))
        self.abcd = abcd

    def get_x_y_z(self):
        if self.current_point_id is None:
            return [0, 0, 0]
        else:
            if self.current_dict_type == "plane":
                return self.plane_point_values_dict[self.current_point_id]
            else:
                return self.line_point_values_dict[self.current_point_id]

    def is_intersect(self):
        is_validate = self._is_validate()
        if is_validate:
            self.interception_or_error_msg = \
                str(self.intersection.have_intersection(self._get_line(), self._get_plane()))
        else:
            if is_validate is not None:
                self.interception_or_error_msg = "Not completed points."
        self.logger.log('Get result: {}'.format(self.interception_or_error_msg))

    def _get_corrected_values(self, dict):
        return list(map(lambda l: list(map(int, l)), list(dict.values())))

    def _get_int_list(self, list_values):
        return list(map(int, list_values))

    def _get_line(self) -> Line:
        line_point_values = self._get_corrected_values(self.line_point_values_dict)
        point_1 = Point3D(line_point_values[0])
        point_2 = Point3D(line_point_values[1])
        return Line(point_1, point_2)

    def _get_plane(self) -> Plane:
        plane_point_values = self._get_corrected_values(self.plane_point_values_dict)
        point_1 = Point3D(plane_point_values[0])
        point_2 = Point3D(plane_point_values[1])
        point_3 = Point3D(plane_point_values[2])
        plane = Plane(point_1, point_2, point_3)
        plane.abcd = self._get_int_list(self.abcd)

        return plane

    def _is_validate(self):
        if len(self.line_point_values_dict.values()) != 2 \
                or len(self.plane_point_values_dict.values()) != 3 \
                or len(self.abcd) != 4:
            return False
        try:

            self._get_line()
            self._get_plane()

        except Exception as e:
            self.interception_or_error_msg = str(e)
            return None

        return True
