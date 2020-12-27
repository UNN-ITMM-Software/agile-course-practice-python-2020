from galochkin_aleksei_lab_1.model.node import Node
from galochkin_aleksei_lab_1.logger.real_logger import RealLogger


class NodeViewModel:
    def __init__(self, logger=RealLogger()):
        self.logger = logger
        self.input_value = ''
        self.root_node = None
        self.error = ''
        self.output_value = []
        self.log_message = ''

    def add_node(self):
        try:
            self.clear_error()
            self.logger.log('Trying to add node with number {}'.format(self.input_value))
            if self.root_node is None:
                self.root_node = Node(self.input_value)
            else:
                Node.insert(self.root_node, self.input_value)

            result_list = []
            Node.dfs(self.root_node, result_list)
            self.output_value = result_list
            self.logger.log('Node added successfully')

        except ValueError:
            self.error = "Please enter numeric positive value"
            self.log_message = "Error occurred: {}".format(self.error)

    def remove_node(self):
        self.clear_error()
        self.logger.log('Trying to remove node with number {}'.format(self.input_value))
        Node.remove(self.root_node, self.input_value)

        result_list = []
        Node.dfs(self.root_node, result_list)
        self.output_value = result_list
        self.logger.log('Node removed successfully')

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

    def get_log_message(self):
        return self.log_message
