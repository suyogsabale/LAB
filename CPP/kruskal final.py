# Kruskal's algorithm in Python

# Complexities of the Kruskal's Algorithm
# Time Complexity :
# O(E*log(E))
# Space Complexity:
# O(E)

    # Find function to determine the subset of an element
def find( parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

    # Function to perform union of two subsets
def apply_union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if rank[xroot] < rank[yroot]:               # decide based on rank
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:                 # greater rank will parent of other 
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

    # Applying Kruskal's algorithm
def kruskal_algo(graph,n):
    result = []
    i= 0
    e=0                                       #edges added to result tree
    graph = sorted(graph, key=lambda item: item[2])  # Sort edges in ascending order of weight======= sort = fun,, lambda specify sort criteria
    parent = []                                        #item:item[2] means 3rd item i.e. weight of edge====
    rank = []           #to give levels to child and parents(in apply union to decide)
    for node in range(n):
        parent.append(node)  # Initialize each node -----par[i]=i    self parent as a separate subset
        rank.append(0)  # Initialize rank of each subset as 0
    while e < n - 1:                            #untill n-1 edges are added to result
        u, v, w = graph[i]  # Pick the smallest edge
        i = i + 1
        x = find(parent, u)  # Find the subset of the vertices
        y = find(parent, v)
        if x != y:  # If including this edge doesn't form a cycle
            e = e + 1           # if no cycle then append edge in result and inc e
            result.append([u, v, w])  # Add the edge to the result
            apply_union(parent, rank, x, y)  # Perform union of two subsets
    for u, v, weight in result:
        print("%d - %d: %d" % (u, v, weight))  # Print the resulting minimum spanning tree

n = int(input("Enter the number of vertices in the graph: "))
graph = []

E = int(input("Enter the number of edges in the graph: "))
print("Enter the edges and weights in the format (u, v, weight):")
for z in range(E):

    u=int(input("Enter the src of edge"+ str(z)))
    v=int(input("Enter the dest of edge"+ str(z)))
    w=int(input("Enter the weight of edge"+ str(z)))
    graph.append([u, v, w])
    
kruskal_algo(graph,n)
