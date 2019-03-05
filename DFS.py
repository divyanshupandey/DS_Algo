#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 16:00:09 2019

@author: dprasad@ad.msystechnologies.com
"""

from collections import defaultdict

class Graph:
    def __init__(self):
        self.g = defaultdict(list)
    def addEdge(self,u,v):
        self.g[u].append(v)
    def DFSUtil(self,v,visited):
        visited[v] = True
#        print(v,end = " ")
        for i in self.g[v]:
            print(i)
            if(visited[i] is False):
                self.DFSUtil(i,visited)
    def DFS(self,v):
        visited = [False] * len(self.g)
        self.DFSUtil(v,visited)
g1 = Graph()
g1.addEdge(0,1)
g1.addEdge(0,2)
g1.addEdge(1,2)
g1.addEdge(2,0)
g1.addEdge(2,3)
g1.addEdge(3,3)
g1.DFS(2)