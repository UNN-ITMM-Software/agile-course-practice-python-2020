import unittest

from interpolation_search.model.interpolation_search import InterpolationSearch


first_case = (1, 2, 3, 4, 5, 6, 7, 8, 9)
second_case = (11, 12, 13, 15, 16, 17, 18)
third_case = (32, 43, 54, 65, 76, 87, 98)
fourth_case = (101, 202, 303, 404, 505, 606)
fifth_case = (3, 20, 44, 75, 92, 106, 709)


class TestInterpolationSearchClass(unittest.TestCase):
    def test_can_create_interpolation_search(self):
        search = InterpolationSearch()
        self.assertTrue(isinstance(search, InterpolationSearch))

    def test_can_create_interpolation_searchearch_else_case(self):
        search = InterpolationSearch()
        self.assertEqual(search.interpolation_search((10, 12, 13, 16, 18, 19, 20, 21), 18), 4)

    def test_can_create_interpolation_searchearch_first_case(self):
        search = InterpolationSearch()
        self.assertEqual(search.interpolation_search(first_case, 8), 7)

    def test_can_create_interpolation_searchearch_second_case(self):
        search = InterpolationSearch()
        self.assertEqual(search.interpolation_search(second_case, 14), -1)

    def test_can_create_interpolation_searchearch_third_case(self):
        search = InterpolationSearch()
        self.assertEqual(search.interpolation_search(third_case, 76), 4)

    def test_can_create_interpolation_searchearch_fourth_case(self):
        search = InterpolationSearch()
        self.assertEqual(search.interpolation_search(fourth_case, 606), 5)

    def test_can_create_interpolation_searchearch_fifth_case(self):
        search = InterpolationSearch()
        self.assertEqual(search.interpolation_search(fifth_case, 3), 0)
