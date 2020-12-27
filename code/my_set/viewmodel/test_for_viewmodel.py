import unittest

from my_set.viewmodel.viewmodel import SetViewModel
from my_set.logger.fakelogger import FakeLogger
from my_set.logger.reallogger import RealLogger


class TestSetViewModel(unittest.TestCase):
    def setUp(self):
        self.viewmodel = SetViewModel(FakeLogger())

    def test_can_add_element_to_set_a(self):
        self.viewmodel.add('1', 'A')
        self.assertEqual(self.viewmodel.set_A, [1])

    def test_can_add_element_to_set_b(self):
        self.viewmodel.add('1', 'B')
        self.assertEqual(self.viewmodel.set_B, [1])

    def test_get_status_when_add_incorrect_value(self):
        self.viewmodel.add(1, 'A')
        self.assertEqual(
            'ERR: Entered value is not correct!!!', self.viewmodel.get_status())

    def test_get_status_when_add_correct_value(self):
        self.viewmodel.add('1', 'A')
        self.assertEqual('SUCCESS!!!', self.viewmodel.get_status())

    def test_can_delete_element_from_set_a(self):
        self.viewmodel.add('1', 'A')
        self.viewmodel.delete('1', 'A')
        self.assertEqual(self.viewmodel.set_A, [])

    def test_can_delete_element_from_set_b(self):
        self.viewmodel.add('1', 'B')
        self.viewmodel.delete('1', 'B')
        self.assertEqual(self.viewmodel.set_B, [])

    def test_get_status_when_delete_missing_element(self):
        self.viewmodel.add('1', 'B')
        self.viewmodel.delete('2', 'B')
        self.assertEqual('ERR: Entered value is not correct!!!', self.viewmodel.get_status())

    def test_get_status_when_delete_existing_element(self):
        self.viewmodel.add('1', 'B')
        self.viewmodel.delete('1', 'B')
        self.assertEqual('SUCCESS!!!', self.viewmodel.get_status())

    def test_can_union_a_b_sets(self):
        self.viewmodel.add('1', 'A')
        self.viewmodel.add('5', 'B')

        self.viewmodel.union()

        self.assertEqual(self.viewmodel.set_A, [1, 5])
        self.assertEqual(self.viewmodel.set_B, [5])

    def test_can_intersection_a_b_sets(self):
        self.viewmodel.add('1', 'A')
        self.viewmodel.add('5', 'A')
        self.viewmodel.add('5', 'B')

        result = self.viewmodel.intersection()

        self.assertEqual(result, '[5]')

    def test_can_difference_a_b_sets(self):
        self.viewmodel.add('1', 'A')
        self.viewmodel.add('5', 'A')
        self.viewmodel.add('5', 'B')

        result = self.viewmodel.difference(mode='A\B')

        self.assertEqual(result, '[1]')

    def test_can_difference_b_a_sets(self):
        self.viewmodel.add('1', 'A')
        self.viewmodel.add('5', 'A')
        self.viewmodel.add('5', 'B')

        result = self.viewmodel.difference(mode='B\A')

        self.assertEqual(result, '[]')

    def test_can_convert_set_a_to_str(self):
        self.viewmodel.add('18', 'A')
        result = self.viewmodel.set_a_to_str()
        self.assertEqual(result, '[18]')

    def test_can_convert_set_b_to_str(self):
        self.viewmodel.add('18', 'B')
        result = self.viewmodel.set_b_to_str()
        self.assertEqual(result, '[18]')


class TestSetViewModelFakeLogging(unittest.TestCase):
    def setUp(self):
        self.viewmodel = SetViewModel(FakeLogger())

    def test_logging_init(self):
        self.assertEqual('Welcome!', self.viewmodel.logger.get_last_message())

    def test_logging_add_element_to_set_a(self):
        self.viewmodel.add('1', 'A')
        self.assertEqual('Resulting set A: [1]', self.viewmodel.logger.get_last_message())

    def test_logging_add_element_to_set_b(self):
        self.viewmodel.add('1', 'B')
        self.assertEqual('Resulting set B: [1]', self.viewmodel.logger.get_last_message())

    def test_logging_delete_element_from_set_a(self):
        self.viewmodel.add('1', 'A')
        self.viewmodel.delete('1', 'A')
        self.assertEqual('Resulting set A: []', self.viewmodel.logger.get_last_message())

    def test_logging_delete_element_from_set_b(self):
        self.viewmodel.add('1', 'B')
        self.viewmodel.delete('1', 'B')
        self.assertEqual('Resulting set B: []', self.viewmodel.logger.get_last_message())

    def test_logging_union_a_b_sets(self):
        self.viewmodel.add('1', 'A')
        self.viewmodel.add('5', 'B')

        self.viewmodel.union()

        self.assertEqual('Resulting set A: [1, 5]', self.viewmodel.logger.get_last_message())

    def test_logging_intersection_a_b_sets(self):
        self.viewmodel.add('1', 'A')
        self.viewmodel.add('5', 'A')
        self.viewmodel.add('5', 'B')

        self.viewmodel.intersection()

        self.assertEqual('Result: [5]', self.viewmodel.logger.get_last_message())

    def test_logging_difference_a_b_sets(self):
        self.viewmodel.add('1', 'A')
        self.viewmodel.add('5', 'A')
        self.viewmodel.add('5', 'B')

        self.viewmodel.difference(mode='A\B')

        self.assertEqual('Result: [1]', self.viewmodel.logger.get_last_message())

    def test_logging_difference_b_a_sets(self):
        self.viewmodel.add('1', 'A')
        self.viewmodel.add('5', 'A')
        self.viewmodel.add('5', 'B')

        self.viewmodel.difference(mode='B\A')

        self.assertEqual('Result: []', self.viewmodel.logger.get_last_message())

    def test_logging_setting_set_a_to_str(self):
        self.viewmodel.add('18', 'A')
        self.viewmodel.set_a_to_str()
        self.assertEqual('Setting A to [18]', self.viewmodel.logger.get_last_message())

    def test_logging_setting_set_b_to_str(self):
        self.viewmodel.add('18', 'B')
        self.viewmodel.set_b_to_str()
        self.assertEqual('Setting B to [18]', self.viewmodel.logger.get_last_message())


class TestSetViewModelRealLogging(TestSetViewModelFakeLogging):
    def setUp(self):
        self.viewmodel = SetViewModel(RealLogger())
