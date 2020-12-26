from galochkin_aleksei_lab_1.model.node import Node


class NodeViewModel:
    def __init__(self):
        self.input_value = ''
        self.root_node = None
        self.error = ''
        self.output_value = []

    def add_node(self):
        try:
            self.clear_error()
            if self.root_node is None:
                self.root_node = Node(self.input_value)
            else:
                Node.insert(self.root_node, self.input_value)

            result_list = []
            Node.dfs(self.root_node, result_list)
            self.output_value = result_list

        except ValueError:
            self.error = "Please enter numeric positive value"

    def remove_node(self):
        self.clear_error()
        Node.remove(self.root_node, self.input_value)

        result_list = []
        Node.dfs(self.root_node, result_list)
        self.output_value = result_list

    def get_error(self):
        return self.error

    def set_input_value(self, value):
        self.input_value = value

    def get_input_value(self):
        return self.input_value

    def get_output_value(self):
        return self.output_value

    def clear_error(self):
        self.error = ''
