from triangle.model.triangle import Triangle


def is_valid(vert):
    if vert.isdigit():
        return True
    else:
        try:
            float(vert)
            return True
        except ValueError:
            return False


class TriangleViewModel:
    def __init__(self):
        self.vertices_list = []
        self.answer = ''
        self.operation = 'get ab'
        self.set_btn_disabled()

    def get_vertices(self):
        return self.vertices_list

    def set_vertices(self, vertices):
        self.vertices_list = vertices
        all_vertices_are_digits = sum([is_valid(vert) for vert in vertices])
        if (all_vertices_are_digits == 6):
            self.triangle = Triangle(float(vertices[0]), float(vertices[1]),
                                     float(vertices[2]), float(vertices[3]),
                                     float(vertices[4]), float(vertices[5]))
            self.validate_text()
        else:
            self.set_btn_disabled()

    def set_answer(self, answer_str):
        self.answer = answer_str

    def get_button_convert_state(self):
        return self.button_convert_state

    def set_btn_enabled(self):
        self.button_convert_state = 'normal'

    def set_btn_disabled(self):
        self.button_convert_state = 'disabled'

    def get_answer(self):
        return self.answer

    def validate_text(self):
        is_triangle = False
        if ('' not in self.vertices_list):
            is_triangle = Triangle.is_triangle(self.triangle)
        if is_triangle:
            self.set_btn_enabled()
        else:
            self.set_btn_disabled()

    def set_operation(self, operation):
        self.operation = operation

    def click_button(self):
        if self.operation == 'get ab':
            self.answer = str(self.triangle.get_ab())
        elif self.operation == 'get bc':
            self.answer = str(self.triangle.get_bc())
        elif self.operation == 'get ca':
            self.answer = str(self.triangle.get_ca())
        elif self.operation == 'get area':
            self.answer = str(self.triangle.get_area())
        elif self.operation == 'get perimeter':
            self.answer = str(self.triangle.get_perimeter())
        elif self.operation == 'get circumcircle':
            self.answer = str(self.triangle.get_circumcircle_center()) + '    ' + str(
                self.triangle.get_circumcircle_radius())
        elif self.operation == 'get incircle':
            self.answer = str(self.triangle.get_incircle_center()) + '    ' + str(self.triangle.get_incircle_radius())
        elif self.operation == 'get side type':
            self.answer = str(self.triangle.get_triangle_type_by_sides())
        elif self.operation == 'get angle type':
            self.answer = str(self.triangle.get_triangle_type_by_angles())
