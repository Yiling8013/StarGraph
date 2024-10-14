import networkx as nx
import matplotlib.pyplot as plt

# Function to create a star graph
def create_star_graph(n):
    star_graph = nx.star_graph(n)
    return star_graph

# Number of nodes (including the center node)
num_nodes = 100

# Generate the star graph
star_graph = create_star_graph(num_nodes - 1)  # num_nodes - 1 since center node is included in the count

# Plot the star graph
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(star_graph)  # Use spring layout for positioning nodes
nx.draw(star_graph, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500, font_size=10)
plt.title(f"Star Graph with {num_nodes} Nodes")
plt.show()

