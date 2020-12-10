import unittest
from lines_intersect.viewmodel.viewmodel import LinesIntersectViewModel


class TestLinesIntersectViewModel(unittest.TestCase):

    def test_is_valid_coord1(self):
        self.assertEqual(True, LinesIntersectViewModel.is_valid_coord('1 2'))
