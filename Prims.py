
import sys

class Graph():
    def __init__(self,v):
        self.V = v
        self.graph = {}
        
    def min_key(self,key,traversed):
        min_val = sys.maxsize
        for v in range(self.V):
            if traversed[v] == False and min_val > key[v]:
                min_val = key[v]
                min_index = v
        return min_index
    def prims(self):
        key = [sys.maxsize] * self.V
        key[0] = 0
        traversed = [False] * self.V
        parent = [None] *self.V
        parent[0] = [-1] 
        
        for val in range(self.V):
            u = self.min_key(key,traversed)
            traversed[u] = True
            for v in self.graph[u]:
                if traversed[v] == False:
                    key[v] = min(key[v],self.graph[u][v])
                    parent[v] = u
        for x in range(1,self.V):
            print("Edge",parent[x]," - ",x," Weight =",self.graph[parent[x]][x])

g= Graph(9)
g.graph = {0:{1:4,7:8},1:{0:4,2:8,7:11},2:{1:8,3:7,5:4,8:2},3:{2:7,4:9,5:14},4:{3:9,5:10},
           5:{2:4,3:14,4:10,6:2},6:{5:2,7:1,8:6},7:{0:8,1:11,6:1,8:7},8:{2:2,6:6,7:7}}
g.prims()
