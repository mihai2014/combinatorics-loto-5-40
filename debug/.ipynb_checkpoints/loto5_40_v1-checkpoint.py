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

class Reducere():
    def __init__(self, arr, max_intersect):
        print("init")
        self.max_intersect = max_intersect
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

        #intersects between combinations (common digits)
        self.intersect = self.m1 @ self.m2.T
        #restrict number of intersections (common digits)
        #change to 0 all values < max_intersect
        self.intersect = np.where(self.intersect < self.max_intersect, 0, self.intersect)
        
        print("end intersect")
        
        print("verif-distinct intersections selected: ",np.unique(self.intersect))
    
        #test 10 numbers (1st choice: total 55 intersections) for max_intersect = 4
        #print(self.fv(self.intersect[0]))
        
    
    def select(self,i,f):

        #another possibility of selection : to explore
        #totalintersects = np.sum(self.intersect,axis=1)
        
        #selected intersections
        nonzero = np.count_nonzero(self.intersect,axis=1)
        #index of c5
        first_max_idx = np.where(nonzero == np.max(nonzero))[0][0]
        
        if(nonzero[first_max_idx] != 0):
            print(i,"intersect:",nonzero[first_max_idx], "c5 selection (index):",first_max_idx, self.c1[first_max_idx])

            f.write( str(self.c1[first_max_idx])+'\n' )
            self.solutions.append(first_max_idx)
        
        #mark selection
                
        #empty selected c6 (intesext columns)
        c6_indexes = np.where(self.intersect[first_max_idx] > 0)
        self.intersect[:,c6_indexes] = 0
        
        #empty selected c5 (intersect row)
        self.intersect[first_max_idx] = 0
        
        return nonzero[first_max_idx]

    def free_mem(self):
        try:
            del self.m1
            del self.m2
            del self.c1
            del self.c2
            del self.intersect        
            del self.intersect2
        except:
            pass
        gc.collect()
    
    def diagnose(self):
        print("Evaluate solution")
        
        print("Free memory(intersections matrix)...")
        del self.intersect
        gc.collect()

        print("Recompute intersections only with chosen solutions...")
        sol = np.array(self.solutions)
        self.m1Sol = self.m1[sol,:]
        #print(self.m1Sol)
        self.intersect2 = self.m1Sol @ self.m2.T
        #change to 0 all values < max_intersect
        self.intersect2 = np.where(self.intersect2 < self.max_intersect, 0, self.intersect2)
        
        print("ready")
        print("Solution intersections matrix:")
        #print(self.intersect2.shape)
        print(self.intersect2)
        
        print("verif-selected intersections: ",np.unique(self.intersect2))    
        
        t = np.sum(self.intersect2,axis=0)
        #sums of all intersections specified / every c6
        #print(t)
        c6_not_hitted = np.where(t == 0)[0]
        if (c6_not_hitted.size == 0):
            print("Solution ok. All c6 are 'hitted' by the intersect condition")
        else:
            print(f"Error: {c6_not_hitted.size} c6 combinations are not 'hitted' by the intersect condition!")    

        #max intersect / every c6
        c6_hit = np.max(self.intersect2,axis=0)
        #fv 
        c6_total_cover_fv = self.fv(c6_hit)
        print("c6 cover frequency:\n", c6_total_cover_fv)
        print("Total c6(verif): ", np.sum(c6_total_cover_fv,axis=0)[1])
            
        #calc_count = self.fv(t)
        #print(calc_count)

        #print("Solution intersections:")
        
        #nr = len(self.solutions)
        #for nr in range(nr):
        #    print("---------------------------")
        #    c6_count = self.fv(self.intersect2[nr])
        #    #exclude 0 frequency
        #    c6_count = c6_count[c6_count[:,0] > 0] 
        #    print(nr,'\n',c6_count)
        
    
    def go(self):
        self.solutions = []
        self.calc_intersect()

        os.system("rm result.txt")
        f = open("result.txt", "a")

        i = 0
        score = -1
        while(score != 0):
            i+=1
            score = self.select(i,f)

        f.close()

        self.diagnose()
        
        print("See result.txt")
       
#arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#or
#m=10
#max_intersect = 4
#arr = np.arange(start=1, stop=m+1, step=1)
#calc = Reducere(arr,max_intersect)
#calc.go()
