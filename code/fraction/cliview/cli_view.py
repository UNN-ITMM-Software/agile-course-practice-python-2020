import os
import sys

from fraction.viewmodel import viewmodel


class CLIView:
    view_model = viewmodel.FractionViewModel()
    WIDTH = 80
    message_text = ''
    first_fraction = ''
    second_fraction = ''
    operation = '+'
    is_calc_enabled = False
    is_second_fraction_enabled = True

    result = ''

    def center_text(self, string):
        signs_we_need = int((self.WIDTH - len(string)) / 2)
        remainder = int((self.WIDTH - len(string)) % 2)
        return '=' * signs_we_need + string + '=' * (signs_we_need + remainder)

    def left_text(self, string):
        signs_we_need = (self.WIDTH - len(string)) - 1
        return '=' + string + '=' * signs_we_need

    def print_main_window(self):
        os.system('clear')
        print(self.center_text(''))
        print(self.center_text('Welcome to fractions calculator'))
        print(self.left_text('First fraction:  %s ' % self.first_fraction))
        print(self.left_text('Operation:  %s ' % self.operation))
        if self.is_second_fraction_enabled:
            print(self.left_text('Second fraction:  %s ' % self.second_fraction))
        if self.result:
            print(self.center_text('Calculation result: %s' % self.result))
        print(self.center_text('Possible commands:'))
        print(self.left_text('"SetFirst,x", where x is fraction value, to set first fraction'))
        if self.is_second_fraction_enabled:
            print(self.left_text('"SetSecond,x", where x is fraction '
                                 'value, to set second fraction'))
        print(self.left_text('"SetOp,x", where x is '
                             'one of +-*/ or "Convert to continuous"'))
        if self.is_calc_enabled:
            print(self.left_text('"Calc" to get a result'))
        print(self.left_text('"Exit" to exit'))

    def mvvm_bind(self):
        self.view_model.set_first_fraction(self.first_fraction)
        self.view_model.set_second_fraction(self.second_fraction)
        self.view_model.set_operation(self.operation)

    def mvvm_back_bind(self):
        self.first_fraction = self.view_model.get_first_fraction()
        self.second_fraction = self.view_model.get_second_fraction()
        self.message_text = self.view_model.get_msg_text()
        self.is_calc_enabled = \
            self.view_model.get_button_convert_state() == 'normal'
        self.is_second_fraction_enabled = \
            self.view_model.get_second_fraction_text_state() == 'normal'
        self.result = self.view_model.get_msg_text()
        self.print_main_window()

    def convert_clicked(self):
        self.mvvm_bind()
        self.view_model.click_convert()
        self.mvvm_back_bind()

    def first_frac_txt_changed(self):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def second_frac_txt_changed(self):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def operation_changed(self):
        self.mvvm_bind()
        self.mvvm_back_bind()

    def mainloop(self):
        while True:
            self.print_main_window()
            raw_command = input('Enter your choice: ')
            if ',' not in raw_command:
                command = raw_command
                value = None
            else:
                command, value = raw_command.split(',')

            if command == 'Exit':
                sys.exit(0)
            elif command == 'SetFirst':
                self.first_fraction = value
                self.first_frac_txt_changed()
            elif command == 'SetSecond' and self.is_second_fraction_enabled:
                self.second_fraction = value
                self.second_frac_txt_changed()
            elif command == 'SetOp':
                self.operation = value
                self.operation_changed()
            elif command == 'Calc' and self.is_calc_enabled:
                self.convert_clicked()
