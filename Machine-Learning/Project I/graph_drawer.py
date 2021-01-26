import networkx as nx
import matplotlib.pyplot as plt

g = nx.DiGraph()
g.add_node('a')
g.add_node('s')
g.add_node('t')
g.add_node('l')
g.add_node('b')
g.add_node('e')
g.add_node('x')
g.add_node('d')
g.add_edge('s', 'b')
g.add_edge('s', 'l')
g.add_edge('a', 't')
g.add_edge('t', 'e')
g.add_edge('l', 'e')
g.add_edge('e', 'x')
g.add_edge('e', 'd')
g.add_edge('b', 'd')

nx.draw(g, pos=nx.kamada_kawai_layout(g), with_labels=True, node_size = 1000)
plt.show()