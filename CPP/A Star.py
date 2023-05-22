def aStarAlgo(start_node, stop_node):
         
        open_set = set(start_node)     #A,B,E,C,G
        closed_set = set()
        g = {} #store distance from starting node      # {'A':0,'B':2,'E':3,'C':3,'G':11}
        parents = {}# parents contains an adjacency map of all nodes    'C:B'
 
        g[start_node] = 0 #ditance of starting node from itself is zero
        #start_node is root node i.e it has no parent nodes
        parents[start_node] = start_node         #so start_node is set to its own parent node
         
        while len(open_set) > 0:   #loop untill opesn becomes empty
            fn = None
 
            #node with lowest f() is found
            for v in open_set:   # for every node in openset find node with lowest g value
                if fn == None or g[v] + heuristic(v) < g[fn] + heuristic(fn):              # TRAVERSE OPEN SET ,,, GET FN== V WITH LOWEST F() VALUE 
                    fn = v      
             
                     
            if fn == stop_node or Graph_nodes[fn] == None:
                pass
            else:
                for (nb, weight) in get_neighbors(fn):  #for every neighbour of fn
                    #nodes 'm' not in first and last set are added to first
                    #n is set its parent
                    if nb not in open_set and nb not in closed_set:  # check if neb is in any list , if not then add in open and set its parent =fn, calculate g value
                        open_set.add(nb)
                        parents[nb] = fn
                        g[nb] = g[fn] + weight
                         
     
                    #for each node m,compare its distance from start i.e g(m) to the
                    #from start through n node
                    else:                                  # if neb is present in any (already visited/calculated) then compare new g value and neb's g value
                        if g[nb] > g[fn] + weight:         #    update if new g val of neb is small , update parent of neb=fn 
                            #update g(m)
                            g[nb] = g[fn] + weight
                            #change parent of m to n
                            parents[nb] = fn      
                             
                           
                            if nb in closed_set:
                                closed_set.remove(nb)            #if neb is in closed set,remove from close and add to open ....as it comes to new path
                                open_set.add(nb)
                                    
                                        
                                             #checked every neb and exited
            if fn == None:                                      # if fn has no connection/child/branch then exit prog
                print('Path does not exist!')
                return None
 
            # if the current node is the stop_node
            # then we begin reconstructin the path from it to the start_node
            if fn == stop_node:                                #if goal node found ,,, start creating final path using array
                path = []
 
                while parents[fn] != fn:                           # append the node in path untill self parent is encounterderd
                    path.append(fn)
                    fn = parents[fn]                                                                    
 
                path.append(start_node)                            # append start as it exited from loop 
    
                path.reverse()                                     # GCBA====ABCG
 
                print('Path found: {}'.format(path))
                return path
 
 
            # remove fn from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_set.remove(fn)                                         # visited fn , hence add it in closed and remove from open
            closed_set.add(fn)
                    
        print('Path does not exist!')
        return None
         
#define fuction to return neighbor and its distance
#from the passed node
def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None
#for simplicity we ll consider heuristic distances given
#and this function returns heuristic distance for all nodes
def heuristic(n):
        return H_dist[n]
 
#Describe your graph here  

Graph_nodes = { }
H_dist={ }
n=int(input("Enter the Number of Node "))
start=input("Enter the start Node:-")
goal=input("Enter the goal Node:-")

for i in range(1,n+1):
    node=input("Enter the Node ")
    print("Node :",node)
    hd=int(input("Enter the Heuristic value:"))
    H_dist[node]=hd
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

aStarAlgo(start,goal)



