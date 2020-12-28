from tree.model.tree import Tree


class TreeViewModel:
    def __init__(self, size=None, logger=RealLogger()):
        self.input_button_enabled = 'disabled'
        self.find_button_enabled = 'disabled'

        self.tree = None
        self.input_value = None
        self.find_value = None
        self.find_result = ""
        self.error = ""
    
        self.logger = logger
        self.logger.log('Program started')

    def validate_input(self):
        if isinstance(self.input_value, int):
            self.set_input_button_enabled()
            return True
        else:
            self.set_input_button_disabled()
            return False

    def validate_find(self):
        if isinstance(self.find_value, int):
            self.set_find_button_enabled()
            return True
        else:
            self.set_find_button_disabled()
            return False

    def set_input_button_enabled(self):
        self.input_button_enabled = 'normal'

    def set_input_button_disabled(self):
        self.input_button_enabled = 'disabled'

    def set_find_button_enabled(self):
        self.find_button_enabled = 'normal'

    def set_find_button_disabled(self):
        self.find_button_enabled = 'disabled'

    def input_click(self):
        if self.validate_input() and self.is_input_button_enable() == 'normal':
            try:
                self.clear_find_result()
                self.clear_error()
                if self.tree is None:
                    self.tree = Tree(self.input_value)
                else:
                    self.tree.insert(self.input_value)
                self.set_find_button_enabled()
                self.logger.log('Число %s добавлено' % self.input_value)
            except:
                self.error = 'Error insert value'
                self.logger.log(self.error)
        else:
            self.error = 'Incorrect input value'
            self.logger.log(self.error)

    def find_click(self):
        if self.tree is not None and self.validate_find() and self.is_find_button_enable():
            try:
                self.clear_find_result()
                self.clear_error()
                self.find_result = self.tree.find_value(self.find_value)
                self.logger.log('Результат поиска %s' % self.find_result)
            except:
                self.error = 'Error find value'
                self.logger.log(self.error)
        else:
            self.error = 'Incorrect find value or empty Tree'
            self.logger.log(self.error)

    def set_input_value(self, value):
        try:
            self.input_value = int(value)
        except:
            self.input_value = value
        self.validate_input()

    def set_find_value(self, value):
        try:
            self.find_value = int(value)
        except:
            self.find_value = value
        self.validate_find()

    def get_input_value(self):
        return self.input_value

    def get_find_value(self):
        return self.find_value

    def get_find_result(self):
        return self.find_result

    def clear_find_result(self):
        self.find_result = ""

    def is_input_button_enable(self):
        return self.input_button_enabled

    def is_find_button_enable(self):
        return self.find_button_enabled

    def get_tree_values(self):
        if self.tree is not None:
            return self.tree.get_tree()
        else:
            return ""

    def clear_error(self):
        self.error = ""

    def get_error(self):
        return self.error

    def get_log_messages(self):
        return self.logger.get_log_messages()
