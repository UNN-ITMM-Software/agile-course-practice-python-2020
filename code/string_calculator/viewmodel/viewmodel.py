import os

from string_calculator.model.string_calculator import StrCalculator, StrCalculatorParser
from string_calculator.logger.reallogger import RealLogger


class StrCalculatorViewModel:
    def __init__(self,
                 logger=RealLogger(os.path.join('..', '..', 'tmp', 'string_calculator.log'))):
        self.logger = logger
        self.logger.log('Hello')
        self.instr = ''
        self.answer = ''
        self.button_convert_state = 'disabled'
        self.strcalc = StrCalculator()

    def get_button_convert_state(self):
        return self.button_convert_state

    def set_btn_enabled(self):
        self.logger.log('Button status: normal')
        self.button_convert_state = 'normal'

    def set_btn_disabled(self):
        self.logger.log('Button status: disabled')
        self.button_convert_state = 'disabled'

    def validate_text(self):
        parser = StrCalculatorParser()
        try:
            parser.parse(self.instr)
        except:
            self.logger.log('Invalid input')
            self.set_btn_disabled()
        else:
            self.logger.log('Correct input')
            self.set_btn_enabled()

    def set_instr(self, instr):
        self.logger.log('Set inst: {}'.format(instr))
        self.instr = instr
        self.validate_text()

    def get_instr(self):
        return self.instr

    def set_answer(self, answer_str):
        self.answer = self.strcalc.add(self.instr)
        self.logger.log('Answer: {}'.format(self.answer))

    def get_answer(self):
        return self.answer

    def click_button(self):
        self.logger.log('Button clicked')
        self.set_answer(self.instr)
