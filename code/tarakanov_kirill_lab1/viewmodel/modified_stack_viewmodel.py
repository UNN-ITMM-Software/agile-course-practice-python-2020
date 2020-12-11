from tarakanov_kirill_lab1.model.modified_stack import ModifiedStack


class ModifiedStackViewModel(object):
    def __init__(self):
        self.pushed_element = None
        self.top = None
        self.min = None
        self.pop_size = None
        self.modified_stack = ModifiedStack()
        self.error_message = None

    def set_pushed_element(self, value):
        self.pushed_element = int(value)

    def push(self):
        self.modified_stack.push(self.pushed_element)

    def pop(self):
        try:
            self.modified_stack.pop(int(self.pop_size))
            self.clear_error_message()
        except Exception as e:
            self.error_message = str(e)

    def get_top(self):
        self.top = self.modified_stack.look_top()

    def get_min(self):
        self.min = self.modified_stack.find_min()

    def set_pop_size(self, size):
        self.pop_size = size

    def get_error_message(self):
        return self.error_message

    def clear_error_message(self):
        self.error_message = None

# def is_correct_vertex_number(value):
#     if value is None or len(str(value).strip()) == 0:
#         return False
#     else:
#         is_int_value = re.match("[1-9]\\d*$", str(value))
#         if is_int_value is None:
#             return False
#         else:
#             return True


class DAViewModel:
    def __init__(self):
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
        except Exception:
            self.errors = "Smth wrong with weights or start vertex"
            return []