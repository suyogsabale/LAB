import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def minKey(self, key, mstSet):
        min_val = sys.maxsize
        min_idx = -1

        for v in range(self.V):
            if key[v] < min_val and not mstSet[v]:
                min_val = key[v]
                min_idx = v

        return min_idx

    def primMST(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V

        for _ in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and not mstSet[v] and self.graph[u][v] < key[v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        return parent

    def addEdge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight

# Take input from the user
V = int(input("Enter the number of vertices in the graph: "))
g = Graph(V)

E = int(input("Enter the number of edges in the graph: "))
print("Enter the edges and weights in the format (u, v, weight):")
for _ in range(E):
    u, v, weight = map(int, input().split())
    g.addEdge(u, v, weight)

mst = g.primMST()

print("Edges in the Minimum Spanning Tree:")
for i in range(1, g.V):
    print(f"{mst[i]} - {i}")
