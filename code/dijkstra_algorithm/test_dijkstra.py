import sys
import unittest

from dijkstra_algorithm.dijkstra import Graph


class TestDijkstraClass(unittest.TestCase):
    def test_can_create_graph(self):
        graph = Graph(1)
        self.assertTrue(isinstance(graph, Graph))

    def test_create_graph_float_vertices(self):
        self.assertRaises(TypeError, Graph, 3.2)

    def test_create_graph_dict_vertices(self):
        self.assertRaises(TypeError, Graph, {})

    def test_create_graph_list_vertices(self):
        self.assertRaises(TypeError, Graph, [])

    def test_create_graph_string_vertices(self):
        self.assertRaises(TypeError, Graph, '')

    def test_create_graph_negative_vertices(self):
        self.assertRaises(ValueError, Graph, -2)

    def test_can_create_matrix(self):
        graph = Graph(1)
        self.assertTrue(graph.graph == [[0]])

    def test_can_create_matrix_some_elements(self):
        graph = Graph(3)
        self.assertTrue(graph.graph == [[0, 0, 0],
                                        [0, 0, 0],
                                        [0, 0, 0]])
