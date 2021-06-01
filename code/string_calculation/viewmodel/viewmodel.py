from model.formula_calculator import Calculator
from infrastructure.real_logger import RealLogger


class StringFormulaCalculationViewModel:
    def __init__(self, logger=RealLogger()):
        self.calculator = Calculator()
        self.string_formula = self.result = ''
        self.warning = ''
        self.logger = logger
        self.logger.log('Start Logging')

    def set_formula(self, formula=''):
        self.logger.log('Setting formula sting: {}'.format(formula))
        self.string_formula = formula

    def calculate_formula(self):
        self.warning = ''
        self.logger.log('Calculate: {}'.format(self.string_formula))
        try:
            self.calculator.set_formula(self.string_formula)
            self.result = self.calculator.eval()
            self.logger.log('Calculation result: {}'.format(self.result))
        except:
            self.warning = 'Invalid operation!'

    def get_formula(self):
        return self.string_formula

    def get_result(self):
        return self.result

    def get_warning(self):
        return self.warning
