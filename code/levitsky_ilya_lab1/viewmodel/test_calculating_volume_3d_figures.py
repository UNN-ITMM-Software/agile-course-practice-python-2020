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


class TestLoggerViewModel(unittest.TestCase):
    def test_init_logging(self):
        model = VolumeViewModel()
        self.assertEqual('Hi!', model.logger.get_last_message())

    def test_set_start_value_logging(self):
        model = VolumeViewModel()
        model.set_start_value(4)
        self.assertEqual('Setting radius value - 4', model.logger.get_last_message())

    def test_set_end_value_logging(self):
        model = VolumeViewModel()
        model.set_end_value(6)
        self.assertEqual('Setting height value - 6', model.logger.get_last_message())

    def test_model_perform_logging(self):
        model = VolumeViewModel()
        model.set_start_value(3)
        model.set_end_value(10)
        model.perform()
        self.assertEqual('Result = 1000', model.logger.get_last_message())

    def test_model_perform_all_message_logging(self):
        model = VolumeViewModel()
        model.set_start_value(3)
        model.set_end_value(10)
        model.perform()

        log_message = ['Hi!', 'Setting radius value - 3',
                       'Setting height value - 10', 'Radiobutton 0 (cube) selected',
                       'Result = 1000']
        self.assertEqual(log_message, model.logger.get_log_messages()[-5:])

    def test_model_sphere_message_logging(self):
        model = VolumeViewModel()
        model.set_figure_type(1)
        model.set_start_value(10)
        model.set_end_value(3)
        model.perform()

        log_message = ['Hi!', 'Setting radius value - 10',
                       'Setting height value - 3', 'Radiobutton 1 (sphere) selected',
                       'Result = 4188.79']
        self.assertEqual(log_message, model.logger.get_log_messages()[-5:])

    def test_model_cylinder_message_logging(self):
        model = VolumeViewModel()
        model.set_figure_type(2)
        model.set_start_value(10)
        model.set_end_value(3)
        model.perform()

        log_message = ['Hi!', 'Setting radius value - 10',
                       'Setting height value - 3', 'Radiobutton 2 (cylinder) selected',
                       'Result = 942.478']
        self.assertEqual(log_message, model.logger.get_log_messages()[-5:])
