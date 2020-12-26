
class InvalidDemandError(Exception):
    pass


class InvalidDeltaPriceError(Exception):
    pass


class ElasticOfDemand:
    def __init__(self, start_price, finish_price, start_demand, finish_demand):
        if start_demand == 0:
            raise InvalidDemandError('demand cannot be equal to zero')
        if finish_price - start_price == 0:
            raise InvalidDeltaPriceError('delta price cannot be equal to zero')
