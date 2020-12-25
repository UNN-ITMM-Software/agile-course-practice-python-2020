from modified_stack.model.modified_stack import ModifiedStack

from modified_stack.logger.reallogger import RealLogger


def to_int(value):
    try:
        return int(value)
    except ValueError:
        raise ValueError('Input contains non int value')


class ModifiedStackViewModel(object):
    def __init__(self, logger=RealLogger()):
        self.logger = logger
        self.modified_stack = ModifiedStack()
        self.pushed_element = None
        self.push_state = None
        self.pop_size = None
        self.top = None
        self.min = None
        self.input_array = None
        self.error_message = None
        self.logger.log('Stack object was successfully created')

    def size(self):
        return self.modified_stack.size()

    def push(self):
        self.logger.log('Push button was clicked')
        self.clear_error_message()
        try:
            if self.push_state == 'One':
                self.modified_stack.push(to_int(self.pushed_element))
                self.logger.log('Operation push successfully completed with single element. Push: {}'.
                                format(to_int(self.pushed_element)))
            elif self.push_state == 'N':
                self.modified_stack.push([to_int(element) for element in self.input_array])
                self.logger.log('Operation push successfully completed with array. Push: {}'.
                                format(self.input_array))
        except Exception as e:
            self.set_error_message(str(e))
            self.logger.log('Push error: {}'.format(self.get_error_message()))

    def pop(self):
        self.logger.log('Pop button was clicked')
        self.clear_error_message()
        try:
            self.modified_stack.pop(to_int(self.pop_size))
            self.logger.log('Operation pop successfully completed. Pop: {}'.format(to_int(self.pop_size)))
        except Exception as e:
            self.set_error_message(str(e))
            self.logger.log('Pop error: {}'.format(self.get_error_message()))

    def get_top(self):
        self.logger.log('Getting top button was clicked')
        self.clear_error_message()
        if self.modified_stack.is_empty():
            self.set_error_message('Stack is empty')
            self.logger.log('Result from getting top element: {}'.format(self.get_error_message()))
        else:
            self.top = self.modified_stack.look_top()
            self.logger.log('Result from getting top element: {}'.format(self.top))

    def get_min(self):
        self.logger.log('Getting min button was clicked')
        self.clear_error_message()
        if self.modified_stack.is_empty():
            self.set_error_message('Stack is empty')
            self.logger.log('Result from getting min element: {}'.format(self.get_error_message()))
        else:
            self.min = self.modified_stack.find_min()
            self.logger.log('Result from getting min element: {}'.format(self.min))

    def set_pop_size(self, size):
        self.pop_size = size
        self.logger.log('Setting pop size to: {}'.format(self.pop_size))

    def set_push_state(self, state):
        self.push_state = state
        self.logger.log('Setting push state to: {}'.format(self.push_state))

    def set_pushed_element(self, value):
        self.pushed_element = value
        self.logger.log('Setting pushed element to: {}'.format(self.pushed_element))

    def set_input_array(self, input_array):
        self.input_array = input_array
        self.logger.log('Setting input array to: {}'.format(self.input_array))

    def set_error_message(self, message):
        self.error_message = message
        self.logger.log('Setting error message to: {}'.format(self.error_message))

    def get_error_message(self):
        return self.error_message

    def clear_error_message(self):
        self.error_message = None
        self.logger.log('Error message was successfully cleared')
