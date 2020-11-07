import unittest

class SortingTest(unittest.TestCase):
    def test_can_create_sorting(self):
        sorting = Sorting()
        self.assertTrue(isinstance(sorting, Sorting))

if __name__ == '__main__':
    unittest.main()