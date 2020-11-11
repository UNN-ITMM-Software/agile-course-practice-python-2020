import unittest

from game_of_life import GameOfLife
from game_of_life import GameOfLifeParser


class TestGameOfLifeClass(unittest.TestCase):
    def test_add_empty_string_is_0(self):
        strcalc = GameOfLife()
        result = strcalc.add("")
        self.assertTrue(result == 0)

    def test_add_2x2_all_points_are_dead(self):
        strcalc = GameOfLife()
        result = strcalc.add("..\n..")
        field_test = "..\n.."
        self.assertTrue(result == field_test)

    def test_add_2x2_first_point_live(self):
        strcalc = GameOfLife()
        result = strcalc.add("*.\n..")
        field_test = "..\n.."
        self.assertTrue(result == field_test)

    def test_add_2x2_two_points_on_the_first_line_are_live(self):
        strcalc = GameOfLife()
        result = strcalc.add("**\n..")
        field_test = "..\n.."
        self.assertTrue(result == field_test)

    def test_add_2x2_last_point_is_dead(self):
        strcalc = GameOfLife()
        result = strcalc.add("**\n*.")
        field_test = "**\n**"
        self.assertTrue(result == field_test)

    def test_add_3x3_living_square(self):
        strcalc = GameOfLife()
        result = strcalc.add("**.\n*..\n...")
        field_test = "**.\n**.\n..."
        self.assertTrue(result == field_test)

    def test_add_4x8_general_example(self):
        strcalc = GameOfLife()
        result = strcalc.add("........\n....*...\n...**...\n........")
        field_test = "........\n...**...\n...**...\n........"
        self.assertTrue(result == field_test)

    def test_add_4x8_line(self):
        strcalc = GameOfLife()
        result = strcalc.add("........\n...***..\n........\n........")
        field_test = "....*...\n....*...\n....*...\n........"
        self.assertTrue(result == field_test)

    def test_counting_neighbors_0(self):
        parser = GameOfLifeParser()
        game_of_life = GameOfLife()
        field = parser.parse("........\n....*...\n........\n........")
        result = game_of_life.counting_neighbors(field, 1, 4)
        self.assertTrue(result == 0)

    def test_counting_neighbors_8(self):
        parser = GameOfLifeParser()
        game_of_life = GameOfLife()
        field = parser.parse("...***..\n...***..\n...***..\n........")
        result = game_of_life.counting_neighbors(field, 1, 4)
        self.assertTrue(result == 8)

    def test_counting_neighbors_5(self):
        parser = GameOfLifeParser()
        game_of_life = GameOfLife()
        field = parser.parse("...***..\n...***..\n...***..\n........")
        result = game_of_life.counting_neighbors(field, 1, 3)
        self.assertTrue(result == 5)

    def test_counting_neighbors_3_x_0_y_0(self):
        parser = GameOfLifeParser()
        game_of_life = GameOfLife()
        field = parser.parse(".*......\n**......\n........\n........")
        result = game_of_life.counting_neighbors(field, 0, 0)
        self.assertTrue(result == 3)

    def test_counting_neighbors_3_x_8_y_4(self):
        parser = GameOfLifeParser()
        game_of_life = GameOfLife()
        field = parser.parse("........\n........\n......**\n......**")
        result = game_of_life.counting_neighbors(field, 3, 7)
        self.assertTrue(result == 3)

    def test_convert_to_string_2x2_all_points_are_dead(self):
        converter = GameOfLife()
        field_test = [[0 for i in range(2)] for j in range(2)]
        result = converter.convert_to_string(field_test)
        self.assertTrue(result == "..\n..")

    def test_convert_to_string_2x2_first_point_live(self):
        converter = GameOfLife()
        field_test = [[0 for i in range(2)] for j in range(2)]
        field_test[0][0] = 1
        result = converter.convert_to_string(field_test)
        self.assertTrue(result == "*.\n..")

    def test_convert_to_string_2x2_second_point_live(self):
        converter = GameOfLife()
        field_test = [[0 for i in range(2)] for j in range(2)]
        field_test[0][1] = 1
        result = converter.convert_to_string(field_test)
        self.assertTrue(result == ".*\n..")

    def test_convert_to_string_2x2_two_points_second_column_live(self):
        converter = GameOfLife()
        field_test = [[0 for i in range(2)] for j in range(2)]
        field_test[0][1] = 1
        field_test[1][1] = 1
        result = converter.convert_to_string(field_test)
        self.assertTrue(result == ".*\n.*")

    def test_convert_to_string_4x4_last_point_live(self):
        converter = GameOfLife()
        field_test = [[0 for i in range(4)] for j in range(4)]
        field_test[3][3] = 1
        result = converter.convert_to_string(field_test)
        self.assertTrue(result == "....\n....\n....\n...*")

    def test_convert_to_string_4x8_general_example(self):
        converter = GameOfLife()
        field_test = [[0 for i in range(8)] for j in range(4)]
        field_test[1][4] = 1
        field_test[2][3] = 1
        field_test[2][4] = 1
        result = converter.convert_to_string(field_test)
        self.assertTrue(result == "........\n....*...\n...**...\n........")


