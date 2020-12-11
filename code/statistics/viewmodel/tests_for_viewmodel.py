import unittest

from statistics.viewmodel.viewmodel import StatisticsViewModel


class TestStatisticsViewModel(unittest.TestCase):

    def setUp(self):
        self.view_model = StatisticsViewModel()

    def test_by_default_button_disabled(self):
        self.assertEqual('disabled', self.view_model.get_button_convert_state())
