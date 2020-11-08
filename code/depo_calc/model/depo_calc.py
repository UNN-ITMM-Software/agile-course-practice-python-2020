
class DepoCalc():
    def __init__(
                self,
                s0=100.,  # Start depo
                t=1.,  # Depo time, years
                r=0.05,  # interest rate
                is_add_to_depo=False,
                capitalization_freq=4,  # capitalization frequency
                replenishment_freq=-1):
        assert all([s0 > 0,
                    t > 0,
                    r > 0,
                    r < 1,
                    is_add_to_depo in [True, False],
                    capitalization_freq in [1, 2, 3, 4, 6, 12],
                    replenishment_freq in [-1, 1, 2, 3, 4, 6, 12],
                    t*12 >= capitalization_freq,
                    capitalization_freq > replenishment_freq
                    ])
        self.s0 = s0
        self.t = t
        self.r = r
        self.is_add_to_depo = is_add_to_depo
        self.capitalization_freq = capitalization_freq
        self.replenishment_freq = replenishment_freq
        self.income = 0
        self.repl = 0

    def capitalization(self):
        income = self.s0 * self.r / self.capitalization_freq
        self.income += income
        if self.is_add_to_depo:
            self.s0 += income

    def replenishment(self, value):
        assert value > 0
        self.s0 += value
        self.repl += value

    def revenue(self, values=None):
        if self.replenishment_freq != -1:
            assert self.capitalization_freq % self.replenishment_freq == 0
        if self.replenishment_freq != -1:
            assert len(values) == self.replenishment_freq * self.t
            for i in range(int(self.capitalization_freq * self.t)):
                j = 0
                if (i+1) % (self.capitalization_freq / self.replenishment_freq) == 0:
                    self.capitalization()
                    self.replenishment(values[j])
                    j += 1
                else:
                    self.capitalization()
        else:
            for i in range(self.capitalization_freq):
                self.capitalization()
        return int(self.income)

    def get_data(self):
        return self.s0, self.repl, self.income
