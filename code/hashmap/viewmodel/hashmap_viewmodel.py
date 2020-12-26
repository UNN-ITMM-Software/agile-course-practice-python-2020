from hashmap.model.hashmap import Hashmap
from hashmap.logger.reallogger import RealLogger
from enum import Enum


class HashmapOperation(Enum):
    INSERT = "insert"
    DELETE = "delete"
    GET = "get"
    UPDATE = "update"


class State(Enum):
    ENABLED = "normal"
    DISABLED = "disabled"


class HashmapViewModel:
    MSG_TYPES = {
        "insert_msg": "Insert: key is '%s', value is '%s'",
        "delete_msg": "Delete: key is '%s'",
        "get_msg": "Get: key is '%s', found value is '%s'",
        "update_msg": "Update: key is '%s', value is '%s'",
        "key_not_exist_msg": "ERROR: key '%s' does not exist",
        "key_exist_msg": "ERROR: key '%s' already exists",
    }
    MAX_MESSAGE_NUMBER = 10

    def __init__(self, logger=RealLogger()):
        self.logger = logger
        self.logger.log("create view")
        self.hashmap = Hashmap()
        self.messages = []
        self.key = ""
        self.value = ""
        self.operation = HashmapOperation.INSERT
        self.set_value_textbox_enabled()
        self.set_button_run_disabled()

    def validate_text(self):
        if self.key and (self.value or self.value_textbox_state == State.DISABLED):
            self.set_button_run_enabled()
        else:
            self.set_button_run_disabled()

    def set_button_run_enabled(self):
        self.button_run_state = State.ENABLED

    def set_button_run_disabled(self):
        self.button_run_state = State.DISABLED

    def get_button_run_state(self):
        return self.button_run_state.value

    def set_value_textbox_enabled(self):
        self.value_textbox_state = State.ENABLED

    def set_value_textbox_disabled(self):
        self.set_value("")
        self.value_textbox_state = State.DISABLED

    def get_value_textbox_state(self):
        return self.value_textbox_state.value

    def get_key(self):
        return self.key

    def set_key(self, key):
        self.key = key
        self.validate_text()

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value
        self.validate_text()

    def get_message_text(self):
        return "\n".join(self.messages)

    def update_messages(self, new_message):
        self.messages.insert(0, new_message)
        if len(self.messages) > self.MAX_MESSAGE_NUMBER:
            self.messages = self.messages[:self.MAX_MESSAGE_NUMBER]

    def set_operation(self, operation):
        self.operation = operation
        if operation in [HashmapOperation.DELETE, HashmapOperation.GET]:
            self.set_value_textbox_disabled()
            self.set_value("")
        else:
            self.set_value_textbox_enabled()
        self.validate_text()

    def click_run_button(self):
        if self.button_run_state == State.DISABLED:
            self.logger.log("button is disabled")
            return
        if self.operation == HashmapOperation.INSERT:
            try:
                self.hashmap.insert(self.key, self.value)
                self.update_messages(self.MSG_TYPES["insert_msg"] % (self.key, self.value))
                self.logger.log(self.MSG_TYPES["insert_msg"] % (self.key, self.value))
            except KeyError:
                self.update_messages(self.MSG_TYPES["key_exist_msg"] % (self.key))
                self.logger.log(self.MSG_TYPES["key_exist_msg"] % (self.key))

        elif self.operation == HashmapOperation.DELETE:
            try:
                self.hashmap.delete(self.key)
                self.update_messages(self.MSG_TYPES["delete_msg"] % (self.key))
                self.logger.log(self.MSG_TYPES["delete_msg"] % (self.key))
            except KeyError:
                self.update_messages(self.MSG_TYPES["key_not_exist_msg"] % (self.key))
                self.logger.log(self.MSG_TYPES["key_not_exist_msg"] % (self.key))

        elif self.operation == HashmapOperation.GET:
            try:
                value = self.hashmap.get(self.key)
                self.update_messages(self.MSG_TYPES["get_msg"] % (self.key, value))
            except KeyError:
                self.update_messages(self.MSG_TYPES["key_not_exist_msg"] % (self.key))

        elif self.operation == HashmapOperation.UPDATE:
            try:
                value = self.hashmap.update(self.key, self.value)
                self.update_messages(self.MSG_TYPES["update_msg"] % (self.key, self.value))
            except KeyError:
                self.update_messages(self.MSG_TYPES["key_not_exist_msg"] % (self.key))
