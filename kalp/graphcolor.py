class GraphColoring:
    def __init__(self, graph, colors):
        self.graph = graph
        self.colors = colors
        self.num_vertices = len(graph)
        self.solution = [-1] * self.num_vertices

    def is_safe(self, vertex, color):
        for v in range(self.num_vertices):
            if self.graph[vertex][v] == 1 and self.solution[v] == color:
                return False
        return True

    def solve_graph_coloring(self, vertex):
        if vertex == self.num_vertices:
            return True

        for color in range(self.colors):
            if self.is_safe(vertex, color):
                self.solution[vertex] = color

                if self.solve_graph_coloring(vertex + 1):
                    return True

                self.solution[vertex] = -1

        return False

    def solve(self):
        if self.solve_graph_coloring(0):
            return self.solution
        else:
            return []


# Take input from the user
num_vertices = int(input("Enter the number of vertices in the graph: "))
colors = int(input("Enter the number of colors available: "))

graph = []
print("Enter the adjacency matrix for the graph:")
for _ in range(num_vertices):
    row = list(map(int, input().split()))
    graph.append(row)

# Create an instance of GraphColoring class and solve the problem
graph_coloring = GraphColoring(graph, colors)
solution = graph_coloring.solve()

# Print the solution
if solution:
    print("Solution:")
    for vertex, color in enumerate(solution):
        print(f"Vertex {vertex + 1} is colored with color {color + 1}")
else:
    print("No solution exists for the given graph and number of colors.")
