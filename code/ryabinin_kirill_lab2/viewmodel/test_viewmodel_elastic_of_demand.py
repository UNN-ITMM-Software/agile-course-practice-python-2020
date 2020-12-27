import unittest

from ryabinin_kirill_lab2.viewmodel.viewmodel_elastic_of_demand import ViewModelElasticOfDemand
from ryabinin_kirill_lab2.model.model_elastic_of_demand import DemandTypes


class TestViewModelElasticOfDemand(unittest.TestCase):

    def test_set_arguments_from_array1(self):
        viewmodel = ViewModelElasticOfDemand()
        array = ['4', '3', '4', '5', '\n', '\n']
        viewmodel.set_arguments_from_array(array)
        self.assertEqual(array, viewmodel.get_arguments_from_array())

    def test_set_arguments_from_array2(self):
        viewmodel = ViewModelElasticOfDemand()
        array = ['4', '3', '4', '5', '6', '5']
        viewmodel.set_arguments_from_array(array)
        self.assertEqual(array, viewmodel.get_arguments_from_array())

    def test_set_arguments_from_array3(self):
        viewmodel = ViewModelElasticOfDemand()
        array = ['4', '3', '\n', '\n', '6', '5']
        viewmodel.set_arguments_from_array(array)
        self.assertEqual(array, viewmodel.get_arguments_from_array())

    def test_inelastic(self):
        viewmodel = ViewModelElasticOfDemand()
        viewmodel.set_arguments_from_array(['5', '4', '3', '4', '\n', '\n'])
        viewmodel.calc_by_price()
        self.assertEqual(viewmodel.get_type_price(), DemandTypes.Inelastic)

    def test_unit_elasticity(self):
        viewmodel = ViewModelElasticOfDemand()
        viewmodel.set_arguments_from_array(['4', '5', '4', '3', '\n', '\n'])
        viewmodel.calc_by_price()
        self.assertEqual(viewmodel.get_type_price(), DemandTypes.UnitElasticity)

    def test_elastic(self):
        viewmodel = ViewModelElasticOfDemand()
        viewmodel.set_arguments_from_array(['5', '10', '5', '4', '\n', '\n'])
        viewmodel.calc_by_price()
        self.assertEqual(viewmodel.get_type_price(), DemandTypes.Elastic)

    def test_luxury(self):
        viewmodel = ViewModelElasticOfDemand()
        viewmodel.set_arguments_from_array(['10', '13', '\n', '\n', '500', '600'])
        viewmodel.calc_by_price()
        self.assertEqual(viewmodel.get_type_price(), DemandTypes.Luxury)

    def test_essential(self):
        viewmodel = ViewModelElasticOfDemand()
        viewmodel.set_arguments_from_array(['50', '53', '\n', '\n', '500', '600'])
        viewmodel.calc_by_price()
        self.assertEqual(viewmodel.get_type_price(), DemandTypes.Essential)

    def test_lowquality(self):
        viewmodel = ViewModelElasticOfDemand()
        viewmodel.set_arguments_from_array(['200', '180', '\n', '\n', '500', '600'])
        viewmodel.calc_by_price()
        self.assertEqual(viewmodel.get_type_price(), DemandTypes.Lowquality)
