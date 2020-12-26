import unittest

from ryabinin_kirill_lab1.src.elastic_of_demand import ElasticOfDemand, InvalidArgumentError, DemandTypes


class TestElasticOfDemand(unittest.TestCase):

    # INIT TESTS
    def test_raise_init_with_zero_demand(self):
        with self.assertRaises(InvalidArgumentError):
            ElasticOfDemand(start_price=4, end_price=3, start_demand=0, end_demand=2)

    def test_raise_init_with_zero_delta_price(self):
        with self.assertRaises(InvalidArgumentError):
            ElasticOfDemand(start_price=3, end_price=3, start_demand=2, end_demand=1)

    def test_raise_init_with_zero_sum_demand(self):
        with self.assertRaises(InvalidArgumentError):
            ElasticOfDemand(start_price=4, end_price=3, start_demand=-1, end_demand=1)

    def test_raise_init_with_zero_delta_salary(self):
        with self.assertRaises(InvalidArgumentError):
            ElasticOfDemand(start_demand=4, end_demand=5, start_salary=1, end_salary=1)

    def test_raise_with_invalid_delta_demand(self):
        with self.assertRaises(InvalidArgumentError):
            ElasticOfDemand(start_price=4, end_price=3, start_demand=4, end_demand=1)

    def test_raise_with_invalid_delta_price(self):
        with self.assertRaises(InvalidArgumentError):
            ElasticOfDemand(start_price=4, end_price=5, start_demand=4, end_demand=6)

    # SMOKE TESTS

    def test_raise_with_not_init_price(self):
        elastic = ElasticOfDemand(start_demand=4, end_demand=5, start_salary=1, end_salary=1)
        with self.assertRaises(InvalidArgumentError):
            elastic.by_price()

    def test_raise_with_not_init_salary(self):
        elastic = ElasticOfDemand(start_demand=4, end_demand=5, start_price=1, end_price=1)
        with self.assertRaises(InvalidArgumentError):
            elastic.by_salary()

    def test_inelastic(self):
        elastic = ElasticOfDemand(start_price=3, end_price=4, start_demand=5, end_demand=4)
        demand_type, _ = elastic.by_price()
        self.assertEqual(demand_type, DemandTypes.Inelastic)

    def test_unit_elasticity(self):
        elastic = ElasticOfDemand(start_price=4, end_price=3, start_demand=4, end_demand=5)
        demand_type, _ = elastic.by_price()
        self.assertEqual(demand_type, DemandTypes.UnitElasticity)

    def test_elastic(self):
        elastic = ElasticOfDemand(start_price=5, end_price=4, start_demand=5, end_demand=10)
        demand_type, _ = elastic.by_price()
        self.assertEqual(demand_type, DemandTypes.Elastic)

    def test_luxury(self):
        elastic = ElasticOfDemand(start_demand=10, end_demand=13, start_salary=500, end_salary=600)
        demand_type, _ = elastic.by_salary()
        self.assertEqual(demand_type, DemandTypes.Luxury)

    def test_essential(self):
        elastic = ElasticOfDemand(start_demand=50, end_demand=53, start_salary=500, end_salary=600)
        demand_type, _ = elastic.by_salary()
        self.assertEqual(demand_type, DemandTypes.Essential)

    def test_lowquality(self):
        elastic = ElasticOfDemand(start_demand=200, end_demand=180, start_salary=500, end_salary=600)
        demand_type, _ = elastic.by_salary()
        self.assertEqual(demand_type, DemandTypes.Lowquality)
