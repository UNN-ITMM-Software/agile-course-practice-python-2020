from deposit_calc.model.deposit_calc import DepositCalc


class DepositCalcViewModel:
    def __init__(self):
        self.start_depo = 0.0
        self.depo_time = 0.0
        self.rate = 0.0
        self.capitalization = 0.0
        self.replenishment_freq = 0.0
        self.replenishment_size = 0.0
        self.result = ''
        self.set_handle_btn_disabled()

    def set_handle_btn_enabled(self):
        self.handle_btn_state = 'normal'

    def set_handle_btn_disabled(self):
        self.handle_btn_state = 'disabled'

    def get_handle_btn_state(self):
        return self.handle_btn_state

    def set_start_depo(self, start_depo):
        try:
            self.start_depo = float(start_depo)
            self.set_handle_btn_enabled()
        except:
            self.set_handle_btn_disabled()

    def set_depo_time(self, depo_time):
        try:
            self.depo_time = float(depo_time)
            self.set_handle_btn_enabled()
        except:
            self.set_handle_btn_disabled()

    def set_rate(self, rate):
        try:
            self.rate = float(rate)
            self.set_handle_btn_enabled()
        except:
            self.set_handle_btn_disabled()

    def set_capitalization(self, capitalization):
        try:
            self.capitalization = int(capitalization)
            self.set_handle_btn_enabled()
        except:
            self.set_handle_btn_disabled()

    def set_replenishment_freq(self, replenishment_freq):
        try:
            self.replenishment_freq = int(replenishment_freq)
            self.set_handle_btn_enabled()
        except:
            self.set_handle_btn_disabled()

    def set_replenishment_size(self, replenishment_size):
        try:
            self.replenishment_size = int(replenishment_size)
            self.set_handle_btn_enabled()
        except:
            self.set_handle_btn_disabled()

    def get_start_depo(self):
        return self.start_depo

    def get_result(self):
        return self.result

    def handle_btn_clicked(self):
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
