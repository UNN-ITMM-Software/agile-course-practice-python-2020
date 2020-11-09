import sys
import unittest

from dijkstra_algorithm.dijkstra import Graph


class TestDijkstraClass(unittest.TestCase):
    def test_can_create_graph(self):
        graph = Graph(1)
        self.assertTrue(isinstance(graph, Graph))
