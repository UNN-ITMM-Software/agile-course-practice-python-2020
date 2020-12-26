import unittest

from ryabinin_kirill_lab1.src.elastic_of_demand import *


class TestElasticOfDemand(unittest.TestCase):

    def test_raise_init_with_zero_demand(self):
        with self.assertRaises(InvalidDemandError):
            ElasticOfDemand(4, 3, 0, 2)

    def test_raise_init_with_zero_delta_price(self):
        with self.assertRaises(InvalidDeltaPriceError):
            ElasticOfDemand(3, 3, 1, 2)
