import unittest

from hashmap.model.hashmap import Hashmap


class TestHashmap(unittest.TestCase):

    def test_can_create_hashmap(self):
        Hashmap()

    def test_can_insert_and_get_item(self):
        hmap = Hashmap()
        obj = "zero"
        hmap.insert(0, obj)
        res = hmap.get(0)
        self.assertEqual(obj, res)

    def test_can_insert_few_items_and_get_items(self):
        hmap = Hashmap()
        key1 = 0
        key2 = 1
        obj1 = "zero"
        obj2 = "one"
        hmap.insert(key1, obj1)
        hmap.insert(key2, obj2)
        res1 = hmap.get(key1)
        res2 = hmap.get(key2)
        self.assertEqual(obj1, res1)
        self.assertEqual(obj2, res2)
