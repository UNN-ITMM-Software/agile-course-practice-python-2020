import unittest

from dijkstra_algorithm.logger.fakelogger import FakeLogger
from dijkstra_algorithm.logger.reallogger import RealLogger
from dijkstra_algorithm.viewmodel.dijkstra_algorithm_viewmodel import DAViewModel


class TestDAViewModel(unittest.TestCase):

    def test_by_default_button_create_graph_disable(self):
        model = DAViewModel()

        self.assertEqual('disabled', model.get_btn_create_graph_state())

    def test_when_enter_correct_number_button_create_graph_enabled(self):
        model = DAViewModel()
        model.set_num_vertex('5')

        self.assertEqual('normal', model.get_btn_create_graph_state())

    def test_when_clear_number_button_create_graph_disabled(self):
        model = DAViewModel()
        model.set_num_vertex(None)

        self.assertEqual('disabled', model.get_btn_create_graph_state())

    def test_when_enter_less_zero_number_button_create_graph_disabled(self):
        model = DAViewModel()
        model.set_num_vertex('-1')

        self.assertEqual('disabled', model.get_btn_create_graph_state())

    def test_when_enter_incorrect_number_button_create_graph_keeps_disabled(self):
        model = DAViewModel()
        model.set_num_vertex('some incorrect input')

        self.assertEqual('disabled', model.get_btn_create_graph_state())

    def test_can_get_vertex_number(self):
        model = DAViewModel()
        model.set_num_vertex('5')

        self.assertEqual('5', model.get_num_vertex())

    def test_can_set_get_start_vertex(self):
        model = DAViewModel()
        model.set_start_vertex('0')

        self.assertEqual('0', model.get_start_vertex())

    def test_run_dijkstra_return_correct_result(self):
        model = DAViewModel()

        model.set_num_vertex('3')
        model.set_start_vertex('2')
        matrix = [['0', '2', '1'], ['2', '0', '3'], ['1', '3', '0']]

        self.assertEqual(model.run_dijkstra(matrix), [1, 3, 0])

    def test_run_dijkstra_with_incorrect_weights_return_error(self):
        model = DAViewModel()

        model.set_num_vertex('3')
        model.set_start_vertex('2')
        matrix = [['0', '5', '1'], ['2', '0', '3'], ['1', '3', '0']]
        model.run_dijkstra(matrix)

        self.assertEqual(model.get_error(), "Matrix is not symmetric")

    def test_run_dijkstra_with_incorrect_start_vertex_return_error(self):
        model = DAViewModel()

        model.set_num_vertex('3')
        model.set_start_vertex('-2')
        matrix = [['0', '2', '1'], ['2', '0', '3'], ['1', '3', '0']]
        model.run_dijkstra(matrix)

        self.assertEqual(model.get_error(), "Wrong value of source vertex")


class TestViewModelFakeLogging(unittest.TestCase):
    def setUp(self):
        self.view_model = DAViewModel(FakeLogger())

    def test_logging_init(self):
        self.assertEqual('Welcome!', self.view_model.logger.get_last_message())

    def test_logging_enable_set_graph_button(self):
        self.view_model.set_btn_create_graph_enabled()

        self.assertEqual('Can create graph', self.view_model.logger.get_last_message())

    def test_logging_disable_set_graph_button(self):
        self.view_model.set_btn_create_graph_disabled()

        self.assertEqual('Can\'t create graph', self.view_model.logger.get_last_message())

    def test_logging_set_start_vertex(self):
        self.view_model.set_start_vertex('322')

        self.assertEqual('Result from setting start vertex: 322', self.view_model.logger.get_last_message())

    def test_logging_set_correct_vertex_number(self):
        self.view_model.set_num_vertex('5')

        self.assertEqual('Result from setting number of vertex: 5', self.view_model.logger.get_last_message())

    def test_logging_set_incorrect_vertex_number(self):
        self.view_model.set_num_vertex('Z')

        self.assertEqual('Entered value isn\'t correct!', self.view_model.logger.get_last_message())

    def test_logging_run_dijkstra_return_correct_result(self):
        self.view_model.set_num_vertex('3')
        self.view_model.set_start_vertex('2')
        matrix = [['0', '2', '1'], ['2', '0', '3'], ['1', '3', '0']]
        self.view_model.run_dijkstra(matrix)

        self.assertEqual('Dijkstra algorithm successfully completed',
                         self.view_model.logger.get_last_message())

    def test_logging_run_dijkstra_return_error(self):
        self.view_model.set_num_vertex('2')
        self.view_model.set_start_vertex('0')
        matrix = [['A', 'B'], ['C', 'D']]
        self.view_model.run_dijkstra(matrix)

        self.assertEqual('Error: invalid literal for int() with base 10: \'A\'',
                         self.view_model.logger.get_last_message())


class TestViewModelRealLogging(TestViewModelFakeLogging):
    def setUp(self):
        self.view_model = DAViewModel(RealLogger())
