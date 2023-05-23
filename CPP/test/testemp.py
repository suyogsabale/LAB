def find(parent,i):
    if parent[i]==i:
        return i
    return find(parent,parent[i])

def apply_union(parent,rank,x,y):
    xroot=find(parent,x)
    yroot=find(parent,y)

    if rank[xroot]>rank[yroot]:
        parent[yroot]=xroot
    elif rank[yroot]<rank[xroot]:
        parent[xroot]=yroot
    else:
        parent[xroot]=yroot
        rank[xroot]+=1
    
    

def kruskal_algo(graph,n):
    result=[]
    i=0
    e=0
    rank=[]
    parent=[]

    graph=sorted(graph,key=lambda item:item[2])

    for node in range(n):
        parent.append(node)
        rank.append(0)
    while e<n-1:
        u,v,w=graph[i]
        
        i=i+1
        
        x=find(parent,u)
        y=find(parent,v)

        if x!=y:
            result.append([u,v,w])
            e=e+1
            apply_union(parent,rank,x,y)
    for u,v,w in result:
        print("%d -> %d :: %d"%(u,v,w))



n=int(input("Enter no of verticess"))
e=int(input("Enterenno of edges"))

graph=[]

for z in range(e):
    u=int(input("Enter the src of edge"+ str(z)))
    v=int(input("Enter the dest of edge"+ str(z)))
    w=int(input("Enter the weight of edge"+ str(z)))
    graph.append([u, v, w])

kruskal_algo(graph,n)