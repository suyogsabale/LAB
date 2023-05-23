# Kruskal's algorithm in Python

# Complexities of the Kruskal's Algorithm

# Time Complexity :
# O(E*log(E))

# Space Complexity:
# O(E)

# Class representing a graph
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    # Function to add an edge to the graph
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # Find function to determine the subset of an element
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # Function to perform union of two subsets
    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    # Applying Kruskal's algorithm
    def kruskal_algo(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])  # Sort edges in ascending order of weight
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)  # Initialize each node as a separate subset
            rank.append(0)  # Initialize rank of each subset as 0
        while e < self.V - 1:
            u, v, w = self.graph[i]  # Pick the smallest edge
            i = i + 1
            x = self.find(parent, u)  # Find the subset of the vertices
            y = self.find(parent, v)
            if x != y:  # If including this edge doesn't form a cycle
                e = e + 1
                result.append([u, v, w])  # Add the edge to the result
                self.apply_union(parent, rank, x, y)  # Perform union of two subsets
        for u, v, weight in result:
            print("%d - %d: %d" % (u, v, weight))  # Print the resulting minimum spanning tree


# Take input from the user
n = int(input("Enter the number of vertices in the graph: "))
g = Graph(n)

E = int(input("Enter the number of edges in the graph: "))
print("Enter the edges and weights in the format (u, v, weight):")
for z in range(E):
    # u, v, weight = map(int, input().split())
    # g.add_edge(u, v, weight)

    a=int(input("Enter the src of edge"+ str(z)))
    b=int(input("Enter the dest of edge"+ str(z)))
    c=int(input("Enter the weight of edge"+ str(z)))
    g.add_edge(a,b,c)
    
# Apply Kruskal's algorithm and print the resulting minimum spanning tree
g.kruskal_algo()
