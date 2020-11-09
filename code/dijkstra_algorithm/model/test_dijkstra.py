import sys
import unittest

from dijkstra_algorithm.model.dijkstra import Graph


class TestDijkstraClass(unittest.TestCase):
    def test_can_create_graph(self):
        graph = Graph(1)
        self.assertTrue(isinstance(graph, Graph))

    def test_can_create_matrix(self):
        graph = Graph(1)
        self.assertTrue(graph.graph == [[0]])

    def test_can_create_matrix_some_elements(self):
        graph = Graph(3)
        self.assertTrue(graph.graph == [[0, 0, 0],
                                        [0, 0, 0],
                                        [0, 0, 0]])

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

    def test_finding_correct_minimal_index(self):
        graph = Graph(1)
        graph.graph = [[0]]
        distances = [sys.maxsize] * 1
        distances[0] = 0
        found_vertex_distances = [False] * 1
        self.assertTrue(graph.minimal_distance(distances, found_vertex_distances) == 0)

    def test_finding_correct_minimal_index_from_two_elements(self):
        graph = Graph(2)
        graph.graph = [[0, 2],
                       [2, 0]]
        dists = [0, sys.maxsize]
        is_vertex_distances = [False, False]
        self.assertTrue(graph.minimal_distance(dists, is_vertex_distances) == 0)

    def test_finding_correct_minimal_index_from_two_elements_second_step(self):
        graph = Graph(2)
        graph.graph = [[0, 2],
                       [2, 0]]
        dists = [0, 2]
        is_vertex_distances = [True, False]
        self.assertTrue(graph.minimal_distance(dists, is_vertex_distances) == 1)

    def test_finding_correct_minimal_index_from_three_elements_zero_vert(self):
        graph = Graph(3)
        graph.graph = [[0, 2, 1],
                       [2, 0, 3],
                       [1, 3, 0]]
        distances = [0, sys.maxsize, sys.maxsize]
        found_vertex_distances = [False, False, False]
        self.assertTrue(graph.minimal_distance(distances, found_vertex_distances) == 0)

    def test_finding_correct_minimal_index_from_three_elements_second_step_zero_vert(self):
        graph = Graph(3)
        graph.graph = [[0, 2, 1],
                       [2, 0, 3],
                       [1, 3, 0]]
        dists = [0, 2, 1]
        is_vertex_distances = [True, False, False]
        self.assertTrue(graph.minimal_distance(dists, is_vertex_distances) == 2)

    def test_finding_correct_minimal_index_from_three_elements_third_step_zero_vert(self):
        graph = Graph(3)
        graph.graph = [[0, 2, 1],
                       [2, 0, 3],
                       [1, 3, 0]]
        dists = [0, 2, 1]
        is_vertex_distances = [True, False, True]
        self.assertTrue(graph.minimal_distance(dists, is_vertex_distances) == 1)

    def test_dijkstra_one_element_graph(self):
        graph = Graph(1)
        graph.graph = [[0]]
        shortest_distances = graph.dijkstra(0)
        self.assertTrue(shortest_distances == [0])

    def test_dijkstra_correctness_zero_vert(self):
        graph = Graph(3)
        graph.graph = [[0, 2, 1],
                       [2, 0, 3],
                       [1, 3, 0]]
        shortest_distances_zero = graph.dijkstra(0)
        self.assertTrue(shortest_distances_zero == [0, 2, 1])

    def test_dijkstra_correctness_first_vert(self):
        graph = Graph(3)
        graph.graph = [[0, 2, 1],
                       [2, 0, 3],
                       [1, 3, 0]]
        shortest_distances_one = graph.dijkstra(1)
        self.assertTrue(shortest_distances_one == [2, 0, 3])

    def test_dijkstra_correctness_second_vert(self):
        graph = Graph(3)
        graph.graph = [[0, 2, 1],
                       [2, 0, 3],
                       [1, 3, 0]]
        shortest_distances_two = graph.dijkstra(2)
        self.assertTrue(shortest_distances_two == [1, 3, 0])

    def test_dijkstra_correctness_2_float_zero_vert(self):
        graph = Graph(4)
        graph.graph = [[0, 4, 1.2, 3],
                       [4, 0, 1.1, 0],
                       [1.2, 1.1, 0, 1],
                       [3, 0, 1, 0]]
        shortest_distances_zero = graph.dijkstra(0)
        self.assertTrue(shortest_distances_zero == [0, 2.3, 1.2, 2.2])

    def test_dijkstra_correctness_2_float_first_vert(self):
        graph = Graph(4)
        graph.graph = [[0, 4, 1.2, 3],
                       [4, 0, 1.1, 0],
                       [1.2, 1.1, 0, 1],
                       [3, 0, 1, 0]]
        shortest_distances_one = graph.dijkstra(1)
        self.assertTrue(shortest_distances_one == [2.3, 0, 1.1, 2.1])

    def test_dijkstra_correctness_2_float_second_vert(self):
        graph = Graph(4)
        graph.graph = [[0, 4, 1.2, 3],
                       [4, 0, 1.1, 0],
                       [1.2, 1.1, 0, 1],
                       [3, 0, 1, 0]]
        shortest_distances_two = graph.dijkstra(2)
        self.assertTrue(shortest_distances_two == [1.2, 1.1, 0, 1])

    def test_dijkstra_correctness_2_float_third_vert(self):
        graph = Graph(4)
        graph.graph = [[0, 4, 1.2, 3],
                       [4, 0, 1.1, 0],
                       [1.2, 1.1, 0, 1],
                       [3, 0, 1, 0]]
        shortest_distances_three = graph.dijkstra(3)
        self.assertTrue(shortest_distances_three == [2.2, 2.1, 1, 0])

    def test_dijkstra_correctness_3_zero_vert(self):
        graph = Graph(7)
        graph.graph = [[0, 0, 1, 3, 0, 4, 1],
                       [0, 0, 0, 2, 0, 0, 0],
                       [1, 0, 0, 0, 0, 2, 0],
                       [3, 2, 0, 0, 1, 0, 0],
                       [0, 0, 0, 1, 0, 2, 3],
                       [4, 0, 2, 0, 2, 0, 0],
                       [1, 0, 0, 0, 3, 0, 0]]
        shortest_distances_zero = graph.dijkstra(0)
        self.assertTrue(shortest_distances_zero == [0, 5, 1, 3, 4, 3, 1])

    def test_dijkstra_correctness_3_first_vert(self):
        graph = Graph(7)
        graph.graph = [[0, 0, 1, 3, 0, 4, 1],
                       [0, 0, 0, 2, 0, 0, 0],
                       [1, 0, 0, 0, 0, 2, 0],
                       [3, 2, 0, 0, 1, 0, 0],
                       [0, 0, 0, 1, 0, 2, 3],
                       [4, 0, 2, 0, 2, 0, 0],
                       [1, 0, 0, 0, 3, 0, 0]]
        shortest_distances_one = graph.dijkstra(1)
        self.assertTrue(shortest_distances_one == [5, 0, 6, 2, 3, 5, 6])

    def test_dijkstra_correctness_3_second_vert(self):
        graph = Graph(7)
        graph.graph = [[0, 0, 1, 3, 0, 4, 1],
                       [0, 0, 0, 2, 0, 0, 0],
                       [1, 0, 0, 0, 0, 2, 0],
                       [3, 2, 0, 0, 1, 0, 0],
                       [0, 0, 0, 1, 0, 2, 3],
                       [4, 0, 2, 0, 2, 0, 0],
                       [1, 0, 0, 0, 3, 0, 0]]
        shortest_distances_two = graph.dijkstra(2)
        self.assertTrue(shortest_distances_two == [1, 6, 0, 4, 4, 2, 2])

    def test_dijkstra_correctness_3_third_vert(self):
        graph = Graph(7)
        graph.graph = [[0, 0, 1, 3, 0, 4, 1],
                       [0, 0, 0, 2, 0, 0, 0],
                       [1, 0, 0, 0, 0, 2, 0],
                       [3, 2, 0, 0, 1, 0, 0],
                       [0, 0, 0, 1, 0, 2, 3],
                       [4, 0, 2, 0, 2, 0, 0],
                       [1, 0, 0, 0, 3, 0, 0]]
        shortest_distances_three = graph.dijkstra(3)
        self.assertTrue(shortest_distances_three == [3, 2, 4, 0, 1, 3, 4])

    def test_dijkstra_correctness_3_fourth_vert(self):
        graph = Graph(7)
        graph.graph = [[0, 0, 1, 3, 0, 4, 1],
                       [0, 0, 0, 2, 0, 0, 0],
                       [1, 0, 0, 0, 0, 2, 0],
                       [3, 2, 0, 0, 1, 0, 0],
                       [0, 0, 0, 1, 0, 2, 3],
                       [4, 0, 2, 0, 2, 0, 0],
                       [1, 0, 0, 0, 3, 0, 0]]
        shortest_distances_four = graph.dijkstra(4)
        self.assertTrue(shortest_distances_four == [4, 3, 4, 1, 0, 2, 3])

    def test_dijkstra_correctness_3_fifth_vert(self):
        graph = Graph(7)
        graph.graph = [[0, 0, 1, 3, 0, 4, 1],
                       [0, 0, 0, 2, 0, 0, 0],
                       [1, 0, 0, 0, 0, 2, 0],
                       [3, 2, 0, 0, 1, 0, 0],
                       [0, 0, 0, 1, 0, 2, 3],
                       [4, 0, 2, 0, 2, 0, 0],
                       [1, 0, 0, 0, 3, 0, 0]]
        shortest_distances_five = graph.dijkstra(5)
        self.assertTrue(shortest_distances_five == [3, 5, 2, 3, 2, 0, 4])

    def test_dijkstra_correctness_3_six_vert(self):
        graph = Graph(7)
        graph.graph = [[0, 0, 1, 3, 0, 4, 1],
                       [0, 0, 0, 2, 0, 0, 0],
                       [1, 0, 0, 0, 0, 2, 0],
                       [3, 2, 0, 0, 1, 0, 0],
                       [0, 0, 0, 1, 0, 2, 3],
                       [4, 0, 2, 0, 2, 0, 0],
                       [1, 0, 0, 0, 3, 0, 0]]
        shortest_distances_six = graph.dijkstra(6)
        self.assertTrue(shortest_distances_six == [1, 6, 2, 4, 3, 4, 0])

    def test_dijkstra_correctness_start_index_value_left_condition(self):
        graph = Graph(3)
        graph.graph = [[0, 2, 1],
                       [2, 0, 3],
                       [1, 3, 0]]
        self.assertRaises(ValueError, graph.dijkstra, -4)

    def test_dijkstra_correctness_start_index_value_right_condition(self):
        graph = Graph(3)
        graph.graph = [[0, 2, 1],
                       [2, 0, 3],
                       [1, 3, 0]]
        self.assertRaises(ValueError, graph.dijkstra, 10)

    def test_dijkstra_correctness_start_index_type_str(self):
        graph = Graph(3)
        graph.graph = [[0, 2, 1],
                       [2, 0, 3],
                       [1, 3, 0]]
        self.assertRaises(TypeError, graph.dijkstra, 'a')

    def test_dijkstra_correctness_start_index_type_list(self):
        graph = Graph(3)
        graph.graph = [[0, 2, 1],
                       [2, 0, 3],
                       [1, 3, 0]]
        self.assertRaises(TypeError, graph.dijkstra, [])

    def test_dijkstra_correctness_start_index_type_dict(self):
        graph = Graph(3)
        graph.graph = [[0, 2, 1],
                       [2, 0, 3],
                       [1, 3, 0]]
        self.assertRaises(TypeError, graph.dijkstra, {})

    def test_dijkstra_correctness_graph_weight_string(self):
        graph = Graph(3)
        graph.graph = [[0, 2, 'test'],
                       [2, 0, 3],
                       [1, 3, 0]]
        self.assertRaises(TypeError, graph.dijkstra, 1)

    def test_dijkstra_correctness_graph_weight_list(self):
        graph = Graph(3)
        graph.graph = [[0, 2, 1],
                       [2, 0, 3],
                       [1, [], 0]]
        self.assertRaises(TypeError, graph.dijkstra, 1)

    def test_dijkstra_correctness_graph_weight_tuple(self):
        graph = Graph(3)
        graph.graph = [[0, 2, 1],
                       [2, 0, 3],
                       [(1, 3), 3, 0]]
        self.assertRaises(TypeError, graph.dijkstra, 1)

    def test_dijkstra_correctness_graph_weight_dict(self):
        graph = Graph(3)
        graph.graph = [[0, 2, 1],
                       [{}, 0, 3],
                       [1, 3, 0]]
        self.assertRaises(TypeError, graph.dijkstra, 1)

    def test_dijkstra_correctness_graph_weight_len(self):
        graph = Graph(3)
        graph.graph = [[]]
        self.assertRaises(ValueError, graph.dijkstra, 1)
