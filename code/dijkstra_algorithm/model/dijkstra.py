import sys


class Graph(object):
    def __init__(self, vertices, graph):
        if not isinstance(vertices, int):
            raise TypeError('Incorrect type of input vertices. Expected: int')
        if vertices <= 0:
            raise ValueError('Unacceptable input value of vertices')
        self.vertices = vertices
        if len(graph) != self.vertices:
            raise ValueError('Wrong length in graphs row')

        for row in range(self.vertices):
            if len(graph[row]) != self.vertices:
                raise ValueError('Wrong length in graphs column')
            for column in range(self.vertices):
                if not isinstance(graph[row][column], int) and \
                        not isinstance(graph[row][column], float):
                    raise TypeError('Wrong type of value in graph matrix')

        for row in range(0, len(graph) - 1):
            for column in range(row + 1, len(graph[row])):
                if graph[row][column] != graph[column][row]:
                    raise ValueError('Matrix is not symmetric')
        self.graph = graph

    def minimal_distance(self, distances, visited_vertices):
        minimal = sys.maxsize
        minimal_index = 0

        for vertex in range(self.vertices):
            if distances[vertex] < minimal and vertex not in visited_vertices:
                minimal = distances[vertex]
                minimal_index = vertex
        return minimal_index

    def dijkstra(self, start_vertex):
        if not isinstance(start_vertex, int):
            raise TypeError('Wrong type of source vertex')

        if start_vertex < 0 or start_vertex >= self.vertices:
            raise ValueError('Wrong value of source vertex')

        distances = [sys.maxsize] * self.vertices
        distances[start_vertex] = 0
        visited_vertices = set()

        for count in range(self.vertices):
            idx_current_min_vertex = self.minimal_distance(distances, visited_vertices)
            visited_vertices.add(idx_current_min_vertex)
            for vertex in range(self.vertices):
                if vertex not in visited_vertices and \
                        self.graph[idx_current_min_vertex][vertex] > 0 and \
                        distances[vertex] > distances[idx_current_min_vertex] +\
                        self.graph[idx_current_min_vertex][vertex]:
                    distances[vertex] = distances[idx_current_min_vertex] + \
                                        self.graph[idx_current_min_vertex][vertex]

        return distances
