import unittest
from lines_intersect.viewmodel.viewmodel import LinesIntersectViewModel


class TestLinesIntersectViewModel(unittest.TestCase):

    def setUp(self):
        self.view_model = LinesIntersectViewModel()

    def test_is_valid_coord1(self):
        self.assertTrue(LinesIntersectViewModel.is_valid_coord('1 -2'))

    def test_is_valid_coord2(self):
        self.assertTrue(LinesIntersectViewModel.is_valid_coord('1. -0.2'))

    def test_is_valid_coord3(self):
        self.assertFalse(LinesIntersectViewModel.is_valid_coord('1.o -0.2'))

    def test_is_valid_coord4(self):
        self.assertFalse(LinesIntersectViewModel.is_valid_coord('1.,-0.2'))

    def test_is_valid_coord_with_multispace(self):
        self.assertTrue(LinesIntersectViewModel.is_valid_coord('1   -2'))

    def test_can_set_get_point1(self):
        self.view_model.set_point1("1 2")
        self.assertEqual("1 2", self.view_model.get_point1())

    def test_can_set_get_point2(self):
        self.view_model.set_point2("1 2")
        self.assertEqual("1 2", self.view_model.get_point2())

    def test_can_set_get_point3(self):
        self.view_model.set_point3("1 2")
        self.assertEqual("1 2", self.view_model.get_point3())

    def test_can_set_get_point4(self):
        self.view_model.set_point4("1 2")
        self.assertEqual("1 2", self.view_model.get_point4())

    def test_can_calculate(self):
        self.view_model.set_point1("2 3")
        self.view_model.set_point2("2 3")
        self.view_model.set_point3("2 3")
        self.view_model.set_point4("2 3")
        self.view_model.click_calculate()
        self.assertEqual(self.view_model.RESULT_STR % "True", self.view_model.get_result())

    def test_check(self):
        self.view_model.set_point1("2 3")
        self.view_model.set_point2("2 3")
        self.view_model.set_point3("2 3")
        self.view_model.set_point4("2 error")
        self.view_model.click_calculate()
        self.assertEqual("", self.view_model.get_result())
