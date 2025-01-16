class Graph:
    def __init__(self):
        self.adjacency_list = {}
    def add_node(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []

    def add_edge(self, from_node, to_node):
        if from_node in self.adjacency_list:
            self.adjacency_list[from_node].append(to_node)

    def detect_deadlock(self):
        visited = set()
        rec_stack = set()
        def dfs(node):
            if node in rec_stack:
                return True
            if node in visited:
                return False
            visited.add(node)
            rec_stack.add(node)
            for neighbor in self.adjacency_list.get(node, []):
                if dfs(neighbor):
                    return True
            rec_stack.remove(node)
            return False
        for node in self.adjacency_list:
            if dfs(node):
                return True
        return False

# Example to build and check for deadlock using the graph
graph = Graph()
processes = ['P1', 'P2', 'P3']
resources = ['R1', 'R2']

for p in processes:
    graph.add_node(p)
for r in resources:
    graph.add_node(r)

# Adding edges to simulate deadlock scenario
graph.add_edge('P1', 'R1')
graph.add_edge('R1', 'P3')
graph.add_edge('P3', 'R2')
graph.add_edge('R2', 'P2')
graph.add_edge('P2', 'R1')

if graph.detect_deadlock():
    print("Deadlock detected")
else:
    print("No deadlock detected")
