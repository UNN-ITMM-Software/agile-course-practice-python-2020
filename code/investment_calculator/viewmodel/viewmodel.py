from investment_calculator.model.investmentcalculator import InvestmentCalculator

from investment_calculator.logger.reallogger import RealLogger


def parser_marks(string):
    marks_str = string.split()
    marks_int = []
    for mark_str in marks_str:
        marks_int.append(int(mark_str))
    return marks_int


class InvestmentCalculatorViewModel:
    def __init__(self, logger=RealLogger()):
        self.logger = logger
        self.logger.log("Welcome to net present value calculator!")

        self.button_convert_state = 'normal'
        self.K = 1
        self.R = 1
        self.q = 1
        self.n = 1
        self.W = 0
        self.K_txt = ''
        self.R_txt = ''
        self.q_txt = ''
        self.n_txt = ''
        self.W_txt = ''

    def get_button_convert_state(self):
        return self.button_convert_state

    def set_btn_enabled(self):
        self.button_convert_state = 'normal'
        self.logger.log('Button state was set to "normal"')

    def set_btn_disabled(self):
        self.button_convert_state = 'disabled'
        self.logger.log('Button state was set to "disabled"')


    def set_instr(self, R_str, K_str, n_str, q_str):
        self.K_txt = K_str
        self.K = float(K_str)
        self.R_txt = R_str
        self.R = float(R_str)
        self.q_txt = q_str
        self.q = float(q_str)
        self.n_txt = n_str
        self.n = float(n_str)
        self.logger.log('Entered data: R=%s, K=%s, q=%s, n=%s' % (self.K_txt, self.R_txt, self.q_txt, self.n_txt))

    def get_K_txt(self):
        return self.K_txt

    def get_R_txt(self):
        return self.R_txt

    def get_q_txt(self):
        return self.q_txt

    def get_n_txt(self):
        return self.n_txt

    def get_answer(self):
        return self.W

    def click_button(self):
        self.logger.log('Button clicked')
        if self.button_convert_state != 'disabled':
            self.logger.log('Button clicked')
            journal = InvestmentCalculator(self.R, self.K, self.n, self.q)
            self.answer = journal.calculate_net_present_value()
            self.W = self.answer
            self.logger.log('Result: %s' % self.answer)
