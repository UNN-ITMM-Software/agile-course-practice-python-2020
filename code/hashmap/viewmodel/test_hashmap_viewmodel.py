import unittest

from hashmap.viewmodel.hashmap_viewmodel import HashmapViewModel, State, HashmapOperation


class TestHashmapViewModel(unittest.TestCase):

    def setUp(self):
        self.view_model = HashmapViewModel()

    def test_by_default_button_disabled(self):
        self.assertEqual(State.DISABLED.value, self.view_model.get_button_run_state())

    def test_when_entered_insert_operation_value_textbox_enabled(self):
        self.view_model.set_operation(HashmapOperation.INSERT)
        self.assertEqual(State.ENABLED.value, self.view_model.get_value_textbox_state())

    def test_when_entered_update_operation_value_textbox_enabled(self):
        self.view_model.set_operation(HashmapOperation.UPDATE)
        self.assertEqual(State.ENABLED.value, self.view_model.get_value_textbox_state())

    def test_when_entered_get_operation_value_textbox_disabled(self):
        self.view_model.set_operation(HashmapOperation.GET)
        self.assertEqual(State.DISABLED.value, self.view_model.get_value_textbox_state())

    def test_when_entered_delete_operation_value_textbox_disabled(self):
        self.view_model.set_operation(HashmapOperation.DELETE)
        self.assertEqual(State.DISABLED.value, self.view_model.get_value_textbox_state())

    def test_when_making_value_textbox_disabled_its_value_become_empty(self):
        self.view_model.set_value("value")
        self.view_model.set_value_textbox_disabled()
        self.assertEqual("", self.view_model.get_value())

    def test_when_entered_insert_operation_and_both_textboxes_button_enabled(self):
        self.view_model.set_operation(HashmapOperation.INSERT)
        self.view_model.set_key("key")
        self.view_model.set_value("value")
        self.assertEqual(State.ENABLED.value, self.view_model.get_button_run_state())

    def test_delete_after_insert_leaves_button_enabled(self):
        self.view_model.set_operation(HashmapOperation.INSERT)
        self.view_model.set_key("key")
        self.view_model.set_value("value")
        self.view_model.set_operation(HashmapOperation.DELETE)
        self.assertEqual(State.ENABLED.value, self.view_model.get_button_run_state())

    def test_can_get_key(self):
        self.view_model.set_key("key")
        self.assertEqual("key", self.view_model.get_key())

    def test_insert_after_delete_leaves_button_disabled(self):
        self.view_model.set_operation(HashmapOperation.DELETE)
        self.view_model.set_key("key")
        self.view_model.set_operation(HashmapOperation.INSERT)
        self.assertEqual(State.DISABLED.value, self.view_model.get_button_run_state())

    def test_number_of_messages_is_limited(self):
        for i in range(self.view_model.MAX_MESSAGE_NUMBER):
            self.view_model.update_messages(str(i))
        self.view_model.update_messages("last message")
        expected_text = "\n".join([str(i) for i in range(self.view_model.MAX_MESSAGE_NUMBER-1, 0, -1)])
        expected_text = "last message\n" + expected_text
        self.assertEqual(expected_text, self.view_model.get_message_text())

    def test_clicks_on_disabled_button_do_nothing(self):
        self.view_model.click_run_button()
        self.assertEqual(self.view_model.get_message_text(), "")

    def test_when_entered_insert_operation_and_key_textbox_only_button_disabled(self):
        self.view_model.set_operation(HashmapOperation.INSERT)
        self.view_model.set_key("key")
        self.view_model.set_value("")
        self.assertEqual(State.DISABLED.value, self.view_model.get_button_run_state())

    def test_when_entered_insert_operation_and_value_textbox_only_button_disabled(self):
        self.view_model.set_operation(HashmapOperation.INSERT)
        self.view_model.set_key("")
        self.view_model.set_value("value")
        self.assertEqual(State.DISABLED.value, self.view_model.get_button_run_state())

    def test_when_insert_there_is_approciate_message(self):
        self.view_model.set_operation(HashmapOperation.INSERT)
        self.view_model.set_key("key")
        self.view_model.set_value("value")
        self.view_model.click_run_button()
        expected_msg = HashmapViewModel.MSG_TYPES["insert_msg"] % ("key", "value")
        self.assertNotEqual(-1, self.view_model.get_message_text().find(expected_msg))

    def test_when_update_there_is_approciate_message(self):
        self.view_model.hashmap.insert("key", "value")
        self.view_model.set_operation(HashmapOperation.UPDATE)
        self.view_model.set_key("key")
        self.view_model.set_value("value2")
        self.view_model.click_run_button()
        expected_msg = HashmapViewModel.MSG_TYPES["update_msg"] % ("key", "value2")
        self.assertNotEqual(-1, self.view_model.get_message_text().find(expected_msg))

    def test_when_get_there_is_approciate_message(self):
        self.view_model.hashmap.insert("key", "value")
        self.view_model.set_operation(HashmapOperation.GET)
        self.view_model.set_key("key")
        self.view_model.click_run_button()
        expected_msg = HashmapViewModel.MSG_TYPES["get_msg"] % ("key", "value")
        self.assertNotEqual(-1, self.view_model.get_message_text().find(expected_msg))

    def test_when_delete_there_is_approciate_message(self):
        self.view_model.hashmap.insert("key", "value")
        self.view_model.set_operation(HashmapOperation.DELETE)
        self.view_model.set_key("key")
        self.view_model.click_run_button()
        expected_msg = HashmapViewModel.MSG_TYPES["delete_msg"] % ("key")
        self.assertNotEqual(-1, self.view_model.get_message_text().find(expected_msg))

    def test_when_update_nonexisting_key_there_is_approciate_message(self):
        self.view_model.hashmap.insert("key", "value")
        self.view_model.set_operation(HashmapOperation.UPDATE)
        self.view_model.set_key("key2")
        self.view_model.set_value("value2")
        self.view_model.click_run_button()
        expected_msg = HashmapViewModel.MSG_TYPES["key_not_exist_msg"] % ("key2")
        self.assertNotEqual(-1, self.view_model.get_message_text().find(expected_msg))

    def test_when_insert_existing_key_there_is_approciate_error_message(self):
        self.view_model.hashmap.insert("key", "value")
        self.view_model.set_operation(HashmapOperation.INSERT)
        self.view_model.set_key("key")
        self.view_model.set_value("value2")
        self.view_model.click_run_button()
        expected_msg = HashmapViewModel.MSG_TYPES["key_exist_msg"] % ("key")
        self.assertNotEqual(-1, self.view_model.get_message_text().find(expected_msg))

    def test_when_get_nonexisting_key_there_is_approciate_error_message(self):
        self.view_model.hashmap.insert("key", "value")
        self.view_model.set_operation(HashmapOperation.GET)
        self.view_model.set_key("key2")
        self.view_model.click_run_button()
        expected_msg = HashmapViewModel.MSG_TYPES["key_not_exist_msg"] % ("key2")
        self.assertNotEqual(-1, self.view_model.get_message_text().find(expected_msg))

    def test_when_delete_nonexisting_key_there_is_approciate_error_message(self):
        self.view_model.hashmap.insert("key", "value")
        self.view_model.set_operation(HashmapOperation.DELETE)
        self.view_model.set_key("key2")
        self.view_model.click_run_button()
        expected_msg = HashmapViewModel.MSG_TYPES["key_not_exist_msg"] % ("key2")
        self.assertNotEqual(-1, self.view_model.get_message_text().find(expected_msg))

class TestHashmapFakeLogger(unittest.TestCase):

    def setUp(self):
        self.view_model = HashmapViewModel()

    def test_log_init(self):
        self.assertEqual("create view", self.view_model.logger.get_last_message())

    def test_log_clicks_on_disabled_button(self):
        self.view_model.click_run_button()
        self.assertEqual(self.view_model.logger.get_last_message(), "button is disabled")
