from triangle.model.triangle import Triangle


class TriangleViewModel:
    def __init__(self):
        self.triangle = Triangle(0, 0, 0, 1, 1, 0)
        self.answer = ''

    def get_vertices(self):
        return [self.triangle.x1, self.triangle.y1, self.triangle.x2, self.triangle.y2,
                self.triangle.x3.self.triangle.y3]

    def set_vertices(self, vertices):
        self.triangle = Triangle(vertices[0], vertices[1], vertices[2], vertices[3],
                                 vertices[4], vertices[6])

    def set_answer(self, answer_str):
        self.answer = answer_str

    def get_triangle_ab(self):
        return self.triangle.get_ab()

    def get_triangle_bc(self):
        return self.triangle.get_bc()

    def get_triangle_ca(self):
        return self.triangle.get_ca()

    def get_triangle_area(self):
        return self.triangle.get_area()

    def get_triangle_perimeter(self):
        return self.triangle.get_perimeter()

    def get_triangle_circumcircle(self):
        return {"center": self.triangle.get_circumcircle_center(), "radius": self.triangle.get_circumcircle_radius()}

    def get_triangle_incircle(self):
        return {"center": self.triangle.get_incircle_center(), "radius": self.triangle.get_incircle_radius()}

    def get_triangle_type_by_sides(self):
        return self.triangle.get_triangle_type_by_sides()

    def get_triangle_type_by_angles(self):
        return self.triangle.get_triangle_type_by_angles()
