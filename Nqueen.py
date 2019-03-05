#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 18:32:52 2019

@author: dprasad@ad.msystechnologies.com
"""

N=8
def isSafe(x,y,sol):
    for i in range(y):
        if(sol[x][i] is 1):
            return False
    for i,j in zip(range(x,-1,-1),range(y,-1,-1)):

        if(sol[i][j] is 1):
            return False
    for i,j in zip(range(x,N,1),range(y,-1,-1)):
        if(sol[i][j] is 1):
            return False    
        
    return True
def nqueen(col,sol):
    if col>=N:
        return True
    else:
        for i in range(N):
            if isSafe(i,col,sol):
                sol[i][col] = 1
                if(nqueen(col+1,sol) == True):
                    return True
                sol[i][col] = 0
        return False
def main():
    sol = []
    for i in range(N):
        l1 = []
        for j in range(N):
            l1.append(0)
        sol.append(l1)
    n = nqueen(0,sol)
    if(n is not True):
        print("solution not possible")
    else:
        print(sol)
print(main())



