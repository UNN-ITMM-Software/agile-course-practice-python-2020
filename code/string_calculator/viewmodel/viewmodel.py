from string_calculator.model.string_calculator import StrCalculator, StrCalculatorParser


class StrCalculatorViewModel:
    def __init__(self):
        self.instr = ''
        self.answer = ''
        self.strcalc = StrCalculator()
        self.set_btn_disabled()

    def get_button_convert_state(self):
        return self.button_convert_state

    def set_btn_enabled(self):
        self.button_convert_state = 'normal'

    def set_btn_disabled(self):
        self.button_convert_state = 'disabled'

    def validate_text(self):
        parser = StrCalculatorParser()
        try:
            parser.parse(self.instr)
        except:
            self.set_btn_disabled()
        else:
            self.set_btn_enabled()

    def set_instr(self, instr):
        self.instr = instr
        self.validate_text()

    def get_instr(self):
        return self.instr

    def set_answer(self, answer_str):
        self.answer = self.strcalc.add(self.instr)

    def get_answer(self):
        return self.answer

    def click_button(self):
        self.set_answer(self.instr)
