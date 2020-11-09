class Graph(object):
    def __init__(self, vertices):
        if not isinstance(vertices, int):
            raise TypeError
        if vertices < 0:
            raise ValueError
        self.vertices = vertices

