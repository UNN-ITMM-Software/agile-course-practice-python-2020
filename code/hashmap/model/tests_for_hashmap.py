import unittest

from hashmap.model.hashmap import Hashmap


class TestHashmap(unittest.TestCase):

    def test_create_hashmap_positive(self):
        Hashmap()

    def test_key_not_hashable_negative(self):
        hmap = Hashmap()
        key = ([])
        obj = "zero"
        with self.assertRaises(TypeError):
            hmap.insert(key, obj)

    def test_get_item_not_exists_negative(self):
        hmap = Hashmap()
        with self.assertRaises(KeyError):
            hmap.get(0)

    def test_insert_and_get_item_positive(self):
        hmap = Hashmap()
        key = 0
        obj = "zero"
        hmap.insert(key, obj)
        res = hmap.get(key)
        self.assertEqual(obj, res)

    def test_insert_few_items_and_get_items_positive(self):
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

    def test_insert_two_items_with_same_key_negative(self):
        hmap = Hashmap()
        key = 0
        obj1 = "zero"
        obj2 = "one"
        hmap.insert(key, obj1)
        with self.assertRaises(KeyError):
            hmap.insert(key, obj2)

    def test_insert_two_items_with_same_hash_positive(self):
        hmap = Hashmap(1)
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

    def test_update_item_positive(self):
        hmap = Hashmap()
        key = 0
        obj = "zero"
        obj_updated = "0"
        hmap.insert(key, obj)
        hmap.update(key, obj_updated)
        res = hmap.get(key)
        self.assertEqual(obj_updated, res)

    def test_update_item_not_exists_negative(self):
        hmap = Hashmap()
        key = 0
        obj = "zero"
        with self.assertRaises(KeyError):
            hmap.update(key, obj)

    def test_get_keys_empty_hashmap_positive(self):
        hmap = Hashmap()
        keys = []
        ret_keys = hmap.keys()
        self.assertEqual(keys, ret_keys)

    def test_get_keys_three_items_hashmap_positive(self):
        hmap = Hashmap()
        keys = [123, "asda", 1023]
        for key in keys:
            hmap.insert(key, "dummy")
        ret_keys = hmap.keys()
        self.assertEqual(keys.sort(key=lambda x: hash(x)), ret_keys.sort(key=lambda x: hash(x)))
