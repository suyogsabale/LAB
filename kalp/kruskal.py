class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, weight):
        self.graph.append([u, v, weight])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskalMST(self):
        result = []
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        i = 0
        e = 0

        while e < self.V - 1:
            u, v, weight = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e += 1
                result.append([u, v, weight])
                self.union(parent, rank, x, y)

        return result


# Take input from the user
V = int(input("Enter the number of vertices in the graph: "))
g = Graph(V)

E = int(input("Enter the number of edges in the graph: "))
print("Enter the edges and weights in the format (u, v, weight):")
for _ in range(E):
    u, v, weight = map(int, input().split())
    g.addEdge(u, v, weight)

mst = g.kruskalMST()

print("Edges in the Minimum Spanning Tree:")
for u, v, weight in mst:
    print(f"{u} - {v}, Weight: {weight}")
