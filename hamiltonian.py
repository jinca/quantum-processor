""" This file is a module to be called in the main.py program """

class Qubit:
    """ Define a qubit and its frequency """
    def __init__(self, id, frequency):
        self.id = id
        self.frequency = frequency
        self.adjacent = {}
    
    """ Represent the qubit and its frequency """
    def __str__(self):
        return f'<Qubit:{self.frequency}>'

    def __repr__(self):
        return self.__str__()

    """ Add each coupling strenght """
    def add_neighbor(self, neighbor, strength=0):
        self.adjacent[neighbor] = strength

    """ Get the adjacent vertices """
    def get_connections(self):
        return self.adjacent.keys()  

    """ Get the value of frequency """
    def get_frequency(self, neighbor):
        return self.adjacent[neighbor]

class CoaxmonQubit(Qubit):
    
    def __init__(self, id, outer_radius, inner_radius):
        self.id = id
        self.outer_radius = outer_radius
        self.inner_radius = inner_radius
        self.adjacent = {}

class RectanglemonQubit(Qubit):

    def __init__(self, id, rect_one_height,rect_one_length, rect_two_height, rect_two_length):
        self.id = id
        self.rect_one_height = rect_one_height
        self.rect_one_length = rect_one_length
        self.rect_two_height = rect_two_height
        self.rect_two_length = rect_two_length
        self.adjacent = {}

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __str__(self):
        return f'<Graph:{list(self.vert_dict.items())}>'

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_qubit(self, vertex):
        self.num_vertices = self.num_vertices + 1
        self.vert_dict[vertex] = vertex

    def get_vertex(self, vertex):
        self.vert_dict.get(vertex)

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_qubit(frm)
        if to not in self.vert_dict:
            self.add_qubit(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.values()

    def get_edges(self):
        output = []
        """ __vertex is the inner vertex to calculate strength"""
        for vertex in self.get_vertices():
            for _vertex in vertex.adjacent.keys():
                output.append((vertex,_vertex))
        return output

class Hamiltonian:

    def __init__(self, graph):
        self.graph = graph

    def sum(self):
        output = []

        for vertex in self.graph.get_vertices():
            if isinstance(vertex, CoaxmonQubit):
                output.append(f'{vertex.outer_radius/vertex.inner_radius}Z{vertex.id}')
            elif isinstance(vertex,RectanglemonQubit):
                output.append(f'{(vertex.rect_one_height*vertex.rect_one_length)/(vertex.rect_two_height*vertex.rect_two_length)}Z{vertex.id}')
            else:
                output.append(f'{vertex.frequency/2}Z{vertex.id}')

        for edge in self.graph.get_edges():
            start_vertex, end_vertex = edge
            output.append(f'{start_vertex.adjacent[end_vertex]}X{start_vertex.id}X{end_vertex.id}')
        return output

    def print_Hamiltonian(self):
        print('H=',' + '.join(self.sum()))
