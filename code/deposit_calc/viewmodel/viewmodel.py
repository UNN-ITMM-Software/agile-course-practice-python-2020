from deposit_calc.model.deposit_calc import DepositCalc
from fraction.logger.reallogger import RealLogger


class DepositCalcViewModel:
    def __init__(self, logger=RealLogger()):
        self.logger = logger
        self.start_depo = 0.0
        self.depo_time = 0.0
        self.rate = 0.0
        self.capitalization = 0.0
        self.replenishment_freq = 0.0
        self.replenishment_size = 0.0
        self.result = ''
        self.set_handle_btn_disabled()
        self.logger.log('Welcome!')

    def set_handle_btn_enabled(self):
        self.handle_btn_state = 'normal'

    def set_handle_btn_disabled(self):
        self.handle_btn_state = 'disabled'

    def get_handle_btn_state(self):
        return self.handle_btn_state

    def set_start_depo(self, start_depo):
        if start_depo != '':
            self.start_depo = float(start_depo)
            self.logger.log('Setting start deposit to %s' % self.start_depo)
            self.set_handle_btn_enabled()

    def set_depo_time(self, depo_time):
        if depo_time != '':
            self.depo_time = float(depo_time)
            self.logger.log('Setting deposit time to %s' % self.depo_time)
            self.set_handle_btn_enabled()

    def set_rate(self, rate):
        if rate != '':
            self.rate = float(rate)
            self.logger.log('Setting interest rate to %s' % self.rate)
            self.set_handle_btn_enabled()

    def set_capitalization(self, capitalization):
        if capitalization != '':
            self.capitalization = int(capitalization)
            self.logger.log('Setting capitalization frequency to %s' % self.capitalization)
            self.set_handle_btn_enabled()

    def set_replenishment_freq(self, replenishment_freq):
        if replenishment_freq != '':
            self.replenishment_freq = int(replenishment_freq)
            self.logger.log('Setting replenishment frequency to %s' % self.replenishment_freq)
            self.set_handle_btn_enabled()

    def set_replenishment_size(self, replenishment_size):
        if replenishment_size != '':
            self.replenishment_size = int(replenishment_size)
            self.logger.log('Setting replenishment size to %s' % self.replenishment_size)
            self.set_handle_btn_enabled()

    def get_start_depo(self):
        return self.start_depo

    def get_result(self):
        return self.result

    def handle_btn_clicked(self):
        self.logger.log('Button clicked')
        calc = DepositCalc(
            s0=self.start_depo,
            t=self.depo_time,
            r=self.rate,
            is_add_to_depo=True,
            capitalization_freq=self.capitalization,
            replenishment_freq=self.replenishment_freq
        )
        arr = []
        range_val = int(self.depo_time * self.replenishment_freq)

        for i in range(range_val):
            arr.append(self.replenishment_size)

        self.result = str(calc.revenue(values=arr))
        self.logger.log('Result: %s' % self.result)
