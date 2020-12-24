import unittest

from levitsky_ilya_lab1.viewmodel.viewmodel import VolumeViewModel


class TestVolumeViewModel(unittest.TestCase):

    def test_default_button_is_disable(self):
        model = VolumeViewModel()
        self.assertEqual('disabled', model.is_button_enable())

    def test_button_enabled_3_5(self):
        model = VolumeViewModel(3, 5)
        self.assertTrue(model.is_button_enable())

    def test_button_disabled_none_5(self):
        model = VolumeViewModel(3, 5)
        model.set_start_value(None)
        self.assertEqual('disabled', model.is_button_enable())

    def test_button_disabled_3_none(self):
        model = VolumeViewModel(3, 5)
        model.set_end_value(None)
        self.assertEqual('disabled', model.is_button_enable())

    def test_correct_set_value(self):
        model = VolumeViewModel()
        model.set_start_value(3)
        model.set_end_value(5)
        self.assertEqual(3, model.get_start_value())
        self.assertEqual(5, model.get_end_value())

    def test_calculate_cube_volume_5(self):
        model = VolumeViewModel(3, 5)
        model.set_figure_type(0)
        model.perform()
        self.assertEqual(125, model.get_result())

    def test_calculate_sphere_volume_3(self):
        model = VolumeViewModel(3, 5)
        model.set_figure_type(1)
        model.perform()
        self.assertEqual(113.097, model.get_result())

    def test_calculate_cylinder_volume_3_5(self):
        model = VolumeViewModel(3, 5)
        model.set_figure_type(2)
        model.perform()
        self.assertEqual(141.372, model.get_result())

    def test_entered_incorrect_values(self):
        model = VolumeViewModel('asd', '11a')
        self.assertEqual('disabled', model.is_button_enable())
