import unittest

from my_set.model.my_set import MySet


class TestSetClass(unittest.TestCase):
    def test_can_init_with_default_constructor(self):
        test_set = MySet()
        self.assertTrue(isinstance(test_set, MySet))

    def test_can_get_size_of_set(self):
        test_set = MySet([1, 2, 5])
        size = test_set.get_size()
        self.assertEqual(size, 3)

    def test_can_init_with_init_constructor(self):
        test_list_of_elements = [1, 2, 3, 5, 7]
        test_set = MySet(test_list_of_elements)
        self.assertEqual(test_set.get_size(), 5)

    def test_set_with_size_0_is_empty(self):
        test_set = MySet()
        result = test_set.is_empty()
        self.assertTrue(result)

    def test_set_with_some_elements_is_not_empty(self):
        test_set = MySet([1, 2, 4, 5])
        result = test_set.is_empty()
        self.assertFalse(result)

    def test_can_check_element_contain(self):
        test_set = MySet([1, 2, 4, 5])
        element = 4
        result = element in test_set
        self.assertTrue(result)

    def test_can_check_element_not_contain(self):
        test_set = MySet([1, 2, 4, 5])
        element = 7
        result = element in test_set
        self.assertFalse(result)

    def test_can_add_new_element(self):
        test_set = MySet([1, 2, 4, 5])
        element = 7
        test_set.add(element)
        self.assertTrue(element in test_set)

    def test_dont_add_ununic_element(self):
        test_set = MySet([1, 2, 4, 5])
        element = 2
        test_set.add(element)
        self.assertEqual(test_set.get_size(), 4)

    def test_can_delete_element(self):
        test_set = MySet([1, 2, 4, 5])
        element = 1
        test_set.delete(element)
        self.assertFalse(element in test_set)

    def test_after_delete_size_became_less_on_one(self):
        test_set = MySet([1, 2, 4, 5])
        element = 2
        test_set.delete(element)
        self.assertEqual(test_set.get_size(), 3)

    def test_can_union_with_list(self):
        test_set = MySet([1, 2, 4, 5])
        test_list = [7, 8, 10]
        test_set.union(test_list)
        self.assertEqual(test_set.get_size(), 7)

    def test_can_union_with_list_contain_same_elements(self):
        test_set = MySet([1, 2, 4, 5])
        test_list = [2, 5, 10]
        test_set.union(test_list)
        self.assertEqual(test_set.get_size(), 5)

    def test_can_union_with_set(self):
        test_set = MySet([1, 2, 4, 5])
        another_set = MySet([6, 9, 14, 15])
        test_set.union(another_set)
        self.assertEqual(test_set.get_size(), 8)

    def test_can_union_with_set_contain_same_elements(self):
        test_set = MySet([1, 2, 4, 5])
        another_set = MySet([1, 5, 14, 15])
        test_set.union(another_set)
        self.assertEqual(test_set.get_size(), 6)

    def test_can_union_with_one_element(self):
        test_set = MySet([1, 2, 4, 5])
        test_set.union(7)
        self.assertEqual(test_set.get_size(), 5)

    def test_can_init_with_default_constructor_one_elem_set(self):
        test_set = MySet(5)
        self.assertEqual(test_set.get_size(), 1)

    def test_cant_init_with_default_constructor_invalide_arg(self):
        with self.assertRaises(TypeError):
            MySet("invalide argument")

    def test_cant_delete_uncontain_element(self):
        test_set = MySet([1, 2, 4, 5])
        uncontain_element = 7
        with self.assertRaises(ValueError):
            test_set.delete(uncontain_element)

    def test_cant_union_with_invalide_argument(self):
        test_set = MySet([1, 2, 4, 5])
        with self.assertRaises(TypeError):
            test_set.union("invalide argument")

    def test_can_check_equalities_of_eqvivalent_sets(self):
        test_set_1 = MySet([1, 2, 4, 5])
        test_set_2 = MySet([1, 2, 4, 5])
        result = (test_set_1 == test_set_2)
        self.assertTrue(result)

    def test_can_check_equalities_of_uneqvivalent_sets(self):
        test_set_1 = MySet([1, 2, 4, 5])
        test_set_2 = MySet([1, 3, 4, 5])
        result = (test_set_1 == test_set_2)
        self.assertFalse(result)

    def test_can_check_equalities_of_set_and_list(self):
        test_set = MySet([1, 2, 4, 5])
        test_list = [1, 2, 4, 5]
        result = (test_set == test_list)
        self.assertTrue(result)

    def test_can_check_equalities_of_set_and_int(self):
        test_set = MySet([1])
        test_int = 1
        result = (test_set == test_int)
        self.assertTrue(result)

    def test_can_check_equalities_of_no_one_element_set_and_int(self):
        test_set = MySet([1, 3])
        test_int = 1
        result = (test_set == test_int)
        self.assertFalse(result)

    def test_cant_eq_with_invalide_argument(self):
        test_set = MySet([1, 2, 4, 5])
        with self.assertRaises(TypeError):
            test_set == "invalide argument"
