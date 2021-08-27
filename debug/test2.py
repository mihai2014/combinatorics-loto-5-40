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
import sys

class Reducere2():
    def __init__(self, arr):
        pass
        self.n = len(arr)
        self.m5, self.c5 = self.matrix5(arr)
        self.matrix5(arr)
        print("m5-",self.m5.shape)
        #dim = self.m5.shape[0]
    
    def comb(self, arr, k):
        # return list of all subsets of length k
        # to deal with duplicate subsets use 
        # set(list(combinations(arr, k)))
        return list(combinations(arr, k))
    
    #"graphical" matrix (0/1 --> int64)
    def matrix5(self,arr):
        comb = self.comb(arr,5)
        cols = self.n
        rows = math.comb(cols,5)

        z = np.zeros((rows), dtype = np.uint64)
        i = 0
        for c in comb:
            
            n1 = c[0]-1
            n2 = c[1]-1
            n3 = c[2]-1
            n4 = c[3]-1
            n5 = c[4]-1
            
            n = 2**n5+2**n4+2**n3+2**n2+2**n1             
            
            z[i] = n
            
            i += 1

        return z, comb   

    def test_m5(self):
        i = 0
        for n in self.m5:
            print(n,int(np.binary_repr(n),2))
            print(f"{np.binary_repr(n).rjust(40):<40}")
            print(f"{calc.c5[i]}".rjust(40))
            i += 1        
        

    def calc_intersect(self):
        i = 0
        for n1 in self.m5:
            j = 0
            for n2 in self.m5:
                
                res = np.bitwise_and(n1, n2)
                bites = np.unpackbits(np.array([res], dtype='>i8').view(np.uint8))
                common = np.sum(bites)
                
                j += 1
            print(i)   
            i += 1    
            
    def go(self):
        #memory garbage collector
        gc.enable()
        gc.collect()
    
#arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#or
m=10
arr = np.arange(start=1, stop=m+1, step=1)
calc = Reducere2(arr)  
calc.calc_intersect()
print("end")
#calc.test_m5()
#calc.go()
