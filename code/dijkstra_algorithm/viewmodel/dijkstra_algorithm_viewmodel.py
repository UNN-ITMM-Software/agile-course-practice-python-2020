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
        self.num_vertex = ''
        self.start_vertex = ''
        self.errors = ''
        self.btn_create_graph_state = 'disabled'
        self.logger = logger
        self.logger.log('Welcome!')

    def set_num_vertex(self, value):
        self.logger.log('Setting number of vertex')
        self.num_vertex = value
        if is_correct_vertex_number(value):
            self.set_btn_create_graph_enabled()
            self.logger.log('Result from setting number of vertex: {}'.format(self.num_vertex))
        else:
            self.set_btn_create_graph_disabled()
            self.logger.log('Entered value isn\'t correct!')

    def get_num_vertex(self):
        return self.num_vertex

    def set_btn_create_graph_disabled(self):
        self.btn_create_graph_state = 'disabled'
        self.logger.log('Can\'t create graph')

    def set_btn_create_graph_enabled(self):
        self.btn_create_graph_state = 'normal'
        self.logger.log('Can create graph')

    def get_btn_create_graph_state(self):
        return self.btn_create_graph_state

    def set_start_vertex(self, start):
        self.logger.log('Setting start vertex')
        self.start_vertex = start
        self.logger.log('Result from setting start vertex: {}'.format(self.start_vertex))

    def get_start_vertex(self):
        return self.start_vertex

    def get_error(self):
        return self.errors

    def run_dijkstra(self, matrix):
        self.logger.log('Running dijkstra algorithm')
        try:
            weights = [[int(val) for val in row] for row in matrix]
            graph = Graph(int(self.num_vertex), weights)
            result = graph.dijkstra(int(self.start_vertex))
            self.errors = ''
            self.logger.log('Dijkstra algorithm successfully completed')
            return result
        except Exception as e:
            self.errors = str(e)
            self.logger.log('Error: {}'.format(self.errors))
            return []
