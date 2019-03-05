#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 13:58:50 2019

@author: dprasad@ad.msystechnologies.com
"""

class Node:
    def __init__(self,data=None,left=None,right=None,height=1):
        self.data = data
        self.left = left
        self.right = right
        self.height = 1

class AVL_Tree():
    def __init__(self,root=None):
        self.root = root
    def insert(self,root,key):
        if not root:
            return Node(key)
        elif root.data < key:
            root.right = self.insert(root.right,key)
        else:
            root.left = self.insert(root.left,key)
        #get height
        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))
        #get balance
        balance = self.balance(root)

        #case 1 LL
        if (balance>1) and key < root.left.data:
            root = self.rightRotate(root)
            return root
        #case 2 RR
        elif (balance<-1) and key >root.right.data:
            root = self.leftRotate(root)
            return root
        #case 3
        if (balance>1) and key > root.left.data:
            root.left = self.leftRotate(root.left)
            root = self.rightRotate(root)
            return root
        #case 4
        elif (balance<-1) and key < root.right.data:
            root.right = self.rightRotate(root.right)
            root = self.leftRotate(root)
            return root
#        print("hello")
        return root
    def leftRotate(self,root):
        rchild = root.right
        rchildleft = rchild.left
        #left side rotating
        rchild.left = root
        root.right = rchildleft
        #height update
        root.height = 1 +  max(root.left,root.right)
        rchild.height = 1 +  max(rchild.left,rchild.right)
        print("hi")
        return rchild
    def rightRotate(self,root):
        lchild = root.left
        lchildright = lchild.right
        #right  side rotating
        lchild.right = root
        root.left = lchildright
        #updating height
        root.height = 1 +  max(root.left,root.right)
        lchild.height = 1 +  max(lchild.left,lchild.right)

        return lchild
    def getHeight(self,root):
        if not root:
            return 0
        return root.height
    def balance(self,root):
        if not root:
            return 0
        return (self.getHeight(root.left)-self.getHeight(root.right))
    def inorder(self,root):
        if root is not None:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)

avl = AVL_Tree()
avl.root = avl.insert(avl.root,25)
#print(avl.root.data)
avl.root = avl.insert(avl.root,10)
#print(avl.root.data)
avl.inorder(avl.root)