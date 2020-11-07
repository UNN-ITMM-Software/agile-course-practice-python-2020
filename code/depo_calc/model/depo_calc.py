
class Depo_calc():
    def __init__(self,
                S0=100, # Start depo
                T=1, # Depo time, years
                T0=0, # or XX.XX.XXXX
                r=0.05, # percent
                is_add_to_depo=False,
                freq=4, # capitalization frequency
                is_add_to_S0=False):
        assert all([S0 > 0,
                    T > 0,
                    T0 >= 0,
                    r > 0,
                    r < 1,
                    is_add_to_depo in [True, False],
                    freq in [1, 2, 3, 4, 6, 12],
                    is_add_to_S0 in [True, False]
                    ])
        self.S0=S0       
        self.T=T
        self.T0=T0
        self.r=r
        self.is_add_to_depo=is_add_to_depo
        self.freq=freq
        self.is_add_to_S0=is_add_to_S0
        self.income=0

    def capitalization(self):
        income = self.S0 * self.r / self.freq
        self.income += income
        if self.is_add_to_depo:
            self.S0 += income

    def replenishment(self):
        pass

    def revenue(self):
        for i in range(self.freq):
            self.capitalization()
        return self.income
