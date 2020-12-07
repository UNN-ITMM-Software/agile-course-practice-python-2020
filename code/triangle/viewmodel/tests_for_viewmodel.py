import math
import unittest

from triangle.viewmodel.viewmodel import TriangleViewModel


class TestFractionCalculatorViewModel(unittest.TestCase):

    def setUp(self):
        self.view_model = TriangleViewModel()

    def test_by_default_button_disabled(self):
        self.assertEqual('disabled', self.view_model.get_button_convert_state())

    def test_when_entered_valid_triangle_button_enabled(self):
        self.view_model.set_vertices(['0', '0', '3', '0', '0', '4'])
        self.assertNotEqual('disabled', self.view_model.get_button_convert_state())

    def test_when_entered_invalid_triangle_button_enabled(self):
        self.view_model.set_vertices(['0', '0', '1', '0', '2', '0'])
        self.assertNotEqual('normal', self.view_model.get_button_convert_state())

    def test_can_retrieve_vertices_text(self):
        self.view_model.set_vertices(['0', '0', '3', '0', '0', '4'])
        actual_triangle = self.view_model.get_vertices()
        self.assertEqual(['0', '0', '3', '0', '0', '4'], actual_triangle)

    def test_when_entered_vertices_then_clear_one_button_disabled(self):
        self.view_model.set_vertices(['0', '0', '3', '0', '0', '4'])
        self.view_model.set_vertices(['0', '0', '', '0', '0', '4'])
        self.assertEqual('disabled', self.view_model.get_button_convert_state())

    def test_when_entered_not_vertex_button_disabled(self):
        self.view_model.set_vertices(['0', '0', '3', '0', '0', '4a'])
        self.assertEqual('disabled', self.view_model.get_button_convert_state())

    def test_can_get_ab(self):
        self.view_model.set_vertices(['0', '0', '3', '0', '0', '4'])
        self.view_model.click_button()
        self.assertEqual('3.0', self.view_model.get_answer())

    def test_can_get_bc(self):
        self.view_model.set_vertices(['0', '0', '3', '0', '0', '4'])
        self.view_model.set_operation('get bc')
        self.view_model.click_button()
        self.assertEqual('5.0', self.view_model.get_answer())

    def test_can_get_ca(self):
        self.view_model.set_vertices(['0', '0', '3', '0', '0', '4'])
        self.view_model.set_operation('get ca')
        self.view_model.click_button()
        self.assertEqual('4.0', self.view_model.get_answer())

    def test_can_get_area(self):
        self.view_model.set_vertices(['0', '0', '3', '0', '0', '4'])
        self.view_model.set_operation('get area')
        self.view_model.click_button()
        self.assertEqual('6.0', self.view_model.get_answer())

    def test_can_get_perimeter(self):
        self.view_model.set_vertices(['0', '0', '3', '0', '0', '4'])
        self.view_model.set_operation('get perimeter')
        self.view_model.click_button()
        self.assertEqual('12.0', self.view_model.get_answer())

    def test_can_get_circumcircle(self):
        self.view_model.set_vertices(['0', '0', '0', '3', '4', '0'])
        self.view_model.set_operation('get circumcircle')
        self.view_model.click_button()
        self.assertEqual('[2.0, 1.5]    2.5', self.view_model.get_answer())

    def test_can_get_incircle(self):
        self.view_model.set_vertices(['0', '0', '0', '3', '4', '0'])
        self.view_model.set_operation('get incircle')
        self.view_model.click_button()
        self.assertEqual('[1.0, 1.0]    1.0', self.view_model.get_answer())

    def test_can_get_type_by_side_equilateral(self):
        self.view_model.set_vertices(['1', '1', '2', str(math.sqrt(3) + 1), '3', '1'])
        self.view_model.set_operation('get side type')
        self.view_model.click_button()
        self.assertEqual('equilateral', self.view_model.get_answer())

    def test_can_get_type_by_side_isosceles(self):
        self.view_model.set_vertices(['0', '0', '0', '1', '1', '0'])
        self.view_model.set_operation('get side type')
        self.view_model.click_button()
        self.assertEqual('isosceles', self.view_model.get_answer())

    def test_can_get_type_by_side_various(self):
        self.view_model.set_vertices(['0', '0', '0', '1', '2', '0'])
        self.view_model.set_operation('get side type')
        self.view_model.click_button()
        self.assertEqual('various', self.view_model.get_answer())

    def test_can_get_type_by_angle_various(self):
        self.view_model.set_vertices(['1', '1', '2', str(math.sqrt(3) + 1), '3', '1'])
        self.view_model.set_operation('get angle type')
        self.view_model.click_button()
        self.assertEqual('acute', self.view_model.get_answer())

    def test_can_get_type_by_angle_right(self):
        self.view_model.set_vertices(['0', '0', '0', '3', '3', '0'])
        self.view_model.set_operation('get angle type')
        self.view_model.click_button()
        self.assertEqual('right', self.view_model.get_answer())

    def test_can_get_type_by_angle_obtuse(self):
        self.view_model.set_vertices(['0', '0', '0', '3', '4', '-1'])
        self.view_model.set_operation('get angle type')
        self.view_model.click_button()
        self.assertEqual('obtuse', self.view_model.get_answer())
