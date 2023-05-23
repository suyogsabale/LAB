def dijikstra(start_node, stop_node):
         
        open_set = set(start_node)     #A,B,E,C,G
        closed_set = set()
        g = {} 
        parents = {}
  
        g[start_node] = 0
        parents[start_node] = start_node
         
        while len(open_set) > 0:
            fn = None

           
            for v in open_set:
                if fn == None or g[v]  < g[fn] :              #compare g value only
                    fn = v      


            if fn == stop_node or Graph_nodes[fn] == None:
                pass
            else:
                for (nb, weight) in get_neighbors(fn):
                   
                    if nb not in open_set and nb not in closed_set:
                        open_set.add(nb)
                        parents[nb] = fn
                        g[nb] = g[fn] + weight
                        
                    
                    else:
                        if g[nb] > g[fn] + weight:
                            g[nb] = g[fn] + weight
                            parents[nb] = fn      
                             
                           
                            if nb in closed_set:
                                closed_set.remove(nb)
                                open_set.add(nb)

            if fn == None:
                print('Path does not exist!')
                return None
 
           
            if fn == stop_node:
                path = []
 
                while parents[fn] != fn:
                    path.append(fn)
                    fn = parents[fn]
 
                path.append(start_node)
 
                path.reverse()
 
                print('Path found: {}'.format(path))
                return path
 
 
            
            open_set.remove(fn)
            closed_set.add(fn)
 
        print('Path does not exist!')
        return None
         

def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None

# Graph_nodes = {
#     'A': [('B', 2), ('E', 3)],
#     'B': [('C', 1),('G', 9)],
#     'C': None,
#     'E': [('D', 6)],
#     'D': [('G', 1)],

# }

Graph_nodes = { }
n=int(input("Enter the Number of Node "))
start=input("Enter the start Node:-")
goal=input("Enter the goal Node:-")

for i in range(1,n+1):
    node=input("Enter the Node ")
    print("Node :",node)
    array=[]
    adn=int(input("Enter the number of Adjacent node for "+node))
    print("AD Node :",adn)
    if(adn==0):
        Graph_nodes[node]=None
    else:
        for j in range(1,adn+1):
            adjK=input("Enter the Adjacent Node ")
            adjV=int(input("Enter the Adjacent Edge Weight "))
            t=(adjK,adjV)
            array.append(t)
        print(array)
        Graph_nodes[node]=array
        print("Graph Nodes :",Graph_nodes)
    
        array=[]                            # EMPTY THE ARRAY AFTER PUTTING IT IN GRAPH NODE FOR PARTICULAR NODE
        
        
print(Graph_nodes)


dijikstra('A', 'G')
