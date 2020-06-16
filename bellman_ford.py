import sys 
  
class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = {}

    def bellman_ford(self,source):
        distance = [sys.maxsize] * self.V
        distance[source] = 0
        before = [sys.maxsize] * self.V
        for i  in range(self.V-1):
            before = list(distance)
            for u in range(self.V):
                for v in self.graph[u]:
                        distance[v] = min(distance[v],distance[u]+self.graph[u][v])
            if(before==distance):
                print(i)
                break
                
        print("from the give source vertex -- > ",source)
        for vertex in range(self.V):
            print("Vertex ",vertex," --> Distance = ",distance[vertex])
        print(i)
                
g  = Graph(9) 
g.graph = {0:{1:4,7:8},1:{0:4,2:8,7:11},2:{1:8,3:7,5:4,8:2},3:{2:7,4:9,5:14},4:{3:9,5:10},
           5:{2:4,3:14,4:10,6:2},6:{5:2,7:1,8:6},7:{0:8,1:11,6:1,8:7},8:{2:2,6:6,7:7}}
g.bellman_ford(5)
