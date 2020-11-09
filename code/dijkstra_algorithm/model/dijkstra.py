import sys


class Graph(object):
    def __init__(self, vertices):
        if not isinstance(vertices, int):
            raise TypeError
        if vertices < 0:
            raise ValueError
        self.vertices = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def minimal_distance(self, distances, found_vertex_distances):
        minimal = sys.maxsize
        minimal_index = 0

        for vertex in range(self.vertices):
            if distances[vertex] < minimal and not found_vertex_distances[vertex]:
                minimal = distances[vertex]
                minimal_index = vertex
        return minimal_index

    def dijkstra(self, start_vertex):
        if not isinstance(start_vertex, int):
            raise TypeError('Wrong type of source vertex')

        if start_vertex < 0 or start_vertex >= self.vertices:
            raise ValueError('Wrong value of source vertex')

        if len(self.graph) != self.vertices:
            raise ValueError('Wrong length in graphs row')

        for row in range(self.vertices):
            if len(self.graph[row]) != self.vertices:
                raise ValueError('Wrong length in graphs column')
            for column in range(self.vertices):
                if not isinstance(self.graph[row][column], int) and \
                        not isinstance(self.graph[row][column], float):
                    raise TypeError('Wrong type of value in graph matrix')
        distances = [sys.maxsize] * self.vertices
        distances[start_vertex] = 0
        found_vertex_distances = [False] * self.vertices

        for count in range(self.vertices):
            idx_current_min_vertex = self.minimal_distance(distances, found_vertex_distances)
            found_vertex_distances[idx_current_min_vertex] = True
            for vertex in range(self.vertices):
                if self.graph[idx_current_min_vertex][vertex] > 0 and \
                        not found_vertex_distances[vertex] and \
                        distances[vertex] > distances[idx_current_min_vertex] +\
                        self.graph[idx_current_min_vertex][vertex]:
                    distances[vertex] = distances[idx_current_min_vertex] + \
                                        self.graph[idx_current_min_vertex][vertex]

        return distances
