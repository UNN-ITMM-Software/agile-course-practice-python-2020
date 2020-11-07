
class Depo_calc():
    def __init__(self,
                S0=100, # Start depo
                T=1, # Depo time, years
                T0=0, # or XX.XX.XXXX
                r=0.05, # percent
                is_add_to_depo=False,
                freq=4, # capitalization frequency
                is_add_to_S0=False):
        self.S0=S0       
        self.T=T
        self.T0=T0
        self.r=r
        self.is_add_to_depo=is_add_to_depo
        self.freq=freq
        self.is_add_to_S0=is_add_to_S0
        self.income=0
