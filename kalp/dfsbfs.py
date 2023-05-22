from collections import defaultdict

# Class representing a graph
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    # Function to add an edge to the graph
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    # Recursive function for DFS traversal
    def dfs_recursive(self, v, visited):
        visited.add(v)
        print(v, end=" ")

        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited)

    # Function for DFS traversal
    def dfs(self, start_vertex):
        visited = set()
        self.dfs_recursive(start_vertex, visited)

    # Function for BFS traversal
    def bfs(self, start_vertex):
        visited = set()
        queue = []
        queue.append(start_vertex)
        visited.add(start_vertex)

        while queue:
            v = queue.pop(0)
            print(v, end=" ")

            for neighbor in self.graph[v]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)


# Create a graph
graph = Graph()

# Take user input for the number of edges and vertices
num_vertices = int(input("Enter the number of vertices: "))
num_edges = int(input("Enter the number of edges: "))

# Take user input for the edges
print("Enter the edges (format: source destination):")
for _ in range(num_edges):
    u, v = map(int, input().split())
    graph.add_edge(u, v)

# Take user input for the start vertex
start_vertex = int(input("Enter the start vertex: "))

# Perform DFS and BFS traversal
print("DFS Traversal:")
graph.dfs(start_vertex)

print("\nBFS Traversal:")
graph.bfs(start_vertex)
