from enum import Enum

from fibonacci_heap.logger.reallogger import RealLogger
from fibonacci_heap.model.fibonacci_heap import FibonacciHeap, _Node


class State(Enum):
    ENABLED = 'normal'
    DISABLED = 'disabled'


class NodeOperations(Enum):
    INSERT = 'insert'
    DELETE = 'delete'
    FIND_MIN = 'find_min'


class HeapViewModel:
    """
    Main GUI model View
    """
    INFO_MSG = {
        'insert': 'Inserted node: key - %s, value - %s',
        'delete': 'Deleted node: key - %s',
        'find': 'Found node: key - %s, value - %s',
        'key_invalid': 'ERROR: key %s does not exist or has invalid format',
        'key_mess': 'ERROR: key %s already exists',
    }
    MAX_MESSAGE_NUMBER = 100

    def __init__(self, logger=RealLogger()):
        self.logger = logger
        self.logger.log('Welcome!')

        # heap operations
        self.heap = FibonacciHeap()
        self.key = ''
        self.value = ''
        self.unique_keys = []
        self.messages = []
        self.operation = NodeOperations.INSERT

        # UI states
        self.key_textbox_state = State.ENABLED
        self.value_textbox_state = State.ENABLED
        self.main_button_state = State.ENABLED
        self.set_value_textbox_enabled()
        self.set_main_button_disabled()

    def validate_text(self, operation=None):
        """
        Check if run button should be enabled
        """
        if operation == NodeOperations.DELETE or operation == NodeOperations.FIND_MIN:
            self.set_main_button_enabled()
        elif self.key and (self.value or self.value_textbox_state == State.DISABLED):
            self.set_main_button_enabled()
        else:
            self.set_main_button_disabled()

    def set_main_button_enabled(self):
        """
        Set enabled state to button
        """
        self.main_button_state = State.ENABLED

    def set_value_textbox_enabled(self):
        """
        Set disabled state to value input area
        """
        self.value_textbox_state = State.ENABLED

    def set_main_button_disabled(self):
        """
        Set disabled state to button
        """
        self.main_button_state = State.DISABLED

    def set_value_textbox_disabled(self):
        """
        Set disabled state to value input area
        """
        self.value_textbox_state = State.DISABLED

    def get_main_button_state(self):
        """
        Get current button state
        :return: State value
        """
        return self.main_button_state.value

    def set_key_textbox_disabled(self):
        """
        Set disabled state to key input area
        """
        self.key_textbox_state = State.DISABLED

    def get_value_textbox_state(self):
        """
        Get current value input area state
        :return: State value
        """
        return self.value_textbox_state.value

    def set_key(self, key):
        """
        Set key value
        :param key: value to set
        """
        self.logger.log('Set key is %s' % key)
        self.key = key
        self.validate_text()

    def set_value(self, value):
        """
        Set node value
        :param value: value to set
        """

        self.logger.log('Set value is %s' % value)
        self.value = value
        self.validate_text()

    def get_message_text(self):
        """
        Get messages
        :return: messages as one multiline string
        """
        return '\n'.join(self.messages)

    def update_messages(self, new_message):
        """
        Update messages
        :param new_message: new message to add
        """
        self.messages.insert(0, new_message)
        if len(self.messages) > self.MAX_MESSAGE_NUMBER:
            self.messages = self.messages[:self.MAX_MESSAGE_NUMBER]

    def set_operation(self, operation):
        """
        Set operation to do by clicking button
        :param operation: operation to do
        """
        self.operation = operation
        if operation == NodeOperations.FIND_MIN:
            self.set_value_textbox_disabled()
            self.set_value('')

            self.set_key_textbox_disabled()
            self.set_key('')

        if operation == NodeOperations.DELETE:
            self.set_value_textbox_disabled()
            self.set_value('')
        else:
            self.set_value_textbox_enabled()
        self.validate_text(operation)

    def click_run_button(self):
        """
        Process selected operations by clicking button
        :return: None
        """
        if self.main_button_state == State.DISABLED:
            return

        self.logger.log('Run button clicked')
        self.logger.log('Selected operation is %s' % self.operation)
        if self.operation == NodeOperations.INSERT:
            try:
                self.heap.insert(int(self.key), self.value)
                self.unique_keys.append(self.key)

                msg = self.INFO_MSG['insert'] % (self.key, self.value)
                self.logger.log(msg)
                self.update_messages(msg)
            except ValueError:
                msg = self.INFO_MSG['key_invalid'] % self.key
                self.logger.error(msg)
                self.update_messages(msg)

        elif self.operation == NodeOperations.DELETE:
            try:
                node = _Node(int(self.key), self.value)
                self.heap.delete(node)
                self.update_messages(self.INFO_MSG['delete'] % self.key)
            except (ValueError, AssertionError):
                msg = self.INFO_MSG['key_invalid'] % self.key
                self.logger.error(msg)
                self.update_messages(msg)

        elif self.operation == NodeOperations.FIND_MIN:
            min_node = self.heap.find_min()
            key, val = min_node.key, min_node.val

            msg = self.INFO_MSG['find'] % (key, val)
            self.logger.log(msg)
            self.update_messages(msg)
