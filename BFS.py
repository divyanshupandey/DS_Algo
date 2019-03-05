## Python3 Program to print BFS traversal 
## from a given source vertex. BFS(int s) 
## traverses vertices reachable from s. 
#from collections import defaultdict 
#  
## This class represents a directed graph 
## using adjacency list representation 
#class Graph: 
#  
#    # Constructor 
#    def __init__(self): 
#  
#        # default dictionary to store graph 
#        self.graph = defaultdict(list) 
#  
#    # function to add an edge to graph 
#    def addEdge(self,u,v): 
#        self.graph[u].append(v) 
#  
#    # Function to print a BFS of graph 
#    def BFS(self, s): 
#  
#        # Mark all the vertices as not visited 
#        visited = [False] * (len(self.graph)) 
#  
#        # Create a queue for BFS 
#        queue = [] 
#  
#        # Mark the source node as  
#        # visited and enqueue it 
#        queue.append(s) 
#        visited[s] = True
#  
#        while queue: 
#  
#            # Dequeue a vertex from  
#            # queue and print it 
#            s = queue.pop(0) 
#            print (s, end = " ") 
#  
#            # Get all adjacent vertices of the 
#            # dequeued vertex s. If a adjacent 
#            # has not been visited, then mark it 
#            # visited and enqueue it 
#            for i in self.graph[s]: 
#                if visited[i] == False: 
#                    queue.append(i) 
#                    visited[i] = True
#  
## Driver code 
#  
## Create a graph given in 
## the above diagram 
#g = Graph() 
#g.addEdge(0, 1) 
#g.addEdge(0, 2) 
#g.addEdge(1, 2) 
#g.addEdge(2, 0) 
#g.addEdge(2, 3) 
#g.addEdge(3, 3)
#g.BFS(3)



from collections import defaultdict

class Graph:
    def __init__(self):
        self.g = defaultdict(list)
    def addEdge(self,u,v):
        self.g[u].append(v)
    def BFS(self,vertex):
        if vertex in self.g:
            visited = [False] * len(self.g)
            queue = [vertex]
            visited[vertex] = True
            while queue:
                s = queue.pop()
                print(s, end = " ")
                for i in self.g[s]:
                    if(visited[i] == False):
                        queue.append(i)
                        visited[i] = True
        
g1 = Graph()
g1.addEdge(0,1)
g1.addEdge(0,2)
g1.addEdge(1,2)
g1.addEdge(2,0)
g1.addEdge(2,3)
g1.addEdge(3,3)
if(4 in g1.g):
    print("ji")
print(g1.g.items())
g1.BFS(2)