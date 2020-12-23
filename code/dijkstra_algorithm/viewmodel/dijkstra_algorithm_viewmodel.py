from dijkstra_algorithm.logger.reallogger import RealLogger
from dijkstra_algorithm.model.dijkstra import Graph


def is_correct_vertex_number(value):
    try:
        value = int(value)
        return True if value > 0 else False
    except (ValueError, TypeError):
        return False


class DAViewModel:
    def __init__(self, logger=RealLogger()):
        self.logger = logger
        self.num_vertex = ''
        self.start_vertex = ''
        self.errors = ''
        self.btn_create_graph_state = 'disabled'

    def set_num_vertex(self, value):
        self.num_vertex = value
        if is_correct_vertex_number(value):
            self.set_btn_create_graph_enabled()
        else:
            self.set_btn_create_graph_disabled()

    def get_num_vertex(self):
        return self.num_vertex

    def set_btn_create_graph_disabled(self):
        self.btn_create_graph_state = 'disabled'

    def set_btn_create_graph_enabled(self):
        self.btn_create_graph_state = 'normal'

    def get_btn_create_graph_state(self):
        return self.btn_create_graph_state

    def set_start_vertex(self, start):
        self.start_vertex = start
        self.logger.log('Setting start vertex to: {}'.format(self.start_vertex))

    def get_start_vertex(self):
        return self.start_vertex

    def get_error(self):
        return self.errors

    def run_dijkstra(self, matrix):
        try:
            weights = [[int(val) for val in row] for row in matrix]
            graph = Graph(int(self.num_vertex), weights)
            result = graph.dijkstra(int(self.start_vertex))
            self.errors = ''
            return result
        except Exception as e:
            self.errors = str(e)
            return []
