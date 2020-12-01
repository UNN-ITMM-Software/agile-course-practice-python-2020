# import unittest
#
# from matrix.viewmodel.viewmodel import MatrixViewModel
# from matrix.infrastructure.fake_logger import FakeLogger
# from matrix.infrastructure.real_logger import RealLogger
#
#
# class TestForViewModel(unittest.TestCase):
#
#     def setUp(self):
#         self.view_model = MatrixViewModel(FakeLogger())
#
#     def test_check_number_or_rows_in_init(self):
#         self.assertEqual(self.view_model.get_number_of_rows(), 3)
#
#     def test_check_init_matrix_by_zero_values(self):
#         self.assertEqual(self.view_model.get_matrix_as_list(), [[0]*3]*3)
#
#     def test_check_init_matrix_by_non_zero_values(self):
#         content = [[2, 1, 2], [0, 3, 0], [3, 1, 1]]
#         self.view_model.update_matrix_content(content)
#         self.assertEqual(self.view_model.get_matrix_as_list(), [[2, 1, 2], [0, 3, 0], [3, 1, 1]])
#
#     def test_get_number_of_rows(self):
#         self.view_model.set_number_of_rows(4)
#         self.assertEqual(self.view_model.get_number_of_rows(), 4)
#
#     def test_change_matrix_rank(self):
#         self.view_model.set_number_of_rows(4)
#         self.assertEqual(self.view_model.init_zero_matrix_with_new_rank_value(), [[0]*4]*4)
#
#     def test_calculate_determinant(self):
#         content = [[2, 1, 2], [0, 3, 0], [3, 1, 1]]
#         self.view_model.update_matrix_content(content)
#         self.assertEqual(self.view_model.calculate_determinant(), -12)
#
#     def test_set_answer(self):
#         answer_str = '1'
#         self.view_model.set_answer(answer_str)
#         self.assertEqual(self.view_model.answer, answer_str)
#
#     def test_check_correct_answer(self):
#         content = [[2, 1, 2], [0, 3, 0], [3, 1, 1]]
#         self.view_model.update_matrix_content(content)
#         self.view_model.calculate_determinant()
#         self.assertEqual(self.view_model.answer, -12)
#
#
# class TestForViewModeWithFakeLogging(unittest.TestCase):
#     def setUp(self):
#         self.view_model = MatrixViewModel(FakeLogger())
#
#     def test_start_logging(self):
#         self.assertEqual(['\n\n##    Start logging...    ##'],
#                          self.view_model.my_logger.get_last_messages_from_logs_list(1))
#
#     def test_get_number_of_rows_logging(self):
#         self.view_model.get_number_of_rows()
#         self.assertEqual(['Getting matrix\'s rows: 3'],
#                          self.view_model.my_logger.get_last_messages_from_logs_list(1))
#
#     def test_set_number_of_rows(self):
#         self.view_model.set_number_of_rows(4)
#         self.assertEqual(['Setting matrix\'s rows: 4'],
#                          self.view_model.my_logger.get_last_messages_from_logs_list(1))
#
#     def test_get_matrix_as_list(self):
#         self.view_model.get_matrix_as_list()
#         self.assertEqual(['Getting matrix as data lines: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]'],
#                          self.view_model.my_logger.get_last_messages_from_logs_list(1))
#
#     def test_set_answer(self):
#         self.view_model.set_answer('0')
#         self.assertEqual(['Setting answer: 0'], self.view_model.my_logger.get_last_messages_from_logs_list(1))
#
#     def test_update_matrix_content(self):
#         content = [[2, 1, 2], [0, 3, 0], [3, 1, 1]]
#         self.view_model.update_matrix_content(content)
#         self.assertEqual(['Updating matrix\'s content: [[2, 1, 2], [0, 3, 0], [3, 1, 1]]'],
#                          self.view_model.my_logger.get_last_messages_from_logs_list(1))
#
#     def test_calculate_determinant(self):
#         content = [[2, 1, 2], [0, 3, 0], [3, 1, 1]]
#         self.view_model.update_matrix_content(content)
#         self.view_model.calculate_determinant()
#         self.assertEqual(['Calculating determinant: -12'],
#                          self.view_model.my_logger.get_last_messages_from_logs_list(1))
#
#     def test_init_zero_matrix_with_new_rank_value(self):
#         self.view_model.init_zero_matrix_with_new_rank_value()
#         self.assertEqual(['Getting matrix as data lines: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]'],
#                          self.view_model.my_logger.get_last_messages_from_logs_list(1))
#
#
# class TestForViewModeWithRealLogging(TestForViewModeWithFakeLogging):
#     def setUp(self):
#         self.view_model = MatrixViewModel(RealLogger())
