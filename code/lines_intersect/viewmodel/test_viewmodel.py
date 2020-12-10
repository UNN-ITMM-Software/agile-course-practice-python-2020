import unittest
from lines_intersect.viewmodel.viewmodel import LinesIntersectViewModel


class TestLinesIntersectViewModel(unittest.TestCase):

    def test_is_valid_coord1(self):
        self.assertTrue(LinesIntersectViewModel.is_valid_coord('1 -2'))

    def test_is_valid_coord2(self):
        self.assertTrue(LinesIntersectViewModel.is_valid_coord('1. -0.2'))

    def test_is_valid_coord3(self):
        self.assertFalse(LinesIntersectViewModel.is_valid_coord('1.o -0.2'))

    def test_is_valid_coord4(self):
        self.assertFalse(LinesIntersectViewModel.is_valid_coord('1.,-0.2'))
