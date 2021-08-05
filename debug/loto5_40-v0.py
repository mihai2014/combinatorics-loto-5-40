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

class Reducere():
    def __init__(self, arr):
        print("init")
        self.intersect = np.empty([0])
        self.arr = arr
        self.n = len(self.arr)
        self.m1, self.c1 = self.matrix(self.arr,5)
        self.m2, self.c2 = self.matrix(self.arr,6)     
        print("m1-",self.m1.shape)
        print("m2-",self.m2.shape)        
        print("ready")

    def mem(self):
        #total = 0
        #total += self.m1.nbytes
        #total += self.m2.nbytes
        #total += self.intersect.nbytes
        #total = round(total / 1024, 2)
        #print(f"Memory usage: {total} Kb")

        total = 0
        total += sys.getsizeof(self.m1)
        total += sys.getsizeof(self.m2)
        total += sys.getsizeof(self.intersect)
        total = round(total / 1024, 2)
        print(f"Memory usage: {total} Kb")
        
    def fv(self,number_list):        
        # freqeuncies of unique numbers in list ("calc count all")
        (unique, counts) = np.unique(number_list, return_counts=True)
        frequencies = np.asarray((unique, counts)).T
        return frequencies
        
    def comb(self, arr, k):
        # return list of all subsets of length k
        # to deal with duplicate subsets use 
        # set(list(combinations(arr, k)))
        return list(combinations(arr, k))

    #"graphical" matrix (0/1 int8)
    def matrix(self,arr,k):
        comb = self.comb(arr,k)
        cols = self.n
        rows = math.comb(cols,k)
        
        z = np.zeros((rows,cols), dtype = np.int8)
        i = 0
        for c in comb:
            
            n1 = c[0]
            n2 = c[1]
            n3 = c[2]
            n4 = c[3]
            n5 = c[4]
            if(k==6): 
                n6 = c[5]
            
            z[i,n1-1] = 1
            z[i,n2-1] = 1
            z[i,n3-1] = 1
            z[i,n4-1] = 1
            z[i,n5-1] = 1
            if(k==6): 
                z[i,n6-1] = 1
                
            #print(i,z[i])
            i += 1

        return z, comb   

    def count_c6(self):
        #1st, every c6 will have 6 sum (1x6)
        #after selection, sum=0
        sums = np.sum(self.m2,axis=1)
        #nr of 6's
        #print("c6-remaining",np.sum(sums)/6)
        return (np.sum(sums)/6)

    def calc_intersect(self):
        #intersect
        #m1   rows = (index) C arr 5
        #m2   rows = (index) C arr 6
        #m2.T cols = (index) C arr 6

        print("start intersect")

        #intesects between combinations
        self.intersect = self.m1 @ self.m2.T
        #change to 0 all values < 4
        self.intersect = np.where(self.intersect < 4, 0, self.intersect)
        
        print("end intersect")

        #test 10 numbers (total 55 intersections)
        #print(self.fv(self.intersect[0]))
        
    
    def select(self,i,f):

        #another possibility of selection : to explore
        #totalintersects = np.sum(calc.intersect,axis=1)
        
        #intersection 4 or 5
        nonzero = np.count_nonzero(self.intersect,axis=1)
        #index of c5
        first_max_idx = np.where(nonzero == np.max(nonzero))[0][0]
        print(i,"intersect:",nonzero[first_max_idx], "c5 selection (index):",first_max_idx, self.c1[first_max_idx])

        f.write( str(self.c1[first_max_idx])+'\n' )

        #mark selection
                
        #empty selected c6 (intesext columns)
        c6_indexes = np.where(self.intersect[first_max_idx] > 0)
        self.intersect[:,c6_indexes] = 0
        
        #empty selected c5 (intersect row)
        self.intersect[first_max_idx] = 0
        
        return nonzero[first_max_idx]

    def go(self):
        self.calc_intersect()

        os.system("rm result.txt")
        f = open("result.txt", "a")

        i = 0
        score = -1
        while(score != 0):
            i+=1
            score = self.select(i,f)

        f.close()

        print("See result.txt")
       
#arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#arr = np.arange(start=1, stop=11, step=1)
#calc = Reducere(arr)
#calc.go()







