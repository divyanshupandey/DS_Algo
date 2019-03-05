import sys 
  
class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = {}
    def min_distance(self,distance,traversed):
        min_index = 0 
        min_value = sys.maxsize
        for i in range(self.V):
            if traversed[i] is False and min_value > distance[i]:
                min_value = distance[i]
                min_index = i
        return min_index
    def dijkstra(self,source):
        distance = [sys.maxsize] * self.V
        traversed = [False] * self.V
        distance[source] = 0
        for i  in range(self.V):
            u = self.min_distance(distance,traversed)
            traversed[u] = True
            for v in self.graph[u]:
                if(traversed[v] is False):
                    distance[v] = min(distance[v],distance[u]+self.graph[u][v])
        print("from the give source vertex -- > ",source)
        for vertex in range(self.V):
            print("Vertex ",vertex," --> Distance = ",distance[vertex])
                
g  = Graph(9) 
g.graph = {0:{1:4,7:8},1:{0:4,2:8,7:11},2:{1:8,3:7,5:4,8:2},3:{2:7,4:9,5:14},4:{3:9,5:10},
           5:{2:4,3:14,4:10,6:2},6:{5:2,7:1,8:6},7:{0:8,1:11,6:1,8:7},8:{2:2,6:6,7:7}}
g.dijkstra(0)
#g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
#           [4, 0, 8, 0, 0, 0, 0, 11, 0], 
#           [0, 8, 0, 7, 0, 4, 0, 0, 2], 
#           [0, 0, 7, 0, 9, 14, 0, 0, 0], 
#           [0, 0, 0, 9, 0, 10, 0, 0, 0], 
#           [0, 0, 4, 14, 10, 0, 2, 0, 0], 
#           [0, 0, 0, 0, 0, 2, 0, 1, 6], 
#           [8, 11, 0, 0, 0, 0, 1, 0, 7], 
#           [0, 0, 2, 0, 0, 0, 6, 7, 0] 
#          ]; 
# Python program for Dijkstra's single  
# source shortest path algorithm. The program is  
# for adjacency matrix representation of the graph 
  
# Library for INT_MAX 
#import sys 
#  
#class Graph(): 
#  
#    def __init__(self, vertices): 
#        self.V = vertices 
#        self.graph = [[0 for column in range(vertices)]  
#                      for row in range(vertices)] 
#  
#    def printSolution(self, dist): 
#        print ("Vertex tDistance from Source")
#        for node in range(self.V): 
#            print (node,"t",dist[node] )
#  
#    # A utility function to find the vertex with  
#    # minimum distance value, from the set of vertices  
#    # not yet included in shortest path tree 
#    def minDistance(self, dist, sptSet): 
#  
#        # Initilaize minimum distance for next node 
#        min = sys.maxsize 
#  
#        # Search not nearest vertex not in the  
#        # shortest path tree 
#        for v in range(self.V): 
#            if dist[v] < min and sptSet[v] == False: 
#                min = dist[v] 
#                min_index = v 
#  
#        return min_index 
#  
#    # Funtion that implements Dijkstra's single source  
#    # shortest path algorithm for a graph represented  
#    # using adjacency matrix representation 
#    def dijkstra(self, src): 
#  
#        dist = [sys.maxsize] * self.V 
#        dist[src] = 0
#        sptSet = [False] * self.V 
#  
#        for cout in range(self.V): 
#  
#            # Pick the minimum distance vertex from  
#            # the set of vertices not yet processed.  
#            # u is always equal to src in first iteration 
#            u = self.minDistance(dist, sptSet) 
#  
#            # Put the minimum distance vertex in the  
#            # shotest path tree 
#            sptSet[u] = True
#  
#            # Update dist value of the adjacent vertices  
#            # of the picked vertex only if the current  
#            # distance is greater than new distance and 
#            # the vertex in not in the shotest path tree 
#            for v in range(self.V): 
#                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]: 
#                        dist[v] = dist[u] + self.graph[u][v] 
#  
#        self.printSolution(dist) 
#  
## Driver program 
#g  = Graph(9) 
#g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
#           [4, 0, 8, 0, 0, 0, 0, 11, 0], 
#           [0, 8, 0, 7, 0, 4, 0, 0, 2], 
#           [0, 0, 7, 0, 9, 14, 0, 0, 0], 
#           [0, 0, 0, 9, 0, 10, 0, 0, 0], 
#           [0, 0, 4, 14, 10, 0, 2, 0, 0], 
#           [0, 0, 0, 0, 0, 2, 0, 1, 6], 
#           [8, 11, 0, 0, 0, 0, 1, 0, 7], 
#           [0, 0, 2, 0, 0, 0, 6, 7, 0] 
#          ]; 
#  
#g.dijkstra(0); 