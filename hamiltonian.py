""" This file is a module to be called in the main.py program """

class Vertex:
    """ Define vertex itself """
    def __init__(self, frequency):
        self.frequency = frequency
        self.adjacent = {}

    """ Define floating point values for each qubit frequency and for each coupling strenght """
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
        return self.vert_dict.keys()

class Hamiltonian:

    def sum_frequency(self):
        pass

    def print_Hamiltonian(self):
        pass
