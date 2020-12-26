from enum import Enum


class DemandTypes(Enum):
    # Elastic of demand by price
    Inelastic = 0
    UnitElasticity = 1
    Elastic = 2

    # Elastic of demand by salary
    Luxury = 3
    Essential = 4
    Lowquality = 5


class InvalidArgumentError(Exception):
    pass


class ElasticOfDemand:
    def __init__(self, start_demand, end_demand, start_price=None, end_price=None,
                 start_salary=None, end_salary=None):
        if start_demand == 0:
            raise InvalidArgumentError('demand cannot be equal to zero')

        if start_price is not None and end_price is not None:
            if end_price - start_price == 0:
                raise InvalidArgumentError('delta price cannot be equal to zero')
            if end_price - start_price < 0 and end_demand - start_demand < 0:
                raise InvalidArgumentError('delta price < 0 not supported with delta demand < 0')
            if end_price - start_price > 0 and end_demand - start_demand > 0:
                raise InvalidArgumentError('delta price > 0 not supported with delta demand > 0')

        if start_demand == -end_demand:
            raise InvalidArgumentError('sum demand cannot be equal to zero')
        if start_salary is not None and end_salary is not None and end_salary - start_salary == 0:
            raise InvalidArgumentError('delta salary cannot be equal to zero')

        self._start_demand = start_demand
        self._end_demand = end_demand
        self._start_price = start_price
        self._end_price = end_price
        self._start_salary = start_salary
        self._end_salary = end_salary

    @staticmethod
    def get_demand_by_price_type(coef):
        if coef > 1:
            return DemandTypes.Elastic
        if coef == 1:
            return DemandTypes.UnitElasticity
        if coef < 1:
            return DemandTypes.Inelastic

    @staticmethod
    def get_demand_by_salary_type(coef):
        if coef > 1:
            return DemandTypes.Luxury
        if 0 <= coef <= 1:
            return DemandTypes.Essential
        if coef < 0:
            return DemandTypes.Lowquality

    def by_price(self):
        if self._start_price is None and self._end_price is None:
            raise InvalidArgumentError('')

        result = ((self._end_demand - self._start_demand) / self._start_demand) / \
                 ((self._end_price - self._start_price) / self._start_price)

        return self.get_demand_by_price_type(result), result

    def by_salary(self):
        if self._start_salary is None and self._end_salary is None:
            raise InvalidArgumentError('')

        result = ((self._end_demand - self._start_demand) / (self._start_demand + self._end_demand)) * \
                 ((self._end_salary + self._start_salary) / (self._end_salary - self._start_salary))

        return self.get_demand_by_salary_type(result), result

