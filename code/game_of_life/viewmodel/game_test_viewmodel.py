import unittest

from game_of_life.logger.fakelogger import FakeLogger
from game_of_life.logger.reallogger import RealLogger
from game_of_life.viewmodel.game_viewmodel import GameOfLifeViewModel


def fake_default_field_for_tests():
    field = []
    for i in range(2):
        field.append([])
        for j in range(2):
            field[i].append(dict())
            field[i][j]["bg"] = "White"
    return field


class TestGameOfLifeViewModel(unittest.TestCase):
    def setUp(self):
        self.view_model = GameOfLifeViewModel()

    def test_by_default_next_step_btn_is_disabled(self):
        self.assertEqual('disabled', self.view_model.get_next_step_btn_state())

    def test_by_default_numbers_of_rows_is_2(self):
        self.assertEqual(2, self.view_model.get_number_of_rows())

    def test_by_default_numbers_of_columns_is_2(self):
        self.assertEqual(2, self.view_model.get_number_of_columns())

    def test_can_set_number_of_rows(self):
        self.view_model.set_number_of_rows(5)
        self.assertEqual(5, self.view_model.get_number_of_rows())

    def test_can_set_number_of_columns(self):
        self.view_model.set_number_of_columns(5)
        self.assertEqual(5, self.view_model.get_number_of_columns())

    def test_cant_remove_row_if_2_rows(self):
        self.assertEqual('disabled', self.view_model.get_remove_row_btn_state(2))

    def test_can_remove_row_if_more_than_2_rows(self):
        self.assertEqual('normal', self.view_model.get_remove_row_btn_state(5))

    def test_cant_remove_column_if_2_columns(self):
        self.assertEqual('disabled', self.view_model.get_remove_column_btn_state(2))

    def test_can_remove_column_if_more_than_2_columns(self):
        self.assertEqual('normal', self.view_model.get_remove_column_btn_state(5))

    def test_by_default_current_field_is_empty(self):
        self.assertEqual([], self.view_model.get_current_color_field())

    def test_by_default_next_field_is_empty(self):
        self.assertEqual([], self.view_model.get_next_color_field())

    def test_when_field_is_set_next_step_btn_is_enabled(self):
        self.view_model.set_current_color_field(fake_default_field_for_tests())
        self.view_model.color_changed(0, 0)
        self.assertEqual('normal', self.view_model.get_next_step_btn_state())

    def test_field_is_white_again_set_next_step_btn_is_disabled(self):
        self.view_model.set_current_color_field(fake_default_field_for_tests())
        self.view_model.color_changed(0, 0)
        self.view_model.color_changed(0, 0)
        self.assertEqual('disabled', self.view_model.get_next_step_btn_state())

    def test_by_default_all_is_white(self):
        self.view_model.set_current_color_field(fake_default_field_for_tests())
        self.assertTrue(self.view_model.is_all_white())

    def test_when_set_field_not_all_is_white(self):
        self.view_model.set_current_color_field(fake_default_field_for_tests())
        self.view_model.color_changed(0, 0)
        self.assertFalse(self.view_model.is_all_white())

    def test_convert_color_field_to_binary(self):
        self.view_model.set_current_color_field(fake_default_field_for_tests())
        self.view_model.color_changed(0, 1)
        self.view_model.color_changed(1, 0)
        self.view_model.convert_field_to_binary(self.view_model.current_color_field)
        self.assertTrue([[0, 1], [1, 0]] == self.view_model.current_binary_field)

    def test_convert_binary_field_to_color(self):
        self.view_model.next_binary_field = [[0, 1], [1, 0]]
        self.view_model.set_next_color_field(fake_default_field_for_tests())
        self.view_model.convert_field_to_color()
        result = fake_default_field_for_tests()
        result[0][1]["bg"] = "Black"
        result[1][0]["bg"] = "Black"
        for i in range(2):
            for j in range(2):
                self.assertEqual(result[i][j]['bg'], self.view_model.next_color_field[i][j]['bg'])

    def test_compute_next_step(self):
        self.view_model.set_current_color_field(fake_default_field_for_tests())
        self.view_model.set_next_color_field(fake_default_field_for_tests())
        self.view_model.color_changed(0, 0)
        self.view_model.color_changed(0, 1)
        self.view_model.color_changed(1, 0)

        self.view_model.compute_next_step()

        self.view_model.color_changed(1, 1)
        result = self.view_model.get_current_color_field()
        for i in range(2):
            for j in range(2):
                self.assertEqual(result[i][j]['bg'], self.view_model.next_color_field[i][j]['bg'])

    def test_no_changes_if_try_reduce_2_rows(self):
        self.view_model.set_number_of_rows(2)
        self.view_model.clicked_remove('row')
        self.assertEqual(2, self.view_model.get_number_of_rows())

    def test_no_changes_if_try_reduce_2_columns(self):
        self.view_model.set_number_of_columns(2)
        self.view_model.clicked_remove('column')
        self.assertEqual(2, self.view_model.get_number_of_columns())

    def test_remove_clicked_if_more_2_rows(self):
        self.view_model.set_number_of_rows(3)
        self.view_model.clicked_remove('row')
        self.assertEqual(2, self.view_model.get_number_of_rows())

    def test_remove_clicked_if_more_2_columns(self):
        self.view_model.set_number_of_columns(11)
        self.view_model.clicked_remove('column')
        self.assertEqual(10, self.view_model.get_number_of_columns())

    def test_add_rows_clicked(self):
        self.view_model.set_number_of_rows(3)
        self.view_model.clicked_add('row')
        self.assertEqual(4, self.view_model.get_number_of_rows())

    def test_add_columns_clicked(self):
        self.view_model.set_number_of_columns(11)
        self.view_model.clicked_add('column')
        self.assertEqual(12, self.view_model.get_number_of_columns())


class TestViewModelFakeLogging(unittest.TestCase):
    def setUp(self):
        self.view_model = GameOfLifeViewModel(FakeLogger())

    def test_logging_init(self):
        self.assertEqual('Welcome to Game of Life', self.view_model.logger.get_last_message())

    def test_logging_changing_number_of_rows(self):
        self.view_model.set_number_of_rows('2')
        self.assertEqual('Setting number of rows to 2', self.view_model.logger.get_last_message())

    def test_logging_changing_number_of_columns(self):
        self.view_model.set_number_of_columns('3')
        self.assertEqual('Setting number of columns to 3', self.view_model.logger.get_last_message())

    def test_logging_all(self):
        self.view_model.set_current_color_field(fake_default_field_for_tests())
        self.view_model.set_next_color_field(fake_default_field_for_tests())
        self.view_model.color_changed(0, 0)
        self.view_model.color_changed(0, 1)
        self.view_model.color_changed(1, 0)

        self.view_model.compute_next_step()

        self.view_model.color_changed(1, 1)
        result = ['Welcome to Game of Life', 'Button clicked']
        for i in range(2):
            for j in range(2):
                result.append('Next color field is %s' % self.view_model.next_color_field[i][j]['bg'])
        self.assertEqual(result, self.view_model.logger.get_log_messages())


class TestViewModelRealLogging(TestViewModelFakeLogging):
    def setUp(self):
        self.view_model = GameOfLifeViewModel(RealLogger())
