import unittest

from game_of_life import GameOfLife


class TestGameOfLifeClass(unittest.TestCase):
    def test_start_2x2_all_points_are_dead(self):
        game = GameOfLife()
        field_test = [[0, 0],
                      [0, 0]]
        result = game.start(field_test)
        self.assertTrue(result == field_test)

    def test_start_2x2_first_point_live(self):
        game = GameOfLife()
        field_test = [[1, 0],
                      [0, 0]]
        result = game.start(field_test)
        correct_field = [[0, 0],
                         [0, 0]]
        self.assertTrue(result == correct_field)

    def test_start_2x2_two_points_on_the_first_line_are_live(self):
        game = GameOfLife()
        field_test = [[1, 1],
                      [0, 0]]
        result = game.start(field_test)
        correct_field = [[0, 0],
                         [0, 0]]
        self.assertTrue(result == correct_field)

    def test_start_2x2_last_point_is_dead(self):
        game = GameOfLife()
        field_test = [[1, 1],
                      [1, 0]]
        result = game.start(field_test)
        correct_field = [[1, 1],
                         [1, 1]]
        self.assertTrue(result == correct_field)

    def test_start_3x3_living_square(self):
        game = GameOfLife()
        field_test = [[1, 1, 0],
                      [1, 0, 0],
                      [0, 0, 0]]
        result = game.start(field_test)
        correct_field = [[1, 1, 0],
                         [1, 1, 0],
                         [0, 0, 0]]
        self.assertTrue(result == correct_field)

    def test_start_4x8_general_example(self):
        game = GameOfLife()
        field_test = [[0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 1, 0, 0, 0],
                      [0, 0, 0, 1, 1, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0]]
        result = game.start(field_test)
        correct_field = [[0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 1, 1, 0, 0, 0],
                         [0, 0, 0, 1, 1, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0]]
        self.assertTrue(result == correct_field)

    def test_start_4x8_line(self):
        game = GameOfLife()
        field_test = [[0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 1, 1, 1, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0]]
        result = game.start(field_test)
        correct_field = [[0, 0, 0, 0, 1, 0, 0, 0],
                         [0, 0, 0, 0, 1, 0, 0, 0],
                         [0, 0, 0, 0, 1, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0]]
        self.assertTrue(result == correct_field)

    def test_start_4x8_column(self):
        game = GameOfLife()
        field_test = [[0, 0, 0, 0, 1, 0, 0, 0],
                      [0, 0, 0, 0, 1, 0, 0, 0],
                      [0, 0, 0, 0, 1, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0]]
        result = game.start(field_test)
        correct_field = [[0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 1, 1, 1, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0]]
        self.assertTrue(result == correct_field)
