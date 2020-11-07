import unittest

class SortingTest(unittest.TestCase):
    def test_can_create_sorting(self):
        sort = Sorting()
        self.assertTrue(isinstance(sort, Sorting))

if __name__ == '__main__':
    unittest.main()