import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def minDistance(self, dist, sptSet):
        min_val = sys.maxsize
        min_idx = -1

        for v in range(self.V):
            if dist[v] < min_val and not sptSet[v]:
                min_val = dist[v]
                min_idx = v

        return min_idx

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for _ in range(self.V):
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and not sptSet[v] and dist[u] + self.graph[u][v] < dist[v]:
                    dist[v] = dist[u] + self.graph[u][v]

        return dist

    def addEdge(self, u, v, weight):
        self.graph[u][v] = weight

# Take input from the user
V = int(input("Enter the number of vertices in the graph: "))
g = Graph(V)

E = int(input("Enter the number of edges in the graph: "))
print("Enter the edges and weights in the format (u, v, weight):")
for _ in range(E):
    u, v, weight = map(int, input().split())
    g.addEdge(u, v, weight)

src = int(input("Enter the source vertex: "))

shortest_distances = g.dijkstra(src)

print("Shortest distances from source vertex", src)
for i in range(g.V):
    print("Vertex", i, ":", shortest_distances[i])
