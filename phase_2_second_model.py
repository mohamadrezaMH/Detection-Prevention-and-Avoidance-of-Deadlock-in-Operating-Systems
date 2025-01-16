import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.graph = nx.DiGraph()  # Directed graph
        self.request_edges = []  # Edges representing requests
        self.allocate_edges = []  # Edges representing allocations

    def add_node(self, node):
        if node not in self.graph:
            self.graph.add_node(node)

    def add_request_edge(self, from_node, to_node):
        self.graph.add_edge(from_node, to_node)
        self.request_edges.append((from_node, to_node))

    def add_allocate_edge(self, from_node, to_node):
        self.graph.add_edge(from_node, to_node)
        self.allocate_edges.append((from_node, to_node))

    def detect_deadlock(self):
        try:
            cycles = list(nx.find_cycle(self.graph, orientation='original'))
            if cycles:
                return True
        except nx.exception.NetworkXNoCycle:
            return False

    def draw_graph(self):
        pos = nx.spring_layout(self.graph)
        process_nodes = [node for node in self.graph.nodes if node.startswith('P')]
        resource_nodes = [node for node in self.graph.nodes if node.startswith('R')]

        nx.draw_networkx_nodes(self.graph, pos, nodelist=process_nodes, node_shape='s', node_color='gray', node_size=2000)
        nx.draw_networkx_nodes(self.graph, pos, nodelist=resource_nodes, node_shape='o', node_color='lightblue', node_size=2000)

        nx.draw_networkx_edges(self.graph, pos, edgelist=self.request_edges, edge_color='red', style='dashed', label='request')
        nx.draw_networkx_edges(self.graph, pos, edgelist=self.allocate_edges, edge_color='green', label='allocate')

        nx.draw_networkx_labels(self.graph, pos, font_size=10, font_weight='bold')

        request_labels = {edge: 'request' for edge in self.request_edges}
        allocate_labels = {edge: 'allocate' for edge in self.allocate_edges}
        edge_labels = {**request_labels, **allocate_labels}

        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels, font_color='blue')

        # plt.legend(loc='best')
        plt.show()

# Example to create and check for deadlock using the graph
graph = Graph()
processes = ['P1', 'P2', 'P3']
resources = ['R1', 'R2']

for p in processes:
    graph.add_node(p)
for r in resources:
    graph.add_node(r)

# Add edges to simulate a deadlock scenario
graph.add_request_edge('P1', 'R1')
graph.add_allocate_edge('R1', 'P3')
graph.add_request_edge('P3', 'R2')
# graph.add_allocate_edge('R2', 'P2')
graph.add_request_edge('P2', 'R1')

if graph.detect_deadlock():
    print("Deadlock detected")
else:
    print("No deadlock detected")

# Draw the graph
graph.draw_graph()
