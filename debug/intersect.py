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
        #init intersect file on disk
        fp_intersect = np.memmap('data_c5.bin', dtype=np.int8, mode='w+', shape=(dim,dim))
    
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
    
        
    def calc_intersect(self):
        dim = self.m5.shape[0]        
        self.fp_intersect = np.memmap('data_c5.bin', dtype=np.int8, mode='r+', shape=(dim,dim))        
        #data = np.zeros((dim,dim), dtype = np.int8)
        #fp_intersect[:]=data[:]
        #row1
        #fp_intersect[1,:] = np.ones((1,dim), dtype = np.int8)
        #row2
        #fp_intersect[2,:] = np.ones((1,dim), dtype = np.int8)

        print("start generating intersections file...")
        #scan1
        #start = time.time()
        for i in range(dim):
            print(dim,"<--",i)
            row1 = self.m5[i,:]    
            for j in range(dim):
                #print(i,j)
                row2 = self.m5[j,:]    
                result = row1@row2
                self.fp_intersect[i,j] = result
        #end = time.time()
        #print(end - start)            

        #scan2
        #it = np.nditer(self.m5, flags=['f_index'],order='C')
        #newline = 0
        #acc = []
        #start = time.time()
        #for x in it:
        #    newline += 1
        #    #print(f"{it.index}--{x}")
        #    acc.append(int(x))
        #    if(newline == self.n):
        #        #print(acc)
        #        newline = 0
        #        acc = []
        #end = time.time()
        #print(end - start)                 
            
        #write modif
        self.fp_intersect.flush()


    def load(self):
        dim = self.m5.shape[0]
        newfp = np.memmap('data_c5.bin', dtype=np.int8, mode='r', shape=(dim,dim))
        print(newfp)
        

    def go(self):
        #memory garbage collector
        gc.enable()
        gc.collect()
        self.calc_intersect()
        #verif
        self.load()
    
#arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#or
m=40
arr = np.arange(start=1, stop=m+1, step=1)
calc = Reducere2(arr)   
calc.go()
