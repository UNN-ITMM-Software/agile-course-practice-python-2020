import unittest

from calculate_area.model.calculating_area import Figure, InvalidFigureError


class TestCalculatingArea(unittest.TestCase):

    def test_can_create_figure_default(self):
        figure = Figure()
        self.assertTrue(isinstance(figure, Figure))

    def test_can_create_figure_init_all(self):
        figure = Figure(1, 2, 3, 4)
        self.assertTrue(figure.a == 1 and figure.r == 2
                        and figure.h == 3 and figure.l == 4)

    def test_can_create_figure_init_cone(self):
        figure = Figure(r=2, l=3)
        self.assertTrue(figure.r == 2 and figure.l == 3)

    def test_can_create_figure_init_cube(self):
        figure = Figure(5)
        self.assertTrue(figure.a == 5)

    def test_can_create_figure_init_cylinder(self):
        figure = Figure(r=2, h=4)
        self.assertTrue(figure.r == 2, figure.h == 4)

    def test_can_create_figure_init_sphere(self):
        figure = Figure(r=2)
        self.assertTrue(figure.r == 2)

    def test_can_create_figure_neg_init_str(self):
        with self.assertRaises(InvalidFigureError):
            Figure(a="abc")

    def test_can_create_figure_neg_init_list(self):
        with self.assertRaises(InvalidFigureError):
            Figure([1, 2])

    def test_can_create_figure_neg_init_set(self):
        with self.assertRaises(InvalidFigureError):
            Figure({1, 2})

    def test_can_create_figure_neg_init_bool(self):
        with self.assertRaises(InvalidFigureError):
            Figure(a=True)

    def test_can_create_figure_neg_init_0(self):
        with self.assertRaises(InvalidFigureError):
            Figure(a=0)

    def test_can_create_figure_neg_init_1(self):
        with self.assertRaises(InvalidFigureError):
            Figure(a=-1)

    def test_calculate_area_cone_default(self):
        self.assertEqual(Figure().calculate_area_cone(), 6.283)

    def test_calculate_area_cube_default(self):
        self.assertEqual(Figure().calculate_area_cube(), 6)

    def test_calculate_area_cylinder_default(self):
        self.assertEqual(Figure().calculate_area_cylinder(), 12.566)

    def test_calculate_area_sphere_default(self):
        self.assertEqual(Figure().calculate_area_sphere(), 12.566)

    def test_calculate_area_cone_int(self):
        self.assertEqual(Figure(r=2, l=3).calculate_area_cone(), 31.416)

    def test_calculate_area_cube_int(self):
        self.assertEqual(Figure(a=5).calculate_area_cube(), 150)

    def test_calculate_area_cylinder_int(self):
        self.assertEqual(Figure(r=2, h=4).calculate_area_cylinder(), 75.398)

    def test_calculate_area_sphere_int(self):
        self.assertEqual(Figure(r=2).calculate_area_sphere(), 50.265)

    def test_calculate_area_cone_float(self):
        self.assertEqual(Figure(r=2.3, l=3.8).calculate_area_cone(), 44.077)

    def test_calculate_area_cube_float(self):
        self.assertEqual(Figure(a=5.9).calculate_area_cube(), 208.86)

    def test_calculate_area_cylinder_float(self):
        self.assertEqual(Figure(r=2.3, h=4.2).calculate_area_cylinder(), 93.934)

    def test_calculate_area_sphere_float(self):
        self.assertEqual(Figure(r=2.3).calculate_area_sphere(), 66.476)
