""" This file is a module to be called in the main.py program """

class Vertex:
    """ Define vertex itself """
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    """ Define floating point values for each qubit frequency and for each coupling strenght """
    def __float__(self):
        return float(self.id) + ' adjacent: ' + float([x.id for x in self.adjacent])

    """ Define the frequency of the neighbor """
    def add_neighbor(self, neighbor, freq=0):
        self.adjacent[neighbor] = freq

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_freq(self, neighbor):
        return self.adjacent[neighbor]

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

class Hamiltonian:
    def print_Hamiltonian(self):
