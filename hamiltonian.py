""" This file is a module to be called in the main.py program """

class Vertex:
    """ Define a vertex and its frequency """
    def __init__(self, frequency):
        self.frequency = frequency
        self.adjacent = {}
    
    """ Represent the vertex and its frequency """
    def __str__(self):
        return f'<Vertex:{self.frequency}>'

    def __repr__(self):
        return self.__str__()

    """ Add each coupling strenght """
    def add_neighbor(self, neighbor, strength=0):
        self.adjacent[neighbor] = strength

    def get_connections(self):
        return self.adjacent.keys()  

    def get_frequency(self, neighbor):
        return self.adjacent[neighbor]

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __str__(self):
        return f'<Graph:{list(self.vert_dict.items())}>'

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.values()

class Hamiltonian:

    def __init__(self, graph):
        self.graph = graph

    def sum(self):
        print(self.graph.get_vertices())

    def print_Hamiltonian(self):
        pass
