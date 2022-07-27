import hamiltonian
 
v1 = hamiltonian.Vertex(10.0)
v2 = hamiltonian.Vertex(15.0)
v3 = hamiltonian.Vertex(5.5)
v4 = hamiltonian.Vertex(12.2)

graph = hamiltonian.Graph()
graph.add_vertex(v1)
graph.add_vertex(v2)
graph.add_vertex(v3)
graph.add_vertex(v4)

graph.add_edge(v1, v2, 0.5)
graph.add_edge(v2, v3, 0.6)
graph.add_edge(v3, v4, 0.3)
graph.add_edge(v4, v1, 0.55)

print(v1, v2, v3, v4)
print(graph)

h = hamiltonian.Hamiltonian(graph)
h.sum()
