import unittest

from hashmap.model.hashmap import Hashmap


class TestHashmap(unittest.TestCase):

    def test_can_create_hashmap(self):
        Hashmap()

    def test_can_insert_and_get_item(self):
        map = Hashmap()
        obj = "zero"
        map.insert(0, obj)
        res = map.get(0)
        self.assertEqual(obj, res)
