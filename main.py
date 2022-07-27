import hamiltonian
 
v1 = hamiltonian.Qubit(1, 10.0)
v2 = hamiltonian.Qubit(2, 15.0)
v3 = hamiltonian.Qubit(3, 5.5)
v4 = hamiltonian.Qubit(4, 12.2)

graph = hamiltonian.Graph()
graph.add_qubit(v1)
graph.add_qubit(v2)
graph.add_qubit(v3)
graph.add_qubit(v4)

graph.add_edge(v1, v2, 0.5)
graph.add_edge(v2, v3, 0.6)
graph.add_edge(v3, v4, 0.3)
graph.add_edge(v4, v1, 0.55)

h = hamiltonian.Hamiltonian(graph)
h.print_Hamiltonian()
