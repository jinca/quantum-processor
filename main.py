class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0
