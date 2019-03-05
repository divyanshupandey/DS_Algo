#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 17:04:10 2019

@author: dprasad@ad.msystechnologies.com
"""
class Node:
    def __init__(self,data,nextnode):
        self.data = data
        self.nextnode = nextnode 
        
        
        
        
class LL:
    def __init__(self):
        self.head = None
    def node_add_last(self,data):
        node = Node(data,None)
        if(self.head==None):
            self.head = node
        else:
            itr = self.head
            while (itr.nextnode != None):
                itr = itr.nextnode
            itr.nextnode = node
    def node_add_first(self,data):
        node = Node(data,None)
        if(self.head==None):
            self.head = node
        else:
            node.nextnode = self.head
            self.head = node
    def print_list(self):
        itr = self.head
        while(itr != None):
            print(itr.data)
            itr = itr.nextnode
            
            

list1  = LL()
list1.node_add_last(3)
list1.node_add_last(2)
list1.node_add_last(1)
list1.print_list()



