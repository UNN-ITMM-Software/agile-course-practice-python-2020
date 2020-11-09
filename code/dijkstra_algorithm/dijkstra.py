class Graph(object):
    def __init__(self, vertices):
        if not isinstance(vertices, int):
            raise TypeError
        if vertices < 0:
            raise ValueError
        self.vertices = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
