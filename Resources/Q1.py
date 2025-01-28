import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

def generate_lattice(n):
    G = nx.grid_2d_graph(n, n)
    return G

def percolate_lattice(G, p):
    for edge in list(G.edges()):
        if np.random.rand() > p:
            G.remove_edge(*edge)
    return G

def find_largest_cluster_size(G):
    clusters = list(nx.connected_components(G))
    if clusters:
        largest_cluster = max(clusters, key=len)
        largest_cluster_size = len(largest_cluster)
    else:
        largest_cluster_size = 0
    return largest_cluster_size

# Parameters
L = 20  # Size of the smaller lattice
p_values = np.linspace(0, 1, 100)  # Percolation probabilities
largest_cluster_sizes_L = []
largest_cluster_sizes_2L = []

# Generate and percolate lattices, track largest cluster sizes
for p in p_values:
    G_L = generate_lattice(L)
    G_L = percolate_lattice(G_L, p)
    largest_cluster_sizes_L.append(find_largest_cluster_size(G_L))

    G_2L = generate_lattice(2 * L)
    G_2L = percolate_lattice(G_2L, p)
    largest_cluster_sizes_2L.append(find_largest_cluster_size(G_2L))

# Plotting
plt.plot(p_values, largest_cluster_sizes_L, label='Lattice Size LxL')
plt.plot(p_values, largest_cluster_sizes_2L, label='Lattice Size 2Lx2L')
plt.xlabel('Occupation Probability (p)')
plt.ylabel('Size of Largest Cluster')
plt.title('Largest Cluster Size vs. Occupation Probability')
plt.legend()
plt.show()
