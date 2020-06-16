
class Graph:
    def __init__(self,v):
        self.V = v
        self.graph = []
    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])
    def find(self,parent,i):
        if(parent[i] == i):
            return i
        else:
            return self.find(parent,parent[i])
    def union(self,parent,rank,x,y):
        xroot = self.find(parent,x)
        yroot = self.find(parent,y)
        if(rank[xroot]>rank[yroot]):
            parent[yroot] = xroot
        elif(rank[xroot]<rank[yroot]):
            parent[xroot] = yroot
        else:
            parent[xroot] = yroot
            rank[yroot]+=1
            
    def kruskal(self):
        e=0
        i=0
        result = []
        self.graph = sorted(self.graph,key = lambda item:item[2])
        parent = []
        rank = []
        for j in range(self.V):
            parent.append(j)
            rank.append(0)
        while e < self.V-1:
            u,v,w = self.graph[i]
            i+=1
            x=self.find(parent,u)
            y=self.find(parent,v)
            if x!=y:
                e+=1
                result.append([u,v,w])
                self.union(parent,rank,x,y)
        print("  Edge -->  Weight")
        for i in result:
            print( " ",i[0],i[1]," -->  ",i[2])

g = Graph(4) 
g.addEdge(0, 1, 10) 
g.addEdge(0, 2, 6) 
g.addEdge(0, 3, 5) 
g.addEdge(1, 3, 15) 
g.addEdge(2, 3, 4) 
  
g.kruskal() 
                
                
                
                
                
                
                
                
                
