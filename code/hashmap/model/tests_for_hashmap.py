import unittest

from hashmap.model.hashmap import Hashmap


class TestHashmap(unittest.TestCase):

    def test_create_hashmap_positive(self):
        Hashmap()

    def test_insert_and_get_item_positive(self):
        hmap = Hashmap()
        obj = "zero"
        hmap.insert(0, obj)
        res = hmap.get(0)
        self.assertEqual(obj, res)

    def test_can_insert_few_items_and_get_items_positive(self):
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

    def test_delete_item_not_exists_negative(self):
        hmap = Hashmap()
        with self.assertRaises(KeyError):
            hmap.delete(0)
