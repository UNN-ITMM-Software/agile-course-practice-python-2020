class Graph(object):
    def __init__(self, vertices):
        if vertices < 0:
            raise ValueError
        self.vertices = vertices

