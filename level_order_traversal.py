#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 16:06:24 2019

@author: dprasad@ad.msystechnologies.com
"""
#import math
#
#class Node:
#    def __init__(self,data=None,left=None,right=None):
#        self.data = data
#        self.left = left
#        self.right = right
#        
#        
#
#r = Node(4)
#r.right = Node(6)
#r.right.left = Node(5)
#r.right.left.left = Node(5)
#
#def traverse(root):
#    if not root:
#        return 0
#    else:
#        return 1+traverse(root.left)+traverse(root.right)
#no = traverse(r)
#height = math.floor(math.log2(no))+1
#print(height)


class Node: 
  
    # A utility function to create a new node 
    def __init__(self, key): 
        self.data = key  
        self.left = None
        self.right = None
  
  
# Function to  print level order traversal of tree 
def printLevelOrder(root): 
    h = height(root) 
    for i in range(1, h+1): 
        printGivenLevel(root, i) 
  
  
# Print nodes at a given level 
def printGivenLevel(root , level): 
    if root is None: 
        return
    if level == 1: 
        print (root.data)
    elif level > 1 : 
        printGivenLevel(root.left , level-1) 
        printGivenLevel(root.right , level-1) 
  
  
""" Compute the height of a tree--the number of nodes 
    along the longest path from the root node down to 
    the farthest leaf node 
"""
def height(node): 
    if node is None: 
        return 0 
    else : 
        # Compute the height of each subtree  
        lheight = height(node.left) 
        rheight = height(node.right) 
  
        #Use the larger one 
        if lheight > rheight : 
            return lheight+1
        else: 
            return rheight+1
  
# Driver program to test above function 
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.left.right = Node(5) 
  
print ("Level order traversal of binary tree is -")
printLevelOrder(root)