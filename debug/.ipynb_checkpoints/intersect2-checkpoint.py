#        m1                             m2
#Ex: 12......n                       12....n       
# -------------------5-----------------------------6
#    1111100000 |  C    = rows      11111100.. | C
#    1111010000 |   arr             1111101..  |  arr
#    ...        |                   ...        |
#         11111 V                      111111  V
#
# intersect   = m1 X m2.T
#    c6 ---->  (axis=1)
# c5 
# |   5 5 ....
# |   ... 
# v   ..  0 0
#
# (axis=0)

# Function which returns subset or r length from n
from itertools import combinations
import numpy as np
import math
import sys
import os
import gc
import time

class Reducere2():
    def __init__(self, arr):
        pass
        self.n = len(arr)
        self.m5, self.c5 = self.matrix5(arr)
        print("m5-",self.m5.shape)
        dim = self.m5.shape[0]
    
    def comb(self, arr, k):
        # return list of all subsets of length k
        # to deal with duplicate subsets use 
        # set(list(combinations(arr, k)))
        return list(combinations(arr, k))
    
    #"graphical" matrix (0/1 int8)
    def matrix5(self,arr):
        comb = self.comb(arr,5)
        cols = self.n
        rows = math.comb(cols,5)

        z = np.zeros((rows,cols), dtype = np.int8)
        i = 0
        for c in comb:
            
            n1 = c[0]
            n2 = c[1]
            n3 = c[2]
            n4 = c[3]
            n5 = c[4]

            z[i,n1-1] = 1
            z[i,n2-1] = 1
            z[i,n3-1] = 1
            z[i,n4-1] = 1
            z[i,n5-1] = 1
                
            #print(i,z[i])
            i += 1

        return z, comb   
    
        


        

    def go(self):
        #memory garbage collector
        gc.enable()
        gc.collect()
    
#arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#or
m=10
arr = np.arange(start=1, stop=m+1, step=1)
calc = Reducere2(arr)   
calc.go()