class TestGameOfLifeParserClass(unittest.TestCase):
    def test_can_create_parser(self):
        parser = GameOfLifeParser()
        self.assertTrue(isinstance(parser, GameOfLifeParser))

    def test_parse_check_string_2x2_all_points_are_dead(self):
        parser = GameOfLifeParser()
        field_test = [[0 for i in range(2)] for j in range(2)]
        result = parser.parse("..\n..")
        self.assertTrue(result == field_test)

    def test_parse_check_string_2x2_first_point_live(self):
        parser = GameOfLifeParser()
        field_test = [[0 for i in range(2)] for j in range(2)]
        field_test[0][0] = 1
        result = parser.parse("*.\n..")
        self.assertTrue(result == field_test)

    def test_parse_check_string_2x2_second_point_live(self):
        parser = GameOfLifeParser()
        field_test = [[0 for i in range(2)] for j in range(2)]
        field_test[0][1] = 1
        result = parser.parse(".*\n..")
        self.assertTrue(result == field_test)

    def test_parse_check_string_3x3_second_point_live(self):
        parser = GameOfLifeParser()
        field_test = [[0 for i in range(3)] for j in range(3)]
        field_test[0][1] = 1
        result = parser.parse(".*.\n...\n...")
        self.assertTrue(result == field_test)

    def test_parse_check_string_3x2_second_point_live(self):
        parser = GameOfLifeParser()
        field_test = [[0 for i in range(2)] for j in range(3)]
        field_test[0][1] = 1
        result = parser.parse(".*\n..\n..")
        self.assertTrue(result == field_test)

    def test_parse_check_string_3x3_second_line_second_point_live(self):
        parser = GameOfLifeParser()
        field_test = [[0 for i in range(3)] for j in range(3)]
        field_test[1][1] = 1
        result = parser.parse("...\n.*.\n...")
        self.assertTrue(result == field_test)

    def test_parse_check_string_3x2_second_line_second_point_live(self):
        parser = GameOfLifeParser()
        field_test = [[0 for i in range(2)] for j in range(3)]
        field_test[1][1] = 1
        result = parser.parse("..\n.*\n..")
        self.assertTrue(result == field_test)

    def test_parse_check_string_4x4_last_point_live(self):
        parser = GameOfLifeParser()
        field_test = [[0 for i in range(4)] for j in range(4)]
        field_test[3][3] = 1
        result = parser.parse("....\n....\n....\n...*")
        self.assertTrue(result == field_test)

    def test_parse_check_string_3x2_last_point_live(self):
        parser = GameOfLifeParser()
        field_test = [[0 for i in range(3)] for j in range(4)]
        field_test[3][2] = 1
        result = parser.parse("...\n...\n...\n..*")
        self.assertTrue(result == field_test)

    def test_parse_check_string_4x8_general_example(self):
        parser = GameOfLifeParser()
        field_test = [[0 for i in range(8)] for j in range(4)]
        field_test[1][4] = 1
        field_test[2][3] = 1
        field_test[2][4] = 1
        result = parser.parse("........\n....*...\n...**...\n........")
        self.assertTrue(result == field_test)
